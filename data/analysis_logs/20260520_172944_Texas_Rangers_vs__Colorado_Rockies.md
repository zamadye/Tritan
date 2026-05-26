# Market Analysis — 2026-05-20 17:29 UTC

## Market
- **Question:** Texas Rangers vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $58,950
- **Liquidity:** $197,370

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,466 (+0.8% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,242 (+0.5% 24h) → neutral

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
- → Colorado Rockies: starting pitchers are Jack Leiter for the Rangers and Kyle Freeland for the Rockies. The Rangers take on the Rockies in an afterno
- [Wed, 20 May 2026] Texas Rangers lineup for May 20, 2026
- → The Texas Rangers cruised to a 10-0 victory against the Colorado Rockies on Tuesday. Tyler Alexander started as an opener before Kumar Rocker turned
- [Wed, 20 May 2026] Rangers’ Kumar Rocker gets brutally honest after setting new career-high vs. Rockies
- → Rockies starter Kyle Freeland is allowing a disastrous 11.76 hits per nine innings, leading to a bloated, 7.22 ERA.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 47.2%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.72

### Reasoning
Strong statistical signal (n=13,967) shows markets at 54% resolve YES only 44.7% of the time — indicating ~9% overpricing of YES. Rangers have key injuries (Seager, Langford on IL; Gore day-to-day) which slightly weakens their lineup, though Rockies also have injuries. No breaking news contradicts the statistical edge. Confidence tempered by weak WR=33% pattern in 50-60% entry zone (n=9), but large-sample stat edge (13,967 obs) outweighs this. Market appears to be pricing YES too high relative to historical resolution rates.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Rangers'})` → INJURY [texas rangers] Wyatt Langford (LF): 10-Day-IL
INJURY [texas rangers] MacKenzie Gore (SP): Da
- `get_sports_data({'sport': 'mlb', 'team': 'Rockies'})` → INJURY [colorado rockies] Brenton Doyle (CF): Day-To-Day
INJURY [colorado rockies] Ryan Feltner (SP)
- `search_web({'query': 'Texas Rangers vs Colorado Rockies recent news 2025'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Rangers vs. Rockies: Prediction, Lineups, How to W
- `search_web({'query': 'Texas Rangers today 2025 roster moves'})` → [Thu, 26 Mar 2026] Google News
[Sat, 08 Nov 2025] Tracking every team's offseason moves - MLB.com
[M
- `get_market_context({'keyword': 'Texas Rangers'})` → No related markets found for 'Texas Rangers'
- `get_market_context({'keyword': 'Rangers Rockies'})` → No related markets found for 'Rangers Rockies'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Rangers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Texas Rangers vs Colorado Rockies game odds betting line May 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Rangers vs. Rockies Prediction, Odds, Probable Pit

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*