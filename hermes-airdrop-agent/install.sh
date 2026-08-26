#!/usr/bin/env bash
# ===========================================================================
# Hermes Airdrop Agent — one-click installer
# ===========================================================================
#
#   ./install.sh                 full install
#   ./install.sh --dry-run       print every step, change nothing
#   ./install.sh --skip-browser  don't install Camofox
#   ./install.sh --skip-hermes   reuse an existing Hermes install
#   ./install.sh --no-cron       don't schedule jobs
#
# Also works piped, though --dry-run is the safer first run:
#   curl -fsSL <raw-url>/install.sh | bash -s -- --dry-run
#
# What it does, in order:
#   1. check prerequisites (git, curl, python3)
#   2. install Hermes Agent  -> ~/.hermes/
#   3. install Camofox       -> Docker image, or the npm server
#   4. install this package  -> `haa` on PATH
#   5. lay down config, profiles, skills, SOUL files
#   6. create .env from .env.example  (NEVER overwrites an existing one)
#   7. schedule the cron jobs
#   8. run `haa doctor`
#
# Idempotent: re-running repairs a partial install without destroying state.
# ===========================================================================
set -euo pipefail

VERSION="0.1.0"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
HERMES_INSTALL_URL="https://hermes-agent.nousresearch.com/install.sh"
CAMOFOX_IMAGE="jo-inc/camofox-browser"
CAMOFOX_NPM="@askjo/camofox-browser"
CAMOFOX_PORT="${CAMOFOX_PORT:-9377}"

DRY_RUN=0
SKIP_BROWSER=0
SKIP_HERMES=0
SKIP_CRON=0
ASSUME_YES=0

HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
PROJECT_DIR="$SCRIPT_DIR"

# ---------------------------------------------------------------- output ---
if [[ -t 1 ]]; then
  C_G=$'\033[0;32m'; C_Y=$'\033[0;33m'; C_R=$'\033[0;31m'; C_C=$'\033[0;36m'; C_0=$'\033[0m'
else
  C_G=""; C_Y=""; C_R=""; C_C=""; C_0=""
fi

step()  { printf '\n%s==> %s%s\n' "$C_C" "$*" "$C_0"; }
info()  { printf '    %s\n' "$*"; }
ok()    { printf '    %s✓%s %s\n' "$C_G" "$C_0" "$*"; }
warn()  { printf '    %s!%s %s\n' "$C_Y" "$C_0" "$*" >&2; }
err()   { printf '    %s✗%s %s\n' "$C_R" "$C_0" "$*" >&2; }

# run <cmd...> — execute, or print in dry-run mode.
run() {
  if (( DRY_RUN )); then
    printf '    %s[dry-run]%s %s\n' "$C_Y" "$C_0" "$*"
    return 0
  fi
  "$@"
}

have() { command -v "$1" >/dev/null 2>&1; }

# compose_cmd — prefer the Docker Compose v2 plugin, fall back to the v1 binary.
compose_cmd() {
  if docker compose version >/dev/null 2>&1; then echo "docker compose"
  elif command -v docker-compose >/dev/null 2>&1; then echo "docker-compose"
  else return 1; fi
}

usage() {
  sed -n '2,30p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'
  exit 0
}

# ------------------------------------------------------------------ args ---
while (( $# )); do
  case "$1" in
    --dry-run)      DRY_RUN=1 ;;
    --skip-browser) SKIP_BROWSER=1 ;;
    --skip-hermes)  SKIP_HERMES=1 ;;
    --no-cron)      SKIP_CRON=1 ;;
    -y|--yes)       ASSUME_YES=1 ;;
    -h|--help)      usage ;;
    *) err "unknown option: $1"; exit 2 ;;
  esac
  shift
done

printf '%s\n' "Hermes Airdrop Agent installer v${VERSION}"
printf '%s\n' "==========================================="
(( DRY_RUN )) && warn "dry run — nothing will be changed"

# ------------------------------------------------------- 1. prerequisites ---
step "1/8  Checking prerequisites"
MISSING=()
for t in git curl python3; do
  if have "$t"; then ok "$t $( "$t" --version 2>&1 | head -1 )"; else MISSING+=("$t"); fi
done
# Hermes' installer fetches Node as a .tar.xz on Linux.
if [[ "$(uname -s)" == "Linux" ]] && ! have xz; then
  warn "xz-utils missing — Hermes' installer needs it on Linux"
  MISSING+=("xz-utils")
fi
if (( ${#MISSING[@]} )); then
  err "missing: ${MISSING[*]}"
  info "Debian/Ubuntu : sudo apt install -y ${MISSING[*]}"
  info "macOS         : brew install ${MISSING[*]}"
  exit 1
fi

PY_OK=$(python3 -c 'import sys; print(1 if sys.version_info >= (3,10) else 0)')
if [[ "$PY_OK" != "1" ]]; then
  err "Python 3.10+ required, found $(python3 --version 2>&1)"
  exit 1
fi
ok "Python $(python3 -c 'import platform;print(platform.python_version())')"

# ------------------------------------------------------------ 2. hermes ---
step "2/8  Hermes Agent"
if (( SKIP_HERMES )); then
  info "skipped (--skip-hermes)"
elif have hermes; then
  ok "already installed: $(command -v hermes)"
  info "update later with: hermes update"
else
  info "installing from ${HERMES_INSTALL_URL}"
  if (( DRY_RUN )); then
    run bash -c "curl -fsSL ${HERMES_INSTALL_URL} | bash"
  else
    curl -fsSL "$HERMES_INSTALL_URL" | bash
  fi
  export PATH="$HOME/.local/bin:$PATH"
  have hermes && ok "hermes installed" || warn "hermes not on PATH yet — open a new shell or: export PATH=\$HOME/.local/bin:\$PATH"
fi

# ----------------------------------------------------------- 3. camofox ---
step "3/8  Camofox browser (GUI, anti-detection Firefox)"
NOVNC_PORT="${NOVNC_PORT:-6080}"
if (( SKIP_BROWSER )); then
  info "skipped (--skip-browser)"
elif have docker; then
  info "starting via docker compose — GUI (noVNC) is on by default"
  if ! compose_cmd >/dev/null 2>&1; then
    err "docker is present but neither 'docker compose' nor 'docker-compose' works"
    exit 1
  fi
  if (( DRY_RUN )); then
    run $(compose_cmd) up -d camofox
  else
    ( cd "$PROJECT_DIR" && $(compose_cmd) up -d camofox )
  fi
  ok "container 'camofox-browser' requested"
  info "agent control API : http://localhost:${CAMOFOX_PORT}"
  info "GUI (watch/take over): http://localhost:${NOVNC_PORT}/vnc.html"
  info "first start downloads the Camoufox engine (~300MB)"
  if [[ -z "${VNC_PASSWORD:-}" ]]; then
    warn "VNC_PASSWORD is unset — the noVNC port is open to anyone who can reach it,"
    warn "and that browser is logged into your accounts. Set it in .env."
  fi
elif have npx; then
  info "Docker not found — falling back to the npm server with the GUI plugin"
  if (( DRY_RUN )); then
    run bash -c "ENABLE_VNC=1 npx -y ${CAMOFOX_NPM} &"
  else
    ENABLE_VNC=1 nohup npx -y "$CAMOFOX_NPM" >/tmp/camofox.log 2>&1 &
  fi
  info "GUI at http://localhost:${NOVNC_PORT}/vnc.html (logs: /tmp/camofox.log)"
  info "Docker is preferred: it survives reboots via --restart unless-stopped"
else
  warn "neither Docker nor npx found — install one, then re-run with --skip-hermes"
  err "without a browser no worker can do anything: airdrop work is GUI, not CLI"
  exit 1
fi

# -------------------------------------------------------- 4. this package ---
step "4/8  Installing the haa control plane"
cd "$PROJECT_DIR"
if (( DRY_RUN )); then
  run python3 -m pip install -e .
else
  if python3 -m pip install -e . >/dev/null 2>&1; then
    ok "haa installed"
  else
    warn "pip install failed (externally-managed environment?)"
    info "retrying with a venv at ${PROJECT_DIR}/.venv"
    python3 -m venv .venv
    ./.venv/bin/pip install -e . >/dev/null
    ln -sf "${PROJECT_DIR}/.venv/bin/haa" "$HOME/.local/bin/haa" 2>/dev/null || true
    ok "haa installed into .venv"
  fi
fi
export PATH="$HOME/.local/bin:$PATH"

# ------------------------------------------------------ 5. hermes config ---
step "5/8  Installing config, profiles and skills into ${HERMES_HOME}"
run mkdir -p "$HERMES_HOME" "$HERMES_HOME/skills" "$HERMES_HOME/profiles"
run mkdir -p "$PROJECT_DIR/data/campaigns" "$PROJECT_DIR/data/logs" \
             "$PROJECT_DIR/data/screenshots" "$PROJECT_DIR/browser-profiles"

install_file() {  # src dst
  local src="$1" dst="$2"
  if [[ -e "$dst" ]] && (( ! ASSUME_YES )); then
    run cp "$src" "${dst}.new"
    info "$(basename "$dst") exists — wrote $(basename "$dst").new for comparison"
  else
    run cp "$src" "$dst"
    ok "$(basename "$dst")"
  fi
}

install_file "$PROJECT_DIR/config/hermes/config.yaml" "$HERMES_HOME/config.yaml"

for pdir in "$PROJECT_DIR"/config/hermes/profiles/*/; do
  name="$(basename "$pdir")"
  run mkdir -p "$HERMES_HOME/profiles/$name"
  install_file "$pdir/config.yaml" "$HERMES_HOME/profiles/$name/config.yaml"
  if [[ -f "$pdir/SOUL.md" ]]; then
    install_file "$pdir/SOUL.md" "$HERMES_HOME/profiles/$name/SOUL.md"
  fi
done

for sdir in "$PROJECT_DIR"/skills/*/; do
  name="$(basename "$sdir")"
  run mkdir -p "$HERMES_HOME/skills/$name"
  install_file "$sdir/SKILL.md" "$HERMES_HOME/skills/$name/SKILL.md"
done

# --------------------------------------------------------------- 6. .env ---
step "6/8  Environment file"
ENV_FILE="$PROJECT_DIR/.env"
if [[ -e "$ENV_FILE" ]]; then
  ok ".env already present — left untouched"
else
  run cp "$PROJECT_DIR/.env.example" "$ENV_FILE"
  ok "created .env from .env.example"
fi
# Point the configs at this checkout. Absolute paths only — ${HAA_PROJECT_DIR}
# is substituted by Hermes at load time.
if (( ! DRY_RUN )) && [[ -e "$ENV_FILE" ]]; then
  chmod 600 "$ENV_FILE"
  for pair in "HAA_PROJECT_DIR=$PROJECT_DIR" "HAA_DATA_DIR=$PROJECT_DIR/data"; do
    key="${pair%%=*}"; val="${pair#*=}"
    if grep -q "^${key}=" "$ENV_FILE"; then
      sed -i.bak "s|^${key}=.*|${key}=${val}|" "$ENV_FILE" && rm -f "${ENV_FILE}.bak"
    else
      printf '%s=%s\n' "$key" "$val" >> "$ENV_FILE"
    fi
  done
  info "set HAA_PROJECT_DIR and HAA_DATA_DIR"
fi
warn "edit $ENV_FILE and add your model API key — the agent will not start without one"

# -------------------------------------------------------------- 7. cron ---
step "7/8  Scheduled jobs"
if (( SKIP_CRON )); then
  info "skipped (--no-cron)"
elif ! have hermes; then
  warn "hermes not on PATH — skipping. Run scripts/cron-jobs.sh after Hermes is available."
else
  run bash "$PROJECT_DIR/scripts/cron-jobs.sh"
fi

# ------------------------------------------------------------- 8. doctor ---
step "8/8  Health check"
if (( DRY_RUN )); then
  run haa doctor
  printf '\n%sDry run complete.%s No files were changed.\n' "$C_G" "$C_0"
  info "Re-run without --dry-run to install for real."
  exit 0
fi

export HAA_PROJECT_DIR="$PROJECT_DIR"
if have haa; then
  haa doctor || warn "doctor reported problems — see the ✗ lines above"
else
  warn "'haa' is not on PATH. Try: export PATH=\$HOME/.local/bin:\$PATH"
fi

cat <<NEXT

Next steps
----------
  1. Edit ${ENV_FILE} and add a model API key (one provider is enough).
  2. Start the browser :  ./scripts/start-browser.sh
  3. Check health      :  haa doctor
  4. Read the guide    :  README.md

NEXT
