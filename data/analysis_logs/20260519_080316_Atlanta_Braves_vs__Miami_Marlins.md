# Market Analysis — 2026-05-19 08:03 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $68,104
- **Liquidity:** $153,922

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,168 (+0.2% 24h) → neutral
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
- [Mon, 18 May 2026] atlanta braves miami marlins
- → The Atlanta Braves came up empty in virtually every way on Monday as they were demolished by the Miami Marlins 12-0. The matchup was largely quiet f
- [Mon, 18 May 2026] Watch: Marlins catch fire and destroy Braves 12-0
- → According to Francys Romero of Beisbol FR, the Atlanta Braves are calling up a player to the MLB. They are in a series with the Marlins.
- [Mon, 18 May 2026] Atlanta Braves Make Roster Move After Marlins Game
- → Here's how to watch Monday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 52.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MISPRICING
- **Catalyst Strength:** 0.70

### Reasoning
Strong historical mispricing signal: markets at 57% price point historically resolve YES only 44.7% of the time (n=13,967), representing a ~12.3% edge for NO. While Braves are NL East leaders with pitching edge (Ritchie vs Meyer), the market is systematically overpricing YES at this price point. Sports pattern shows 80% WR overall but 50-60% entry zone has only 33% WR for YES bets, confirming this range is typically overpriced. Information gap exists between crowd perception and historical resolution rates.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'sport': 'mlb', 'team': 'Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 prediction odds'})` → [Tue, 19 May 2026] Google News
[Mon, 13 Apr 2026] Braves vs Marlins Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Atlanta Braves recent results 2025'})` → [Sat, 20 Sep 2025] Google News
[Sun, 28 Sep 2025] Atlanta Braves at Detroit Tigers Game Story, Score
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `search_web({'query': 'Braves Marlins May 2026 starting pitcher lineup'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] How To Watch Marlins vs. Braves Game 1: Max Meyer 
- `search_web({'query': 'Atlanta Braves win streak 2026 season record'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Every team's odds to win the 2026 World Series: Do
- `search_web({'query': 'Max Meyer Marlins 2026 stats ERA'})` → [Tue, 24 Feb 2026] Google News
[Thu, 18 Dec 2025] Miami Marlins 2026 Starting Pitchers and SP Prospe
- `search_web({'query': 'JR Ritchie Braves pitcher 2026 ERA stats'})` → [Thu, 23 Apr 2026] Google News
[Mon, 16 Mar 2026] What to expect from Braves No. 2 prospect Ritchie 
- `search_web({'query': 'Braves vs Marlins May 19 2026 prediction picks'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] MLB Picks Today: Greg Peterson Best Bets Tuesday, 
- `search_web({'query': 'Atlanta Braves 2026 record standings NL East'})` → [Tue, 05 May 2026] Google News
[Thu, 23 Apr 2026] Is the NL East Race Already Over? - FanGraphs
[Thu
- `search_web({'query': '"JR Ritchie" Braves 2026 season stats win loss'})` → [Thu, 23 Apr 2026] Google News
[Thu, 23 Apr 2026] JR Ritchie picks up first career win in MLB debut 
- `search_web({'query': 'Miami Marlins 2026 season record wins losses'})` → [Sun, 17 May 2026] Google News
[Tue, 24 Mar 2026] 2026 Cardinals Standings and Record: Regular Seaso

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*