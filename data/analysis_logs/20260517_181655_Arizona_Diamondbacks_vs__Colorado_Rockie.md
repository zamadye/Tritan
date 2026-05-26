# Market Analysis — 2026-05-17 18:16 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $111,059
- **Liquidity:** $395,580

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,106 (-0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,040 (-0.2% 24h) → neutral
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
- → Here's how to watch Sunday's Colorado Rockies vs Arizona Diamondbacks game, including start times, TV channels, scores and how to stream.
- [Sat, 16 May 2026] Where to watch Arizona Diamondbacks vs Colorado Rockies: TV channel, start time, streaming for May 17
- → The Colorado Rockies notched a close win over the Arizona Diamondbacks in a bit of an odd game where the final score doesn’t quite reflect how many 
- [Sun, 17 May 2026] Rockies 4, Diamondbacks 2: Colorado bounces back in a game of small ball at Coors Field
- → Arizona Diamondbacks (21-23, third in the NL West) vs. Colorado Rockies (18-28, fifth in the NL West) Denver; Sunday, 3:10 p.m. EDT PITCHING PROBABL

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.40

### Reasoning
Conflicting signals prevent actionable bet. Strong stat signal (n=13,967) suggests market overprices YES (historical resolution 44.7% vs 57% market price, implying 12.3% edge for NO). However, base rate (n=6077) suggests 60% resolution favoring YES, and bookmaker odds align with market at ~57% vig-free. Gate check fails (gap 3% < 5% threshold). Both teams have comparable injuries. No breaking news or specific catalyst to resolve signal conflict.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies June 2025 prediction'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks vs Rockies Prediction, Odds, Moneylin
- `search_web({'query': 'MLB Diamondbacks Rockies recent performance June 2025'})` → [Fri, 15 May 2026] Google News
[Sun, 17 Aug 2025] 2026 MLB Standings and Records: Regular Season - M
- `get_market_context({'keyword': 'Arizona Diamondbacks'})` → No related markets found for 'Arizona Diamondbacks'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Arizona Diamondbacks'})` → [ODDS] baseball_mlb — 1 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]
- `search_web({'query': 'Diamondbacks vs Rockies May 17 2026 starting pitchers odds'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks vs Rockies Prediction, Odds &amp; Pla
- `get_market_context({'keyword': 'Rockies Diamondbacks MLB'})` → No related markets found for 'Rockies Diamondbacks MLB'
- `search_web({'query': 'Arizona Diamondbacks Colorado Rockies head to head 2026 season results'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks wrap road trip, head home for Giants,
- `search_web({'query': '"Diamondbacks" "Rockies" May 2026 injury update roster'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Diamondbacks wrap road trip, head home for Giants,

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*