# Market Analysis — 2026-05-16 15:27 UTC

## Market
- **Question:** Gauff vs. Svitolina: Match O/U 21.5
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $35,482
- **Liquidity:** $5,328

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,071 (-1.5% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,129 (-1.2% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 52.9%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STAT_EDGE
- **Catalyst Strength:** 0.65

### Reasoning
Strong statistical signal: markets at 56% historically resolve YES only 44.7% of the time (n=13,967), indicating systematic overpricing of YES. No specific information gap or breaking news identified. Crowd appears to be overpricing YES at this price level without factual justification — a classic case of retail bias in sports totals markets. The pattern data confirms strong edge: Sports category WR=85% (n=13), Entry 50-60% WR=86% (n=7). No daily catalyst, but the historical overpricing pattern is robust. Base rate of 59% vs actual resolution of 44.7% at this price shows persistent market inefficiency.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<3%

## Tool Calls
- `search_web({'query': 'Gauff vs Svitolina match today news injury form'})` → [Sat, 16 May 2026] Google News
[Mon, 26 Jan 2026] Coco Gauff vs Elina Svitolina: How to watch, Live 
- `search_web({'query': 'Coco Gauff vs Elina Svitolina 2026 match prediction odds over under games'})` → [Fri, 15 May 2026] Google News
[Mon, 26 Jan 2026] Coco Gauff vs. Elina Svitolina prediction, odds, p
- `get_market_context({'keyword': 'Gauff Svitolina over under games'})` → No related markets found for 'Gauff Svitolina over under games'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*