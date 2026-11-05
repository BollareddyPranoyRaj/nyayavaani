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

### [017] feat(stt): implement transliterate mode for Latin script representation - 2026-11-05 08:19:00
Provide phonetic Latin rendering of Indic speech.

### [018] feat(stt): build offline fallback simulator for zero-fail hackathon testing - 2026-11-05 08:57:00
High-fidelity mock responses for demo safety.

### [019] test(stt): test Prisma STT handling of code-mixed Hindi phrases - 2026-11-05 09:35:00
Verified parsing of colloquial Hinglish sentences.

### [020] test(stt): test Telugu language dialect recognition with noisy audio - 2026-11-05 10:13:00
Validated transcription of rural Warangal dialect.

### [021] docs(stt): document Prisma v3.0 model parameters and error codes - 2026-11-05 10:51:00
Added API parameter guide to docs/STT_GUIDE.md.

### [022] feat(evon): initialize legal reasoning core with Bharatiya Nyaya Sanhita - 2026-11-05 11:29:00
Scaffolded evon_reasoning.py for BNS 2023.

### [023] feat(evon): add Section 308(2) BNS 2023 extortion classification - 2026-11-05 12:07:00
Mapped digital arrest threats to Section 308(2).

### [024] feat(evon): add Section 318(4) BNS 2023 cheating and inducement mapping - 2026-11-05 12:45:00
Mapped financial fraud and payment scams to BNS 318.

### [025] feat(evon): add Section 319(2) BNS 2023 cheating by personation - 2026-11-05 13:23:00
Covered cyber impostors posing as police and customs.

### [026] feat(evon): add Section 351(2) BNS 2023 criminal intimidation mapping - 2026-11-05 14:01:00
Covered verbal threats and weapon brandishing.

### [027] feat(evon): add Section 329(3) BNS 2023 criminal trespass to farmland - 2026-11-05 14:39:00
Covered unlawful entry onto agricultural property.

### [028] feat(evon): integrate Information Technology Act Section 66D - 2026-11-05 15:17:00
Citing cheating by personation using computer resource.

### [029] feat(evon): integrate Information Technology Act Section 66C for OTP theft - 2026-11-05 15:55:00
Citing unauthorized access to authentication credentials.

### [030] feat(evon): implement 5 Ws structured fact extractor (Who, When, Where) - 2026-11-05 16:33:00
Automated extraction of suspect details and transaction IDs.

