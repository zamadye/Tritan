# Market Analysis — 2026-05-20 18:56 UTC

## Market
- **Question:** Texas Rangers vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $68,523
- **Liquidity:** $266,698

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,352 (+0.7% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,352 (+0.7% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- [SPORTS] Recent games:
- TEX @ COL | Scheduled | Colorado Rockies(home) 19-30 score:0 vs Texas Rangers(away) 23-25 score:0
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Corbin Burnes — 60-Day-IL (Surgery)
- ?: James McCann — 10-Day-IL (Strain)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: texas rangers colorado rockies
- [Bing News]
- [Wed, 20 May 2026] texas rangers colorado rockies
- → Rockies starter Kyle Freeland is allowing a disastrous 11.76 hits per nine innings, leading to a bloated, 7.22 ERA.
- [Wed, 20 May 2026] Colorado Rockies vs. Texas Rangers: Game preview, picks and props for Wednesday
- → The Texas Rangers cruised to a 10-0 victory against the Colorado Rockies on Tuesday. Tyler Alexander started as an opener before Kumar Rocker turned
- [Wed, 20 May 2026] Rangers’ Kumar Rocker gets brutally honest after setting new career-high vs. Rockies
- → The Colorado Rockies will be facing the Texas Rangers on Wendesday afternoon. They will be without one of their outfielders in the game.

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 46.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** HISTORICAL_STATISTICAL_EDGE
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 54% resolve YES only 44.7% of the time, creating a 9.3% edge for NO. Market overprices YES by ~9 points. Both teams have comparable injuries (Rangers: Seager, Langford IL; Rockies: Feltner, Vodnik IL). Previous SKIP decisions at same price failed gate due to 2% gap, but the underlying stat signal at 54% price level shows persistent market overpricing. Entry range 50-60% has weak historical WR (33%), supporting NO. Macro fear environment irrelevant to sports. No direct news catalyst found to contradict statistical edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Texas Rangers'})` → INJURY [texas rangers] MacKenzie Gore (SP): Day-To-Day
INJURY [texas rangers] Wyatt Langford (LF): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Colorado Rockies'})` → INJURY [colorado rockies] Victor Vodnik (RP): 15-Day-IL
INJURY [colorado rockies] Brenton Doyle (CF)
- `search_web({'query': 'Texas Rangers vs Colorado Rockies 2025'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Rangers vs. Rockies: Prediction, Lineups, How to W
- `search_web({'query': 'Rangers Rockies starting pitchers May 20 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Texas Rangers lineup for May 20, 2026 - Yahoo Spor
- `get_market_context({'keyword': 'Texas Rangers'})` → No related markets found for 'Texas Rangers'
- `get_market_context({'keyword': 'Colorado Rockies'})` → No related markets found for 'Colorado Rockies'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Rangers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*