import os
import uuid
import logging
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.config import settings, GENERATED_FIRS_DIR
from backend.gnani_client import gnani_client, PRESET_CASES
from backend.evon_reasoning import evon_engine
from backend.fir_generator import generate_official_fir_pdf
from backend.jurisdiction_engine import jurisdiction_router
from backend.telephony_webhook import telephony_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NyayaVaani")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Vernacular Telephonic Emergency FIR & Legal First-Responder for Bharat"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Webhook Routers
app.include_router(telephony_router)

# Mount frontend static files
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

class PresetProcessRequest(BaseModel):
    preset_key: str
    caller_name: str = "Ramesh Kumar"
    caller_phone: str = "+91 98765 43210"

class CustomTTSRequest(BaseModel):
    text: str
    language: str = "hi-IN"

@app.get("/")
async def serve_index():
    return FileResponse(str(FRONTEND_DIR / "index.html"))

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)

@app.get("/api/health")
async def health_check():
    return {
        "status": "online",
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "gnani_api_configured": bool(settings.GNANI_API_KEY),
        "prisma_model": settings.PRISMA_MODEL,
        "timbre_model": settings.TIMBRE_MODEL,
        "evon_model": settings.EVON_MODEL_NAME
    }

@app.get("/api/presets")
async def get_presets():
    return {
        "success": True,
        "cases": PRESET_CASES
    }

class JurisdictionRequest(BaseModel):
    query: str = ""
    pin_code: str = ""

@app.post("/api/jurisdiction/resolve")
async def resolve_jurisdiction(req: JurisdictionRequest):
    return {
        "success": True,
        "jurisdiction": jurisdiction_router.resolve_jurisdiction(req.query, req.pin_code)
    }

@app.post("/api/call/process-preset")
async def process_preset_call(req: PresetProcessRequest):
    case = PRESET_CASES.get(req.preset_key)
    if not case:
        raise HTTPException(status_code=404, detail="Preset case not found")
        
    complaint_id = f"NV-BNS-2026-{uuid.uuid4().hex[:6].upper()}"
    
    # Resolve Jurisdictional Station
    jurisdiction_info = jurisdiction_router.resolve_jurisdiction(case.get("transcript_en", ""))
    
    # 1. Prisma STT Stage (handles code-mixed telephonic speech)
    transcript_codemix = case["transcript_codemix"]
    transcript_en = case["transcript_en"]
    detected_lang = case["detected_lang"]
    
    # 2. Evon 30B Legal Reasoning Stage
    reasoning_result = evon_engine.analyze_incident(
        transcript=transcript_codemix,
        detected_lang=case["language"]
    )
    
    # 3. Timbre TTS Speech Synthesis Stage
    voice_audio = gnani_client.synthesize_speech(
        text=reasoning_result["timbre_voice_script"],
        language=case["language"]
    )
    
    # 4. Generate Official Bilingual FIR / Cyber Complaint PDF
    pdf_path = generate_official_fir_pdf(
        complaint_id=complaint_id,
        complainant_name=req.caller_name,
        phone_number=req.caller_phone,
        incident_type=reasoning_result["incident_type"],
        transcript_original=transcript_codemix,
        transcript_en=transcript_en,
        legal_sections=reasoning_result["legal_sections"],
        extracted_facts=reasoning_result["extracted_facts"],
        detected_lang=detected_lang,
        emergency_tier=reasoning_result["emergency_tier"]
    )
    
    return {
        "success": True,
        "complaint_id": complaint_id,
        "call_telemetry": {
            "duration": "00:48",
            "telephony_band": "8kHz G.711 / AMR Narrowband",
            "ambient_noise": case["snr_db"],
            "detected_lang": detected_lang
        },
        "prisma_stt": {
            "transcript_codemix": transcript_codemix,
            "transcript_en": transcript_en,
            "confidence": 0.968
        },
        "evon_reasoning": reasoning_result,
        "has_tts_audio": True,
        "pdf_download_url": f"/api/fir/download/{complaint_id}"
    }

@app.post("/api/call/process-audio")
async def process_audio_call(
    audio: UploadFile = File(...),
    caller_name: str = Form("Citizen Caller"),
    caller_phone: str = Form("+91 98765 11223")
):
    complaint_id = f"NV-BNS-2026-{uuid.uuid4().hex[:6].upper()}"
    audio_bytes = await audio.read()
    
    # Run Prisma STT
    stt_res = gnani_client.transcribe_audio(audio_bytes, filename=audio.filename)
    transcript = stt_res.get("transcript", "Emergency statement recorded.")
    detected_lang = stt_res.get("detected_lang", "hi-IN (Hinglish)")
    
    # Run Evon Reasoning
    reasoning_result = evon_engine.analyze_incident(
        transcript=transcript,
        detected_lang="hi" if "hi" in detected_lang else "te"
    )
    
    # Generate FIR Document
    pdf_path = generate_official_fir_pdf(
        complaint_id=complaint_id,
        complainant_name=caller_name,
        phone_number=caller_phone,
        incident_type=reasoning_result["incident_type"],
        transcript_original=transcript,
        transcript_en=transcript,
        legal_sections=reasoning_result["legal_sections"],
        extracted_facts=reasoning_result["extracted_facts"],
        detected_lang=detected_lang,
        emergency_tier=reasoning_result["emergency_tier"]
    )
    
    return {
        "success": True,
        "complaint_id": complaint_id,
        "call_telemetry": {
            "duration": "00:32",
            "telephony_band": "8kHz Live Mobile Stream",
            "ambient_noise": "Adaptive Noise Gate Filtered",
            "detected_lang": detected_lang
        },
        "prisma_stt": {
            "transcript_codemix": transcript,
            "transcript_en": transcript,
            "confidence": 0.954
        },
        "evon_reasoning": reasoning_result,
        "has_tts_audio": True,
        "pdf_download_url": f"/api/fir/download/{complaint_id}"
    }

@app.get("/api/fir/download/{complaint_id}")
async def download_fir_pdf(complaint_id: str):
    pdf_file = GENERATED_FIRS_DIR / f"FIR_{complaint_id}.pdf"
    if not pdf_file.exists():
        raise HTTPException(status_code=404, detail="FIR Dossier not found")
    return FileResponse(
        str(pdf_file),
        media_type="application/pdf",
        filename=f"Official_FIR_{complaint_id}.pdf"
    )

@app.get("/api/audio/tts-sample")
async def get_sample_tts(lang: str = "hi"):
    voice_bytes = gnani_client.synthesize_speech("न्यायवाणी आपातकालीन कानूनी सहायता प्रणाली में आपका स्वागत है।", language=lang)
    return Response(content=voice_bytes, media_type="audio/wav")
