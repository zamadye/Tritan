# Market Analysis — 2026-05-19 02:23 UTC

## Market
- **Question:** Athletics vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $152,647
- **Liquidity:** $51,627

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,710 (-0.4% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,744 (-0.3% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)
- ?: Max Muncy — 10-Day-IL (Fracture)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: athletics angeles angels
- [Bing News]
- [Mon, 18 May 2026] athletics angeles angels
- → New Series Begins Tonight ...
- [Mon, 18 May 2026] Game #47: Athletics at Angels game thread
- → The Sacramento Athletics (23-22) are headed to Angel Stadium on Monday where they will go up against the Los Angeles Angels (16-30). The moneyline o
- [Mon, 18 May 2026] Sacramento Athletics vs Los Angeles Angels Prediction, 5/18/2026 MLB Picks, Best Bets &amp; Odds
- → Athletics (23-23, first in the AL West) vs. Los Angeles Angels (16-31, fifth in the AL West) Anaheim, California; Monday, 9:38 p.m. EDT PITCHING PRO

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 59.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 56% resolve YES only 44.7% of the time, indicating systematic YES overpricing. However, current gap is only +3% (56% vs 59% base rate), falling below the 5% threshold required for entry. Injuries are balanced: Athletics missing Wilson (SS) and Muncy (3B) on offense; Angels missing d'Arnaud (C) and two relievers. No direct catalyst found to explain why this specific game would differ from historical pattern. Previous similar decisions (gap 1% and 3%) were correctly skipped. Recommendation: Watch for gap to widen beyond 5% for a BET_NO opportunity.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Athletics'})` → INJURY [athletics] Jacob Wilson (SS): 10-Day-IL
INJURY [athletics] Max Muncy (3B): 10-Day-IL
INJURY 
- `get_sports_data({'sport': 'mlb', 'team': 'Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `search_web({'query': 'Athletics vs Angels MLB game today odds'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] A's at Angels odds, picks and predictions - Sports
- `get_odds({'sport': 'baseball_mlb', 'team': 'Athletics'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Athletics Angels recent results form May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Where to watch Athletics vs Los Angeles Angels: TV
- `search_web({'query': 'Athletics Angels starting pitcher May 18 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Angels look for answers to Ryan Johnson’s reduced 
- `search_web({'query': '"Athletics vs Angels" prediction May 18 2026 odds'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Athletics vs Angels Prediction, Pick, MLB Odds for

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*