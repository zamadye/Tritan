# Market Analysis — 2026-05-16 16:55 UTC

## Market
- **Question:** New York Yankees vs. New York Mets
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 7
- **Volume 24h:** $72,506
- **Liquidity:** $293,533

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,176 (-1.3% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,154 (-1.3% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 46.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STAT_EDGE
- **Catalyst Strength:** 0.70

### Reasoning
Market at 53% historically resolves YES only 44.7% of the time (n=13,967), indicating systematic overpricing of YES.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<3%

## Tool Calls
- `search_web({'query': 'New York Yankees vs New York Mets game today 2025-11-21'})` → [Fri, 21 Nov 2025] Google News
[Fri, 21 Nov 2025] Can the Yankees land Cody Bellinger and Kyle Tucke
- `search_web({'query': 'Yankees vs Mets Polymarket prediction market'})` → [Sat, 16 May 2026] Google News
[Fri, 15 May 2026] PGA Championship Polymarket promo code “SILIVE” up
- `search_web({'query': '"Yankees vs Mets" 2025'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] Where to watch Yankees vs. Mets: Subway Series sch

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*