#!/bin/bash
# start.sh — jalankan backend + frontend tanpa systemd (untuk dev/testing)
set -e

ROOT="$(cd "$(dirname "$0")" && pwd)"

echo "=== Starting polymarket-agent (backend) ==="
cd "$ROOT"
nohup .venv/bin/python main.py run > /tmp/polymarket-agent.log 2>&1 &
echo "Backend PID: $!"

echo "=== Starting polymarket-web (frontend) ==="
cd "$ROOT/web"
nohup node node_modules/.bin/next start -p 3000 > /tmp/polymarket-web.log 2>&1 &
echo "Frontend PID: $!"

echo ""
echo "Logs: tail -f /tmp/polymarket-agent.log"
echo "      tail -f /tmp/polymarket-web.log"
echo "Web:  http://localhost:3000"
