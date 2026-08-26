#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Start the Camofox GUI browser server and confirm BOTH endpoints answer:
#   :9377  agent control API   (what Hermes talks to)
#   :6080  noVNC GUI           (what YOU watch and take over through)
#
# The GUI check is not optional. Camofox runs on an Xvfb display at 1x1
# resolution unless the VNC plugin is enabled — so without :6080 the browser
# is unwatchable and nobody can solve the CAPTCHA or MFA prompt the agent
# halts on.
# ---------------------------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
PORT="${CAMOFOX_PORT:-9377}"
NOVNC="${NOVNC_PORT:-6080}"
API="http://localhost:${PORT}"
GUI="http://localhost:${NOVNC}/vnc.html"

[[ -f "$PROJECT_DIR/.env" ]] && set -a && . "$PROJECT_DIR/.env" && set +a

compose_cmd() {
  if docker compose version >/dev/null 2>&1; then echo "docker compose"
  elif command -v docker-compose >/dev/null 2>&1; then echo "docker-compose"
  else return 1; fi
}

up() {
  if compose_cmd >/dev/null 2>&1; then
    ( cd "$PROJECT_DIR" && $(compose_cmd) up -d camofox )
  elif command -v npx >/dev/null 2>&1; then
    echo "→ no Docker; starting the npm server with the GUI plugin"
    ENABLE_VNC=1 nohup npx -y @askjo/camofox-browser >/tmp/camofox.log 2>&1 &
  else
    echo "✗ Need Docker (preferred) or Node.js." >&2
    exit 1
  fi
}

if curl -fsS -m 5 -o /dev/null "$API" 2>/dev/null; then
  echo "✓ Camofox API already responding at ${API}"
else
  up
fi

echo -n "→ waiting for the control API at ${API} "
for _ in $(seq 1 90); do
  if curl -fsS -m 3 -o /dev/null "$API" 2>/dev/null; then echo; break; fi
  echo -n "."; sleep 2
done
curl -fsS -m 5 -o /dev/null "$API" 2>/dev/null || {
  echo; echo "✗ control API did not come up within 180s." >&2
  echo "  docker compose logs camofox   (or: cat /tmp/camofox.log)" >&2
  exit 1; }
echo "✓ control API up at ${API}"

echo -n "→ waiting for the GUI at ${GUI} "
GUI_OK=0
for _ in $(seq 1 45); do
  if curl -fsS -m 3 -o /dev/null "$GUI" 2>/dev/null; then GUI_OK=1; echo; break; fi
  echo -n "."; sleep 2
done

if (( GUI_OK )); then
  echo "✓ GUI up at ${GUI}"
  [[ -z "${VNC_PASSWORD:-}" ]] && \
    echo "  ! VNC_PASSWORD is unset — set it in .env; this port drives a browser" \
         "that is logged into your accounts"
else
  echo
  echo "✗ The GUI is not reachable. The browser is running UNWATCHABLE:" >&2
  echo "  you will not be able to take over for a CAPTCHA or MFA prompt." >&2
  echo "  Fix: make sure ENABLE_VNC=1 is set for the Camofox server." >&2
  echo "       'docker compose up -d camofox' does this by default;" >&2
  echo "       the 'headless' profile deliberately does not." >&2
  exit 1
fi

cat <<DONE

Camofox ready.
  agent API : ${API}
  GUI       : ${GUI}

Set in .env:  CAMOFOX_URL=${API}

Sessions persist per worker (browser.camofox.user_id), so logins survive
restarts. Each worker keeps its own profile:
  haa-worker-analyzer / -daily / -quests / -discord / -monitor

Check readiness with:  haa browser check
DONE
