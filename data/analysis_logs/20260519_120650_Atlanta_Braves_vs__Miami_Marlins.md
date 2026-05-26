# Market Analysis — 2026-05-19 12:06 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $94,768
- **Liquidity:** $211,000

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,679 (-0.8% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,679 (-0.8% 24h) → neutral

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
- [Mon, 18 May 2026] atlanta braves miami marlins
- → According to Francys Romero of Beisbol FR, the Atlanta Braves are calling up a player to the MLB. They are in a series with the Marlins.
- [Tue, 19 May 2026] Atlanta Braves Make Roster Move After Marlins Game
- → Here's how to watch Tuesday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Tue, 19 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 19
- → Atlanta Braves (32-16, first in the NL East) vs. Miami Marlins (22-26, fourth in the NL East) Miami; Tuesday, 4:10 p.m. EDT PITCHING PROBABLES: Brav

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Stat signal (n=13,967) shows YES overpricing at 57% → 44.7% resolution, suggesting NO value. HOWEVER: gap only 3% (below 5% gate), prior SKIP decisions on identical market (gap < 5%), entry range 50-60% has poor 33% WR history. No concrete catalyst or team-specific edge identified. Stat signal alone insufficient without actionable timing or gap meeting threshold.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins MLB'})` → No related markets found for 'Atlanta Braves Miami Marlins MLB'
- `search_web({'query': 'Atlanta Braves vs Miami Marlins April 2025 pitching matchup'})` → [Wed, 15 Apr 2026] Google News
[Mon, 27 Apr 2026] Bryce Elder looks to get pitching back on track in
- `search_web({'query': 'Atlanta Braves recent performance MLB 2025'})` → [Tue, 05 May 2026] Google News
[Tue, 03 Mar 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Atlanta Braves win loss record April 2026 MLB standings'})` → [Tue, 05 May 2026] Google News
[Mon, 04 May 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Miami Marlins starting pitcher today baseball'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] How To Watch Marlins vs. Braves Game 1: Max Meyer 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*