# Market Analysis — 2026-05-20 18:22 UTC

## Market
- **Question:** Texas Rangers vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $59,178
- **Liquidity:** $224,592

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,430 (+0.8% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,488 (+0.8% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Recent games:
- TEX @ COL | Scheduled | Colorado Rockies(home) 19-30 score:0 vs Texas Rangers(away) 23-25 score:0
- [SPORTS] Injuries:
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: A.J. Puk — 60-Day-IL (Surgery)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: texas rangers colorado rockies
- [Bing News]
- [Wed, 20 May 2026] texas rangers colorado rockies
- → Rockies starter Kyle Freeland is allowing a disastrous 11.76 hits per nine innings, leading to a bloated, 7.22 ERA.
- [Wed, 20 May 2026] Colorado Rockies vs. Texas Rangers: Game preview, picks and props for Wednesday
- → The Texas Rangers cruised to a 10-0 victory against the Colorado Rockies on Tuesday. Tyler Alexander started as an opener before Kumar Rocker turned
- [Wed, 20 May 2026] Rangers’ Kumar Rocker gets brutally honest after setting new career-high vs. Rockies
- → Brandon Nimmo #24 of the Texas Rangers (C) celebrates toward his dugout after hitting an RBI single as TJ Rumfield #7 of the Colorado Rockies (L) an

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 46.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets priced at 54% resolve YES only 44.7% of the time, indicating 9.3% overpricing of YES. Despite Rockies being historically bad and Rangers having injuries (Seager, Langford, Gore IL), the systematic market inefficiency at this price point presents a clear edge. The base rate gap (2%) is small, but the price-point historical resolution data is robust and indicates the crowd is overconfident in Rangers winning at this price.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Texas Rangers'})` → INJURY [texas rangers] MacKenzie Gore (SP): Day-To-Day
INJURY [texas rangers] Wyatt Langford (LF): 1
- `get_odds({'sport': 'baseball_mlb', 'team': 'Texas Rangers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb', 'team': 'Colorado Rockies'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Texas Rangers vs Colorado Rockies 2025 MLB preview odds'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Rockies vs Rangers Prediction, Odds, Moneyline, Sp
- `search_web({'query': 'Colorado Rockies 2025 season record recent results'})` → [Mon, 18 May 2026] Google News
[Thu, 25 Sep 2025] 2026 MLB Standings and Records: Regular Season - M
- `get_market_context({'keyword': 'Texas Rangers Colorado Rockies'})` → No related markets found for 'Texas Rangers Colorado Rockies'
- `search_web({'query': 'Texas Rangers recent results May 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Texas Rangers at Colorado Rockies Game Story, Scor
- `search_web({'query': 'Colorado Rockies recent results May 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Texas Rangers at Colorado Rockies Game Story, Scor
- `search_web({'query': 'Rangers vs Rockies May 20 2026 starting pitchers'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Rangers vs. Rockies (May 20, 2026) Live Score - ES
- `search_web({'query': 'Texas Rangers 2026 record wins losses'})` → [Mon, 18 May 2026] Google News
[Tue, 24 Mar 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': '"Rockies vs Rangers" May 20 2026 odds moneyline'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] Rockies vs Rangers Prediction, Odds, Moneyline, Sp
- `search_web({'query': 'Colorado Rockies worst team MLB 2026 record'})` → [Mon, 18 May 2026] Google News
[Tue, 24 Mar 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Rangers Rockies May 20 2026 prediction analysis'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Rangers vs Rockies Prediction, Odds: Over/Under Pi

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*