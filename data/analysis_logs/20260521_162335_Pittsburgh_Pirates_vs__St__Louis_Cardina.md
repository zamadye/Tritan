# Market Analysis — 2026-05-21 16:23 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 7
- **Volume 24h:** $165,522
- **Liquidity:** $479,477

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,156 (-0.2% 24h) → neutral
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
- → Here's how to watch Thursday's St. Louis Cardinals vs Pittsburgh Pirates game, including start times, TV channels, scores and how to stream.
- [Thu, 21 May 2026] Where to watch Pittsburgh Pirates vs St. Louis Cardinals: TV channel, start time, streaming for May 21
- → After ending a four-game skid Wednesday night, the Pittsburgh Pirates are now looking to take their midweek series against the Cardinals outright in

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 45.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** SYSTEMATIC MARKET BIAS
- **Catalyst Strength:** 0.70

### Reasoning
Stat signal shows markets priced at 52% historically resolve YES only 44.7% of the time (n=13,967), indicating YES is overpriced by ~7.3%. While the base rate gap is only 1%, the large-sample systematic bias provides a verifiable edge for a NO bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Jared Jones (SP): 60-Day-IL
INJURY [pittsburgh pirates] Ryan O'Hearn (RF
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Nathan Church (LF): Day-To-Day
INJURY [st. louis cardinals] Ramon Urias
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals 2025 schedule'})` → [Tue, 26 Aug 2025] Google News
[Mon, 25 Aug 2025] Pittsburgh Pirates at St. Louis Cardinals Game Sto
- `search_web({'query': 'Pittsburgh Pirates vs Cardinals preview August 2025 odds'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Pirates vs Cardinals Prediction, Odds, Moneyline, 
- `search_web({'query': 'Pittsburgh Pirates St. Louis Cardinals today 2025 game'})` → [Tue, 26 Aug 2025] Google News
[Wed, 27 Aug 2025] Pittsburgh Pirates at St. Louis Cardinals Game Sto
- `get_market_context({'keyword': 'Pittsburgh Pirates'})` → No related markets found for 'Pittsburgh Pirates'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*