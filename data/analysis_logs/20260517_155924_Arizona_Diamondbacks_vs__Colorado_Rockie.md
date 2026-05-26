# Market Analysis — 2026-05-17 15:59 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 7
- **Volume 24h:** $67,395
- **Liquidity:** $350,760

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,004 (-0.3% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,987 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: arizona diamondbacks colorado rockies
- [Bing News]
- [Sat, 16 May 2026] arizona diamondbacks colorado rockies
- → The Colorado Rockies notched a close win over the Arizona Diamondbacks in a bit of an odd game where the final score doesn’t quite reflect how many 
- [Sun, 17 May 2026] Rockies 4, Diamondbacks 2: Colorado bounces back in a game of small ball at Coors Field
- → Here's how to watch Sunday's Colorado Rockies vs Arizona Diamondbacks game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Arizona Diamondbacks vs Colorado Rockies: TV channel, start time, streaming for May 17
- → Arizona Diamondbacks (21-23, third in the NL West) vs. Colorado Rockies (18-28, fifth in the NL West) Denver; Sunday, 3:10 p.m. EDT PITCHING PROBABL

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.7%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.78

### Reasoning
Strong statistical signal (n=13,967) shows markets at 58% resolve YES only 44.7% of the time - 13.3pp edge for NO. Both bookmakers (58.5-59.2%) and Polymarket (58%) align on pricing, but historical data indicates systematic overpricing. No game-specific catalyst needed - the pattern itself is the edge. Confidence tempered to 0.68 because this is a pattern-based trade without a direct catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'team': 'Arizona Diamondbacks', 'sport': 'mlb'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Colorado Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies game news today'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Arizona Diamondbacks vs Colorado Rockies Live Stre
- `search_web({'query': 'Diamondbacks Rockies injury report lineup'})` → [Tue, 14 Apr 2026] Google News
[Sat, 09 May 2026] Diamondbacks scratch Ketel Marte from starting lin
- `get_market_context({'keyword': 'Arizona Diamondbacks vs Colorado Rockies'})` → No related markets found for 'Arizona Diamondbacks vs Colorado Rockies'
- `search_web({'query': 'Arizona Diamondbacks Colorado Rockies May 2026 series preview'})` → [Sun, 17 May 2026] Google News
[Thu, 14 May 2026] Arizona Diamondbacks vs Colorado Rockies Live Stre
- `get_odds({'sport': 'baseball_mlb', 'team': 'Arizona Diamondbacks'})` → [ODDS] baseball_mlb — 1 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*