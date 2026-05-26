# Market Analysis — 2026-05-17 20:23 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $217,966
- **Liquidity:** $118,904

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,258 (-0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,239 (-0.0% 24h) → neutral
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
- → The Arizona Diamondbacks and Colorado Rockies were to play their series finale in Denver on Sunday, May 17. The game was delayed by the weather.
- [Sun, 17 May 2026] Diamondbacks-Rockies updates. Perdomo's key 2025 moment, weather delay
- → “As we look outside the radio booth right now, tons of dark and not the most welcoming clouds,” Diamondbacks play-by-play voice Chris Garagiola said
- [Sun, 17 May 2026] Start of Diamondbacks-Rockies rubber match delayed due to weather
- → The Colorado Rockies and Arizona Diamondbacks are in a rain delay as inclement weather moves through Denver on Sunday, May 17. Here's what you need 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_SIGNAL
- **Catalyst Strength:** 0.60

### Reasoning
Statistical signal (n=13,967) suggests markets at 57% resolve YES only 44.7% of time, indicating overpricing. However, gap is only 3% (below 5% threshold), bookmaker consensus (59%) is actually higher than market price (57%), and past decisions have been to SKIP when gap <5%. No concrete edge or catalyst found to justify a bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Arizona Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Colorado Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `get_odds({'sport': 'baseball_mlb', 'team': 'Arizona Diamondbacks'})` → [ODDS] baseball_mlb — 2 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]
- `get_market_context({'keyword': 'Arizona Diamondbacks Colorado Rockies'})` → No related markets found for 'Arizona Diamondbacks Colorado Rockies'
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies May 2026 preview'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks vs. Rockies (18 May, 2026) Live Score
- `search_web({'query': 'Arizona Diamondbacks recent form starting pitcher 2026'})` → [Sat, 16 May 2026] Google News
[Wed, 12 Nov 2025] How Rare Was Merrill Kelly's Complete Game, Really

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*