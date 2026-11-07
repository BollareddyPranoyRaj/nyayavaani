#!/bin/bash
set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "================================================================="
echo "   NYAYAVAANI (न्यायवाणी / న్యాయవాణి) - AI FIRST-RESPONDER"
echo "      Powered by Gnani.ai (Prisma v3.0, Evon 30B, Timbre v3.0)"
echo "================================================================="

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

echo ""
echo "🚀 Starting NyayaVaani Tactical Dispatch Server..."
echo "📡 Open your browser at: http://localhost:8000"
echo "Press Ctrl+C to terminate."
echo ""

uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload
