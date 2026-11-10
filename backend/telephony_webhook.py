import logging
from fastapi import APIRouter, Request, Response
from backend.config import settings

logger = logging.getLogger(__name__)
telephony_router = APIRouter(prefix="/api/telephony", tags=["Telephony Webhooks"])

@telephony_router.post("/inbound-call")
async def handle_inbound_call(request: Request):
    """Webhook for incoming citizen emergency calls from Exotel/Twilio telephonic trunk."""
    form_data = await request.form()
    caller_num = form_data.get("From", "+91 Mobile Citizen")
    call_sid = form_data.get("CallSid", "SID-NV-LIVE")
    
    logger.info(f"Incoming telephonic emergency call from {caller_num} (CallSid: {call_sid})")
    
    # Twilio / Exotel compliant Voice XML response
    response_xml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="woman" language="hi-IN">न्यायवाणी आपातकालीन कानूनी सहायता प्रणाली में आपका स्वागत है। अपनी समस्या बताएं।</Say>
    <Record maxLength="120" action="/api/telephony/process-recording" playBeep="true" trim="trim-silence" />
    <Say voice="woman" language="hi-IN">आपकी शिकायत दर्ज कर ली गई है। धन्यवाद।</Say>
</Response>"""
    return Response(content=response_xml, media_type="application/xml")

@telephony_router.post("/process-recording")
async def handle_process_recording(request: Request):
    """Processes incoming recording from telephonic carrier."""
    form_data = await request.form()
    recording_url = form_data.get("RecordingUrl", "")
    caller_num = form_data.get("From", "+91 Unknown")
    
    logger.info(f"Received audio recording for analysis from {caller_num}: {recording_url}")
    return {
        "status": "received",
        "caller": caller_num,
        "action": "dispatched_to_prisma_and_evon"
    }
