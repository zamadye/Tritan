# Market Analysis — 2026-05-19 13:04 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $99,994
- **Liquidity:** $234,295

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,890 (-0.7% 24h) → neutral
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
- **Confidence:** 65%
- **p_true:** 51.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.72

### Reasoning
Strong statistical signal from large sample (n=13,967) shows markets priced at 57% YES resolve YES only 44.7% of time — a 12.3pp overpricing gap. Both teams have meaningful injuries (Braves missing DH/CF). Entry zone 50-60% historically shows weak 33% WR. While base rate (60%) suggests Braves should be favored, the market-level stat signal is the more actionable edge here. Confidence tempered to 0.68 because: (1) game is TODAY so lineups/weather could shift, (2) gap is statistical edge not direct game evidence, (3) past decisions on same market were SKIPs.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `search_web({'query': 'Atlanta Braves vs Miami Marlins game news injury report 2026'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] How to watch Braves vs. Marlins: TV channel and st
- `search_web({'query': 'Braves Marlins MLB recent results and predictions'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Atlanta Braves at Miami Marlins Game Story, Scores
- `get_market_context({'keyword': 'Atlanta Braves MLB'})` → No related markets found for 'Atlanta Braves MLB'
- `search_web({'query': 'Atlanta Braves vs Miami Marlins probable pitchers May 19 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Braves Marlins odds line May 19 2026 who is pitching tonight'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Braves vs. Marlins Prediction, Odds, &amp; Expert 
- `get_market_context({'keyword': 'Braves Marlins baseball'})` → No related markets found for 'Braves Marlins baseball'
- `search_web({'query': 'Atlanta Braves record 2026 season standings results'})` → [Tue, 05 May 2026] Google News
[Mon, 18 May 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Miami Marlins record 2026 season standings results'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] 2026 MLB Standings and Records: Regular Season - M

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*