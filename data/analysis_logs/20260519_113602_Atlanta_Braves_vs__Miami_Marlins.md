# Market Analysis — 2026-05-19 11:36 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 7
- **Volume 24h:** $83,039
- **Liquidity:** $111,611

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,814 (+0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,817 (-0.0% 24h) → neutral

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
- **Confidence:** 0%
- **p_true:** 61.9%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'team': 'Atlanta Braves', 'sport': 'mlb'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'team': 'Miami Marlins', 'sport': 'mlb'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `search_web({'query': 'Atlanta Braves vs Miami Marlins MLB 2024 recent results'})` → [Tue, 05 May 2026] Google News
[Tue, 12 May 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Atlanta Braves injury report today'})` → [Wed, 13 May 2026] Google News
[Thu, 14 May 2026] Latest Atlanta Braves Injury News Includes Ronald 
- `get_market_context({'keyword': 'Atlanta Braves vs Miami Marlins'})` → No related markets found for 'Atlanta Braves vs Miami Marlins'
- `search_web({'query': 'Atlanta Braves vs Miami Marlins probable pitchers May 2024'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Sanoja hits grand slam, Meyer pitches 6 sharp inni
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins May 18 2026 result score'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Atlanta Braves record 2026 season wins losses'})` → [Tue, 05 May 2026] Google News
[Tue, 19 May 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Ronald Acuna Jr. status May 2026 Atlanta Braves'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Atlanta Braves News: Ronald Acuna Jr. Activated fr
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*