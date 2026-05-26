# Market Analysis — 2026-05-17 16:50 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $109,391
- **Liquidity:** $390,930

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,124 (-0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,079 (-0.1% 24h) → neutral

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
- **Confidence:** 48%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Bookmaker consensus (~57.5%) confirms Polymarket price (57%), eliminating information edge. Despite compelling stat signal (44.7% resolution at 57%, n=13,967), conflicting signals between base rate (+3% YES edge) and stat signal (~12% NO edge) create ambiguity. Gap (3%) fails 5% gate threshold. Two prior decisions on this exact market correctly failed gate. No injury/news catalyst to break efficiency. SKIP pending clearer edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Arizona Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `get_odds({'sport': 'baseball_mlb', 'team': 'Arizona Diamondbacks'})` → [ODDS] baseball_mlb — 1 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]
- `get_market_context({'keyword': 'Arizona Diamondbacks Colorado Rockies'})` → No related markets found for 'Arizona Diamondbacks Colorado Rockies'
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies 2026 May preview'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] Colorado Rockies vs. Arizona Diamondbacks: Game pr
- `search_web({'query': 'Arizona Diamondbacks starting pitcher May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Colorado Rockies news: Tomoyuki Sugano notches his
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $78,071.00 | 24h: -0.13%

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*