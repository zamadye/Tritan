# Market Analysis — 2026-05-17 17:40 UTC

## Market
- **Question:** Toronto Blue Jays vs. Detroit Tigers
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 7
- **Volume 24h:** $102,470
- **Liquidity:** $444,988

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,915 (-0.4% 24h) → neutral
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
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 44.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical edge: Markets priced at 53% YES historically resolve YES only 44.7% of the time (n=13,967). This creates an ~8.3% overpricing of YES. Bookmaker odds (Blue Jays 1.85-1.89, implying 53-54%) align with the Polymarket price, confirming market efficiency at this price point—but the historical resolution data reveals systematic overpricing. Both teams have significant injuries (Tigers missing ace Skubal; Blue Jays missing Berrios), but these are already priced in. Sports pattern shows 85% WR from 13 trades (STRONG) and 86% WR at 50-60% entry range. The information gap exists because the crowd hasn't fully incorporated the historical overpricing at this specific price level.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Blue Jays'})` → INJURY [toronto blue jays] Tommy Nance (RP): 15-Day-IL
INJURY [toronto blue jays] Jose Berrios (SP):
- `get_sports_data({'sport': 'mlb', 'team': 'Tigers'})` → INJURY [detroit tigers] Ty Madden (SP): 15-Day-IL
INJURY [detroit tigers] Gleyber Torres (2B): 10-Da
- `get_odds({'sport': 'baseball_mlb', 'team': 'Blue Jays'})` → [ODDS] baseball_mlb — 1 events
  Detroit Tigers vs Toronto Blue Jays (2026-05-17)
    [FanDuel] Detr
- `search_web({'query': 'Toronto Blue Jays vs Detroit Tigers upcoming game preview odds'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Blue Jays vs Tigers Prediction, Odds &amp; Home Ru
- `search_web({'query': 'Blue Jays Tigers starting pitcher rotation news'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Fantasy baseball: Gasser, Rodriguez called up for 
- `search_web({'query': '"Blue Jays" "Tigers" May 17 2026 starting pitcher matchup'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Blue Jays vs Tigers match player stats | 2026 Seri
- `get_market_context({'keyword': 'Blue Jays Tigers'})` → No related markets found for 'Blue Jays Tigers'
- `search_web({'query': 'Blue Jays vs Tigers May 17 2026 starting pitcher Yariel Rodriguez'})` → [Sun, 17 May 2026] Google News
[Tue, 12 May 2026] Blue Jays vs Tigers Game Overview, Stats, Injuries
- `search_web({'query': 'Detroit Tigers May 17 2026 starter Kenta Maeda Matt Manning'})` → [Thu, 12 Mar 2026] Google News
[Wed, 29 May 2024] The Tigers made their sixth round of roster cuts i
- `search_web({'query': '"Blue Jays" "Tigers" May 17 2026 odds moneyline prediction'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Blue Jays vs Tigers Prediction, Odds, Moneyline, S
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'
- `get_market_context({'keyword': 'baseball'})` → No related markets found for 'baseball'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*