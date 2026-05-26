# Market Analysis — 2026-05-17 23:11 UTC

## Market
- **Question:** San Diego Padres vs. Seattle Mariners
- **Category:** sports
- **YES Price:** 42.0%
- **Days Left:** 7
- **Volume 24h:** $1,175,796
- **Liquidity:** $364,575

## Statistical Prior
- **p_base:** 38.1%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,863 (-0.4% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,984 (-0.3% 24h) → neutral
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
- [MULTI-SOURCE NEWS] 2 sources for: diego padres seattle mariners
- [Bing News]
- [Sun, 17 May 2026] diego padres seattle mariners
- → SportsLine's model simulated San Diego Padres vs. Seattle Mariners 10,000 times and revealed its MLB predictions and Sunday Night Baseball picks ...
- [Sun, 17 May 2026] Padres vs. Mariners prediction, odds, time: 2026 MLB picks for Sunday Night Baseball from advanced model
- → SportsLine expert Angelo &quot;Amags&quot; Magliocca has dug up some value bets for a same-game parlay for Padres vs. Mariners on the May 17 edition
- [Sun, 17 May 2026] Padres vs. Mariners same-game parlay from proven MLB expert for Sunday Night Baseball on May 17
- → Sunday Night Baseball features an interesting matchup between two playoff hopefuls, as the Seattle Mariners host the San Diego Padres.&#160; San Die

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 38.1%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Market price (42%) aligns with bookmaker consensus (~41-43%) and base rate (38%). Gap of 4% is below 5% threshold for statistical edge. While Padres have significant pitching disadvantage (3 SPs on IL including Yu Darvish), this information appears already priced in. No new catalyst or information gap identified.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'San Diego Padres'})` → INJURY [san diego padres] Matt Waldron (SP): 15-Day-IL
INJURY [san diego padres] German Marquez (SP)
- `get_sports_data({'sport': 'mlb', 'team': 'Seattle Mariners'})` → INJURY [seattle mariners] Brendan Donovan (3B): 10-Day-IL
INJURY [seattle mariners] Cal Raleigh (C):
- `get_odds({'sport': 'baseball_mlb', 'team': 'Padres'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'San Diego Padres vs Seattle Mariners upcoming series 2025 preview'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Seattle Mariners vs. San Diego Padres prediction, 
- `search_web({'query': 'Padres Mariners starting pitchers rotation June 2025'})` → [Mon, 23 Mar 2026] Google News
[Fri, 27 Mar 2026] Here are the 2026 Opening Day starting pitchers - 
- `get_market_context({'keyword': 'Padres Mariners MLB'})` → No related markets found for 'Padres Mariners MLB'
- `search_web({'query': 'Padres recent results form May 2025'})` → [Tue, 30 Sep 2025] Google News
[Fri, 30 May 2025] How to watch Chicago Cubs vs. San Diego Padres Gam
- `search_web({'query': 'Mariners recent results form May 2025'})` → [Sat, 11 Oct 2025] Google News
[Sun, 19 Oct 2025] MLB playoffs: Previewing Dodgers-Brewers, Mariners

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*