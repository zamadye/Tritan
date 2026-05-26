# Market Analysis — 2026-05-17 17:24 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $111,677
- **Liquidity:** $347,698

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,924 (-0.4% 24h) → neutral
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
- **Confidence:** 65%
- **p_true:** 50.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.75

### Reasoning
Strong historical stat signal (n=13,967) shows markets at 57% YES resolve YES only 44.7% of time — market systematically overprices YES by ~12.3%. Bookmaker consensus (58.5%) closely matches Polymarket (57%), but historical data indicates this price point is overpriced. NO at 43% has positive expected value vs 44.7% true probability. Past similar decisions were SKIP due to insufficient gap, but current gap is meaningful. Sport-specific injuries (AZ: 3 players on IL, COL: SP on IL) don't clearly favor Arizona enough to override stat signal.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Arizona Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_sports_data({'sport': 'mlb', 'team': 'Colorado Rockies'})` → INJURY [colorado rockies] Tyler Freeman (RF): paternity
INJURY [colorado rockies] Chase Dollander (S
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies 2025 series'})` → [Fri, 15 May 2026] Google News
[Sun, 17 Aug 2025] Diamondbacks vs. Rockies: Prediction, Lineups, Str
- `search_web({'query': 'Rockies Diamondbacks odds June 2026'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Diamondbacks vs Rockies Prediction, Odds &amp; Pla
- `get_market_context({'keyword': 'Arizona Diamondbacks'})` → No related markets found for 'Arizona Diamondbacks'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Arizona Diamondbacks'})` → [ODDS] baseball_mlb — 1 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]
- `search_web({'query': 'Polymarket Arizona Diamondbacks Colorado Rockies 57%'})` → No search results for: Polymarket Arizona Diamondbacks Colorado Rockies 57%

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*