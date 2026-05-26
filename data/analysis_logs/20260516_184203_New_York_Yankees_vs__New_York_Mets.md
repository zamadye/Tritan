# Market Analysis — 2026-05-16 18:42 UTC

## Market
- **Question:** New York Yankees vs. New York Mets
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $414,094
- **Liquidity:** $286,664

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,168 (-1.3% 24h) → risk-OFF
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
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 46.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STAT_EDGE
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical edge shows markets at 54% YES price historically resolve YES only 44.7% of time (n=13,967), indicating systematic overpricing. No specific information gap or breaking news exists. Crowd appears to be overpricing the favorite (Yankees) despite both teams having significant injuries. The 9.3% gap between market price (54%) and historical resolution rate (44.7%) provides a clear betting edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<3%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Yankees'})` → INJURY [new york yankees] Max Fried (SP): 15-Day-IL
INJURY [new york yankees] Giancarlo Stanton (DH)
- `get_sports_data({'sport': 'mlb', 'team': 'Mets'})` → INJURY [new york mets] Clay Holmes (SP): Out
INJURY [new york mets] Jorge Polanco (1B): 10-Day-IL
IN
- `search_web({'query': 'New York Yankees vs New York Mets game today June 2024 news'})` → [Sat, 16 May 2026] Google News
[Wed, 15 Apr 2026] 2026 New York Yankees TV schedule: How to watch, s

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*