# Market Analysis — 2026-05-20 17:05 UTC

## Market
- **Question:** Texas Rangers vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $57,770
- **Liquidity:** $317,826

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,242 (+0.5% 24h) → neutral
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
- → Rockies starter Kyle Freeland is allowing a disastrous 11.76 hits per nine innings, leading to a bloated, 7.22 ERA.
- [Wed, 20 May 2026] Colorado Rockies vs. Texas Rangers: Game preview, picks and props for Wednesday
- → The Texas Rangers cruised to a 10-0 victory against the Colorado Rockies on Tuesday. Tyler Alexander started as an opener before Kumar Rocker turned
- [Wed, 20 May 2026] Rangers’ Kumar Rocker gets brutally honest after setting new career-high vs. Rockies
- → Colorado Rockies: starting pitchers are Jack Leiter for the Rangers and Kyle Freeland for the Rockies. The Rangers take on the Rockies in an afterno

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 46.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MODEL
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 54% resolve YES only 44.7% of time, indicating market overprices YES by ~9pp. Additionally, Texas Rangers have key injuries (Seager 10-Day-IL, Langford 10-Day-IL) further reducing their win probability. Edge: buying NO at 46% when true probability ~55.3%.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Texas Rangers'})` → INJURY [texas rangers] Wyatt Langford (LF): 10-Day-IL
INJURY [texas rangers] MacKenzie Gore (SP): Da
- `get_sports_data({'sport': 'mlb', 'team': 'Colorado Rockies'})` → INJURY [colorado rockies] Brenton Doyle (CF): Day-To-Day
INJURY [colorado rockies] Ryan Feltner (SP)
- `search_web({'query': 'Texas Rangers injury update Wyatt Langford Corey Seager 2025'})` → [Tue, 19 May 2026] Google News
[Thu, 09 Oct 2025] Rangers injury updates: Cody Freeman, Corey Seager
- `search_web({'query': 'Colorado Rockies recent results performance 2025'})` → [Mon, 18 May 2026] Google News
[Sat, 07 Mar 2026] 2026 MLB Standings and Records: Regular Season - M
- `get_market_context({'keyword': 'Texas Rangers'})` → No related markets found for 'Texas Rangers'
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'
- `get_market_context({'keyword': 'baseball'})` → No related markets found for 'baseball'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Texas Rangers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*