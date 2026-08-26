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

if command -v docker >/dev/null 2>&1 && docker ps -a --format '{{.Names}}' | grep -qx camofox-browser; then
  docker rm -f camofox-browser >/dev/null
  echo "✓ removed camofox-browser container"
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
