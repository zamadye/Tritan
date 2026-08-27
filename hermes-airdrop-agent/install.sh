#!/usr/bin/env bash
# ===========================================================================
# Hermes Airdrop Agent — system installer
# ===========================================================================
#
#   ./install.sh                full install
#   ./install.sh --dry-run      print every step, change nothing
#   ./install.sh --skip-chrome  don't install a browser
#   ./install.sh --skip-hermes  reuse an existing Hermes install
#   ./install.sh --no-cron      don't schedule jobs
#   ./install.sh --no-gateway   don't set up the Telegram gateway
#
# This is a SYSTEM installer, in the same sense as Hermes' own install.sh or a
# Python/Node installer: it puts the dependencies on the machine, lays the
# framework down into $HERMES_HOME, and leaves you with something that runs.
# It does not merely check for things and tell you to install them yourself.
#
# The step order deliberately mirrors Hermes' setup-hermes.sh:
#   toolchain -> runtime -> framework -> config -> skills -> memory -> verify
#
# Idempotent: re-running repairs a partial install without destroying state.
# Existing .env and config.yaml are never overwritten (a .new file is written
# alongside for comparison instead).
# ===========================================================================
set -euo pipefail

# Catat aktivitas ke dalam framework (ter-commit) supaya error bisa dilacak.
ALOG() { (( ${DRY_RUN:-0} )) && return 0   # dry-run tidak boleh menulis apa pun
         PYTHONPATH="$PROJECT_DIR/src" python3 -m hermes_airdrop.activity_log record \
          --source install --exit "$1" --error-file "${ERR_TMP:-/dev/null}" 2>/dev/null || true; }
trap 'ALOG $?' EXIT

VERSION="0.2.0"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
PROJECT_DIR="$SCRIPT_DIR"
HERMES_INSTALL_URL="https://hermes-agent.nousresearch.com/install.sh"
HERMES_GIT_URL="https://github.com/NousResearch/hermes-agent.git"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
CDP_PORT="${HAA_CDP_PORT:-9222}"

DRY_RUN=0 SKIP_CHROME=0 SKIP_HERMES=0 SKIP_CRON=0 SKIP_GATEWAY=0 ASSUME_YES=0

# ---------------------------------------------------------------- output ---
if [[ -t 1 ]]; then
  C_G=$'\033[0;32m'; C_Y=$'\033[0;33m'; C_R=$'\033[0;31m'; C_C=$'\033[0;36m'; C_0=$'\033[0m'
else
  C_G=""; C_Y=""; C_R=""; C_C=""; C_0=""
fi
step() { printf '\n%s==> %s%s\n' "$C_C" "$*" "$C_0"; }
info() { printf '    %s\n' "$*"; }
ok()   { printf '    %s✓%s %s\n' "$C_G" "$C_0" "$*"; }
warn() { printf '    %s!%s %s\n' "$C_Y" "$C_0" "$*" >&2; }
err()  { printf '    %s✗%s %s\n' "$C_R" "$C_0" "$*" >&2; }

run() {  # execute, or print in dry-run
  if (( DRY_RUN )); then printf '    %s[dry-run]%s %s\n' "$C_Y" "$C_0" "$*"; return 0; fi
  "$@"
}
have() { command -v "$1" >/dev/null 2>&1; }

usage() { sed -n '2,26p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0; }

# ------------------------------------------------------------------ args ---
while (( $# )); do
  case "$1" in
    --dry-run)      DRY_RUN=1 ;;
    --skip-chrome)  SKIP_CHROME=1 ;;
    --skip-hermes)  SKIP_HERMES=1 ;;
    --no-cron)      SKIP_CRON=1 ;;
    --no-gateway)   SKIP_GATEWAY=1 ;;
    -y|--yes)       ASSUME_YES=1 ;;
    -h|--help)      usage ;;
    *) err "unknown option: $1"; exit 2 ;;
  esac
  shift
done

printf '%s\n' "Hermes Airdrop Agent — system installer v${VERSION}"
printf '%s\n' "==================================================="
info "target: $HERMES_HOME"
(( DRY_RUN )) && warn "dry run — nothing will be changed"

# --------------------------------------------------- package manager detect ---
PKG=""
if   have apt-get;  then PKG=apt
elif have dnf;      then PKG=dnf
elif have yum;      then PKG=yum
elif have pacman;   then PKG=pacman
elif have zypper;   then PKG=zypper
elif have brew;     then PKG=brew
fi

SUDO=""
if [[ $EUID -ne 0 && "$PKG" != "brew" && -n "$PKG" ]]; then
  if have sudo; then SUDO="sudo"; else
    warn "not root and sudo is unavailable — system package installs will fail"
  fi
fi

pkg_install() {  # pkg_install <generic-name> <apt> <rpm> <arch> <brew>
  local generic="$1" a="${2:-$1}" r="${3:-$1}" p="${4:-$1}" b="${5:-$1}"
  case "$PKG" in
    apt)           run $SUDO apt-get install -y "$a" ;;
    dnf|yum)       run $SUDO "$PKG" install -y "$r" ;;
    pacman)        run $SUDO pacman -S --noconfirm "$p" ;;
    zypper)        run $SUDO zypper --non-interactive install "$r" ;;
    brew)          run brew install "$b" ;;
    *) warn "no package manager found — install '$generic' manually"; return 1 ;;
  esac
}

pkg_refresh() {
  case "$PKG" in
    apt)     run $SUDO apt-get update -qq ;;
    dnf|yum) run $SUDO "$PKG" makecache -q ;;
    pacman)  run $SUDO pacman -Sy ;;
    zypper)  run $SUDO zypper --non-interactive refresh ;;
  esac
}

# ============================================================ 1. toolchain ===
step "1/10  System packages"
if [[ -z "$PKG" ]]; then
  warn "could not detect a package manager (apt/dnf/yum/pacman/zypper/brew)"
  warn "you will need to install git, curl, xz, ripgrep and a Chromium browser yourself"
else
  ok "package manager: $PKG${SUDO:+ (via $SUDO)}"
  pkg_refresh || true
  for spec in "git:git:git:git:git" "curl:curl:curl:curl:curl" \
              "xz:xz-utils:xz:xz:xz" "ripgrep:ripgrep:ripgrep:ripgrep:ripgrep"; do
    IFS=: read -r g a r p b <<<"$spec"
    if have "${g/xz/xz}"; then ok "$g present"; else
      info "installing $g"
      pkg_install "$g" "$a" "$r" "$p" "$b" || warn "could not install $g"
    fi
  done
fi

# ============================================================== 2. python ===
step "2/10  Python"
PY=""
for c in python3 python3.12 python3.11 python; do
  if have "$c" && "$c" -c 'import sys; raise SystemExit(0 if sys.version_info>=(3,10) else 1)' 2>/dev/null; then
    PY="$c"; break
  fi
done
if [[ -n "$PY" ]]; then
  ok "$($PY --version 2>&1) at $(command -v "$PY")"
else
  info "Python 3.10+ not found — installing"
  if [[ "$PKG" == "brew" ]]; then pkg_install python python python python python
  else pkg_install python3 python3 python3 python python3; fi
  if have python3; then PY=python3; ok "$(python3 --version 2>&1)"; else
    err "Python 3.10+ is required and could not be installed automatically"; exit 1
  fi
fi

# ================================================================ 3. node ===
step "3/10  Node.js"
if have node; then
  ok "node $(node --version)"
else
  info "Node.js not found — installing"
  # Hermes' own installer manages Node for its runtime; we need it available
  # for the browser harness and any npx-based tooling.
  if [[ "$PKG" == "brew" ]]; then pkg_install node node node node node
  else pkg_install nodejs nodejs nodejs nodejs node; fi
  have node && ok "node $(node --version)" || warn "Node.js unavailable — some optional tooling will be skipped"
fi

# ============================================================== 4. chrome ===
step "4/10  Browser: your real Chrome, via CDP"
# The airdrop flow leans on wallet-as-extension (MetaMask/Phantom/Rabby), which
# lives in the operator's real Chrome profile. A bare apt Chromium does not
# carry those extensions, so Chrome is the required default and Chromium only
# via explicit HAA_ALLOW_CHROMIUM=1. CDP works with either; the PROFILE is what
# matters. See scripts/start-browser.sh for the full rationale.
find_chrome() {
  local c
  for c in google-chrome google-chrome-stable google-chrome-beta google-chrome-dev; do
    have "$c" && { echo "$c"; return 0; }
  done
  for c in /usr/bin/google-chrome /opt/google/chrome/google-chrome \
           "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"; do
    [[ -x "$c" ]] && { echo "$c"; return 0; }
  done
  return 1
}
find_chromium() {
  local c
  for c in chromium chromium-browser brave-browser microsoft-edge; do
    have "$c" && { echo "$c"; return 0; }
  done
  for c in /usr/bin/chromium /snap/bin/chromium /opt/brave-bin/brave-browser; do
    [[ -x "$c" ]] && { echo "$c"; return 0; }
  done
  return 1
}
pick_browser() {
  if [[ -n "${HAA_BROWSER_BIN:-}" ]]; then echo "$HAA_BROWSER_BIN"; return 0; fi
  local g; g="$(find_chrome || true)"; [[ -n "$g" ]] && { echo "$g"; return 0; }
  if [[ "${HAA_ALLOW_CHROMIUM:-0}" == "1" ]]; then find_chromium || true; fi
}
BROWSER="$(pick_browser || true)"
if (( SKIP_CHROME )); then
  info "skipped (--skip-chrome)"
elif [[ -n "$BROWSER" ]]; then
  ok "found: $BROWSER"
elif [[ "$PKG" == "brew" ]]; then
  info "installing Google Chrome via Homebrew cask"
  run brew install --cask google-chrome
else
  # Pasang Chrome resmi via .deb — apt ikut menarik dependensi X11 yang dibutuhkan
  # untuk membuka window headed. Best-effort; gagal tidak menghentikan instalasi.
  if (( DRY_RUN )); then
    run curl -fsSL -o /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    run $SUDO apt-get install -y /tmp/google-chrome.deb
  elif [[ "$PKG" == "apt" ]]; then
    info "Google Chrome tidak ditemukan — memasang via .deb resmi"
    if curl -fsSL -o /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb; then
      run $SUDO apt-get install -y /tmp/google-chrome.deb || warn "apt install Chrome gagal — pasang manual google.com/chrome"
    else
      warn "unduh .deb gagal — pasang manual google.com/chrome (Chromium: HAA_ALLOW_CHROMIUM=1)"
    fi
  else
    warn "pasang manual: google.com/chrome (Chromium fallback: HAA_ALLOW_CHROMIUM=1)"
  fi
fi
# Dependensi display + alat verifikasi window headed (xdotool/wmctrl), best-effort.
if [[ "$PKG" == "apt" ]]; then
  info "memastikan libs X11 + xdotool/wmctrl agar window benar-benar terbuka"
  run $SUDO apt-get install -y --no-install-recommends libnss3 libnspr4 libgbm1 \
      libxkbcommon0 libgtk-3-0 libasound2 libx11-xcb1 xdotool wmctrl x11-utils \
      || warn "sebagian dependensi display gagal (butuh sudo)"
fi
BROWSER="$(pick_browser || true)"
[[ -n "$BROWSER" ]] && ok "browser ready: $BROWSER" \
                    || warn "no browser yet — ./scripts/start-browser.sh will explain"

# =============================================================== 5. hermes ===
step "5/10  Hermes Agent framework"
if (( SKIP_HERMES )); then
  info "skipped (--skip-hermes)"
elif have hermes; then
  ok "already installed: $(command -v hermes)"
  info "update later with: hermes update"
else
  # The repo is ~240MB with full history (226k objects) — over a slow link the
  # official full clone can look frozen for hours. Default to a SHALLOW clone
  # (--depth 1) plus the repo's own setup-hermes.sh, which is far smaller, and
  # fall back to the official installer only if that fails. Force the official
  # full install with HAA_HERMES_FULL=1.
  HERMES_REPO="$HERMES_HOME/hermes-agent"
  if (( DRY_RUN )); then
    run git clone --depth 1 "$HERMES_GIT_URL" "$HERMES_REPO"
    run bash "$HERMES_REPO/setup-hermes.sh"
  elif (( ${HAA_HERMES_FULL:-0} == 1 )); then
    info "full official install (HAA_HERMES_FULL=1) — large download"
    curl -fsSL "$HERMES_INSTALL_URL" | bash -s -- --skip-browser   # kita pakai CDP Chrome; lewati unduh browser/Playwright Hermes yang lambat
  elif [[ -d "$HERMES_REPO/.git" ]] || git clone --depth 1 "$HERMES_GIT_URL" "$HERMES_REPO"; then
    info "shallow clone ready — running setup-hermes.sh (venv + symlink)"
    bash "$HERMES_REPO/setup-hermes.sh" \
      || { warn "setup-hermes.sh failed; falling back to official installer"; \
           curl -fsSL "$HERMES_INSTALL_URL" | bash -s -- --skip-browser; }
  else
    warn "shallow clone failed; falling back to official installer (full clone)"
    curl -fsSL "$HERMES_INSTALL_URL" | bash -s -- --skip-browser   # kita pakai CDP Chrome; lewati unduh browser/Playwright Hermes yang lambat
  fi
  export PATH="$HOME/.local/bin:$PATH"
  have hermes && ok "hermes installed" \
              || warn "hermes not on PATH yet — open a new shell, or: export PATH=\$HOME/.local/bin:\$PATH"
fi

# ================================================================== 6. haa ===
step "6/10  Control plane (haa)"
cd "$PROJECT_DIR"
if (( DRY_RUN )); then
  run "$PY" -m venv .venv
  run .venv/bin/pip install -e .
else
  [[ -d .venv ]] || "$PY" -m venv .venv
  ./.venv/bin/pip install --quiet --upgrade pip
  if ./.venv/bin/pip install --quiet -e .; then
    mkdir -p "$HOME/.local/bin"
    ln -sf "$PROJECT_DIR/.venv/bin/haa" "$HOME/.local/bin/haa"
    ok "haa -> \$HOME/.local/bin/haa"
  else
    err "pip install failed"; exit 1
  fi
fi
export PATH="$HOME/.local/bin:$PATH"

# ==================================================== 7. config + profiles ===
step "7/10  Config, profiles and SOUL.md -> $HERMES_HOME"
run mkdir -p "$HERMES_HOME" "$HERMES_HOME/skills" "$HERMES_HOME/profiles" "$HERMES_HOME/memories"
run mkdir -p "$PROJECT_DIR/data/campaigns" "$PROJECT_DIR/data/logs" \
             "$PROJECT_DIR/data/screenshots" "$PROJECT_DIR/browser-profiles"

install_file() {  # src dst
  local src="$1" dst="$2"
  if [[ -e "$dst" ]] && (( ! ASSUME_YES )); then
    run cp "$src" "${dst}.new"
    info "$(basename "$dst") exists — wrote $(basename "$dst").new for comparison"
  else
    run cp "$src" "$dst"
    ok "→ ${dst#"$HERMES_HOME"/}"
  fi
}

install_file "$PROJECT_DIR/config/hermes/config.yaml" "$HERMES_HOME/config.yaml"

for pdir in "$PROJECT_DIR"/config/hermes/profiles/*/; do
  name="$(basename "$pdir")"
  run mkdir -p "$HERMES_HOME/profiles/$name"
  install_file "$pdir/config.yaml" "$HERMES_HOME/profiles/$name/config.yaml"
  [[ -f "$pdir/SOUL.md" ]] && install_file "$pdir/SOUL.md" "$HERMES_HOME/profiles/$name/SOUL.md"
done

# =============================================================== 8. skills ===
step "8/10  Skills -> $HERMES_HOME/skills"
for sdir in "$PROJECT_DIR"/skills/*/; do
  name="$(basename "$sdir")"
  run mkdir -p "$HERMES_HOME/skills/$name"
  install_file "$sdir/SKILL.md" "$HERMES_HOME/skills/$name/SKILL.md"
done

# ===================================================== 9. memory + knowledge ===
step "9/10  Memory and knowledge base"
if [[ -d "$PROJECT_DIR/config/hermes/memories" ]]; then
  for m in "$PROJECT_DIR"/config/hermes/memories/*.md; do
    [[ -f "$m" ]] && install_file "$m" "$HERMES_HOME/memories/$(basename "$m")"
  done
fi
if [[ -d "$PROJECT_DIR/knowledge" ]]; then
  run mkdir -p "$HERMES_HOME/knowledge"
  for k in "$PROJECT_DIR"/knowledge/*.md; do
    [[ -f "$k" ]] && install_file "$k" "$HERMES_HOME/knowledge/$(basename "$k")"
  done
fi

# ================================================================= 10. env ===
step "10/10  Environment, gateway, schedule, verification"
ENV_FILE="$PROJECT_DIR/.env"
if [[ -e "$ENV_FILE" ]]; then
  ok ".env already present — left untouched"
else
  run cp "$PROJECT_DIR/.env.example" "$ENV_FILE"
  ok "created .env from .env.example"
fi
# Populate the paths the configs interpolate, then make Hermes actually see
# the file. The linking is the part that is easy to miss and expensive to
# debug: without it every ${VAR} in the configs resolves to the literal string
# "${VAR}", and Hermes fails looking like it has a bad model name.
if [[ -e "$ENV_FILE" ]] || (( DRY_RUN )); then
  if (( ! DRY_RUN )); then
    chmod 600 "$ENV_FILE"
    for pair in "HAA_PROJECT_DIR=$PROJECT_DIR" "HAA_DATA_DIR=$PROJECT_DIR/data" \
                "HAA_CDP_PORT=$CDP_PORT" \
                "HAA_CHROME_PROFILE=$HOME/.hermes/chrome-debug"; do
      key="${pair%%=*}"; val="${pair#*=}"
      if grep -qE "^#?\s*${key}=" "$ENV_FILE"; then
        sed -i.bak -E "s|^#?\s*${key}=.*|${key}=${val}|" "$ENV_FILE" && rm -f "${ENV_FILE}.bak"
      else
        printf '%s=%s\n' "$key" "$val" >> "$ENV_FILE"
      fi
    done
    ok "set HAA_PROJECT_DIR, HAA_DATA_DIR, HAA_CDP_PORT, HAA_CHROME_PROFILE"
  else
    info "would set HAA_PROJECT_DIR, HAA_DATA_DIR, HAA_CDP_PORT, HAA_CHROME_PROFILE"
  fi

  # Hermes reads $HERMES_HOME/.env -- and a profile is a SEPARATE Hermes home
  # with its OWN .env. Symlinked, not copied, so there is one file to edit.
  link_env() {  # link_env <hermes-home-dir>
    local dir="$1" dst="$1/.env"
    run mkdir -p "$dir"
    if [[ -L "$dst" ]]; then
      run rm -f "$dst"
    elif [[ -e "$dst" ]] && (( ! ASSUME_YES )); then
      run mv "$dst" "${dst}.bak"
    fi
    run ln -s "$ENV_FILE" "$dst"
  }

  link_env "$HERMES_HOME"
  ok "linked .env -> \$HERMES_HOME/.env"
  NPROF=$(find "$PROJECT_DIR"/config/hermes/profiles -mindepth 1 -maxdepth 1 -type d | wc -l)
  for pdir in "$PROJECT_DIR"/config/hermes/profiles/*/; do
    link_env "$HERMES_HOME/profiles/$(basename "$pdir")"
  done
  ok "linked .env into $NPROF profile homes"
else
  warn "no .env to link — copy .env.example to .env first, then re-run"
fi

# --- Telegram gateway ------------------------------------------------------
if (( SKIP_GATEWAY )); then
  info "Telegram gateway skipped (--no-gateway)"
elif ! have hermes; then
  warn "hermes not on PATH — skipping gateway setup"
else
  TOKEN="$(grep -E '^TELEGRAM_BOT_TOKEN=' "$ENV_FILE" 2>/dev/null | cut -d= -f2- || true)"
  if [[ -z "$TOKEN" ]]; then
    warn "TELEGRAM_BOT_TOKEN is empty in .env — the Telegram UI will not start"
    info "get one from @BotFather, put it in $ENV_FILE, then run: hermes gateway setup"
  elif (( DRY_RUN )); then
    run hermes gateway setup
  else
    info "Telegram token found — registering the gateway"
    hermes gateway setup || warn "gateway setup needs interaction; run: hermes gateway setup"
  fi
fi

# --- cron ------------------------------------------------------------------
if (( SKIP_CRON )); then
  info "cron skipped (--no-cron)"
elif ! have hermes; then
  warn "hermes not on PATH — run scripts/cron-jobs.sh once it is available"
else
  run bash "$PROJECT_DIR/scripts/cron-jobs.sh"
fi

# --- verification ----------------------------------------------------------
if (( DRY_RUN )); then
  run "$PROJECT_DIR/.venv/bin/haa" doctor
  printf '\n%sDry run complete.%s Nothing was changed.\n' "$C_G" "$C_0"
  exit 0
fi

cat <<NEXT

Installed. What to do now
-------------------------
  1. Put your model API key in      : $ENV_FILE
     Put your Telegram bot token in : TELEGRAM_BOT_TOKEN (same file)

  2. Start the browser (real window, logs you in once):
       ./scripts/start-browser.sh

  3. Start the Telegram gateway:
       hermes --profile worker-orchestrator gateway run

  4. Then just message your bot on Telegram.

Verify at any time:
       haa doctor          # full health check
       haa browser check   # is Chrome reachable over CDP

NEXT

if have haa; then
  haa doctor || warn "doctor reported problems — see the ✗ lines above"
fi
