---
name: polymarket-scan
description: Scan Polymarket for candidate prediction markets with edge opportunities. Fetches live markets from Gamma API filtered by volume, liquidity, and price range.
user-invocable: true
metadata: {"openclaw":{"emoji":"🔍","requires":{"bins":["python3"],"env":["POLYMARKET_GAMMA_API"]}}}
---

## polymarket-scan

Scan active Polymarket markets and return candidates with trading edge potential.

### Usage
User says: "scan markets", "find opportunities", "scan polymarket"

### Execution
Run this command from the polymarket workspace:

```
cd /root/polymarket && python3 -c "
from dotenv import load_dotenv; load_dotenv('/root/polymarket/.env')
from agent.scanner import get_candidate_markets
markets = get_candidate_markets()
print(f'Found {len(markets)} candidates:')
for m in markets[:10]:
    print(f'  [{m[\"category\"] or \"?\"}] p={m[\"price\"]:.2f} vol=\${m[\"volume_24h\"]:,.0f} | {m[\"question\"][:70]}')
"
```

### Output
Return the list of candidate markets with price, volume, and category to the user.
