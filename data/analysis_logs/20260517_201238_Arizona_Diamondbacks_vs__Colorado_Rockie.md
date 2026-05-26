# Market Analysis — 2026-05-17 20:12 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $212,934
- **Liquidity:** $74,793

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,313 (+0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,333 (+0.1% 24h) → neutral
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
- → Arizona's finale matchup begins in a delay.
- [Sun, 17 May 2026] Diamondbacks game vs Rockies delayed due to weather
- → The Arizona Diamondbacks and Colorado Rockies were to play their series finale in Denver on Sunday, May 17. The game was delayed by the weather.
- [Sun, 17 May 2026] Diamondbacks-Rockies updates. Perdomo's key 2025 moment, weather delay
- → “As we look outside the radio booth right now, tons of dark and not the most welcoming clouds,” Diamondbacks play-by-play voice Chris Garagiola said

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_ANOMALY
- **Catalyst Strength:** 0.70

### Reasoning
Historical data (n=13,967) shows markets at 56% YES price resolve YES only 44.7% of the time, suggesting systematic overpricing of YES by ~11%. While the 3% gap between market (56%) and base rate (59%) is below the 5% gate threshold, the large-sample statistical signal provides a reliable edge for NO bet. Both teams have notable injuries (Diamondbacks: two first basemen on IL; Rockies: starting pitcher on IL), but the key insight is the market inefficiency pattern. The stat signal outweighs the small gap in this case.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies 2025 upcoming series'})` → [Sun, 17 Aug 2025] Google News
[Thu, 14 Aug 2025] Arizona Diamondbacks at Colorado Rockies Game Stor
- `search_web({'query': 'Diamondbacks Rockies injury report August 2025'})` → [Sun, 17 Aug 2025] Google News
[Sun, 02 Nov 2025] Aided by recent callups, Doyle stays hot as Rox tu
- `get_market_context({'keyword': 'Diamondbacks vs Rockies'})` → No related markets found for 'Diamondbacks vs Rockies'
- `get_market_context({'keyword': 'Arizona Diamondbacks'})` → No related markets found for 'Arizona Diamondbacks'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Diamondbacks'})` → [ODDS] baseball_mlb — 2 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*