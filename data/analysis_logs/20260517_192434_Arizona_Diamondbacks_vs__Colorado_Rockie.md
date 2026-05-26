# Market Analysis — 2026-05-17 19:24 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 6
- **Volume 24h:** $203,174
- **Liquidity:** $70,136

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,215 (+0.0% 24h) → neutral
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
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 49.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.80

### Reasoning
Strong statistical signal (n=13,967) shows markets at 58% resolve YES only 44.7% of the time, creating 13.3% edge for NO bet. Market consistently overprices YES in this range. Bookmaker odds align with market but don't override the large-sample historical pattern.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Arizona Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Colorado Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `get_odds({'sport': 'baseball_mlb', 'team': 'Arizona Diamondbacks'})` → [ODDS] baseball_mlb — 2 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]
- `get_market_context({'keyword': 'Diamondbacks'})` → No related markets found for 'Diamondbacks'
- `get_market_context({'keyword': 'Rockies'})` → No related markets found for 'Rockies'
- `get_market_context({'keyword': 'MLB'})` → No related markets found for 'MLB'
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies May 2026 series preview'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks vs. Rockies (18 May, 2026) Live Score
- `search_web({'query': 'Arizona Diamondbacks recent form results May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Where to watch Arizona Diamondbacks vs Colorado Ro
- `search_web({'query': 'Colorado Rockies recent form results May 2026'})` → [Sun, 17 May 2026] Google News
[Fri, 26 Sep 2025] Where to watch Arizona Diamondbacks vs Colorado Ro

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*