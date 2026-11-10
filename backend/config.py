import os
from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent
GENERATED_FIRS_DIR = BASE_DIR / "generated_firs"
SAMPLE_AUDIO_DIR = BASE_DIR / "sample_audio"

GENERATED_FIRS_DIR.mkdir(exist_ok=True)
SAMPLE_AUDIO_DIR.mkdir(exist_ok=True)

# Auto-load .env file if it exists
env_file = BASE_DIR / ".env"
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ[k.strip()] = v.strip()

class Settings(BaseModel):
    PROJECT_NAME: str = "NyayaVaani - AI Telephonic FIR & Legal First-Responder"
    VERSION: str = "1.0.0"
    GNANI_API_KEY: str = os.getenv("GNANI_API_KEY", "")
    GNANI_BASE_URL: str = os.getenv("GNANI_BASE_URL", "https://api.vachana.ai")
    
    # Prisma STT Defaults
    PRISMA_MODEL: str = os.getenv("PRISMA_MODEL", "prisma-v3.0")
    DEFAULT_LANGUAGE: str = "indic-auto"
    DEFAULT_OUTPUT_MODE: str = "codemix"  # codemix | transcribe | verbatim | transliterate
    
    # Timbre TTS Defaults
    TIMBRE_MODEL: str = os.getenv("TIMBRE_MODEL", "timbre-v3.0")
    DEFAULT_VOICE_HINDI: str = "Nalini"
    DEFAULT_VOICE_TELUGU: str = "Kavya"
    DEFAULT_VOICE_ENGLISH: str = "Arun"
    
    # Evon Reasoning Defaults
    EVON_MODEL_NAME: str = "gnani-ai/evon-30b-instruct"
    USE_SIMULATOR_FALLBACK: bool = False if os.getenv("GNANI_API_KEY") else True

settings = Settings()
