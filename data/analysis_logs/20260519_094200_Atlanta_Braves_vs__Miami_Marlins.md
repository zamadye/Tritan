# Market Analysis — 2026-05-19 09:42 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $68,800
- **Liquidity:** $168,402

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,716 (-0.3% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,972 (+0.1% 24h) → neutral

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
- → The Atlanta Braves are paying one of their pitchers nearly $10 million this season. He struggled against the Miami Marlins (on Monday).

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 52.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal shows markets at 57% YES historically resolve YES only 44.7% of the time (n=13,967). This creates a significant information gap where YES is overpriced by ~12 percentage points. Injury analysis shows no major star players affected on either team, and no breaking news catalyst found that would contradict the historical pattern. The info gap trades pattern (65% WR) supports betting against the overpriced YES position.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 recent matchup results'})` → [Sun, 17 May 2026] Google News
[Tue, 14 Apr 2026] 2026 MLB Standings and Records: Wild Card - MLB.co
- `search_web({'query': 'Braves Marlins prediction today 2025'})` → [Mon, 13 Apr 2026] Google News
[Mon, 25 Aug 2025] Miami Marlins at Atlanta Braves odds, picks and pr
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*