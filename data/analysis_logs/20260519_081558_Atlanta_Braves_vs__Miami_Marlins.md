# Market Analysis — 2026-05-19 08:15 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $68,189
- **Liquidity:** $156,152

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,013 (+0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,188 (+0.4% 24h) → neutral

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
- → Atlanta Braves (32-16, first in the NL East) vs. Miami Marlins (22-26, fourth in the NL East) Miami; Tuesday, 4:10 p.m. EDT PITCHING PROBABLES: Brav
- [Mon, 18 May 2026] Marlins try to keep home win streak going, host the Braves
- → According to Francys Romero of Beisbol FR, the Atlanta Braves are calling up a player to the MLB. They are in a series with the Marlins.
- [Mon, 18 May 2026] Atlanta Braves Make Roster Move After Marlins Game
- → The Atlanta Braves came up empty in virtually every way on Monday as they were demolished by the Miami Marlins 12-0. The matchup was largely quiet f

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 52.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** INJURY/STAR PLAYER ABSENCE
- **Catalyst Strength:** 0.70

### Reasoning
Strong historical mispricing signal (57% markets resolve YES only 44.7% of time, n=13,967) combined with Ronald Acuña Jr. unlikely to play and Braves' 12-0 loss in first game. Market overprices YES by ~12% based on historical data, and current specific factors further reduce Braves' win probability.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins upcoming series preview'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] The Week Ahead for Atlanta: Back to the divisional
- `search_web({'query': 'Atlanta Braves starting pitcher tonight Miami Marlins'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Today's Three Things: Atlanta Braves Get Obliterat
- `get_market_context({'query': 'Atlanta Braves Miami Marlins'})` → [YES=50% vol=$14,508,529] Spurs vs. Thunder
[YES=50% vol=$5,821,653] Will Bitcoin hit $150k by June 
- `search_web({'query': "Ronald Acuña Jr. likely won't play vs Marlins reason"})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] When Braves superstar Ronald Acuna Jr. is expected

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*