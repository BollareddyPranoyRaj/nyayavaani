# ⚖️ NyayaVaani: 1-Page Solution Pitch
**AI Vernacular Telephonic Emergency FIR & Legal First-Responder for Bharat**  
*Submitted for the Great Indian AI Internship Challenge by Gnani AI*  
**Team:** Bollareddy Pranoy Raj (Primary) & Co-Builder | **Track:** Speech AI & LLM Reasoning

---

### 1. The Real-World Crisis
Over **95% of citizens in Tier-2/3 towns and rural India** struggle to access emergency legal protection. In 2024–2026, the nationwide surge in **"Digital Arrest" cyber scams, fake courier extortion, and UPI phishing** has left vulnerable citizens terrified. When victims dial emergency helplines:
- **Telephonic & Environmental Noise:** They call from noisy streets, bus stands, or farmlands over band-limited 8kHz mobile lines with heavy ambient interference.
- **Vernacular Code-Mixing:** In panic, citizens speak fragmented **Hinglish, rural Telugu, or Tamil** mixed with colloquial jargon.
- **The New Legal Reform Barrier:** With the Indian Penal Code replaced by the **Bharatiya Nyaya Sanhita (BNS 2023)**, neither citizens nor duty desk officers know the exact legal sections to register immediately.
- **The Lost "Golden Hour":** Crucial evidence and the 2-hour window to freeze defrauded funds via bank nodal officers are lost due to delayed paperwork.

---

### 2. The Solution: NyayaVaani
**NyayaVaani** is a 24x7 voice-first emergency legal copilot that turns any standard telephonic line into an instant, empathetic first-responder:
1. **Listens & Transcribes (Gnani Prisma v3.0 STT):** Operates on noisy 8kHz telephonic audio, auto-detects Indic vernaculars (`indic-auto`), and transcribes code-mixed distress calls verbatim without getting tripped up by traffic or phone static.
2. **De-escalates & Maps Law (Gnani Evon 30B LLM):** Evaluates victim trauma, extracts the 5 Ws (Who, What, When, Where, Stake), and performs precision statutory mapping under **BNS 2023** (e.g., Sec 308 for extortion, Sec 318/319 for cheating/personation) and **IT Act Sec 66D**.
3. **Calms in Mother Tongue (Gnani Timbre v3.0 Neural TTS):** Speaks back with soothing regional voices (Nalini for Hindi, Kavya for Telugu) using inline audio tags (`<pauses>`) to calm traumatized citizens while emergency alerts fire.
4. **Instant BNSS Form 154 Bilingual FIR Dossier:** Auto-generates a stamped, digitally verifiable PDF complaint dossier ready to submit to Thana SHOs or dispatch to the National Cybercrime Portal (1930).

---

### 3. Gnani AI Model Stack Alignment
| Component | Gnani Model Used | Specific Capability Exploited |
|---|---|---|
| **Speech-to-Text** | **Prisma v3.0** | Robust 8kHz narrowband mobile noise tolerance & multi-dialect code-mixing (`codemix` / `verbatim`). |
| **Reasoning Engine** | **Evon 30B** | Native comprehension of Indian socio-legal context, statutory offense extraction & Golden Hour triage. |
| **Voice Synthesis** | **Timbre v3.0** | Low-latency regional voice synthesis with emotional cadence and empathetic acoustic tags (`<pauses>`). |

---

### 4. Impact & Scalability
- **Zero App Barrier:** Operates via standard telephone/cellular lines—no smartphone or high-speed internet needed.
- **Democratizing Justice for 1.4 Billion:** Bridges language, legal literacy, and socio-economic divides.
- **Financial Protection:** Triggers automated bank freeze notices within the critical Golden Hour.

---
**Repository & Live Demo:** [https://github.com/BollareddyPranoyRaj/nyayavaani](https://github.com/BollareddyPranoyRaj/nyayavaani)
