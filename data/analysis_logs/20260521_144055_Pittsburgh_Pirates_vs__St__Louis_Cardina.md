# Market Analysis — 2026-05-21 14:40 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $112,579
- **Liquidity:** $273,687

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,028 (-0.5% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $76,803 (-0.7% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Gunnar Hoglund — 60-Day-IL (Surgery)

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
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 52.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_TREND
- **Catalyst Strength:** 0.60

### Reasoning
Statistical signal from a large sample (n=13,967) indicates that markets at a 54% YES price historically resolve YES only 44.7% of the time, suggesting the crowd is systematically overpricing the YES outcome. While the base rate (56%) is close to the market price, the historical resolution rate provides a ~9.3% edge for the NO side.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'team': 'Pittsburgh Pirates', 'sport': 'mlb'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'team': 'St. Louis Cardinals', 'sport': 'mlb'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `get_odds({'team': 'Pittsburgh Pirates', 'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Pittsburgh Pirates'})` → No related markets found for 'Pittsburgh Pirates'
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals prediction today'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Pirates vs Cardinals Prediction, Picks &amp; Odds 
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals recent performance news'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Where to watch Pittsburgh Pirates vs St. Louis Car
- `search_web({'query': 'Pittsburgh Pirates outfield adjustment May 2026'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Pirates' Konnor Griffin Getting Even Better in May
- `search_web({'query': '"Pittsburgh Pirates" "outfield adjustment" "Cardinals" game May 21 2026'})` → [Wed, 20 May 2026] Google News
[] Pirates Make Big Outfield Adjustment Before Cardinals Game - Sport
- `get_sports_data({'sport': 'mlb'})` → INJURY [arizona diamondbacks] A.J. Puk (RP): 60-Day-IL
INJURY [arizona diamondbacks] Corbin Burnes (

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*