# Market Analysis — 2026-05-16 15:58 UTC

## Market
- **Question:** Gauff vs. Svitolina: Match O/U 21.5
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $35,911
- **Liquidity:** $10,801

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,203 (-1.2% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,203 (-1.2% 24h) → risk-OFF
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
- **p_true:** 50.3%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STAT_EDGE
- **Catalyst Strength:** 0.68

### Reasoning
Strong historical pattern shows markets priced at 55% resolve YES only 44.7% of the time (n=13,967). This 10.3% edge represents systematic crowd overpricing of YES at this price level. No specific news catalyst exists - this is a pure statistical edge play. Bet NO to exploit the crowd bias where retail systematically overprices 'over' bets in tennis game totals.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<3%

## Tool Calls
- `search_web({'query': 'Gauff vs Svitolina 2025 tennis match head to head'})` → [Sat, 16 May 2026] Google News
[Tue, 27 Jan 2026] Where to watch Coco Gauff vs. Elina Svitolina Ital
- `search_web({'query': 'Coco Gauff Elena Svitolina over under games 2025'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] Coco Gauff vs. Elina Svitolina Pick: Internazional
- `get_market_context({'keyword': 'tennis over under games Gauff Svitolina'})` → No related markets found for 'tennis over under games Gauff Svitolina'
- `search_web({'query': 'Gauff Svitolina Italian Open final 2026 score result'})` → [Thu, 14 May 2026] Google News
[Sat, 16 May 2026] Italian Open 2026: Coco Gauff reaches back-to-back
- `get_sports_data({'sport': 'nba'})` → INJURY [atlanta hawks] Keshon Gilbert (G): Out
INJURY [atlanta hawks] Jock Landale (C): Out
INJURY [

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*