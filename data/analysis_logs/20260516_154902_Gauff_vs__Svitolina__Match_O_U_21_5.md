# Market Analysis — 2026-05-16 15:49 UTC

## Market
- **Question:** Gauff vs. Svitolina: Match O/U 21.5
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $35,513
- **Liquidity:** $24,314

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,201 (-1.2% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,129 (-1.2% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [MULTI-SOURCE NEWS] 1 sources for: gauff svitolina: match 21.5
- [Bing News]

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 47.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STAT_EDGE
- **Catalyst Strength:** 0.75

### Reasoning
Market at 55% historically resolves YES only 44.7% (n=13,967) — crowd systematically overprices YES. No specific breaking news or unreported information found. Statistical edge of 10.3% supports NO bet. Historical sports betting data shows 85% win rate from 13 trades in this pattern.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<3%

## Tool Calls
- `search_web({'query': 'Gauff Svitolina match news injury report odds'})` → [Sat, 21 Feb 2026] Google News
[Mon, 26 Jan 2026] Tennis Star Coco Gauff Receiving Awful Messages Af
- `search_web({'query': 'Coco Gauff Elina Svitolina 2026 head to head recent results'})` → [Mon, 26 Jan 2026] Google News
[Mon, 26 Jan 2026] Coco Gauff vs Elina Svitolina, Australian Open 202
- `get_market_context({'keyword': 'Gauff Svitolina tennis total games'})` → No related markets found for 'Gauff Svitolina tennis total games'
- `search_web({'query': 'Gauff Svitolina February 2026 tennis match'})` → [2026-05-15] Coco Gauff and Iga Świątek find similar progress in different results at Italian Open —

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*