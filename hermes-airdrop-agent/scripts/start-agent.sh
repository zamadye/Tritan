#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Start Hermes with one of the airdrop worker profiles.
#
#   ./scripts/start-agent.sh                # interactive, default profile
#   ./scripts/start-agent.sh analyzer       # interactive analyzer
#   ./scripts/start-agent.sh daily -q "Run today's check-ins"
# ---------------------------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

[[ -f "$PROJECT_DIR/.env" ]] && set -a && . "$PROJECT_DIR/.env" && set +a

if ! command -v hermes >/dev/null 2>&1; then
  echo "✗ 'hermes' not found. Run ./install.sh, or: export PATH=\$HOME/.local/bin:\$PATH" >&2
  exit 1
fi
if ! command -v haa >/dev/null 2>&1; then
  echo "✗ 'haa' not found. Run ./install.sh" >&2
  exit 1
fi

PROFILE="${1:-analyzer}"; shift || true
VALID=(analyzer daily quests discord monitor)
case " ${VALID[*]} " in
  *" ${PROFILE} "*) ;;
  *) echo "✗ unknown profile '${PROFILE}'. Valid: ${VALID[*]}" >&2; exit 2 ;;
esac

# Cheap preflight: no point starting a browser agent that cannot reach a model
# or a browser.
echo "→ preflight"
haa doctor --config "${HERMES_HOME:-$HOME/.hermes}/config.yaml" || {
  echo "✗ preflight failed — fix the problems above before starting" >&2
  exit 1
}

echo "→ starting worker-${PROFILE}"
exec hermes --profile "worker-${PROFILE}" "$@"
