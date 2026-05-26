# Market Analysis — 2026-05-21 17:22 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 6
- **Volume 24h:** $381,005
- **Liquidity:** $531,796

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,682 (+0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $76,956 (-0.3% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [SPORTS] Recent games:
- PIT @ STL | Scheduled | St. Louis Cardinals(home) 28-20 score:0 vs Pittsburgh Pirates(away) 25-24 score:0
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Tommy Henry — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: pittsburgh pirates louis cardinals
- [Bing News]
- [Thu, 21 May 2026] pittsburgh pirates louis cardinals
- → The St. Louis Cardinals look to win the series at home against the Pittsburgh Pirates on Thursday afternoon. The Cardinals won Game 1, 9-6, while th
- [Thu, 21 May 2026] Pirates vs. Cardinals prediction, odds, time: 2026 MLB picks for Thursday, May 21 from proven model
- → The Pittsburgh Pirates (24-24) are on their way to Busch Stadium on Thursday where they will attempt to beat the St. Louis Cardinals (28-19). The li
- [Thu, 21 May 2026] Pittsburgh Pirates vs St. Louis Cardinals Prediction, 5/21/2026 MLB Picks, Best Bets &amp; Odds
- → Here's how to watch Thursday's St. Louis Cardinals vs Pittsburgh Pirates game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 53.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL META-SIGNAL
- **Catalyst Strength:** 0.50

### Reasoning
Statistical signal indicates market at 52% YES historically resolves YES only 44.7% of the time (n=13,967), suggesting overpricing. However, gap vs base rate is only +1%, below 5% threshold for actionable edge. Past decisions for same market skipped. Injury data shows both teams have key players out, but no clear catalyst to determine outcome. Confidence moderate but insufficient for bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Jared Jones (SP): 60-Day-IL
INJURY [pittsburgh pirates] Ryan O'Hearn (RF
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Nathan Church (LF): Day-To-Day
INJURY [st. louis cardinals] Ramon Urias
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals series preview 2025'})` → [Thu, 28 Aug 2025] Google News
[Thu, 28 Aug 2025] Pittsburgh Pirates at St. Louis Cardinals Preview 
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals injury news June 2025'})` → [Thu, 21 May 2026] Google News
[Wed, 20 Aug 2025] Mlodzinski, Bullpen Combine to Blank Cardinals; Pi
- `get_market_context({'keyword': 'Pittsburgh Pirates St. Louis Cardinals MLB'})` → No related markets found for 'Pittsburgh Pirates St. Louis Cardinals MLB'
- `search_web({'query': 'Pittsburgh Pirates St. Louis Cardinals today starting pitcher August 2025'})` → [Tue, 19 May 2026] Google News
[Mon, 25 Aug 2025] Buying or Selling the NL’s Most Surprising Contend
- `search_web({'query': '"Pittsburgh Pirates" "St. Louis Cardinals" August 28 2025 probable pitchers'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'Pirates Cardinals 2025 season series results head to head'})` → [Mon, 18 May 2026] Google News
[Mon, 23 Mar 2026] How real are good starts from Rays, Cardinals, Pir

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*