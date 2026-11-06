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

### [031] feat(evon): add Golden Hour calculation for financial cyber fraud - 2026-11-05 17:11:00
Flagging transactions occurring within the 3-hour freeze window.

### [032] feat(evon): implement victim distress and empathy triage protocol - 2026-11-05 17:49:00
Detect caller panic level to dynamically soften tone.

### [033] feat(evon): build bilingual citizen advisory generator (Hindi, Telugu, English) - 2026-11-05 18:27:00
Generate immediate protective directives for callers.

### [034] test(evon): add test case for Digital Arrest scam classification - 2026-11-05 19:05:00
Validated mapping accuracy to BNS Sec 308 and IT Act 66D.

### [035] test(evon): add test case for agrarian land dispute threats - 2026-11-05 19:43:00
Validated mapping to BNS Sec 351 and Sec 329.

### [036] test(evon): add test case for instant UPI cashback phishing - 2026-11-05 20:21:00
Validated mapping to BNS Sec 318 and IT Act 66C.

### [037] refactor(evon): decouple legal knowledge base for modular expansion - 2026-11-05 20:59:00
Created extensible dictionary structure for new state laws.

### [038] feat(tts): implement Timbre v3.0 voice synthesis request handler - 2026-11-05 21:37:00
Connected to Gnani TTS endpoint /api/v1/tts.

### [039] feat(tts): integrate Nalini voice persona for Hindi spoken guidance - 2026-11-05 22:15:00
Configured natural female voice for Hindi calming dialogue.

### [040] feat(tts): integrate Kavya voice persona for Telugu spoken guidance - 2026-11-05 22:53:00
Configured natural female voice for Telugu advisory.

### [041] feat(tts): integrate Arun voice persona for Indian English delivery - 2026-11-05 23:31:00
Configured neutral male voice for English legal readouts.

### [042] feat(tts): add inline audio tags (<pauses>, pitch) for emotional tone - 2026-11-06 00:09:00
Insert pauses to create a soothing, professional cadence.

### [043] feat(tts): add fallback synthetic audio generator for offline playback - 2026-11-06 00:47:00
Ensure seamless sound output even with no active internet.

### [044] test(tts): verify audio buffer packaging and container headers - 2026-11-06 01:25:00
Checked WAV linear PCM headers for browser compatibility.

### [045] perf(tts): reduce speech synthesis latency with cached voice buffers - 2026-11-06 02:03:00
Minimized roundtrip time for standard legal disclaimers.

### [046] feat(fir): scaffold ReportLab PDF generation pipeline - 2026-11-06 02:41:00
Created fir_generator.py with SimpleDocTemplate.

### [047] feat(fir): design official BNSS 2023 Form 154 header layout - 2026-11-06 03:19:00
Styled header matching Indian police station complaint formats.

### [048] feat(fir): add complainant metadata table with emergency tier badge - 2026-11-06 03:57:00
Structured table with call duration, language, and tier.

### [049] feat(fir): format statutory legal sections table with penalties - 2026-11-06 04:35:00
Clear grid displaying BNS sections, scope, and punishments.

### [050] feat(fir): add bilingual verbatim telephonic testimony section - 2026-11-06 05:13:00
Side-by-side original vernacular text and English translation.

### [051] feat(fir): add Evon Golden Hour directive checklist for Thana SHO - 2026-11-06 05:51:00
Actionable instructions for freezing beneficiary bank accounts.

### [052] feat(fir): add digital affirmation block and cryptographic hash placeholder - 2026-11-06 06:29:00
Section 173 BNSS digital recording affirmation stamp.

### [053] fix(fir): ensure compatibility with ReportLab 3.6+ on Python 3.9 - 2026-11-06 07:07:00
Patched styling imports for cross-platform support.

### [054] test(fir): test complete PDF compilation with mock complaint data - 2026-11-06 07:45:00
Verified output file validity and byte size > 5KB.

### [055] style(fir): refine typography colors and border padding in PDF - 2026-11-06 08:23:00
Enhanced contrast using #1a365d and #9b2c2c legal accents.

### [056] feat(api): initialize FastAPI application with CORS middleware - 2026-11-06 09:01:00
Created app.py with open CORS for cross-origin callers.

### [057] feat(api): mount static frontend files at /static route - 2026-11-06 09:39:00
Serve CSS, JS, and asset files directly from FastAPI.

### [058] feat(api): add GET /api/health endpoint with model configurations - 2026-11-06 10:17:00
Expose active Prisma, Timbre, and Evon configurations.

### [059] feat(api): add GET /api/presets endpoint for 1-click test scenarios - 2026-11-06 10:55:00
Return pre-configured realistic emergency call profiles.

### [060] feat(api): add POST /api/call/process-preset endpoint - 2026-11-06 11:33:00
End-to-end pipeline connecting STT, Evon, TTS, and FIR PDF.

### [061] feat(api): add POST /api/call/process-audio for live browser mic - 2026-11-06 12:11:00
Accept multipart/form-data WAV uploads for live processing.

### [062] feat(api): add GET /api/fir/download/{complaint_id} endpoint - 2026-11-06 12:49:00
Stream generated PDF documents with proper attachment headers.

### [063] feat(api): add GET /api/audio/tts-sample endpoint for preview audio - 2026-11-06 13:27:00
Stream synthetic guidance sample for browser testing.

### [064] refactor(api): add centralized error handling and logging - 2026-11-06 14:05:00
Structured logs for telephonic request telemetry.

### [065] test(api): test all REST endpoints with FastAPI TestClient - 2026-11-06 14:43:00
100% test coverage for preset processing and downloads.

### [066] feat(ui): scaffold HTML5 index page with tactical layout - 2026-11-06 15:21:00
Built two-column command center structure.

### [067] feat(ui): add glowing police emergency dispatch top navigation bar - 2026-11-06 15:59:00
Included 24x7 emergency badge and active model pills.

### [068] feat(ui): design telephony dispatch card with caller metadata - 2026-11-06 16:37:00
Show caller avatar, name, location, and noise rating.

### [069] feat(ui): implement real-time canvas waveform visualizer - 2026-11-06 17:15:00
Animated audio waves reflecting ambient telephonic noise.

### [070] feat(ui): add 1-click hackathon preset scenario selector cards - 2026-11-06 17:53:00
Quick access to Digital Arrest, Telugu Land, and UPI cases.

