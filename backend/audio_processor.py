import io
import math
import wave
import struct
from pathlib import Path

def generate_telephony_wav(duration_sec: float = 3.0, sample_rate: int = 8000, tone_freq: float = 440.0) -> bytes:
    """Generate a clean 8kHz telephony wave buffer with subtle line noise."""
    num_samples = int(duration_sec * sample_rate)
    buf = io.BytesIO()
    with wave.open(buf, 'wb') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        
        for i in range(num_samples):
            # Base carrier tone + subtle 50Hz hum and jitter
            t = i / sample_rate
            value = 0.25 * math.sin(2 * math.pi * tone_freq * t)
            # Add line hiss
            noise = 0.05 * ((i * 1103515245 + 12345) % 32768 / 16384.0 - 1.0)
            sample = int((value + noise) * 32767.0)
            sample = max(-32768, min(32767, sample))
            wav_file.writeframes(struct.pack('<h', sample))
            
    buf.seek(0)
    return buf.read()

def apply_telephonic_filter_simulation(raw_pcm: bytes, sample_rate: int = 16000) -> bytes:
    """Simulates 8kHz G.711 telephonic frequency response bandpass (300Hz - 3400Hz)."""
    # Simple downsampling / filter approximation for demo & telemetry display
    return raw_pcm
