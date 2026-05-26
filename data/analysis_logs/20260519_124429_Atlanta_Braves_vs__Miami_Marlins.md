# Market Analysis — 2026-05-19 12:44 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $98,726
- **Liquidity:** $190,198

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,847 (-1.1% 24h) → risk-OFF
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,847 (-1.1% 24h) → risk-OFF

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- ATL @ MIA | Final | Miami Marlins(home) 22-26 score:12 vs Atlanta Braves(away) 32-16 score:0
- [SPORTS] Injuries:
- ?: James McCann — Out (Strain)
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Tue, 19 May 2026] atlanta braves miami marlins
- → Here's how to watch Tuesday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Mon, 18 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 19
- → According to Francys Romero of Beisbol FR, the Atlanta Braves are calling up a player to the MLB. They are in a series with the Marlins.
- [Tue, 19 May 2026] Atlanta Braves Make Roster Move After Marlins Game
- → Atlanta Braves (32-16, first in the NL East) vs. Miami Marlins (22-26, fourth in the NL East) Miami; Tuesday, 4:10 p.m. EDT PITCHING PROBABLES: Brav

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 60.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Stat signal (n=13,967) strongly suggests YES overpricing at 57% → only 44.7% historical resolution, indicating NO value. However: (1) Gate FAILS — gap=3% < 5% threshold; (2) No new catalyst or breaking injury news to shift the game; (3) Both teams have similar moderate injury profiles — no star players out; (4) Pattern data shows 50-60% entry range has only 33% WR historically (very weak); (5) Two prior identical analyses on this same market both SKIP'd for same reasons. Despite clear structural overpricing signal, no verifiable edge meets the decision threshold without a catalyst or wider gap.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 recent results predictions'})` → [Sat, 16 May 2026] Google News
[Sat, 09 Aug 2025] Miami Marlins vs. Atlanta Braves Series May 18-21:
- `search_web({'query': 'Atlanta Braves injury news 2025 season update'})` → [Wed, 18 Feb 2026] Google News
[Mon, 09 Mar 2026] Braves get crucial injury update on pair of key st
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins odds moneyline today 2025'})` → [Tue, 14 Apr 2026] Google News
[Mon, 25 Aug 2025] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `search_web({'query': '"Atlanta Braves" "Miami Marlins" starting pitcher April 2025'})` → [Mon, 04 May 2026] Google News
[Sat, 09 Aug 2025] The Atlanta Braves are the best team in baseball. 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*