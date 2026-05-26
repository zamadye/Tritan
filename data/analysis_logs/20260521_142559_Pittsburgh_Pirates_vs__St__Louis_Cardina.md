# Market Analysis — 2026-05-21 14:25 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $105,656
- **Liquidity:** $253,865

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $76,919 (-0.6% 24h) → neutral
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
- **Confidence:** 0%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Lars Nootbaar (LF): 60-Day-IL
INJURY [st. louis cardinals] Ramon Urias 
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals upcoming game 2024'})` → [Tue, 05 May 2026] Google News
[Wed, 12 Jun 2024] 2026 Spring Training - MLB.com
[Tue, 01 Jul 2025] 
- `search_web({'query': 'Pittsburgh Pirates injury report'})` → [Sun, 17 May 2026] Google News
[Thu, 19 Mar 2026] Cherington: Update on Jones, Pirates Looking at ‘W
- `get_market_context({'keyword': 'Pittsburgh Pirates St. Louis Cardinals'})` → No related markets found for 'Pittsburgh Pirates St. Louis Cardinals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pittsburgh Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb', 'team': 'St. Louis Cardinals'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals odds and prediction May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pirates vs. Cardinals prediction, odds, time: 2026
- `search_web({'query': '"Pittsburgh Pirates" "St. Louis Cardinals" moneyline odds May 21 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pirates vs. Cardinals prediction, odds, time: 2026
- `search_web({'query': 'Pittsburgh Pirates starting pitcher May 21 2026'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `search_web({'query': 'St. Louis Cardinals starting pitcher May 21 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Checking in on St. Louis Cardinals pitching prospe
- `search_web({'query': 'Pittsburgh Pirates recent results May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pittsburgh Pirates at St. Louis Cardinals Game Sto
- `search_web({'query': 'St. Louis Cardinals recent results May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pittsburgh Pirates at St. Louis Cardinals Game Sto
- `search_web({'query': '"Pittsburgh Pirates" "St. Louis Cardinals" odds moneyline May 21 2026 site:vegasinsider.com OR site:oddschecker.com OR site:actionnetwork.com'})` → [Thu, 21 May 2026] Google News
[Wed, 11 Aug 2021] Pirates vs Cardinals Prediction, Pick, Odds: Wind 
- `search_web({'query': 'Pirates Cardinals game 2 score May 20 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Pittsburgh Pirates at St. Louis Cardinals Game Sto

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*