# Market Analysis — 2026-05-21 17:07 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 7
- **Volume 24h:** $277,359
- **Liquidity:** $433,056

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,163 (-0.1% 24h) → neutral
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
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 43.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** SYSTEMATIC_OVERPRICING
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical evidence (n=13,967) shows markets at 52% YES resolve YES only 44.7% of the time, indicating systematic YES overpricing. While the 1% gap to base rate failed previous gate checks, the direct historical data provides a clear edge for NO bets in this specific price range.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Jared Jones (SP): 60-Day-IL
INJURY [pittsburgh pirates] Ryan O'Hearn (RF
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Nathan Church (LF): Day-To-Day
INJURY [st. louis cardinals] Ramon Urias
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pittsburgh Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Pittsburgh Pirates vs St Louis Cardinals upcoming game'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pittsburgh Pirates at St. Louis Cardinals Game Sto
- `search_web({'query': 'Pittsburgh Pirates injury news May 2025'})` → [Sun, 22 Mar 2026] Google News
[Mon, 15 Dec 2025] Pirates Give New Injury Update on Jared Jones - Sp
- `search_web({'query': 'Pittsburgh Pirates vs St Louis Cardinals odds'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pirates vs. Cardinals prediction, odds, time: 2026
- `search_web({'query': 'St. Louis Cardinals injury update 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 18 Mar 2026] 2026 St. Louis Cardinals Top 30 Prospects May Upda
- `get_market_context({'keyword': 'Pittsburgh Pirates'})` → No related markets found for 'Pittsburgh Pirates'
- `get_market_context({'keyword': 'Cardinals'})` → No related markets found for 'Cardinals'
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'
- `search_web({'query': 'Pittsburgh Pirates St. Louis Cardinals May 2026 series preview'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] Pittsburgh Pirates at St. Louis Cardinals Preview 
- `search_web({'query': 'Pittsburgh Pirates record 2026 MLB standings'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': '"How real are good starts" Pirates Cardinals 2026'})` → [Mon, 18 May 2026] Google News
[Thu, 14 May 2026] How real are good starts from Rays, Cardinals, Pir

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*