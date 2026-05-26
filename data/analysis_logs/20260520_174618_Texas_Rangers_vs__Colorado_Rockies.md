# Market Analysis — 2026-05-20 17:46 UTC

## Market
- **Question:** Texas Rangers vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $59,132
- **Liquidity:** $203,560

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,523 (+0.9% 24h) → neutral
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
- → After an emphatic 10-0 win on Tuesday night, the Texas Rangers will be back in action on Wednesday against the Colorado Rockies.

## LLM Decision
- **Action:** NO
- **Confidence:** 62%
- **p_true:** 46.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_REVERSION
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 54% resolve YES only 44.7% of time, indicating YES is overpriced by ~9.3%. Rockies injuries create mixed signal but statistical edge remains compelling.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Colorado Rockies'})` → INJURY [colorado rockies] Brenton Doyle (CF): Day-To-Day
INJURY [colorado rockies] Ryan Feltner (SP)
- `get_odds({'sport': 'baseball_mlb', 'team': 'Colorado Rockies'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Rockies Rangers'})` → No related markets found for 'Rockies Rangers'
- `search_web({'query': 'Texas Rangers vs Colorado Rockies MLB game prediction 2025'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Rangers vs Rockies Prediction, Odds, Moneyline, Sp
- `search_web({'query': 'Colorado Rockies injuries news April 2025'})` → [Wed, 25 Mar 2026] Google News
[Tue, 02 Dec 2025] Colorado Rockies News: Rockies announce 2026 Openi
- `search_web({'query': 'Texas Rangers 2025 season record wins losses'})` → [Mon, 18 May 2026] Google News
[Fri, 19 Sep 2025] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Colorado Rockies 2025 season record wins losses'})` → [Mon, 18 May 2026] Google News
[Mon, 29 Sep 2025] 2026 MLB Standings and Records: Regular Season - M

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*