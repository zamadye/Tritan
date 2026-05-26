# Market Analysis — 2026-05-17 23:19 UTC

## Market
- **Question:** San Diego Padres vs. Seattle Mariners
- **Category:** sports
- **YES Price:** 42.0%
- **Days Left:** 7
- **Volume 24h:** $1,191,566
- **Liquidity:** $394,869

## Statistical Prior
- **p_base:** 38.1%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,829 (-0.5% 24h) → neutral
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
- **Confidence:** 65%
- **p_true:** 38.1%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY_ASYMMETRY
- **Catalyst Strength:** 0.45

### Reasoning
Market appears efficiently priced at 42% YES vs base rate 38% (4% gap < 5% threshold). Padres have significant pitching depth concerns with 3 SPs on IL (including Yu Darvish) vs Mariners' position player injuries, but this is already priced in—bookmaker consensus aligns at ~41-43%. Starting pitching matchup (Giolito vs Kirby) is relatively even. No concrete edge identified despite Padres' injury disadvantage. Previous identical analysis also concluded SKIP.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'San Diego Padres'})` → INJURY [san diego padres] Matt Waldron (SP): 15-Day-IL
INJURY [san diego padres] German Marquez (SP)
- `get_sports_data({'sport': 'mlb', 'team': 'Seattle Mariners'})` → INJURY [seattle mariners] Brendan Donovan (3B): 10-Day-IL
INJURY [seattle mariners] Cal Raleigh (C):
- `get_odds({'sport': 'baseball_mlb', 'team': 'Padres Mariners'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Padres Mariners'})` → No related markets found for 'Padres Mariners'
- `search_web({'query': 'San Diego Padres vs Seattle Mariners 2025 game time starting pitchers'})` → [Sun, 17 May 2026] Google News
[Tue, 14 Apr 2026] Mariners vs Padres Prediction, Odds, Moneyline, Sp
- `search_web({'query': 'Padres Mariners prediction May 2025'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Padres vs. Mariners Prediction, MLB Picks for Sund
- `search_web({'query': '"Padres" "Mariners" starting pitchers tonight May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Where to watch San Diego Padres vs. Seattle Marine
- `search_web({'query': 'Padres Mariners odds spread May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Where to watch San Diego Padres vs. Seattle Marine
- `search_web({'query': 'Padres Mariners May 17 2026 Lucas Giolito George Kirby pitching matchup'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] PADRES-MARINERS ON SUNDAY NIGHT BASEBALL MOVES TO 
- `search_web({'query': 'Padres vs Mariners prediction picks winner May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Padres vs. Mariners Prediction, MLB Picks for Sund
- `search_web({'query': 'Odds Shark Padres Mariners moneyline May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] San Diego Padres vs Seattle Mariners Odds - Sunday

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*