# Market Analysis — 2026-05-20 18:33 UTC

## Market
- **Question:** Texas Rangers vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $61,809
- **Liquidity:** $265,895

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,440 (+0.9% 24h) → neutral
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
- → After last night’s damp, cold, and miserable blowout loss, the Colorado Rockies find themselves tied at a game each in their series with the Texas R

## LLM Decision
- **Action:** SKIP
- **Confidence:** 48%
- **p_true:** 56.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.45

### Reasoning
Strong stat signal (n=13,967) suggests markets at 54% resolve YES only 44.7%, indicating NO edge. However: (1) base rate gap is only 2% (below 5% gate threshold), (2) entry at 50-60% price range has historically poor WR of 33% from 9 trades, (3) this exact market was already analyzed twice with decisions of NO/SKIP, (4) no new catalysts or breaking news to change prior assessment. The mixed signals between strong stat pattern and poor entry zone performance result in confidence below actionable threshold.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Texas Rangers'})` → INJURY [texas rangers] MacKenzie Gore (SP): Day-To-Day
INJURY [texas rangers] Wyatt Langford (LF): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Colorado Rockies'})` → INJURY [colorado rockies] Brenton Doyle (CF): Day-To-Day
INJURY [colorado rockies] Ryan Feltner (SP)
- `get_market_context({'keyword': 'Texas Rangers Colorado Rockies MLB'})` → No related markets found for 'Texas Rangers Colorado Rockies MLB'
- `search_web({'query': 'Texas Rangers vs Colorado Rockies 2025 MLB preview odds'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Rockies vs Rangers Prediction, Odds, Moneyline, Sp
- `search_web({'query': 'Texas Rangers recent results wins losses May 2025'})` → [Mon, 18 May 2026] Google News
[Tue, 05 May 2026] 2026 MLB Standings and Records: Regular Season - M
- `get_odds({'sport': 'baseball_mlb', 'team': 'Rangers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*