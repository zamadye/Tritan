# Market Analysis — 2026-05-19 00:37 UTC

## Market
- **Question:** Cleveland Guardians vs. Detroit Tigers
- **Category:** sports
- **YES Price:** 63.0%
- **Days Left:** 6
- **Volume 24h:** $541,880
- **Liquidity:** $75,974

## Statistical Prior
- **p_base:** 69.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 6.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,194 (+0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,999 (-0.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- CLE @ DET | In Progress | Detroit Tigers(home) 20-27 score:1 vs Cleveland Guardians(away) 26-22 score:2
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: cleveland guardians detroit tigers
- [Bing News]
- [Mon, 18 May 2026] cleveland guardians detroit tigers
- → The Detroit Tigers and Cleveland Guardians entered a rain delay before the start of Monday's series opener due to inclement weather at Comerica Park
- [Mon, 18 May 2026] Detroit Tigers weather, rain delay vs Guardians comes to an end
- → The Detroit Tigers and Cleveland Guardians are finally underway after a 43-minute rain delay at Comerica Park. Originally scheduled for 6:40 p.m., t
- [Mon, 18 May 2026] Tigers-Guardians rain delayed at Comerica; first pitch at 7:23 p.m.
- → The Cleveland Guardians are 26-22 and sit in first place in the American League Central. Aiming to increase their division lead, the Guardians' bull

## LLM Decision
- **Action:** YES
- **Confidence:** 65%
- **p_true:** 79.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** INJURY
- **Catalyst Strength:** 0.75

### Reasoning
Detroit Tigers missing two ace pitchers (Skubal 15-Day IL, Verlander 60-Day IL) significantly weakens their rotation. Cleveland Guardians only have minor injuries (utility player, reliever). Market pricing Cleveland at 63% vs base rate 69% suggests undervaluation given the Tigers' injury situation. The gap of 6% and concrete injury evidence supports a BET_YES.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET YES $1.00

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Cleveland Guardians'})` → INJURY [cleveland guardians] Gabriel Arias (SS): 10-Day-IL
INJURY [cleveland guardians] Carlos Herna
- `get_sports_data({'sport': 'mlb', 'team': 'Detroit Tigers'})` → INJURY [detroit tigers] Tarik Skubal (SP): 15-Day-IL
INJURY [detroit tigers] Troy Melton (RP): 60-Da
- `get_odds({'sport': 'baseball_mlb', 'team': 'Guardians Tigers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Cleveland Guardians Detroit Tigers'})` → No related markets found for 'Cleveland Guardians Detroit Tigers'
- `search_web({'query': 'Cleveland Guardians vs Detroit Tigers 2025 MLB game preview'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Cleveland Guardians at Detroit Tigers Preview - 05
- `search_web({'query': 'Detroit Tigers injuries Tarik Skubal Justin Verlander 2025'})` → [Tue, 05 May 2026] Google News
[Mon, 23 Mar 2026] Tarik Skubal’s injury gives Guardians golden oppor
- `search_web({'query': 'Cleveland Guardians starting pitcher May 2026'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Cleveland Guardians road series vs. Detroit Tigers
- `search_web({'query': 'Detroit Tigers starting pitcher May 2026 rotation'})` → [Fri, 15 May 2026] Google News
[Tue, 12 May 2026] Casey Mize Set to Rejoin Tigers Rotation Saturday 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*