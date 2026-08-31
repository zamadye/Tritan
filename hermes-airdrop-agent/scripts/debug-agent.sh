#!/usr/bin/env bash
# ===========================================================================
# Panggil SATU agent untuk satu task, lihat perilakunya — TANPA orkestrasi.
#
#   ./scripts/debug-agent.sh <agent> "<task>"          # single query, terlihat
#   ./scripts/debug-agent.sh <agent>                   # interaktif
#   ./scripts/debug-agent.sh --list                    # daftar roster
#
# <agent> adalah suffix profile: onboard | daily | research | social | discord
# (juga: analyzer | monitor). Ini cara men-debug perilaku per-agent sebelum
# orkestrasi dinyalakan — lihat mana yang tepat, mana yang error.
# ===========================================================================
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(dirname "$SCRIPT_DIR")"
cd "$ROOT"
[[ -f .env ]] && set -a && . ./.env && set +a

case "${1:-}" in
  --list|-l)
    cat <<'EOF'
Roster (debug per-agent, sebelum orkestrasi):
  onboard   Agent 1 — task airdrop BARU: connect wallet, approve, quest, done
  daily     Agent 2 — lanjutkan Agent 1, HANYA daily task (check-in/claim/like)
  research  Agent 3 — cari fakta/data/angka -> research.md (bahan agent 4)
  social    Agent 4 — content X + share referral, baca research.md
  discord   Agent 5 — join Discord, ngobrol, simpan knowledge
  analyzer  pendukung — screening 4 dimensi
  monitor   pendukung — verifikasi + laporan
EOF
    exit 0 ;;
esac

NAME="${1:-}"; shift || true
case "$NAME" in
  onboard)  PROFILE=worker-quests ;;
  daily)    PROFILE=worker-daily ;;
  research) PROFILE=worker-research ;;
  social)   PROFILE=worker-social ;;
  discord)  PROFILE=worker-discord ;;
  analyzer) PROFILE=worker-analyzer ;;
  monitor)  PROFILE=worker-monitor ;;
  *) echo "agent tidak dikenal: '$NAME' (coba --list)" >&2; exit 2 ;;
esac

if ! command -v hermes >/dev/null 2>&1; then
  echo "✗ hermes belum terpasang / tidak di PATH. Jalankan ./install.sh dulu." >&2
  exit 1
fi

echo "→ agent: $NAME  (profile: $PROFILE)"
ERR_FILE="$(mktemp)"
LOG() {  # LOG <exit>
  PYTHONPATH="$ROOT/src" python3 -m hermes_airdrop.activity_log record \
    --source debug-agent --agent "$NAME" --exit "$1" \
    --task "${TASK:-interactive}" --error-file "$ERR_FILE" 2>/dev/null || true
}
if [[ "${1:-}" == "" ]]; then
  TASK="interactive"
  echo "  mode interaktif — ketik task, /exit untuk keluar"
  hermes --profile "$PROFILE" 2>>"$ERR_FILE"
  RC=$?
else
  TASK="$*"
  echo "  task: $TASK"
  hermes --profile "$PROFILE" chat -q "$TASK" 2>>"$ERR_FILE"
  RC=$?
fi
LOG "$RC"
rm -f "$ERR_FILE"
exit "$RC"
