# Market Analysis — 2026-05-19 08:31 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $68,330
- **Liquidity:** $143,118

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,956 (-0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,000 (+0.1% 24h) → neutral

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
- → Atlanta Braves (32-16, first in the NL East) vs. Miami Marlins (22-26, fourth in the NL East) Miami; Tuesday, 4:10 p.m. EDT PITCHING PROBABLES: Brav
- [Mon, 18 May 2026] Marlins try to keep home win streak going, host the Braves
- → According to Francys Romero of Beisbol FR, the Atlanta Braves are calling up a player to the MLB. They are in a series with the Marlins.
- [Mon, 18 May 2026] Atlanta Braves Make Roster Move After Marlins Game
- → Here's how to watch Monday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Strong historical mispricing signal exists (57% markets resolve YES only 44.7% of time, n=13,967), but multiple risk factors prevent betting: (1) Gap below 5% gate threshold at 3%, (2) Entry range 50-60% shows poor WR of 33% from 6 trades, (3) No direct catalyst or breaking news for this specific matchup, (4) Past decisions on identical market were SKIP, (5) No odds data available for cross-verification. The market overprices YES but the edge isn't reliably exploitable given entry range performance and lack of catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_sports_data({'sport': 'mlb', 'team': 'Miami Marlins'})` → INJURY [miami marlins] Kemp Alderman (RF): Day-To-Day
INJURY [miami marlins] Robby Snelling (SP): 15
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins today 2025 game preview'})` → [Tue, 26 Aug 2025] Google News
[Wed, 15 Apr 2026] Atlanta Braves at Miami Marlins Preview - 08/27/20
- `search_web({'query': 'Atlanta Braves recent results August 2025 performance'})` → [Tue, 19 Aug 2025] Google News
[Mon, 04 Aug 2025] Braves score seven late runs in wild comeback - ML
- `get_market_context({'keyword': 'Atlanta Braves Miami Marlins MLB'})` → No related markets found for 'Atlanta Braves Miami Marlins MLB'
- `get_market_context({'keyword': 'Braves Marlins MLB winner'})` → No related markets found for 'Braves Marlins MLB winner'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*