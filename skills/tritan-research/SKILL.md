---
name: tritan-research
description: Real-time market research for Tritan. Fetches macro data, news, sports stats, causal chains, and builds a research report before betting.
user-invocable: true
metadata: {"openclaw":{"emoji":"🔬","requires":{"bins":["python3"],"env":["AI_API_KEY","POLYMARKET_GAMMA_API"]}}}
---

## tritan-research

Run full research pipeline on a market: macro context, news, causal chains, sports data.

### Usage
User says: "research [market question]", "what's the data on [question]"

### Execution

```bash
cd /root/polymarket && python3 -c "
import sys; sys.path.insert(0,'.')
from dotenv import load_dotenv; load_dotenv('.env', override=True)
from agent.scanner import get_candidate_markets
from agent.research import build_research_report, format_research_for_llm
from agent.osint import get_osint_signals
from agent.sports import get_sports_context

query = 'QUESTION'
markets = get_candidate_markets()
market = next((m for m in markets if query.lower() in m['question'].lower()), None)
if not market:
    market = {'id':'manual','question':query,'price':0.5,'numeric_id':'manual'}

import os; os.remove(f'data/research/{str(market.get(\"id\",\"manual\"))[:20]}.json') if __import__(\"os\").path.exists(f'data/research/{str(market.get(\"id\",\"manual\"))[:20]}.json') else None

report = build_research_report(market)
ctx = format_research_for_llm(report)
osint = get_osint_signals(market['question'])
sports = get_sports_context(market['question'])

print('=== RESEARCH REPORT ===')
print(f'Market: {market[\"question\"]}')
print(f'Price: {market[\"price\"]:.2%}')
print()
print(ctx)
if osint: print(osint)
if sports: print(sports)
print(f'News articles: {len(report[\"news_articles\"])}')
print(f'Causal chains: {len(report[\"causal_chains\"])}')
for c in report['causal_chains'][:4]:
    print(f'  → {c}')
"
```

### Output
Full research context including macro, news, sports, and causal chain analysis.
