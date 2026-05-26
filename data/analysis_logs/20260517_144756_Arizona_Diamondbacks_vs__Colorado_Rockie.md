# Market Analysis — 2026-05-17 14:47 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 7
- **Volume 24h:** $64,695
- **Liquidity:** $391,806

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,005 (-0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,005 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Recent games:
- ARI @ COL | Final | Colorado Rockies(home) 18-28 score:4 vs Arizona Diamondbacks(away) 21-23 score:2
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: arizona diamondbacks colorado rockies
- [Bing News]
- [Sat, 16 May 2026] arizona diamondbacks colorado rockies
- → The Colorado Rockies notched a close win over the Arizona Diamondbacks in a bit of an odd game where the final score doesn’t quite reflect how many 
- [Sun, 17 May 2026] Rockies 4, Diamondbacks 2: Colorado bounces back in a game of small ball at Coors Field
- → Here's how to watch Sunday's Colorado Rockies vs Arizona Diamondbacks game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Arizona Diamondbacks vs Colorado Rockies: TV channel, start time, streaming for May 17
- → The Arizona Diamondbacks get seven home games. Three against the San Francisco Giants and four against the Colorado Rockies.

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 49.1%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** SYSTEMATIC_OVERPRICING
- **Catalyst Strength:** 0.82

### Reasoning
Strong statistical edge: markets at 58% historically resolve YES only 44.7% (n=13,967) — a 13.3pp gap. Bookmaker consensus (~59%) confirms no information asymmetry. The crowd is systematically overpricing YES at this level. Pattern signal (sports WR=85%, entry 50-60% WR=86%) supports fading overpriced YES. NO at 42% offers ~15% edge vs true probability of ~55%.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Arizona Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Colorado Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `get_odds({'sport': 'baseball_mlb', 'team': 'Diamondbacks'})` → [ODDS] baseball_mlb — 1 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies 2025 MLB prediction'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Diamondbacks vs Rockies Prediction, Odds, Moneylin
- `search_web({'query': 'Arizona Diamondbacks recent form 2025 MLB results'})` → [Fri, 15 May 2026] Google News
[Fri, 08 May 2026] 2026 MLB Standings and Records: Wild Card - MLB.co
- `get_market_context({'keyword': 'Arizona Diamondbacks MLB'})` → No related markets found for 'Arizona Diamondbacks MLB'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*