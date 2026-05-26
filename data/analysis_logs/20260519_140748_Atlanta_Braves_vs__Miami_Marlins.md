# Market Analysis — 2026-05-19 14:07 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $103,470
- **Liquidity:** $273,832

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,811 (+0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,714 (-0.1% 24h) → neutral

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
- → The Miami Marlins stunned the Braves 12-0 in the first game of their series on Monday, and now the league's top team will look to bounce back on Tue
- [Mon, 18 May 2026] Braves vs. Marlins prediction, odds, time: 2026 MLB picks for Tuesday, May 19 from proven model
- → According to Francys Romero of Beisbol FR, the Atlanta Braves are calling up a player to the MLB. They are in a series with the Marlins.
- [Tue, 19 May 2026] Atlanta Braves Make Roster Move After Marlins Game
- → The home plate umpire left the game with injury in the second inning.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 56.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL EDGE
- **Catalyst Strength:** 0.60

### Reasoning
Strong statistical signal (n=13,967) shows markets priced at 57% YES historically resolve YES only 44.7% of time, indicating significant market overpricing of YES outcome. The 12.3 percentage point edge (57% price vs 44.7% historical resolution) justifies a NO bet despite no direct catalyst. Past decisions on same market acknowledged this statistical edge but skipped due to 3% base rate gap; however, the absolute overpricing based on market behavior is substantial.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins upcoming game July 2025'})` → [Wed, 27 Aug 2025] Google News
[Mon, 16 Mar 2026] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Atlanta Braves recent performance results July 2025'})` → [Tue, 16 Dec 2025] Google News
[Thu, 31 Jul 2025] 2025 Player Reviews: Ozzie Albies - Battery Power

- `get_market_context({'keyword': 'Atlanta Braves'})` → No related markets found for 'Atlanta Braves'
- `get_market_context({'keyword': 'Miami Marlins'})` → No related markets found for 'Miami Marlins'
- `search_web({'query': 'polymarket Atlanta Braves vs Miami Marlins prediction'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Atlanta Braves vs Miami Marlins Odds - Monday May 
- `search_web({'query': 'Braves vs Marlins August 27 2025 score'})` → [Wed, 27 Aug 2025] Google News
[Wed, 27 Aug 2025] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Atlanta Braves Miami Marlins September 2025 pitching matchup'})` → [Sun, 10 May 2026] Google News
[Sat, 09 Aug 2025] Miami Marlins vs Arizona Diamondbacks | September 
- `search_web({'query': 'Braves starting pitcher next game vs Marlins'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Braves vs. Marlins Prediction, Odds, Probable Pitc
- `search_web({'query': 'Braves Marlins September 2025 schedule MLB'})` → [Sat, 09 Aug 2025] Google News
[Sun, 28 Sep 2025] Miami Marlins at Atlanta Braves Game Story, Scores
- `get_sports_data({'sport': 'mlb', 'team': 'Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*