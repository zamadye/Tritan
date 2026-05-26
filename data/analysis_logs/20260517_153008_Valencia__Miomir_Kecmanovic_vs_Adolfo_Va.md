# Market Analysis — 2026-05-17 15:30 UTC

## Market
- **Question:** Valencia: Miomir Kecmanovic vs Adolfo Vallejo
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 6
- **Volume 24h:** $73,218
- **Liquidity:** $20,181

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,992 (-0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,994 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: valencia: miomir kecmanovic adolfo vallejo
- [Bing News]
- [] valencia: miomir kecmanovic adolfo vallejo
- [Metaculus]
- [] Will Bitcoin trade above $120,000 before August 1, 2026?
- → Community: pending
- [] Will Haiti hold the first round of its presidential election before Se
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 53.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.70

### Reasoning
Strong stat signal (n=13,967) shows markets at 58% resolve YES only 44.7% of time - 13% overpricing. Challenger tennis is volatile, Vallejo has recent form, and pattern signals support NO entry in 50-60% range. No injury data found to contradict edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Kecmanovic'})` → No injury data found for tennis Kecmanovic
- `search_web({'query': 'Miomir Kecmanovic vs Adolfo Vallejo Valencia 2025 prediction'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] H2H, prediction of Miomir Kecmanovic vs Adolfo Dan
- `search_web({'query': 'Miomir Kecmanovic recent form 2025'})` → [Thu, 21 Aug 2025] Google News
[Tue, 22 Jul 2025] US Open 2025: Laver Cup Form Guide - Laver Cup
[Sa
- `get_market_context({'keyword': 'Valencia tennis Kecmanovic'})` → No related markets found for 'Valencia tennis Kecmanovic'
- `get_odds({'sport': 'tennis_atp', 'team': 'Kecmanovic'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Kecmanovic vs Vallejo head to head Valencia Challenger 2026'})` → [Sat, 16 May 2026] Google News
[Fri, 26 Dec 2014] Miomir Kecmanovic vs Adolfo Daniel Vallejo: Scores
- `search_web({'query': 'Adolfo Vallejo tennis ranking form 2026'})` → [Thu, 23 Apr 2026] Google News
[Tue, 24 Feb 2026] Vallejo becomes second Paraguayan to record Master
- `get_market_context({'keyword': 'Valencia Challenger tennis'})` → No related markets found for 'Valencia Challenger tennis'
- `search_web({'query': '"Kecmanovic" "Vallejo" tennis odds prediction site:tennistonic.com OR site:tennisabstract.com'})` → [Fri, 17 Aug 2018] Google News
[Mon, 26 Aug 2019] ATP Elo Ratings - Tennis Abstract
[Wed, 06 Feb 201
- `search_web({'query': 'Miomir Kecmanovic 2026 clay court results'})` → [Sat, 14 Feb 2026] Google News
[Thu, 07 May 2026] What are the draws in Rio de Janeiro and Delray Be

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*