# Market Analysis — 2026-05-16 16:13 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 10.0%
- **Days Left:** 4
- **Volume 24h:** $77,758
- **Liquidity:** $53,949

## Statistical Prior
- **p_base:** 2.2%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,296 (-1.1% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,181 (-1.2% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 1.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** CROWD_BIAS
- **Catalyst Strength:** 0.65

### Reasoning
Market pricing 5x above base rate (10% vs 2%) without specific catalyst. No breaking news, leaked intelligence, or imminent escalation data found. Retail overpricing longshot geopolitical event. Historical airspace closures by Iran are rare (2% base rate) and require major military escalation (e.g., direct US/Israel strikes, full-scale war). Current macro fear (F&G=31) and risk-off sentiment are creating spillover anxiety, but this is NOT specific catalyst for Iran airspace closure. Pattern suggests crowd systematically overprices multi-outcome geopolitical longshots. Price would need credible intelligence of imminent military strike to justify >5%.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=8%<10%

## Tool Calls
- `search_web({'query': 'Iran airspace closure May 2025'})` → [Sun, 01 Mar 2026] Google News
[Mon, 02 Mar 2026] Air fares could rise if Iran conflict lingers as c
- `search_web({'query': 'Iran military tensions March 2025 airspace'})` → [Sun, 01 Mar 2026] Google News
[Wed, 15 Apr 2026] Air fares could rise if Iran conflict lingers as c
- `search_web({'query': 'Iran closes airspace 2025 geopolitical tensions'})` → [Sat, 24 Jan 2026] Google News
[Sat, 24 Jan 2026] Airlines reroute, cancel flights as tensions ramp 

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*