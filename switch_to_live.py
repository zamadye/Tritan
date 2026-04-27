#!/usr/bin/env python3
"""
switch_to_live.py — Run this when ready to go LIVE.
Prerequisites:
  1. Demo win rate >= 55% from 30+ resolved trades
  2. USDC deposited to Polymarket (polymarket.com → Deposit)
  3. Run: python3 switch_to_live.py
"""
import os, sys, json, requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv('/root/polymarket/.env')

def check(label, ok, detail=""):
    icon = "✅" if ok else "❌"
    print(f"  {icon} {label}: {detail}")
    return ok

print("="*55)
print("PRE-LIVE CHECKLIST")
print("="*55)

passed = []

# 1. Demo qualification
trades = json.loads(Path("data/demo_trades.json").read_text())
resolved = [t for t in trades if t.get("actual_outcome")]
wins = [t for t in resolved if t.get("prediction_correct")]
wr = len(wins)/len(resolved) if resolved else 0
min_trades = int(os.getenv("DEMO_MIN_TRADES", 30))
min_wr = float(os.getenv("DEMO_MIN_WIN_RATE", 0.55))
passed.append(check("Resolved trades", len(resolved) >= min_trades,
    f"{len(resolved)}/{min_trades}"))
passed.append(check("Win rate", wr >= min_wr,
    f"{wr:.0%} (need {min_wr:.0%})"))

# 2. USDC balance
try:
    wallet = os.getenv("POLYGON_WALLET_ADDRESS")
    rpc = "https://polygon-mainnet.g.alchemy.com/v2/-LJWrAuXvUC8QszJzGzs0"
    USDC = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
    data = "0x70a08231000000000000000000000000" + wallet[2:].zfill(64)
    r = requests.post(rpc, json={"jsonrpc":"2.0","method":"eth_call",
        "params":[{"to":USDC,"data":data},"latest"],"id":1}, timeout=8)
    bal = int(r.json().get("result","0x0"), 16) / 1e6
    passed.append(check("USDC on Polymarket", bal >= 10, f"${bal:.2f} (need $10+)"))
except Exception as e:
    passed.append(check("USDC balance", False, str(e)[:50]))

# 3. CLOB auth
try:
    from py_clob_client.client import ClobClient
    client = ClobClient(os.getenv("POLYMARKET_CLOB_HOST"),
        key=os.getenv("POLYGON_PRIVATE_KEY"),
        chain_id=137, signature_type=0)
    client.set_api_creds(client.create_or_derive_api_creds())
    client.get_orders()
    passed.append(check("CLOB Auth", True, "API creds valid"))
except Exception as e:
    passed.append(check("CLOB Auth", False, str(e)[:50]))

print("="*55)

if all(passed):
    print("\n✅ ALL CHECKS PASSED — switching to LIVE mode\n")
    # Update .env
    env = Path("/root/polymarket/.env").read_text()
    env = env.replace("AGENT_MODE=demo", "AGENT_MODE=live")
    Path("/root/polymarket/.env").write_text(env)
    # Restart service
    os.system("systemctl restart polymarket-agent.service")
    print("✅ AGENT_MODE=live")
    print("✅ Service restarted")
    print("\n⚠️  LIVE MODE ACTIVE — real USDC will be used!")
else:
    failed = [i for i,p in enumerate(passed) if not p]
    print(f"\n❌ {len(failed)} check(s) failed — fix before going live")
    sys.exit(1)
