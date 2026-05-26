# Market Analysis — 2026-05-18 10:47 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $44,055
- **Liquidity:** $214,501

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,785 (-2.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,795 (-2.1% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Recent games:
- BOS @ ATL | Final | Atlanta Braves(home) 32-15 score:8 vs Boston Red Sox(away) 19-27 score:1
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: boston kansas city royals
- [Bing News]
- [Mon, 18 May 2026] boston kansas city royals
- → Here's how to watch Monday's Kansas City Royals vs Boston Red Sox game, including start times, TV channels, scores and how to stream.
- [Mon, 18 May 2026] Where to watch Boston Red Sox vs Kansas City Royals: TV channel, start time, streaming for May 18
- → Boston Red Sox (19-27, fifth in the AL East) vs. Kansas City Royals (20-27, fifth in the AL Central) Kansas City, Missouri; Monday, 7:40 p.m. EDT PI
- [Sun, 31 Dec 2000] Royals look to break 6-game skid, take on the Red Sox
- → View the latest in Kansas City Royals, MLB team news here. Trending news, game recaps, highlights, player information, rumors, videos and more from 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 45.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MISPRICING
- **Catalyst Strength:** 0.65

### Reasoning
Historical data shows markets at 51% resolve YES only 44.7% of the time (n=13,967), creating ~6.3% edge for NO. Both teams have key injuries (Red Sox: Anthony, Story IL; Royals: Ragans, Strahm IL). Statistical mispricing is the primary catalyst, with no direct event-driven news. The base rate (52%) and market price (51%) both overprice YES relative to the well-documented historical resolution rate.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Carlos Narvaez (C): Day-To-Day
INJURY [boston red sox] Roman Anthony (LF): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Kansas City Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] Matt Strahm (RP)
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals 2025'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Kansas City Royals vs Boston Red Sox Prediction &a
- `search_web({'query': 'Red Sox Royals series 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] MLB 2026 Buzz: Dodgers Place Jack Dreyer on IL, Tr
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Where to watch Boston Red Sox vs Kansas City Royal
- `get_odds({'sport': 'baseball_mlb', 'team': 'Boston Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*