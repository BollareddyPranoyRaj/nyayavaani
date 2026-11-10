// NyayaVaani Frontend Interactive Engine

let isRecording = false;
let mediaRecorder = null;
let recordedAudioChunks = [];
let audioContext = null;
let currentComplaintId = "NV-BNS-2026-AP8921";
let activePreset = "case1_digital_arrest";
let waveformAnimId = null;

// Ensure initialization runs whether DOM is already ready or loading
function init() {
  console.log("NyayaVaani initializing...");
  try {
    if (window.lucide) {
      lucide.createIcons();
    }
  } catch (err) {
    console.warn("Lucide icons warning:", err);
  }
  
  initWaveform();
  bindEvents();
  console.log("NyayaVaani events bound successfully.");
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  // DOM already loaded (common on fast local servers)
  init();
}

// Canvas Waveform Animation
function initWaveform() {
  const canvas = document.getElementById('waveformCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let phase = 0;

  function renderWave() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.lineWidth = 2;
    ctx.strokeStyle = '#38bdf8';
    ctx.beginPath();

    const midY = canvas.height / 2;
    const points = 60;
    const step = canvas.width / points;

    for (let i = 0; i <= points; i++) {
      const x = i * step;
      // Synthesize telephonic noise + voice wave
      const amp = isRecording ? 18 : 6;
      const noise = (Math.sin(phase + i * 0.4) + Math.cos(phase * 1.5 + i * 0.2)) * amp;
      const y = midY + noise * (Math.sin(i / points * Math.PI));

      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.stroke();

    phase += 0.12;
    waveformAnimId = requestAnimationFrame(renderWave);
  }
  renderWave();
}

function bindEvents() {
  // Preset card clicks
  document.querySelectorAll('.preset-card').forEach(card => {
    card.addEventListener('click', (e) => {
      e.preventDefault();
      const presetKey = card.getAttribute('data-preset');
      console.log("Preset selected:", presetKey);
      selectPreset(presetKey, true);
    });
  });

  // Play button inside cards
  document.querySelectorAll('.btn-play-preset').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      e.preventDefault();
      const card = btn.closest('.preset-card');
      if (card) {
        const presetKey = card.getAttribute('data-preset');
        console.log("Play button clicked for:", presetKey);
        selectPreset(presetKey, true);
      }
    });
  });

  // Live Mic Recording
  const btnRecordMic = document.getElementById('btnRecordMic');
  const btnStopRecord = document.getElementById('btnStopRecord');

  if (btnRecordMic) {
    btnRecordMic.addEventListener('click', (e) => {
      e.preventDefault();
      startMicRecording();
    });
  }
  
  if (btnStopRecord) {
    btnStopRecord.addEventListener('click', (e) => {
      e.preventDefault();
      stopMicRecording();
    });
  }

  // Play TTS guidance
  const btnPlayTTS = document.getElementById('btnPlayTTS');
  if (btnPlayTTS) {
    btnPlayTTS.addEventListener('click', (e) => {
      e.preventDefault();
      playTTSGuidance();
    });
  }
}

// Preset selection & processing
window.selectPreset = async function(presetKey, runExecution = true) {
  activePreset = presetKey;
  document.querySelectorAll('.preset-card').forEach(c => c.classList.remove('active'));
  const activeCard = document.querySelector(`[data-preset="${presetKey}"]`);
  if (activeCard) activeCard.classList.add('active');

  const statusBanner = document.getElementById('callStatusBanner');
  const statusText = document.getElementById('callStatusText');
  const callerName = document.getElementById('displayCallerName');
  const noiseLevel = document.getElementById('callNoiseLevel');

  if (presetKey === "case1_digital_arrest") {
    if (callerName) callerName.innerText = "Ramesh Kumar (Citizen)";
    if (noiseLevel) noiseLevel.innerText = "8.4 dB Noise (Traffic/Phone Static)";
  } else if (presetKey === "case2_telugu_land_extortion") {
    if (callerName) callerName.innerText = "Ramayya (Farmer, Warangal)";
    if (noiseLevel) noiseLevel.innerText = "11.2 dB Noise (Tractor/Wind)";
  } else {
    if (callerName) callerName.innerText = "Rahul Verma (Student)";
    if (noiseLevel) noiseLevel.innerText = "14.5 dB Noise (Cellular Handset)";
  }

  if (runExecution) {
    if (statusText) statusText.innerText = "Connecting telephonic line & analyzing with Prisma v3.0...";
    if (statusBanner) statusBanner.style.color = "#fbbf24";

    try {
      const response = await fetch('/api/call/process-preset', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ preset_key: presetKey })
      });
      const data = await response.json();
      if (data.success) {
        updateDashboard(data);
        if (statusText) statusText.innerText = "Incident Triaged & Official FIR Ready";
        if (statusBanner) statusBanner.style.color = "#34d399";
      }
    } catch (e) {
      console.error("Error processing preset:", e);
      if (statusText) statusText.innerText = "Error processing call";
      if (statusBanner) statusBanner.style.color = "#f87171";
    }
  }
};

// Update dashboard with real backend data
function updateDashboard(data) {
  currentComplaintId = data.complaint_id;

  // 1. STT Transcript & Translation
  const sttTranscript = document.getElementById('sttTranscript');
  const sttTranslation = document.getElementById('sttTranslation');
  const dialectBadge = document.getElementById('dialectBadge');

  if (sttTranscript) sttTranscript.innerText = `"${data.prisma_stt.transcript_codemix}"`;
  if (sttTranslation) sttTranslation.innerHTML = `<b>Certified Thana Translation:</b> "${data.prisma_stt.transcript_en}"`;
  if (dialectBadge) dialectBadge.innerText = data.call_telemetry.detected_lang;

  // 2. Evon Reasoning
  const evon = data.evon_reasoning;
  const crimeType = document.getElementById('crimeType');
  const amountAtStake = document.getElementById('amountAtStake');
  const jurisdictionVal = document.getElementById('jurisdictionVal');
  const emergencyTier = document.getElementById('emergencyTier');

  if (crimeType) crimeType.innerText = evon.incident_type;
  if (amountAtStake) amountAtStake.innerText = evon.extracted_facts.amount_at_stake || "N/A";
  if (jurisdictionVal) jurisdictionVal.innerText = evon.extracted_facts.jurisdiction_type;
  if (emergencyTier) emergencyTier.innerText = evon.emergency_tier;

  // Legal Sections List
  const sectionsList = document.getElementById('sectionsList');
  if (sectionsList) {
    sectionsList.innerHTML = '';
    evon.legal_sections.forEach(sec => {
      const item = document.createElement('div');
      item.className = 'section-item';
      item.innerHTML = `
        <div class="sec-badge">${sec.section}</div>
        <div class="sec-desc"><b>${sec.title}</b> - ${sec.relevance} <br/><span style="color:#94a3b8;font-size:0.7rem;">Penalty: ${sec.penalty}</span></div>
      `;
      sectionsList.appendChild(item);
    });
  }

  // 3. Timbre TTS
  const ttsPreviewText = document.getElementById('ttsPreviewText');
  const voicePersonaTag = document.getElementById('voicePersonaTag');

  if (ttsPreviewText) ttsPreviewText.innerText = `"${evon.timbre_voice_script}"`;
  if (voicePersonaTag) {
    voicePersonaTag.innerText = activePreset.includes('telugu') 
      ? "Voice: Kavya (Telugu Regional)" 
      : "Voice: Nalini (Hindi Regional)";
  }

  // 4. FIR Download
  const complaintCode = document.getElementById('complaintCode');
  const btnDownload = document.getElementById('btnDownloadPDF');

  if (complaintCode) complaintCode.innerText = `#${currentComplaintId}`;
  if (btnDownload) btnDownload.href = data.pdf_download_url;

  try {
    if (window.lucide) {
      lucide.createIcons();
    }
  } catch (err) {}
}

// Mic Recording Handling
async function startMicRecording() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    recordedAudioChunks = [];

    mediaRecorder.ondataavailable = e => {
      if (e.data.size > 0) recordedAudioChunks.push(e.data);
    };

    mediaRecorder.onstop = uploadRecordedAudio;
    mediaRecorder.start();

    isRecording = true;
    document.getElementById('btnRecordMic').classList.add('hidden');
    document.getElementById('btnStopRecord').classList.remove('hidden');
    document.getElementById('callStatusText').innerText = "Streaming live telephonic audio to Prisma v3.0...";
    document.getElementById('callStatusBanner').style.color = "#ef4444";
  } catch (err) {
    alert("Microphone access denied or unavailable: " + err.message);
  }
}

function stopMicRecording() {
  if (mediaRecorder && mediaRecorder.state !== 'inactive') {
    mediaRecorder.stop();
  }
  isRecording = false;
  document.getElementById('btnRecordMic').classList.remove('hidden');
  document.getElementById('btnStopRecord').classList.add('hidden');
  document.getElementById('callStatusText').innerText = "Processing live audio with Gnani Models...";
  document.getElementById('callStatusBanner').style.color = "#fbbf24";
}

async function uploadRecordedAudio() {
  const audioBlob = new Blob(recordedAudioChunks, { type: 'audio/wav' });
  const formData = new FormData();
  formData.append('audio', audioBlob, 'live_telephonic_call.wav');
  formData.append('caller_name', 'Live Citizen Caller');
  formData.append('caller_phone', '+91 99887 76655');

  try {
    const response = await fetch('/api/call/process-audio', {
      method: 'POST',
      body: formData
    });
    const data = await response.json();
    if (data.success) {
      updateDashboard(data);
      document.getElementById('callStatusText').innerText = "Live Call Analyzed & FIR Generated!";
      document.getElementById('callStatusBanner').style.color = "#34d399";
    }
  } catch (err) {
    console.error(err);
    document.getElementById('callStatusText').innerText = "Live processing error";
  }
}

// Play synthesized TTS guidance
window.playTTSGuidance = function() {
  const audio = new Audio('/api/audio/tts-sample');
  audio.play().catch(e => {
    console.log("Audio autoplay prevented or sample loaded, falling back to speech synthesis:", e);
    const previewEl = document.getElementById('ttsPreviewText');
    if (previewEl && 'speechSynthesis' in window) {
      const text = previewEl.innerText.replace(/"/g, '').replace(/<[^>]+>/g, '');
      const utter = new SpeechSynthesisUtterance(text);
      utter.rate = 0.95;
      window.speechSynthesis.speak(utter);
    }
  });
};
