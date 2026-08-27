#!/usr/bin/env bash
# ===========================================================================
# Verify a fresh fetch+checkout has EVERYTHING, and that the multi-agent
# workflow is wired to run with all agents on standby.
#
#   ./scripts/verify-checkout.sh            # config-level checks
#   ./scripts/verify-checkout.sh --tests    # also run the test suite
#
# Run this right after:
#   git fetch origin arena/01a037e2-tritan
#   git checkout arena/01a037e2-tritan
#
# It does NOT need Hermes or a browser installed; it validates the wiring.
# Anything that requires the live gateway / Chrome is reported as a NEXT STEP.
# ===========================================================================
set -euo pipefail

# Prefer the project venv's python (has pyyaml) when present; else system python3.
if [[ -x ".venv/bin/python" ]]; then PY=".venv/bin/python"
else PY="python3"; fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(dirname "$SCRIPT_DIR")"
cd "$ROOT"
RUN_TESTS=0; [[ "${1:-}" == "--tests" ]] && RUN_TESTS=1

ok()  { printf '  \033[0;32m✓\033[0m %s\n' "$*"; }
bad() { printf '  \033[0;31m✗\033[0m %s\n' "$*"; FAIL=1; }
FAIL=0

echo "== 1. Kelengkapan file (fetch+checkout membawa semuanya) =="
MISSING=0
for f in install.sh pyproject.toml README.md AGENTS.md \
         scripts/start-browser.sh scripts/extract-standalone.sh scripts/cron-jobs.sh \
         docs/workflows.md \
         config/hermes/config.yaml \
         src/hermes_airdrop/cli.py src/hermes_airdrop/positions.py \
         knowledge/cycles-and-meta.md knowledge/quest-platforms.md; do
  [[ -f "$f" ]] || { bad "hilang: $f"; MISSING=1; }
done
[[ "$MISSING" == 0 ]] && ok "semua file inti ada"
SK=$(ls skills/*/SKILL.md 2>/dev/null | wc -l | tr -d ' ')
SO=$(ls config/hermes/profiles/*/SOUL.md 2>/dev/null | wc -l | tr -d ' ')
[[ "$SK" == 6 ]] && ok "6 skill" || bad "skill=$SK (harus 6)"
[[ "$SO" == 7 ]] && ok "7 SOUL.md" || bad "SOUL=$SO (harus 7)"

echo; echo "== 2. Schema config valid (tidak ada key yang dibuang diam-diam) =="
$PY - <<'PY' || FAIL=1
import sys, pathlib
sys.path.insert(0, "src")
from hermes_airdrop.hermes_schema import validate_file
badc = [str(f) for f in pathlib.Path("config/hermes").rglob("config.yaml") if not validate_file(f).ok]
print("  ✗ invalid:", badc) if badc else print("  ✓ 8 config valid")
sys.exit(1 if badc else 0)
PY

echo; echo "== 3. Workflow: agent standby + alur task benar =="
$PY - <<'PY' || FAIL=1
import sys, pathlib, yaml
sys.path.insert(0, "src")
P = pathlib.Path("config/hermes/profiles")
def load(n): return yaml.safe_load((P/n/"config.yaml").read_text())
main = yaml.safe_load(pathlib.Path("config/hermes/config.yaml").read_text())
okp = lambda m: print(f"  \033[0;32m✓\033[0m {m}")
badp = lambda m: (print(f"  \033[0;31m✗\033[0m {m}"), sys.exit(1))

# Dispatcher harus jalan di dalam gateway -> worker di-spawn on demand (standby)
kb = main.get("kanban", {})
if kb.get("dispatch_in_gateway") is True: okp("dispatcher in-gateway on (worker standby, spawn on demand)")
else: badp("kanban.dispatch_in_gateway bukan true")
if kb.get("auto_subscribe_on_create") is True: okp("hasil kembali ke thread asal (auto_subscribe)")
else: badp("auto_subscribe_on_create bukan true")

# Orchestrator = pintu Telegram; harus bisa delegasi + kanban
o = load("worker-orchestrator"); ots = o["toolsets"]
if {"delegation","kanban","browser"} <= set(ots): okp("orchestrator: delegation+kanban+browser (pintu masuk task)")
else: badp(f"orchestrator toolsets kurang: {ots}")

# Lead = dekomposisi proyek; pekerja = eksekusi; semua punya browser+skills+kanban
for n, need in [("worker-lead", {"delegation","kanban","browser"}),
                ("worker-quests", {"browser","skills","kanban"}),
                ("worker-daily",  {"browser","skills","kanban"}),
                ("worker-discord",{"browser","skills","kanban"}),
                ("worker-monitor",{"browser","skills","kanban"}),
                ("worker-analyzer",{"browser","skills","kanban"})]:
    ts = set(load(n)["toolsets"])
    if need <= ts: okp(f"{n}: {sorted(need)}")
    else: badp(f"{n} toolsets kurang: {sorted(need - ts)}")
    if "terminal" in ts: badp(f"{n} masih grant terminal eksplisit")

# Tidak ada yang boleh men-spawn browser sendiri
need_deny = ["*google-chrome*","*chromium*","*--remote-debugging-port*","*Xvfb*","*pkill*"]
for f in [pathlib.Path("config/hermes/config.yaml")] + sorted(P.glob("*/config.yaml")):
    dn = yaml.safe_load(f.read_text()).get("approvals",{}).get("deny",[])
    miss = [x for x in need_deny if x not in dn]
    if miss: badp(f"{f.name}: deny kurang {miss}")
okp("semua config menahan agent men-spawn browser sendiri")

# Kontrol browser yang dikelola tidak ter-blokir deny
import fnmatch
deny = yaml.safe_load(pathlib.Path("config/hermes/config.yaml").read_text())["approvals"]["deny"]
tools = ["browser_navigate","browser_click","browser_type","browser_scroll","browser_vision","browser_snapshot"]
hit = [t for t in tools for pat in deny if fnmatch.fnmatch(t, pat)]
if not hit: okp("kontrol browser yang dikelola TIDAK terhalang deny")
else: badp(f"deny menghalangi browser tool: {hit}")
PY

echo; echo "== 4. Browser: Chrome + profil konsisten (butuh mesin Anda) =="
if command -v google-chrome >/dev/null 2>&1 || command -v google-chrome-stable >/dev/null 2>&1; then
  ok "Google Chrome terdeteksi"
else
  echo "  ! Chrome belum terdeteksi di mesin ini — pasang google-chrome / brew install --cask google-chrome"
fi
grep -q 'HAA_CHROME_PROFILE' .env 2>/dev/null \
  && ok ".env punya HAA_CHROME_PROFILE (profil yang dipakai agent)" \
  || echo "  ! .env belum punya HAA_CHROME_PROFILE — jalankan ./install.sh dulu"

echo; echo "== 5. Test suite (opsional) =="
if (( RUN_TESTS )); then
  python3 -m pytest tests/ -q --ignore=tests/test_packaging.py | tail -1 || FAIL=1
else
  echo "  · lewati (jalankan dengan --tests)"
fi

echo
if (( FAIL )); then echo "HASIL: ADA MASALAH — lihat ✗ di atas"; exit 1
else echo "HASIL: SEMUA WIRED. Langkah runtime: ./scripts/start-browser.sh lalu hermes --profile worker-orchestrator gateway run"; fi
