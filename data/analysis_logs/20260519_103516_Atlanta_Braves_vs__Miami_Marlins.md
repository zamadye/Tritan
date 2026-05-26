# Market Analysis — 2026-05-19 10:35 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 7
- **Volume 24h:** $71,287
- **Liquidity:** $131,526

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,808 (+0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,710 (-0.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- ATL @ MIA | Final | Miami Marlins(home) 22-26 score:12 vs Atlanta Braves(away) 32-16 score:0
- [SPORTS] Injuries:
- ?: James McCann — Out (Strain)
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Tue, 19 May 2026] atlanta braves miami marlins
- → Here's how to watch Tuesday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.
- [Tue, 19 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV channel, start time, streaming for May 19
- → Atlanta Braves (32-16, first in the NL East) vs. Miami Marlins (22-26, fourth in the NL East) Miami; Tuesday, 4:10 p.m. EDT PITCHING PROBABLES: Brav
- [Mon, 18 May 2026] Marlins try to keep home win streak going, host the Braves
- → According to Francys Romero of Beisbol FR, the Atlanta Braves are calling up a player to the MLB. They are in a series with the Marlins.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 63%
- **p_true:** 53.1%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.72

### Reasoning
Strong stat signal (n=13,967) shows markets at 58% YES resolve YES only 44.7% of time, indicating ~13pp overpricing. No specific catalyst favors Braves; both teams have comparable injuries. Entry range (50-60%) historically has only 33% WR. Base rate conflict and lack of game-specific edge reduce confidence below strong threshold.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins'})` → No related markets found for 'Atlanta Braves Miami Marlins'
- `search_web({'query': 'Atlanta Braves vs Miami Marlins May 2025 prediction preview'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Where to watch Atlanta Braves vs Miami Marlins: TV
- `search_web({'query': 'Atlanta Braves starting pitcher today May 2025'})` → [Wed, 24 Sep 2025] Google News
[Mon, 02 Feb 2026] Despite injury-laden 1st half, Braves feeling opti
- `search_web({'query': 'Braves Marlins May 18 2026 starting pitcher odds'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] How to watch Braves vs. Marlins: TV channel and st
- `get_market_context({'keyword': 'MLB baseball'})` → No related markets found for 'MLB baseball'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*