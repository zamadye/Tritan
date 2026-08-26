#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Remove what install.sh put in place. Your data/ directory is never touched.
# ---------------------------------------------------------------------------
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
PURGE=0
[[ "${1:-}" == "--purge-data" ]] && PURGE=1

read -r -p "Remove airdrop profiles and skills from ${HERMES_HOME}? [y/N] " a
[[ "$a" =~ ^[Yy]$ ]] || { echo "aborted"; exit 0; }

for p in analyzer daily quests discord monitor; do
  rm -rf "${HERMES_HOME}/profiles/worker-${p}"
done
for s in airdrop-analyzer daily-executor quest-executor discord-engager \
         wallet-isolation portfolio-tracker; do
  rm -rf "${HERMES_HOME}/skills/${s}"
done

# Close the CDP Chrome we launched, if it is still running.
CDP_PORT="${HAA_CDP_PORT:-9222}"
if curl -fsS -m 2 "http://127.0.0.1:${CDP_PORT}/json/version" >/dev/null 2>&1; then
  echo "  Chrome is still listening on :${CDP_PORT} — close that window yourself"
  echo "  (killing it from here could lose work in your other tabs)"
fi

PROFILE="${HAA_CHROME_PROFILE:-$HOME/.hermes/chrome-debug}"
if [[ -d "$PROFILE" ]] && (( PURGE )); then
  rm -rf "$PROFILE"
  echo "✓ removed the Chrome profile at $PROFILE (logins gone)"
else
  echo "  Chrome profile kept at $PROFILE (your logins survive)"
fi

echo "✓ removed airdrop profiles and skills"
echo "  Hermes itself is left installed (run 'hermes' to check)"
echo "  ${HERMES_HOME}/config.yaml left in place — remove it by hand if you want"

if (( PURGE )); then
  rm -rf "${PROJECT_DIR}/data"
  echo "✓ purged ${PROJECT_DIR}/data"
else
  echo "  ${PROJECT_DIR}/data kept (campaign records + evidence ledger)"
  echo "  pass --purge-data to remove it too"
fi
