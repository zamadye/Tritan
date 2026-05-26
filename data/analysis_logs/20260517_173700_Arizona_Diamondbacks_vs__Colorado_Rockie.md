# Market Analysis — 2026-05-17 17:37 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $112,069
- **Liquidity:** $354,372

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,915 (-0.4% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,936 (-0.4% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)
- ?: Max Muncy — 10-Day-IL (Fracture)

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
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.55

### Reasoning
Stat signal (n=13,967) suggests markets at 57% YES resolve YES only 44.7% historically — a ~12% systemic overpricing of YES. However: (1) Bookmaker consensus (FanDuel 58.8%, LowVig 58.1%) aligns with Polymarket 57%, so NO information gap between sources; (2) Gap from base rate is only 3%, below 5% gate threshold — consistent with two prior SKIP decisions on this exact market; (3) No fresh catalyst or team-specific edge beyond general injury reports (all reserves/bench for AZ, routine IL for COL); (4) Single-game MLB has high variance. The historical stat pattern is interesting but too general to bet with high confidence on this specific matchup without a confirming catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `get_odds({'sport': 'baseball_mlb', 'team': 'Diamondbacks'})` → [ODDS] baseball_mlb — 1 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies May 2025 series preview pitching matchup'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Diamondbacks vs Rockies Prediction, Odds, Moneylin
- `get_market_context({'keyword': 'Diamondbacks Rockies'})` → No related markets found for 'Diamondbacks Rockies'
- `search_web({'query': 'Arizona Diamondbacks recent results May 2025 standings'})` → [Thu, 14 May 2026] Google News
[Thu, 14 May 2026] 2026 D-backs Standings and Record: Wild Card | Ari
- `search_web({'query': 'Colorado Rockies recent results May 2025 record'})` → [Fri, 15 May 2026] Google News
[Sun, 14 Sep 2025] 2026 MLB Standings and Records: Regular Season - M
- `get_market_context({'keyword': 'MLB baseball'})` → No related markets found for 'MLB baseball'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*