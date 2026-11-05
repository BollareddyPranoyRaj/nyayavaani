# NyayaVaani Project Changelog

All notable changes and milestones documented.

### [001] chore(repo): initialize workspace and directory boundaries - 2026-11-04 22:11:00
Initial repository scaffolding for NyayaVaani.

### [002] docs(readme): add project mission and high-level architecture diagram - 2026-11-04 22:49:00
Added system architecture diagram with Mermaid.

### [003] build(deps): define core requirements.txt with FastAPI, ReportLab and Pydantic - 2026-11-04 23:27:00
Pinned dependencies for reproducible builds.

### [004] config(env): add .env.example with Gnani Vachana platform defaults - 2026-11-05 00:05:00
Added environment variable template for API keys.

### [005] chore(git): configure .gitignore for python virtual environments and artifacts - 2026-11-05 00:43:00
Prevent committing venv and temporary PDF dockets.

### [006] feat(audio): scaffold audio processing module - 2026-11-05 01:21:00
Created audio_processor.py for telephony signal handling.

### [007] feat(audio): implement 8kHz G.711 telephony frequency simulation - 2026-11-05 01:59:00
Added bandpass filter simulation from 300Hz to 3400Hz.

### [008] feat(audio): add line noise and jitter modulation buffer generator - 2026-11-05 02:37:00
Simulate realistic mobile carrier line static and jitter.

### [009] perf(audio): optimize WAV byte stream packing with struct pack - 2026-11-05 03:15:00
Low-latency in-memory PCM audio generation.

### [010] test(audio): add unit tests for synthetic telephony carrier generation - 2026-11-05 03:53:00
Validated 8kHz wave output headers and sample rates.

### [011] refactor(audio): add docstrings and type annotations to audio processor - 2026-11-05 04:31:00
Standardized type hints across audio methods.

### [012] feat(stt): create Gnani AI client skeleton with Vachana endpoints - 2026-11-05 05:09:00
Scaffolded gnani_client.py with base configuration.

### [013] feat(stt): implement Prisma v3.0 REST transcription payload handler - 2026-11-05 05:47:00
Integrated multipart audio file upload to /api/v1/stt.

### [014] feat(stt): add support for indic-auto language identification - 2026-11-05 06:25:00
Allow Prisma to automatically detect native Indian dialects.

### [015] feat(stt): configure codemix transcription mode for Hinglish - 2026-11-05 07:03:00
Ensure words are transcribed in their respective native scripts.

### [016] feat(stt): add verbatim transcription mode support for legal compliance - 2026-11-05 07:41:00
Preserve hesitations and filler words for police records.

