---
name: polymarket-trade
description: Execute a demo or live trade on Polymarket. Runs full scan-analyze-size-execute pipeline for one market cycle.
user-invocable: true
metadata: {"openclaw":{"emoji":"💰","requires":{"bins":["python3"],"env":["AI_API_KEY","POLYGON_PRIVATE_KEY"]}}}
---

## polymarket-trade

Run one full trading cycle: scan → analyze → size → execute (demo or live).

### Usage
User says: "run trade cycle", "execute trades", "trade demo", "trade live"

### Execution
For demo mode:
```
cd /root/polymarket && python3 main.py --mode demo scan
```

For live mode:
```
cd /root/polymarket && python3 main.py --mode live scan
```

Check status:
```
cd /root/polymarket && python3 main.py status
```

Show trade history:
```
cd /root/polymarket && python3 main.py history
```

### Output
Show executed trades with market question, side, size, and reasoning.
