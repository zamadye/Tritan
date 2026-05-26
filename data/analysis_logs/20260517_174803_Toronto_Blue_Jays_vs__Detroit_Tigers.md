# Market Analysis — 2026-05-17 17:48 UTC

## Market
- **Question:** Toronto Blue Jays vs. Detroit Tigers
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 6
- **Volume 24h:** $144,443
- **Liquidity:** $27,921

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,005 (-0.3% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,926 (-0.4% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [SPORTS] Recent games:
- TOR @ DET | Scheduled | Detroit Tigers(home) 20-26 score:0 vs Toronto Blue Jays(away) 20-25 score:0
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: toronto blue jays detroit tigers
- [Bing News]
- [Sun, 17 May 2026] toronto blue jays detroit tigers
- → Here's how to watch Sunday's Detroit Tigers vs Toronto Blue Jays game, including start times, TV channels, scores and how to stream.
- [Sat, 16 May 2026] Where to watch Toronto Blue Jays vs Detroit Tigers: TV channel, start time, streaming for May 17
- → Daulton Varsho drove in the go-ahead run with a single in the 10th inning and Yohendrick Pinango homered Saturday to lead the Toronto Blue Jays to a
- [Sun, 17 May 2026] Detroit Tigers lose to Toronto Blue Jays 2-1 in extra-inning battle
- → The Toronto Blue Jays are shaking things up as they go for a series win on Sunday against the Detroit Tigers (1:40 p.m. ET / 10:40 a.m. PT on Sports

## LLM Decision
- **Action:** SKIP
- **Confidence:** 48%
- **p_true:** 54.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.50

### Reasoning
Historical stat pattern (n=13,967) suggests market overprices YES at 53% (true prob ~44.7%), but conflicting bookmaker odds (FanDuel: Blue Jays 65% vs BetOnline: 53%) and past decision precedent (gap=1%<5%) reduce confidence. Injury data shows both teams missing key players (Skubal for Tigers, Berrios for Blue Jays) but no recent news or direct catalysts identified for this specific game. Edge exists but too uncertain for confident bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Blue Jays'})` → INJURY [toronto blue jays] Tommy Nance (RP): 15-Day-IL
INJURY [toronto blue jays] Jose Berrios (SP):
- `get_sports_data({'sport': 'mlb', 'team': 'Tigers'})` → INJURY [detroit tigers] Ty Madden (SP): 15-Day-IL
INJURY [detroit tigers] Gleyber Torres (2B): 10-Da
- `search_web({'query': 'Toronto Blue Jays vs Detroit Tigers series schedule June 2025'})` → [Wed, 29 Apr 2026] Google News
[Sun, 27 Jul 2025] Cleveland Guardians TV schedule 2026: How to watch
- `search_web({'query': 'Blue Jays Tigers upcoming series pitching matchups'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] How to Watch Tigers Series Opener vs Blue Jays: Li
- `get_market_context({'keyword': 'Blue Jays'})` → No related markets found for 'Blue Jays'
- `get_market_context({'keyword': 'Tigers'})` → No related markets found for 'Tigers'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Blue Jays'})` → [ODDS] baseball_mlb — 1 events
  Detroit Tigers vs Toronto Blue Jays (2026-05-17)
    [FanDuel] Detr

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*