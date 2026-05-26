# Market Analysis — 2026-05-17 19:15 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $201,716
- **Liquidity:** $300,391

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,229 (+0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,200 (-0.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: arizona diamondbacks colorado rockies
- [Bing News]
- [Sun, 17 May 2026] arizona diamondbacks colorado rockies
- → Today’s Lineups DIAMONDBACKS ROCKIES Ildemaro Vargas – 2B Edouard Julien – 2B Corbin Carroll – RF Mickey Moniak – LF Geraldo Perdomo – SS Hunter Goo
- [Sun, 17 May 2026] Arizona Diamondbacks gameday thread, #45: 5/17 @ Rockies
- → Here's how to watch Sunday's Colorado Rockies vs Arizona Diamondbacks game, including start times, TV channels, scores and how to stream.
- [Sat, 16 May 2026] Where to watch Arizona Diamondbacks vs Colorado Rockies: TV channel, start time, streaming for May 17
- → The Colorado Rockies notched a close win over the Arizona Diamondbacks in a bit of an odd game where the final score doesn’t quite reflect how many 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 60.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE_CONFLICT
- **Catalyst Strength:** 0.45

### Reasoning
Strong stat signal (n=13,967) suggests YES at 57% overprices outcome — historical resolution only 44.7%, implying ~12% edge on NO. However, bookmaker consensus (FanDuel 1.69, LowVig 1.71) implies ~59% Diamondbacks win probability, directly contradicting the stat signal. This creates a fundamental conflict: the statistical model says NO is underpriced, while bookmakers (with direct matchup knowledge including pitchers, lineups) favor the YES side. Past decisions on identical market also returned SKIP due to gap below 5% gate. Diamondbacks have multiple injuries (Pavin Smith, Carlos Santana, Jordan Lawlar all on IL), but this alone doesn't explain the bookmaker-stat divergence. Without concrete information explaining why bookmakers disagree with the stat signal (e.g., pitching matchup details, Rockies roster news), I cannot determine which signal is correct. The edge is real in one direction but the conflicting evidence reduces actionable confidence below threshold.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_odds({'sport': 'baseball_mlb', 'team': 'Diamondbacks'})` → [ODDS] baseball_mlb — 2 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]
- `search_web({'query': 'Arizona Diamondbacks recent performance news May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Zac Gallen against the Giants - MLB.com
[Sun, 17 M
- `search_web({'query': 'Colorado Rockies injuries performance news May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Colorado Rockies option Zach Agnos and recall Blas
- `get_market_context({'query': 'Diamondbacks Rockies'})` → [YES=50% vol=$6,566,682] Will Newcastle United FC win on 2026-05-17?
[YES=50% vol=$6,496,290] Will F
- `get_market_context({'query': 'MLB baseball win today'})` → [YES=50% vol=$6,566,682] Will Newcastle United FC win on 2026-05-17?
[YES=50% vol=$6,496,290] Will F
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies preview prediction today'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Arizona Diamondbacks vs. Colorado Rockies predicti

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*