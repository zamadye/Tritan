# Market Analysis — 2026-05-17 15:32 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 7
- **Volume 24h:** $67,217
- **Liquidity:** $431,908

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,992 (-0.2% 24h) → neutral
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
- **p_true:** 61.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Strong statistical signal (n=13,967) shows markets at 58% resolve YES only 44.7% of time - systematic overpricing. No specific catalyst to override pattern. Bookmaker odds align with market price, confirming no information asymmetry.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Arizona Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Colorado Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `get_market_context({'keyword': 'Arizona Diamondbacks Colorado Rockies'})` → No related markets found for 'Arizona Diamondbacks Colorado Rockies'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Arizona Diamondbacks'})` → [ODDS] baseball_mlb — 1 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]
- `search_web({'query': 'Arizona Diamondbacks recent game results injuries news May 2026'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Rockies 4, Diamondbacks 2: Colorado bounces back i
- `search_web({'query': 'Colorado Rockies recent game results injuries news May 2026'})` → [Thu, 14 May 2026] Google News
[Sat, 16 May 2026] Colorado Rockies at Pittsburgh Pirates Game Story,
- `search_web({'query': '"Arizona Diamondbacks vs Colorado Rockies" May 17 2026 game preview starting pitchers'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Diamondbacks vs Rockies Prediction, Odds, Moneylin
- `search_web({'query': 'Diamondbacks Rockies May 2026 series schedule probable pitchers'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] MLB Gameday live updates: D-backs at Rockies game 
- `search_web({'query': 'Arizona Diamondbacks last 5 games results May 2026'})` → [Fri, 15 May 2026] Google News
[Thu, 14 May 2026] Diamondbacks 9-1 Rockies (May 15, 2026) Final Scor
- `search_web({'query': 'Colorado Rockies last 5 games results May 2026'})` → [Sat, 16 May 2026] Google News
[Thu, 14 May 2026] Rockies 4-2 Diamondbacks (May 16, 2026) Final Scor

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*