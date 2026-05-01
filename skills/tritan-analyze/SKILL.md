---
name: tritan-analyze
description: Full momentum analysis for a Tritan market. Runs research + LLM analysis to determine if YES price will move UP or DOWN. Returns bet recommendation with catalyst, confidence, and price target.
user-invocable: true
metadata: {"openclaw":{"emoji":"📊","requires":{"bins":["python3"],"env":["AI_API_KEY","POLYMARKET_GAMMA_API"]}}}
---

## tritan-analyze

Analyze a market for momentum trading opportunity.

### Usage
User says: "analyze [market question]", "should I bet on [question]", "what's the momentum on [question]"

### Execution

```bash
cd /root/polymarket && timeout 60 python3 -c "
import sys, time; sys.path.insert(0,'.')
t0 = time.time()
print('[tritan-analyze] Starting...', flush=True)

from dotenv import load_dotenv; load_dotenv('.env', override=True)
print(f'[tritan-analyze] Env loaded ({time.time()-t0:.1f}s)', flush=True)

from agent.scanner import get_candidate_markets
from agent.analyzer import estimate_probability, fetch_news
from agent.research import build_research_report, format_research_for_llm, get_macro_context
from agent.osint import get_fear_greed_trend
from agent.learner import get_evolution_context
from agent.sizer import calculate_position

query = 'QUESTION'
print(f'[tritan-analyze] Scanning markets...', flush=True)
markets = get_candidate_markets()
market = next((m for m in markets if query.lower() in m['question'].lower()), None)
if not market:
    print(f'[tritan-analyze] Market not found for: {query}')
    exit(1)

print(f'[tritan-analyze] Found: {market[\"question\"][:50]} ({time.time()-t0:.1f}s)', flush=True)
print(f'[tritan-analyze] Fetching research...', flush=True)

macro = get_macro_context()
fg = get_fear_greed_trend()
cycle_macro = f'[MACRO] BTC: \${macro.get(\"crypto_sentiment\",{}).get(\"btc_price\",0):,.0f} | F&G: {macro.get(\"fear_greed\",{}).get(\"current\",\"?\")} | {fg}'
research = build_research_report(market)
research_ctx = format_research_for_llm(research)
news = fetch_news(market)
combined = '\n'.join(filter(None,[cycle_macro, research_ctx, news]))
print(f'[tritan-analyze] Research done ({time.time()-t0:.1f}s) — {len(combined)} chars context', flush=True)

print(f'[tritan-analyze] Calling LLM...', flush=True)
evo_ctx = get_evolution_context('demo')
result = estimate_probability(market, combined, evo_ctx)
print(f'[tritan-analyze] LLM done ({time.time()-t0:.1f}s)', flush=True)

print()
print('=== MOMENTUM ANALYSIS ===')
print(f'Market:       {market[\"question\"]}')
print(f'Price:        {market[\"price\"]:.2%}')
print(f'Direction:    {result.get(\"momentum_direction\",\"?\").upper()}')
print(f'Catalyst:     {result.get(\"catalyst\",result.get(\"reasoning_summary\",\"?\"))[:120]}')
print(f'p_true:       {result.get(\"p_true\",0):.2%}')
print(f'Edge:         {result.get(\"edge\",0):+.2%}')
print(f'Confidence:   {result.get(\"confidence\",0):.0%}')
print(f'Data quality: {result.get(\"data_quality\",\"?\")}')
print(f'Decision:     {result.get(\"recommended_side\",\"SKIP\")}')
print(f'Total time:   {time.time()-t0:.1f}s')

from agent.llm import get_daily_usage
d = get_daily_usage()
print(f'LLM cost:     \${d[\"cost_usd\"]:.4f} today ({d[\"calls\"]} calls)')
" 2>&1 || echo "[tritan-analyze] TIMEOUT or ERROR after 60s"
```

### Output
Full momentum analysis with direction, catalyst, confidence, price target, and bet recommendation.
