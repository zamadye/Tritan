# Market Analysis — 2026-05-19 10:10 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $69,584
- **Liquidity:** $169,268

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,733 (-0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,745 (-0.2% 24h) → neutral

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
- **Confidence:** 62%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 57% YES historically resolve YES only 44.7% of time, suggesting NO value at 57¢. However, past decisions on this same market both resulted in SKIP because gap=3% < 5% threshold. Braves are home team (historical edge) with comparable injury situations on both sides. Pattern shows entry 50-60% has only 33% WR (n=6), limiting confidence. Macro sentiment extreme fear (25/100) doesn't directly impact MLB outcomes. Without a direct catalyst (e.g., confirmed starting pitcher advantage, key player activation), the statistical edge alone does not meet the concrete evidence threshold for a bet. Recommend monitoring for injury news or pitching matchup confirmation before entry.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `search_web({'query': 'Atlanta Braves vs Miami Marlins upcoming game 2025'})` → [Sat, 09 Aug 2025] Google News
[Sun, 10 Aug 2025] Miami Marlins at Atlanta Braves Game Story, Scores
- `search_web({'query': 'Atlanta Braves recent results July 2025'})` → [Mon, 28 Jul 2025] Google News
[Sun, 27 Jul 2025] Atlanta Braves at Kansas City Royals Game Story, S
- `get_market_context({'keyword': 'Atlanta Braves'})` → No related markets found for 'Atlanta Braves'
- `get_market_context({'keyword': 'Miami Marlins'})` → No related markets found for 'Miami Marlins'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*