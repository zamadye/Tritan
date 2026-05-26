# Market Analysis — 2026-05-20 17:58 UTC

## Market
- **Question:** Texas Rangers vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $59,123
- **Liquidity:** $224,764

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,479 (+0.9% 24h) → neutral
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
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 44.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_ARBITRAGE
- **Catalyst Strength:** 0.80

### Reasoning
Strong statistical signal (n=13,967) shows markets priced at 54% resolve YES only 44.7% of the time, indicating a 9.3% edge for NO. While the market-to-baserate gap is only +2%, the historical resolution data reveals systematic overpricing of YES at this price point. Both teams have significant injuries (Seager, Langford for TEX; Feltner, Beck for COL). Past decisions on this same market gated out, but the stat edge here is concrete and large-sample. Entry zone (50-60%) historically has poor WR (33%), further supporting the contrarian NO position.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Texas Rangers'})` → INJURY [texas rangers] Wyatt Langford (LF): 10-Day-IL
INJURY [texas rangers] MacKenzie Gore (SP): Da
- `get_sports_data({'sport': 'mlb', 'team': 'Colorado Rockies'})` → INJURY [colorado rockies] Brenton Doyle (CF): Day-To-Day
INJURY [colorado rockies] Ryan Feltner (SP)
- `get_odds({'sport': 'baseball_mlb', 'team': 'Rangers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Texas Rangers vs Colorado Rockies game prediction odds April 2025'})` → [Sun, 26 Apr 2026] Google News
[Sat, 04 Apr 2026] Sunday’s MLB Odds, Betting Lines and Predictions -
- `search_web({'query': 'Texas Rangers Colorado Rockies 2025 season results standings'})` → [Mon, 18 May 2026] Google News
[Tue, 24 Mar 2026] 2026 MLB Standings and Records: Regular Season - M
- `get_market_context({'keyword': 'Rockies Rangers'})` → No related markets found for 'Rockies Rangers'
- `search_web({'query': 'Texas Rangers 2025 season record results April'})` → [Mon, 18 May 2026] Google News
[Tue, 05 May 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Colorado Rockies 2025 season record results April'})` → [Mon, 18 May 2026] Google News
[Sun, 29 Mar 2026] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'MLB standings April 25 2026 AL West NL West'})` → [Mon, 18 May 2026] Google News
[Thu, 23 Apr 2026] 2026 MLB Standings and Records: Regular Season - M
- `get_market_context({'keyword': 'MLB baseball'})` → No related markets found for 'MLB baseball'
- `search_web({'query': '"Texas Rangers" "Colorado Rockies" 2025 MLB game'})` → [Tue, 05 May 2026] Google News
[Tue, 02 Sep 2025] 2026 Spring Training - MLB.com
[Tue, 04 Nov 2025] 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*