# Market Analysis — 2026-05-20 19:18 UTC

## Market
- **Question:** Texas Rangers vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $76,920
- **Liquidity:** $24,612

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,314 (+0.5% 24h) → neutral
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
- → Here's how to watch Wednesday's Colorado Rockies vs Texas Rangers game, including start times, TV channels, scores and how to stream.
- [Wed, 20 May 2026] Where to watch Texas Rangers vs Colorado Rockies: TV channel, start time, streaming for May 20
- → The Colorado Rockies will be facing the Texas Rangers on Wendesday afternoon. They will be without one of their outfielders in the game.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 48.7%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.72

### Reasoning
Strong statistical signal (n=13,967) shows markets at 55% YES historically resolve YES only 44.7% of the time — a 10.3% overpricing edge. Rangers are missing key bats (Corey Seager and Wyatt Langford both on IL), which weakens their offensive lineup. While base rate gap is only +2% (below 5% threshold), the high-confidence stat signal from large sample size indicates systematic crowd overpricing of YES in this price range. Sports category shows 83% WR overall but 50-60% entry range only 33% WR, confirming difficulty in this zone. The stat edge provides concrete actionable signal.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Texas Rangers'})` → INJURY [texas rangers] MacKenzie Gore (SP): Day-To-Day
INJURY [texas rangers] Wyatt Langford (LF): 1
- `get_sports_data({'sport': 'mlb', 'team': 'Colorado Rockies'})` → INJURY [colorado rockies] Victor Vodnik (RP): 15-Day-IL
INJURY [colorado rockies] Brenton Doyle (CF)
- `search_web({'query': 'Texas Rangers Colorado Rockies 2025 matchup preview'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Colorado Rockies vs. Texas Rangers: Game preview, 
- `search_web({'query': 'Texas Rangers Corey Seager injury update 2025'})` → [Tue, 19 May 2026] Google News
[Wed, 17 Sep 2025] Rangers injury updates: Cody Freeman, Corey Seager
- `get_market_context({'keyword': 'Texas Rangers'})` → No related markets found for 'Texas Rangers'
- `get_market_context({'keyword': 'Rangers Rockies'})` → No related markets found for 'Rangers Rockies'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Rangers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*