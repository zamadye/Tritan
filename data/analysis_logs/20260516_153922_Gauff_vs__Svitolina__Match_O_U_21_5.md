# Market Analysis — 2026-05-16 15:39 UTC

## Market
- **Question:** Gauff vs. Svitolina: Match O/U 21.5
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $35,492
- **Liquidity:** $7,214

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,172 (-1.2% 24h) → risk-OFF
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
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 46.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STAT_EDGE
- **Catalyst Strength:** 0.82

### Reasoning
Statistical edge: Markets priced at 56% historically resolve YES only 44.7% of time (n=13,967) — clear systematic overpricing of YES (Over). Price gap of +3% above base rate (59%) combined with stat signal indicates crowd bias toward Over. Sports pattern shows WR=85% (STRONG) from 13 trades; entry 50-60% pattern shows WR=86%. No breaking news or specific catalyst today — pure statistical asymmetry with large sample size supports NO (Under 21.5 games).

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<3%

## Tool Calls
- `search_web({'query': 'Gauff vs Svitolina match over under 21.5 games prediction'})` → [Mon, 26 Jan 2026] Google News
[Mon, 26 Jan 2026] Gauff vs Svitolina Picks, Predictions &amp; Odds f
- `search_web({'query': '"Gauff" "Svitolina" over under 21.5'})` → [Fri, 15 May 2026] Google News
[Mon, 26 Jan 2026] Coco Gauff vs. Elina Svitolina Pick: Internazional
- `search_web({'query': 'Gauff Svitolina Australian Open 2026 match'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] How to watch Coco Gauff vs. Elina Svitolina in 202

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*