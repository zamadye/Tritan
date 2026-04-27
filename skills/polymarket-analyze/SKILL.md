---
name: polymarket-analyze
description: Deep analysis of a specific Polymarket prediction market. Uses LLM probability estimation with news context and evolution learning to find edge.
user-invocable: true
metadata: {"openclaw":{"emoji":"📊","requires":{"bins":["python3"],"env":["AI_API_KEY","POLYMARKET_GAMMA_API"]}}}
---

## polymarket-analyze

Analyze a specific market question or market ID for trading edge.

### Usage
User says: "analyze [market question or ID]", "what's the edge on [question]"

### Execution
Replace QUESTION with the market question or ID:

```
cd /root/polymarket && python3 -c "
from dotenv import load_dotenv; load_dotenv('/root/polymarket/.env')
from agent.scanner import get_candidate_markets
from agent.analyzer import estimate_probability, fetch_news
from agent.sizer import calculate_position
from agent.learner import get_evolution_context
import os

markets = get_candidate_markets()
query = 'QUESTION'
market = next((m for m in markets if query.lower() in m['question'].lower()), markets[0] if markets else None)
if not market:
    print('Market not found')
else:
    news = fetch_news(market)
    evo = get_evolution_context()
    result = estimate_probability(market, news, evo)
    bankroll = float(os.getenv('DEMO_BANKROLL', 1000))
    size, side, kelly = calculate_position(result['p_true'], market['price'], bankroll)
    print(f'Market: {market[\"question\"]}')
    print(f'p_market={market[\"price\"]:.2%} | p_true={result[\"p_true\"]:.2%} | edge={result[\"edge\"]:+.2%}')
    print(f'Confidence: {result[\"confidence\"]:.0%} | Side: {side} | Size: \${size:.2f}')
    print(f'Reasoning: {result[\"reasoning_summary\"]}')
"
```

### Output
Show full analysis with probability estimate, edge, confidence, and recommended bet size.
