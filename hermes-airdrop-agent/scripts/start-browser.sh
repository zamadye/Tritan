#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Launch Chrome with remote debugging (CDP) and verify the port is really open.
#
#   ./scripts/start-browser.sh
#
# Runs on the HOST with a real visible window. No Docker, no --no-sandbox,
# no VNC -- the window is the GUI.
#
# ---------------------------------------------------------------------------
# THE TRAP THIS SCRIPT EXISTS TO AVOID
# ---------------------------------------------------------------------------
# From Hermes' browser docs, verbatim:
#
#   "Chrome 136+ makes the dedicated profile mandatory. As a security
#    hardening change, Chrome 136 and later silently refuse to open the
#    remote debugging port when --remote-debugging-port is combined with the
#    *default* user-data-dir -- even from a cold start with no other Chrome
#    running. The browser launches normally but nothing ever listens on 9222,
#    so /browser connect fails with connection refused.
#    There is no error message."
#
# So: a dedicated --user-data-dir is not optional, and "Chrome looks like it
# opened" proves nothing. The only trustworthy check is an HTTP GET on
# /json/version. This script does that check and fails loudly.
# ---------------------------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

CDP_PORT="${HAA_CDP_PORT:-9222}"
CDP_URL="http://127.0.0.1:${CDP_PORT}"
PROFILE_DIR="${HAA_CHROME_PROFILE:-$HOME/.hermes/chrome-debug}"

[[ -f "$PROJECT_DIR/.env" ]] && set -a && . "$PROJECT_DIR/.env" && set +a

ok()   { printf '  \033[0;32m✓\033[0m %s\n' "$*"; }
info() { printf '  → %s\n' "$*"; }
err()  { printf '  \033[0;31m✗\033[0m %s\n' "$*" >&2; }

# ------------------------------------------------------- already running? ---
cdp_up() { curl -fsS -m 3 "$CDP_URL/json/version" >/dev/null 2>&1; }

if cdp_up; then
  ok "Chrome CDP already listening on $CDP_URL"
  curl -fsS -m 3 "$CDP_URL/json/version" | python3 -c \
    'import json,sys; d=json.load(sys.stdin); print("    browser:", d.get("Browser","?"))' 2>/dev/null || true
  info "profile: $PROFILE_DIR"
  exit 0
fi

# --------------------------------------------------------- find a browser ---
find_browser() {
  local c
  for c in google-chrome google-chrome-stable chromium chromium-browser brave-browser microsoft-edge; do
    command -v "$c" >/dev/null 2>&1 && { echo "$c"; return 0; }
  done
  # Common absolute paths the PATH may not cover.
  for c in /usr/bin/google-chrome /usr/bin/chromium /opt/google/chrome/google-chrome \
           /snap/bin/chromium /opt/brave-bin/brave-browser \
           "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
           "/Applications/Chromium.app/Contents/MacOS/Chromium" \
           "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" \
           "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"; do
    [[ -x "$c" ]] && { echo "$c"; return 0; }
  done
  return 1
}

BROWSER="$(find_browser || true)"
if [[ -z "$BROWSER" ]]; then
  err "No Chromium-family browser found."
  echo "    Install one of: google-chrome, chromium, brave-browser, microsoft-edge" >&2
  echo "    Debian/Ubuntu : sudo apt install -y chromium" >&2
  echo "    macOS         : brew install --cask google-chrome" >&2
  exit 1
fi
ok "browser: $BROWSER"

# -------------------------------------------------------------- no display? ---
# A real window needs a display. On a headless server there isn't one, and
# Chrome will fail or silently background itself.
if [[ -z "${DISPLAY:-}" && "$(uname -s)" == "Linux" && -z "${WAYLAND_DISPLAY:-}" ]]; then
  err "No DISPLAY set -- this machine has no graphical session."
  echo "    This setup runs Chrome on the host with a real window, which needs" >&2
  echo "    a desktop. On a headless server either:" >&2
  echo "      - run it where you have a desktop, or" >&2
  echo "      - use a containerised browser with VNC instead (not this script)." >&2
  exit 1
fi

# ------------------------------------------------------------------ launch ---
mkdir -p "$PROFILE_DIR"
info "profile dir : $PROFILE_DIR   (dedicated -- required by Chrome 136+)"
info "CDP port    : $CDP_PORT"

"$BROWSER" \
  --remote-debugging-port="$CDP_PORT" \
  --user-data-dir="$PROFILE_DIR" \
  --no-first-run \
  --no-default-browser-check \
  >/tmp/haa-chrome.log 2>&1 &

# ------------------------------------------------------------------ verify ---
echo -n "  → waiting for $CDP_URL/json/version "
for _ in $(seq 1 30); do
  if cdp_up; then echo; break; fi
  echo -n "."
  sleep 1
done

if ! cdp_up; then
  echo
  err "Port $CDP_PORT never opened."
  echo >&2
  echo "    The usual cause is exactly the Chrome 136+ trap: Chrome launched" >&2
  echo "    fine but refused to open the debug port. Check, in order:" >&2
  echo "      1. Is another Chrome already running with your DEFAULT profile?" >&2
  echo "         A new window joins that process, which has no debug port." >&2
  echo "         Close every Chrome window and re-run." >&2
  echo "      2. Is $PROFILE_DIR writable and not your default profile dir?" >&2
  echo "      3. Chrome log: /tmp/haa-chrome.log" >&2
  exit 1
fi

ok "CDP is live at $CDP_URL"
curl -fsS -m 3 "$CDP_URL/json/version" | python3 -c \
  'import json,sys; d=json.load(sys.stdin); print("    browser:", d.get("Browser","?"))' 2>/dev/null || true

cat <<DONE

Chrome ready. A real window should be visible on your desktop.

  CDP endpoint : $CDP_URL
  Profile      : $PROFILE_DIR
  Config       : browser.cdp_url in config/hermes/**/config.yaml already
                 points at $CDP_URL

Log into your accounts in that window now -- the session persists in the
profile directory, so you only do it once.

Check readiness with:  haa browser check

DONE
