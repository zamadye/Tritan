#!/usr/bin/env bash
# ===========================================================================
# Buka Chrome headed (window NYATA) dengan CDP, lalu biarkan hidup untuk agent.
#
#   ./scripts/start-browser.sh              buka / pastikan window terbuka
#   ./scripts/start-browser.sh --restart    tutup Chrome lama, buka baru
#   ./scripts/start-browser.sh --stop       tutup Chrome debug
#
# Kenapa ini penting & berbeda dari "sekadar CDP up":
#   Anda harus MELIHAT window-nya untuk login ke semua account (wallet, X,
#   Discord, dApp). Agent kemudian menempel ke window yang SAMA lewat CDP.
#   Jadi script ini tidak puas dengan "port 9222 menjawab" — ia berusaha
#   memastikan sebuah WINDOW benar-benar terbuka di display Anda.
#
# Script ini juga memasang dependensi runtime Chrome + alat display (xdotool/
# wmctrl) bila kurang, karena di pemakaian nyata sering kali libs X11 belum
# lengkap dan Chrome gagal membuka window secara diam-diam.
# ===========================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

CDP_PORT="${HAA_CDP_PORT:-9222}"
CDP_URL="http://127.0.0.1:${CDP_PORT}"
PROFILE_DIR="${HAA_CHROME_PROFILE:-$HOME/.hermes/chrome-debug}"
START_URL="${HAA_BROWSER_START_URL:-about:blank}"
LOG=/tmp/haa-chrome.log

[[ -f "$PROJECT_DIR/.env" ]] && set -a && . "$PROJECT_DIR/.env" && set +a

ok()   { printf '  \033[0;32m✓\033[0m %s\n' "$*"; }
info() { printf '  → %s\n' "$*"; }
warn() { printf '  \033[0;33m!\033[0m %s\n' "$*" >&2; }
err()  { printf '  \033[0;31m✗\033[0m %s\n' "$*" >&2; }

ALOG() { PYTHONPATH="$PROJECT_DIR/src" python3 -m hermes_airdrop.activity_log record \
          --source start-browser --exit "$1" --error-file "$LOG" 2>/dev/null || true; }
trap 'ALOG $?' EXIT

MODE="${1:-start}"

cdp_up() { curl -fsS -m 3 "$CDP_URL/json/version" >/dev/null 2>&1; }
open_tabs() { curl -fsS -m 3 "$CDP_URL/json/list" 2>/dev/null | python3 -c \
    'import json,sys; print(len(json.load(sys.stdin)))' 2>/dev/null || echo 0; }
pid_on_port() {
  if command -v lsof >/dev/null 2>&1; then lsof -ti tcp:"$1" 2>/dev/null | head -1
  elif command -v fuser >/dev/null 2>&1; then fuser "$1/tcp" 2>/dev/null | tr -s ' ' '\n' | head -1
  elif command -v ss >/dev/null 2>&1; then ss -tlnp "sport = :$1" 2>/dev/null | grep -oE 'pid=[0-9]+' | head -1 | cut -d= -f2
  fi
}
stop_chrome() {
  local pid; pid="$(pid_on_port "$CDP_PORT")"; [[ -n "$pid" ]] && kill "$pid" 2>/dev/null
  pkill -f "user-data-dir=$PROFILE_DIR" 2>/dev/null || true
  for _ in $(seq 1 10); do cdp_up || return 0; sleep 1; done
  return 1
}

# ------------------------------------------------------------- find chrome ---
find_chrome() {
  local c
  for c in google-chrome google-chrome-stable google-chrome-beta; do
    command -v "$c" >/dev/null 2>&1 && { echo "$c"; return 0; }
  done
  for c in /usr/bin/google-chrome /opt/google/chrome/google-chrome \
           "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
    [[ -x "$c" ]] && { echo "$c"; return 0; }
  done
  return 1
}

# ------------------------------------------------------- display & deps ------
have_apt() { command -v apt-get >/dev/null 2>&1; }

install_deps() {
  # Runtime libs Chrome butuh untuk membuka window + alat verifikasi window.
  # Best-effort: gagal tidak fatal (mis. tanpa sudo), tapi dicatat.
  have_apt || return 0
  local SUDO=""; command -v sudo >/dev/null 2>&1 && [[ $EUID -ne 0 ]] && SUDO="sudo"
  info "memastikan dependensi Chrome + display (lib X11, xdotool, wmctrl)…"
  $SUDO apt-get install -y --no-install-recommends \
    libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 \
    libxkbcommon0 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 \
    libasound2 libpango-1.0-0 libcairo2 libx11-xcb1 libgtk-3-0 \
    xdotool wmctrl x11-utils >/dev/null 2>&1 \
    || warn "gagal memasang sebagian dependensi (butuh sudo). Lihat log apt."
}

resolve_display() {
  # Window butuh display. Kalau dijalankan dari SSH (DISPLAY kosong), coba
  # display desktop yang sedang aktif (:0/:1) atau override HAA_DISPLAY.
  if [[ -n "${HAA_DISPLAY:-}" ]]; then echo "$HAA_DISPLAY"; return; fi
  if [[ -n "${DISPLAY:-}" ]]; then echo "$DISPLAY"; return; fi
  if [[ -n "${WAYLAND_DISPLAY:-}" ]]; then echo "wayland"; return; fi
  for d in :0 :1; do
    if DISPLAY="$d" xdpyinfo >/dev/null 2>&1; then echo "$d"; return; fi
  done
  echo ""
}
# Display X nyata (untuk mem-set DISPLAY & verifikasi). Kosong bila wayland.
x_display() { [[ "${1:-}" == :?* ]] && echo "$1"; }

window_open() {
  # Benar-benar ada window Chrome? Pakai xdotool/wmctrl bila ada.
  [[ -n "$XD" ]] || return 1   # wayland: verifikasi window tidak didukung xdotool
  if command -v xdotool >/dev/null 2>&1; then
    DISPLAY="$XD" xdotool search --class "chrome" >/dev/null 2>&1 && return 0
    DISPLAY="$XD" xdotool search --class "Chromium" >/dev/null 2>&1 && return 0
  fi
  if command -v wmctrl >/dev/null 2>&1; then
    DISPLAY="$XD" wmctrl -l 2>/dev/null | grep -qi "chrome" && return 0
  fi
  return 1
}

# ------------------------------------------------------------------ stop -----
if [[ "$MODE" == "--stop" ]]; then
  stop_chrome && ok "Chrome debug ditutup" || warn "port masih ditempati"
  exit 0
fi

# ---------------------------------------------------------------- restart ----
[[ "$MODE" == "--restart" ]] && { info "menutup Chrome lama…"; stop_chrome || { err "port $CDP_PORT masih ditempati; tutup manual"; exit 1; }; }

BROWSER="$(find_chrome || true)"
if [[ -z "$BROWSER" ]]; then
  err "Google Chrome tidak ditemukan."
  echo "    Pasang: sudo apt install google-chrome-stable  (atau unduh google.com/chrome)" >&2
  echo "    Chromium TIDAK disarankan (tanpa extension wallet Anda)." >&2
  exit 1
fi
ok "browser: $BROWSER"

install_deps
USE_DISPLAY="$(resolve_display)"
if [[ -z "$USE_DISPLAY" ]]; then
  err "Tidak ada display yang bisa dipakai."
  echo "    Jalankan script ini dari terminal DI DALAM desktop Anda," >&2
  echo "    atau set HAA_DISPLAY=:0 (display desktop yang aktif)." >&2
  exit 1
fi
XD="$(x_display "$USE_DISPLAY")"   # kosong bila wayland (pakai env apa adanya)
ok "display: $USE_DISPLAY"

# ---------------------------------------------------------------- launch ----
# Chrome 136+ menolak membuka port debug bila --user-data-dir adalah profil
# default, tanpa pesan error. Profil khusus ini menghindarinya.
mkdir -p "$PROFILE_DIR"
info "profile: $PROFILE_DIR"
info "membuka window Chrome (headed)…"

env ${XD:+DISPLAY=$XD} nohup "$BROWSER" \
  --remote-debugging-port="$CDP_PORT" \
  --user-data-dir="$PROFILE_DIR" \
  --no-first-run --no-default-browser-check \
  --start-maximized \
  "$START_URL" >"$LOG" 2>&1 &
disown 2>/dev/null || true

# ---------------------------------------------------------------- verify ----
echo -n "  → menunggu CDP "
for _ in $(seq 1 30); do cdp_up && { echo; break; }; echo -n "."; sleep 1; done
if ! cdp_up; then
  echo; err "CDP tidak terbuka. Log:"; tail -5 "$LOG" >&2
  echo "    Penyebab umum: Chrome lain dengan profile default sudah jalan," >&2
  echo "    atau libs X11 kurang. Jalankan: ./scripts/start-browser.sh --restart" >&2
  exit 1
fi
ok "CDP: $CDP_URL"

# Pastikan ada window NYATA (bukan proses tanpa jendela).
sleep 2
if window_open; then
  ok "window Chrome TERBUKA di display $USE_DISPLAY"
else
  warn "CDP hidup tapi tidak terdeteksi window (xdotool/wmctrl tak tersedia atau window minim)."
  echo "    Cek manual: apakah ada window Chrome? Jika tidak, lihat $LOG" >&2
fi
if [[ "$(open_tabs)" == "0" ]]; then
  curl -fsS -m 3 -X PUT "$CDP_URL/json/new?$START_URL" >/dev/null 2>&1 || true
fi

cat <<DONE

  Browser siap. PENTING:
  1. Window Chrome itu adalah tempat Anda LOGIN ke semua account
     (wallet, X, Discord, dApp). Login sekarang — sesi tersimpan di profil.
  2. JANGAN tutup window-nya; agent menempel ke window yang sama.
  3. Lalu jalankan agent:  ./scripts/debug-agent.sh onboard "<url>"

  Ulang buka:  ./scripts/start-browser.sh --restart
  Tutup:       ./scripts/start-browser.sh --stop
DONE
