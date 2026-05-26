# Market Analysis — 2026-05-17 18:52 UTC

## Market
- **Question:** Arizona Diamondbacks vs. Colorado Rockies
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $126,059
- **Liquidity:** $387,476

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,084 (-0.2% 24h) → neutral
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
- **Confidence:** 64%
- **p_true:** 60.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.80

### Reasoning
Strong stat signal (n=13,967) shows market overprices YES at 57% (true resolution ~44.7%), but gate fails: gap 3% < 5% required threshold. Conflicting bookmaker odds (~59% for Diamondbacks) suggest missing information. Previous similar decisions were SKIP.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Arizona Diamondbacks'})` → INJURY [arizona diamondbacks] Pavin Smith (1B): 60-Day-IL
INJURY [arizona diamondbacks] Carlos Santa
- `search_web({'query': 'Arizona Diamondbacks vs Colorado Rockies 2025'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Diamondbacks vs Rockies Prediction, Odds, Moneylin
- `search_web({'query': 'Diamondbacks Rockies recent form MLB 2025'})` → [Tue, 05 May 2026] Google News
[Sat, 16 Aug 2025] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Rockies 2025 season record'})` → [Fri, 15 May 2026] Google News
[Mon, 29 Sep 2025] 2026 MLB Standings and Records: Regular Season - M
- `search_web({'query': 'Diamondbacks 2025 season record'})` → [Sun, 28 Sep 2025] Google News
[Sun, 28 Sep 2025] The 2025 Diamondbacks season: a knee-jerk reaction
- `get_market_context({'keyword': 'Arizona Diamondbacks'})` → No related markets found for 'Arizona Diamondbacks'
- `get_market_context({'keyword': 'Rockies'})` → No related markets found for 'Rockies'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Diamondbacks'})` → [ODDS] baseball_mlb — 1 events
  Colorado Rockies vs Arizona Diamondbacks (2026-05-17)
    [FanDuel]
- `search_web({'query': 'Arizona Diamondbacks 2026 season record'})` → [Thu, 14 May 2026] Google News
[Wed, 25 Mar 2026] 2026 D-backs Standings and Record: Wild Card | Ari
- `search_web({'query': 'Colorado Rockies 2026 season record'})` → [Fri, 15 May 2026] Google News
[Sat, 28 Mar 2026] 2026 MLB Standings and Records: Regular Season - M

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*