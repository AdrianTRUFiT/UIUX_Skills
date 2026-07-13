#!/usr/bin/env bash
# Start the Evidence Intake Workstation locally (Linux/macOS).
# Evidence and the registry live under EIW_DATA_DIR
# (default: ~/EvidenceIntakeWorkstation) — never inside this repository.
set -euo pipefail
cd "$(dirname "$0")"

PORT="${EIW_PORT:-8741}"

if [ ! -d .venv ]; then
  python3 -m venv --system-site-packages .venv
fi
source .venv/bin/activate
pip install -q -r backend/requirements.txt || echo "pip install failed — continuing with system packages"

if [ ! -d frontend/dist ] && command -v npm >/dev/null; then
  echo "Building frontend (first run)..."
  (cd frontend && npm install --no-audit --no-fund && npm run build) \
    || echo "Frontend build failed — API still available at /api, docs at /docs"
fi

mkdir -p .run
echo "Evidence Intake Workstation on http://127.0.0.1:${PORT}"
python3 -m uvicorn --factory backend.app.main:create_app \
  --host 127.0.0.1 --port "${PORT}" &
echo $! > .run/uvicorn.pid
wait
