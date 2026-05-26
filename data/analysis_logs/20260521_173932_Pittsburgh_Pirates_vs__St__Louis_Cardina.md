# Market Analysis — 2026-05-21 17:39 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 63.0%
- **Days Left:** 6
- **Volume 24h:** $436,816
- **Liquidity:** $33,585

## Statistical Prior
- **p_base:** 69.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 6.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,918 (+0.6% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,906 (+0.5% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Recent games:
- PIT @ STL | In Progress | St. Louis Cardinals(home) 28-20 score:0 vs Pittsburgh Pirates(away) 25-24 score:1
- [SPORTS] Injuries:
- ?: Derek Law — Day-To-Day (Surgery)
- ?: Spencer Giesting — Day-To-Day (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: pittsburgh pirates louis cardinals
- [Bing News]
- [Thu, 21 May 2026] pittsburgh pirates louis cardinals
- → The St. Louis Cardinals look to win the series at home against the Pittsburgh Pirates on Thursday afternoon. The Cardinals won Game 1, 9-6, while th
- [Thu, 21 May 2026] Pirates vs. Cardinals prediction, odds, time: 2026 MLB picks for Thursday, May 21 from proven model
- → The Pittsburgh Pirates (24-24) are on their way to Busch Stadium on Thursday where they will attempt to beat the St. Louis Cardinals (28-19). The li
- [Wed, 20 May 2026] Pittsburgh Pirates vs St. Louis Cardinals Prediction, 5/21/2026 MLB Picks, Best Bets &amp; Odds
- → Spencer Horwitz homered, Konnor Griffin had four singles, and the Pittsburgh Pirates beat the St. Louis Cardinals 7-0 to snap a four-game losing str

## LLM Decision
- **Action:** YES
- **Confidence:** 65%
- **p_true:** 73.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.40

### Reasoning
Historical base rate (69% true prob vs. 63% market price) indicates YES is underpriced by 6%, and pattern data shows strong win rate (83%) for sports bets in the 60-70% entry range. Injury reports for both teams likely cancel out, with no clear asymmetric catalyst. Crowd appears to underestimate YES outcome based on historical mispricing.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET YES $1.00

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Jared Jones (SP): 60-Day-IL
INJURY [pittsburgh pirates] Ryan O'Hearn (RF
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Nathan Church (LF): Day-To-Day
INJURY [st. louis cardinals] Ramon Urias
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals 2025 series'})` → [Tue, 26 Aug 2025] Google News
[Wed, 27 Aug 2025] Pittsburgh Pirates at St. Louis Cardinals Game Sto
- `get_market_context({'keyword': 'Pittsburgh Pirates'})` → No related markets found for 'Pittsburgh Pirates'
- `get_market_context({'keyword': 'St. Louis Cardinals'})` → No related markets found for 'St. Louis Cardinals'
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals preview August 2025'})` → [Thu, 28 Aug 2025] Google News
[Wed, 27 Aug 2025] Pittsburgh Pirates at St. Louis Cardinals Preview 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*