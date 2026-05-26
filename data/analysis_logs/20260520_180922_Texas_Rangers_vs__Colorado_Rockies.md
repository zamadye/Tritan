# Market Analysis — 2026-05-20 18:09 UTC

## Market
- **Question:** Texas Rangers vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $59,123
- **Liquidity:** $224,409

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,455 (+0.8% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,571 (+1.1% 24h) → risk-ON

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- [SPORTS] Recent games:
- TEX @ COL | Scheduled | Colorado Rockies(home) 19-30 score:0 vs Texas Rangers(away) 23-25 score:0
- [SPORTS] Injuries:
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: texas rangers colorado rockies
- [Bing News]
- [Wed, 20 May 2026] texas rangers colorado rockies
- → Rockies starter Kyle Freeland is allowing a disastrous 11.76 hits per nine innings, leading to a bloated, 7.22 ERA.
- [Wed, 20 May 2026] Colorado Rockies vs. Texas Rangers: Game preview, picks and props for Wednesday
- → The Texas Rangers cruised to a 10-0 victory against the Colorado Rockies on Tuesday. Tyler Alexander started as an opener before Kumar Rocker turned
- [Wed, 20 May 2026] Rangers’ Kumar Rocker gets brutally honest after setting new career-high vs. Rockies
- → Here's how to watch Wednesday's Colorado Rockies vs Texas Rangers game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 56.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Texas Rangers'})` → INJURY [texas rangers] Wyatt Langford (LF): 10-Day-IL
INJURY [texas rangers] MacKenzie Gore (SP): Da
- `search_web({'query': 'Texas Rangers vs Colorado Rockies 2025 recent news'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Rangers vs. Rockies: Prediction, Lineups, How to W
- `search_web({'query': 'Rangers Rockies game preview injury updates'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Doyle leaves game with left side contusion, Rockie
- `search_web({'query': 'Brenton Doyle injury update Rangers Rockies'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Doyle leaves game with left side contusion, Rockie
- `get_market_context({'keyword': 'Texas Rangers'})` → No related markets found for 'Texas Rangers'
- `get_market_context({'keyword': 'Colorado Rockies'})` → No related markets found for 'Colorado Rockies'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Rangers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Texas Rangers vs Colorado Rockies May 20 2026 odds betting lines'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Rangers vs. Rockies (May 20, 2026) Odds and Spread
- `search_web({'query': 'Rockies vs Rangers starting pitchers May 20 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Rangers vs. Rockies (May 20, 2026) Live Score - ES

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*