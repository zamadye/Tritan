# Market Analysis — 2026-05-21 16:39 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 7
- **Volume 24h:** $168,121
- **Liquidity:** $483,357

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,161 (+0.0% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,106 (-0.1% 24h) → neutral
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
- → The Pirates are on the road looking to grab a win today.
- [Thu, 21 May 2026] Game #50: Pittsburgh Pirates vs. St. Louis Cardinals
- → The Pittsburgh Pirates (24-24) are on their way to Busch Stadium on Thursday where they will attempt to beat the St. Louis Cardinals (28-19). The li

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 43.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.75

### Reasoning
Stat signal shows systematic YES overpricing: markets at 52% resolve YES only 44.7% of time (n=13,967), creating 7.3% edge for NO. Entry pattern for 50-60% range confirms YES WR=44% (n=18). No game-specific catalyst required when statistical edge is this large and consistent across 13,967 historical observations.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Jared Jones (SP): 60-Day-IL
INJURY [pittsburgh pirates] Ryan O'Hearn (RF
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Nathan Church (LF): Day-To-Day
INJURY [st. louis cardinals] Ramon Urias
- `search_web({'query': 'Pittsburgh Pirates recent games April 2025'})` → [Mon, 23 Jun 2025] Google News
[Tue, 10 Feb 2026] Pittsburgh Pirates at Milwaukee Brewers Game Story
- `search_web({'query': 'St. Louis Cardinals recent games April 2025'})` → [Wed, 20 Aug 2025] Google News
[Tue, 14 Apr 2026] St. Louis Cardinals at Miami Marlins Game Story, S
- `get_market_context({'keyword': 'Pittsburgh Pirates vs St. Louis Cardinals'})` → No related markets found for 'Pittsburgh Pirates vs St. Louis Cardinals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals 2025 season series results head to head'})` → [Mon, 18 May 2026] Google News
[Mon, 23 Mar 2026] How real are good starts from Rays, Cardinals, Pir
- `search_web({'query': 'Pittsburgh Pirates 2025 season record standings'})` → [Mon, 18 May 2026] Google News
[Tue, 05 May 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Pittsburgh Pirates vs Cardinals upcoming series June 2025'})` → [Thu, 28 Aug 2025] Google News
[Wed, 27 Aug 2025] Pirates vs. Cardinals Highlights | 08/28/2025 - ML
- `get_sports_data({'sport': 'mlb'})` → INJURY [arizona diamondbacks] Derek Law (RP): Day-To-Day
INJURY [arizona diamondbacks] Tommy Henry (

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*