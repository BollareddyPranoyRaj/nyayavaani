import os
import sys
from pathlib import Path

# Add project root to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backend.evon_reasoning import evon_engine
from backend.fir_generator import generate_official_fir_pdf
from backend.gnani_client import gnani_client, PRESET_CASES
from fastapi.testclient import TestClient
from backend.app import app

def test_evon_reasoning():
    print("Testing Evon Legal Reasoning...")
    res = evon_engine.analyze_incident(
        transcript=PRESET_CASES["case1_digital_arrest"]["transcript_codemix"],
        detected_lang="hi"
    )
    assert res["incident_type"] == "Cyber Impersonation & Digital Arrest Extortion"
    assert len(res["legal_sections"]) >= 3
    assert "Section 308(2) BNS 2023" in [s["section"] for s in res["legal_sections"]]
    print("✓ Evon Reasoning tests passed.")

def test_fir_pdf_generation():
    print("Testing Official FIR PDF Generation...")
    case = PRESET_CASES["case1_digital_arrest"]
    res = evon_engine.analyze_incident(case["transcript_codemix"], detected_lang="hi")
    
    pdf_path = generate_official_fir_pdf(
        complaint_id="TEST-FIR-001",
        complainant_name="Test Citizen",
        phone_number="+91 98765 00000",
        incident_type=res["incident_type"],
        transcript_original=case["transcript_codemix"],
        transcript_en=case["transcript_en"],
        legal_sections=res["legal_sections"],
        extracted_facts=res["extracted_facts"]
    )
    assert os.path.exists(pdf_path)
    assert os.path.getsize(pdf_path) > 1000
    print(f"✓ PDF generated successfully at {pdf_path} (size: {os.path.getsize(pdf_path)} bytes).")

def test_api_endpoints():
    print("Testing FastAPI Endpoints...")
    client = TestClient(app)
    
    # 1. Health check
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.json()["status"] == "online"
    
    # 2. Presets
    res = client.get("/api/presets")
    assert res.status_code == 200
    assert "case1_digital_arrest" in res.json()["cases"]
    
    # 3. Process Preset Call
    res = client.post("/api/call/process-preset", json={"preset_key": "case1_digital_arrest"})
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert "pdf_download_url" in data
    
    # 4. Download generated FIR
    complaint_id = data["complaint_id"]
    pdf_res = client.get(f"/api/fir/download/{complaint_id}")
    assert pdf_res.status_code == 200
    assert pdf_res.headers["content-type"] == "application/pdf"
    
    print("✓ All API endpoint tests passed.")

if __name__ == "__main__":
    test_evon_reasoning()
    test_fir_pdf_generation()
    test_api_endpoints()
    print("\n🎉 ALL TESTS PASSED SUCCESSFULLY! The system is rock-solid.")
