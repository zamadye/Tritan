# Market Analysis — 2026-05-17 19:03 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $128,940
- **Liquidity:** $384,829

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,197 (-0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,103 (-0.1% 24h) → neutral
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
- **Confidence:** 58%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.15

### Reasoning
Market at 57% vs bookmaker consensus 58.8% shows no clear edge. While historical stat signal suggests overpricing (44.7% true rate at 57%), professional sportsbook odds actually favor Diamondbacks at higher probability. Injury data slightly favors D-backs (Rockies missing SP+RP). Gap (3%) fails 5% gate threshold. No concrete catalyst to justify position.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Arizona Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Colorado Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `get_market_context({'keyword': 'Arizona Diamondbacks Colorado Rockies'})` → No related markets found for 'Arizona Diamondbacks Colorado Rockies'
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies June 2025 series preview'})` → [Sat, 16 May 2026] Google News
[Sun, 22 Jun 2025] Diamondbacks vs Rockies Prediction, Odds, Moneylin
- `search_web({'query': 'Colorado Rockies starting pitcher rotation June 2025'})` → [Tue, 10 Feb 2026] Google News
[Fri, 06 Mar 2026] Colorado Rockies Pitcher Report: A starting rotati
- `get_odds({'sport': 'baseball_mlb', 'team': 'Arizona Diamondbacks'})` → [ODDS] baseball_mlb — 1 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*