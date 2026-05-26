# Market Analysis — 2026-05-19 00:17 UTC

## Market
- **Question:** Cleveland Guardians vs. Detroit Tigers
- **Category:** sports
- **YES Price:** 60.0%
- **Days Left:** 6
- **Volume 24h:** $536,659
- **Liquidity:** $104,644

## Statistical Prior
- **p_base:** 64.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.7%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,068 (-0.2% 24h) → neutral
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
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 64.8%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Guardians'})` → INJURY [cleveland guardians] Gabriel Arias (SS): 10-Day-IL
INJURY [cleveland guardians] Carlos Herna
- `get_odds({'sport': 'baseball_mlb', 'team': 'Guardians'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Cleveland Guardians vs Detroit Tigers game today pitching matchup'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] How to Watch Tigers Series Opener vs Guardians: TV
- `search_web({'query': 'Cleveland Guardians Detroit Tigers injuries 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Guardians vs. Tigers (May 18, 2026) Pregame - ESPN
- `search_web({'query': 'Detroit Tigers missing Skubal Verlander 2026 injury'})` → [Fri, 15 May 2026] Google News
[Sun, 17 May 2026] Tigers pitcher Casey Mize to start Saturday's game
- `search_web({'query': 'Tigers ace Skubal IL 2026'})` → [Mon, 18 May 2026] Google News
[Fri, 15 May 2026] Tigers ace Tarik Skubal gets more work in: 'I feel
- `search_web({'query': 'Verlander 60-Day IL 2026 Tigers'})` → [Mon, 18 May 2026] Google News
[Sun, 10 May 2026] Guardians vs. Tigers (May 18, 2026) Pregame - ESPN

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*