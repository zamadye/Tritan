# Market Analysis — 2026-05-21 15:22 UTC

## Market
- **Question:** Pittsburgh Pirates vs. St. Louis Cardinals
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 7
- **Volume 24h:** $132,528
- **Liquidity:** $565,514

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,131 (-0.6% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $76,894 (-0.7% 24h) → neutral
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
- → After ending a four-game skid Wednesday night, the Pittsburgh Pirates are now looking to take their midweek series against the Cardinals outright in
- [Thu, 21 May 2026] After ending losing skid, Pirates look to build on win against Cardinals
- → The Pittsburgh Pirates (24-24) are on their way to Busch Stadium on Thursday where they will attempt to beat the St. Louis Cardinals (28-19). The li

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 53.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Statistical signal indicates YES overpriced (52% market vs 44.7% historical), but base rate gap is only +1% (<5% gate requirement). Both teams have multiple injuries (Pirates: O'Hearn, Jones, Bart; Cardinals: Urias, Nootbaar, Naughton) but no direct catalyst for this specific 7-day-out matchup. Missing key info: starting pitchers, recent form, head-to-head record. Past decisions on identical markets were SKIP due to insufficient edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Pittsburgh Pirates'})` → INJURY [pittsburgh pirates] Ryan O'Hearn (RF): 10-Day-IL
INJURY [pittsburgh pirates] Jared Jones (SP
- `get_sports_data({'sport': 'mlb', 'team': 'St. Louis Cardinals'})` → INJURY [st. louis cardinals] Ramon Urias (3B): 10-Day-IL
INJURY [st. louis cardinals] Lars Nootbaar 
- `search_web({'query': 'Pittsburgh Pirates vs St. Louis Cardinals 2025'})` → [Tue, 19 May 2026] Google News
[Tue, 26 Aug 2025] Where to watch Pittsburgh Pirates vs St. Louis Car
- `search_web({'query': 'Pittsburgh Pirates injury update'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Cherington: Update on Jones, Pirates Looking at ‘W
- `search_web({'query': 'St. Louis Cardinals injury update'})` → [Tue, 19 May 2026] Google News
[Sat, 16 May 2026] Cardinals’ Oliver Marmol shares Masyn Winn knee in
- `get_market_context({'keyword': 'Pirates Cardinals'})` → No related markets found for 'Pirates Cardinals'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Pittsburgh Pirates'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*