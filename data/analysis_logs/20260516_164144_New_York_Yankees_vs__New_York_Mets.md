# Market Analysis — 2026-05-16 16:41 UTC

## Market
- **Question:** New York Yankees vs. New York Mets
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 7
- **Volume 24h:** $71,484
- **Liquidity:** $318,297

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 31/100 (Fear) | trend: deteriorating
- BTC: $78,233 (-1.3% 24h) → risk-OFF
- Fear&Greed: 31/100 (Fear) | 7d trend: deteriorating
- BTC: $78,248 (-1.1% 24h) → risk-OFF
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
- **p_true:** 48.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STAT_EDGE
- **Catalyst Strength:** 0.65

### Reasoning
Stat signal shows markets priced at 53% historically resolve YES only 44.7% (n=13,967) - indicating systematic overpricing of YES. Yankees are a high-profile public team prone to narrative bias from casual bettors. Both teams have significant injuries (Yankees: Fried, Stanton, Dominguez; Mets: Holmes, Polanco, Alvarez) but these are likely priced in already. No breaking news or information asymmetry detected. Macro fear/risk-off environment doesn't impact sports outcomes. The +1% gap over base rate combined with historical overpricing pattern suggests value on NO side. No longshot rule applies (price is 53%, not 3-15%).

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<3%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Yankees'})` → INJURY [new york yankees] Max Fried (SP): 15-Day-IL
INJURY [new york yankees] Giancarlo Stanton (DH)
- `get_sports_data({'sport': 'mlb', 'team': 'Mets'})` → INJURY [new york mets] Clay Holmes (SP): Out
INJURY [new york mets] Jorge Polanco (1B): 10-Day-IL
IN
- `search_web({'query': 'New York Yankees vs New York Mets game today 2025'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] Yankees vs. Mets FREE live stream: Where to watch 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*