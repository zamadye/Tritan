# Market Analysis — 2026-05-19 09:15 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $68,647
- **Liquidity:** $91,776

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,988 (+0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,972 (+0.1% 24h) → neutral

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
- [Tue, 19 May 2026] Atlanta Braves Make Roster Move After Marlins Game
- → Ronald Acuna Jr. will return to the Atlanta starting lineup on Tuesday when the visiting Braves play the Miami Marlins in the second game of a four-

## LLM Decision
- **Action:** SKIP
- **Confidence:** 50%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Stat signal suggests YES is overpriced at 57% (historical resolution only 44.7%), but gate condition fails: gap between base rate (60%) and market price (57%) is only 3%, below required 5% threshold. No concrete catalyst or new information to justify a bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `get_odds({'sport': 'baseball_mlb', 'team': 'Atlanta Braves vs Miami Marlins'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 recent results and injuries'})` → [Tue, 05 May 2026] Google News
[Wed, 15 Apr 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Braves Marlins series May 2026 pitching matchup'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher
- `get_market_context({'keyword': 'Atlanta Braves vs Miami Marlins'})` → No related markets found for 'Atlanta Braves vs Miami Marlins'
- `search_web({'query': 'Max Meyer JR Ritchie stats 2026 MLB'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Atlanta Braves at Miami Marlins Game Story, Scores
- `search_web({'query': 'Atlanta Braves 2026 season record standings May'})` → [Mon, 18 May 2026] Google News
[Tue, 05 May 2026] How to watch Braves vs. Marlins: TV channel and st

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*