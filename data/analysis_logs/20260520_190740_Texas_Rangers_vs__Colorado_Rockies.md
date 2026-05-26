# Market Analysis — 2026-05-20 19:07 UTC

## Market
- **Question:** Texas Rangers vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $69,652
- **Liquidity:** $266,129

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,290 (+0.6% 24h) → neutral
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
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 47.2%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.72

### Reasoning
Strong statistical signal (n=13,967) shows 54% YES markets resolve YES only 44.7% of time — 9.3% edge on NO. Rangers injuries (Seager, Langford IL) further support underperformance. Market overprices YES by significant margin. However, Entry 50-60% zone has poor historical WR (33%), introducing risk.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Rangers'})` → INJURY [texas rangers] MacKenzie Gore (SP): Day-To-Day
INJURY [texas rangers] Wyatt Langford (LF): 1
- `get_odds({'sport': 'baseball_mlb', 'team': 'Rangers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Texas Rangers Colorado Rockies MLB'})` → No related markets found for 'Texas Rangers Colorado Rockies MLB'
- `search_web({'query': 'Texas Rangers vs Colorado Rockies 2025 MLB game prediction'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Texas Rangers at Colorado Rockies prediction, pick
- `search_web({'query': 'Texas Rangers recent form MLB 2025 results'})` → [Tue, 19 May 2026] Google News
[Thu, 26 Mar 2026] 2026 MLB Season: Schedule Information, Latest Rule

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*