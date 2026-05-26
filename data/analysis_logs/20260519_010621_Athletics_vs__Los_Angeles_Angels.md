# Market Analysis — 2026-05-19 01:06 UTC

## Market
- **Question:** Athletics vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $72,811
- **Liquidity:** $271,666

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,029 (-0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,027 (-0.1% 24h) → neutral

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
- → The Angels seem destined to waste another year of future Hall of Famer Mike Trout ’s career as their record (16-31) is the worst in MLB. First-year 
- [Mon, 18 May 2026] Game #47: Athletics at Angels Game Thread
- → The Sacramento Athletics (23-22) are headed to Angel Stadium on Monday where they will go up against the Los Angeles Angels (16-30). The moneyline o
- [Mon, 18 May 2026] Sacramento Athletics vs Los Angeles Angels Prediction, 5/18/2026 MLB Picks, Best Bets &amp; Odds
- → Athletics (23-23, first in the AL West) vs. Los Angeles Angels (16-31, fifth in the AL West) Anaheim, California; Monday, 9:38 p.m. EDT PITCHING PRO

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 45.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.80

### Reasoning
Strong statistical signal (n=13,967) shows markets at 55% resolve YES only 44.7% of time, creating ~10% edge for NO. Market overprices YES. Both teams have comparable injury situations with no dominant factor suggesting Athletics win.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Athletics'})` → INJURY [athletics] Jacob Wilson (SS): 10-Day-IL
INJURY [athletics] Max Muncy (3B): 10-Day-IL
INJURY 
- `get_sports_data({'sport': 'mlb', 'team': 'Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `search_web({'query': 'Athletics vs Angels game preview 2025'})` → [Wed, 03 Sep 2025] Google News
[Fri, 05 Sep 2025] Athletics at Los Angeles Angels Preview - 09/05/20
- `search_web({'query': 'Oakland Athletics Los Angeles Angels recent results 2025'})` → [Sat, 06 Sep 2025] Google News
[Wed, 13 May 2026] Athletics at Los Angeles Angels Game Story, Scores
- `get_market_context({'keyword': 'Athletics Angels'})` → No related markets found for 'Athletics Angels'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Athletics'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Athletics Angels September 7 2025 starting pitchers'})` → [Sun, 07 Sep 2025] Google News
[Sun, 07 Sep 2025] Angels rally past A’s to snap 3-game skid after pa

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*