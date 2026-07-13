#!/usr/bin/env bash
# Stop the Evidence Intake Workstation started by run.sh.
cd "$(dirname "$0")"
if [ -f .run/uvicorn.pid ]; then
  kill "$(cat .run/uvicorn.pid)" 2>/dev/null && echo "stopped" || echo "not running"
  rm -f .run/uvicorn.pid
else
  echo "no pid file — nothing to stop"
fi
