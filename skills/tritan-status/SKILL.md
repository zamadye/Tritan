---
name: tritan-status
description: Check Tritan agent status, performance, open positions, and LLM cost usage.
user-invocable: true
metadata: {"openclaw":{"emoji":"📈","requires":{"bins":["python3"]}}}
---

## tritan-status

Get full status of the Tritan trading agent.

### Usage
User says: "status", "how is tritan doing", "check performance", "open positions", "cost"

### Execution

```bash
cd /root/polymarket && timeout 30 python3 -c "
import sys, json, os, time; sys.path.insert(0,'.')
t0 = time.time()
print('[tritan-status] Loading...', flush=True)
from dotenv import load_dotenv; load_dotenv('.env', override=True)
from agent.llm import get_daily_usage
import subprocess

# Agent status
active = subprocess.run(['systemctl','is-active','polymarket-agent'], capture_output=True, text=True).stdout.strip()

# Trade stats
trades = json.loads(Path('data/demo_trades.json').read_text())
res = [t for t in trades if t.get('actual_outcome')]
op  = [t for t in trades if not t.get('actual_outcome')]
wins = [t for t in res if t.get('prediction_correct')]
pnl  = sum(t.get('pnl',0) for t in res)
base = float(os.getenv('DEMO_BANKROLL',20))
br   = round(max(base - sum(t['size_usd'] for t in op) + pnl, 0), 2)
wr   = len(wins)/len(res) if res else 0
avg_w = sum(t['pnl'] for t in wins)/len(wins) if wins else 0
avg_l = abs(sum(t['pnl'] for t in [t for t in res if not t.get('prediction_correct')])/max(1,len(res)-len(wins)))
rr = avg_w/avg_l if avg_l else 0

# LLM cost
daily = get_daily_usage()

print(f'=== TRITAN STATUS ===')
print(f'Agent:      {active.upper()}')
print(f'Mode:       {os.getenv(\"AGENT_MODE\",\"demo\").upper()}')
print(f'LLM:        {os.getenv(\"AI_MODEL\",\"?\")}')
print()
print(f'=== PERFORMANCE ===')
print(f'Bankroll:   \${br:.2f}  (started \$20 → +{(br/20-1)*100:.0f}%)')
print(f'P&L:        \${pnl:+.2f}')
print(f'Trades:     {len(trades)} total | {len(res)} resolved | {len(op)} open')
print(f'Win Rate:   {wr:.1%}  ({len(wins)}W/{len(res)-len(wins)}L)')
print(f'R:R Ratio:  {rr:.2f}:1')
print(f'EV/trade:   \${wr*avg_w-(1-wr)*avg_l:+.3f}')
print()
print(f'=== LLM COST TODAY ===')
print(f'Calls:      {daily[\"calls\"]}')
print(f'Tokens in:  {daily[\"input\"]:,}')
print(f'Tokens out: {daily[\"output\"]:,}')
print(f'Cost:       \${daily[\"cost_usd\"]:.4f}')
print(f'Limit:      \${os.getenv(\"LLM_DAILY_COST_LIMIT_USD\",2.0)}')
print()
if op:
    print(f'=== OPEN POSITIONS ({len(op)}) ===')
    for t in op:
        cat = t.get('category','?') or '?'
        print(f'  {t[\"side\"]} \${t[\"size_usd\"]} @ {t[\"price_at_entry\"]:.2f} [{cat}] {t[\"market_question\"][:50]}')
"
```
