# Market Analysis — 2026-05-18 11:05 UTC

## Market
- **Question:** Boston Red Sox vs. Kansas City Royals
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $44,068
- **Liquidity:** $233,232

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,783 (-2.1% 24h) → risk-OFF
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
- **Confidence:** 48%
- **p_true:** 51.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Historical stat signal suggests YES overpriced (~6.3% edge for NO: 51% market vs 44.7% historical resolution), but insufficient concrete evidence for action. Gap is only 1% (<5% threshold). No bookmaker odds available to verify mispricing. Pattern shows Entry 50-60% markets have only 25% win rate historically. Both teams have comparable injury profiles (Red Sox: 2 IL + 1 DTD; Royals: 2 IL + 1 DTD). No direct catalyst identified for this specific matchup. Previous identical market decision was SKIP. Statistical edge alone without verifiable catalyst does not meet concrete evidence requirement for BET_NO at this price level.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Red Sox'})` → INJURY [boston red sox] Carlos Narvaez (C): Day-To-Day
INJURY [boston red sox] Roman Anthony (LF): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Royals'})` → INJURY [kansas city royals] Cole Ragans (SP): 15-Day-IL
INJURY [kansas city royals] Matt Strahm (RP)
- `get_odds({'sport': 'baseball_mlb', 'team': 'Red Sox'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Boston Red Sox vs Kansas City Royals odds today'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Red Sox vs Royals Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Red Sox Royals game 7 days from now probable pitchers'})` → [Mon, 18 May 2026] Google News
[Mon, 23 Mar 2026] Official San Francisco Giants Website - MLB.com
[M
- `get_market_context({'keyword': 'Red Sox Royals'})` → No related markets found for 'Red Sox Royals'
- `search_web({'query': 'Boston Red Sox recent results form May 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Where to watch Boston Red Sox vs Kansas City Royal
- `search_web({'query': 'Kansas City Royals recent results form May 2026'})` → [Mon, 18 May 2026] Google News
[Fri, 01 May 2026] Where to watch Boston Red Sox vs Kansas City Royal
- `search_web({'query': '"Red Sox" "Royals" May 18 2026 odds moneyline'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Red Sox vs Royals Prediction, Odds, Moneyline, Spr
- `search_web({'query': 'Red Sox Royals series preview May 2026 pitching matchup'})` → [Mon, 18 May 2026] Google News
[Mon, 20 Apr 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'Red Sox vs Royals May 18 2026 betting odds implied probability'})` → [Thu, 14 May 2026] Google News
[Sat, 09 May 2026] MLB Rookie of the Year Odds 2026: AL &amp; NL Favo

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*