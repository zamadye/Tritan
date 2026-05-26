# Market Analysis — 2026-05-16 18:23 UTC

## Market
- **Question:** New York Yankees vs. New York Mets
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $313,244
- **Liquidity:** $385,038

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,131 (-1.4% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,131 (-1.4% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 31(Fear) → 43(Fear) → 34(Fear) → 42(Fear) | sentiment worsening
- Will the Fed decrease interest rates by 50+ bps after the Ju → YES=50%
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 56.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<3%

## Tool Calls
- `search_web({'query': 'New York Yankees vs New York Mets game news today'})` → [Fri, 15 May 2026] Google News
[Sat, 16 May 2026] New York Yankees at New York Mets Game Story, Scor
- `get_sports_data({'sport': 'mlb', 'team': 'Yankees'})` → INJURY [new york yankees] Max Fried (SP): 15-Day-IL
INJURY [new york yankees] Giancarlo Stanton (DH)
- `search_web({'query': 'Yankees vs Mets starting pitchers today May 15 2026'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] Yankees vs Mets start time today, how to watch and

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*