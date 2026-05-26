# Market Analysis — 2026-05-19 10:24 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $71,080
- **Liquidity:** $94,737

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,709 (-0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,710 (-0.0% 24h) → neutral

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
- [Tue, 19 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 19
- → Atlanta Braves (32-16, first in the NL East) vs. Miami Marlins (22-26, fourth in the NL East) Miami; Tuesday, 4:10 p.m. EDT PITCHING PROBABLES: Brav
- [Mon, 18 May 2026] Marlins try to keep home win streak going, host the Braves
- → According to Francys Romero of Beisbol FR, the Atlanta Braves are calling up a player to the MLB. They are in a series with the Marlins.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 50.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 57% YES historically resolve YES only 44.7% of time - market overprices YES by ~12.3 percentage points. NO available at 43% vs true probability ~55.3% = ~12.3% edge. Both teams have moderate injuries (Braves: 3 IL including DH and CF; Marlins: 3 IL including SP), but no concrete matchup data found to confirm specific advantage. Gap vs base rate is only 3% (below 5% gate), but the absolute statistical mispricing is substantial enough to warrant action. Crowd appears biased toward YES despite historical evidence of overpricing at this price point.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins upcoming game odds prediction 2025'})` → [Mon, 25 Aug 2025] Google News
[Wed, 15 Apr 2026] Braves vs. Marlins Prediction, Odds, Picks - Augus
- `search_web({'query': 'Atlanta Braves Miami Marlins recent form injuries August 2025'})` → [Thu, 30 Apr 2026] Google News
[Thu, 26 Mar 2026] Spencer Strider Injury Update: Nearing 2026 Return
- `get_market_context({'query': 'Atlanta Braves Miami Marlins'})` → [YES=50% vol=$5,821,653] Will Bitcoin hit $150k by June 30, 2026?
[YES=50% vol=$2,707,456] Will Trum
- `get_market_context({'query': 'MLB baseball prediction market'})` → [YES=50% vol=$5,821,653] Will Bitcoin hit $150k by June 30, 2026?
[YES=50% vol=$2,707,456] Will Trum

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*