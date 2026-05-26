# Market Analysis — 2026-05-17 23:35 UTC

## Market
- **Question:** San Diego Padres vs. Seattle Mariners
- **Category:** sports
- **YES Price:** 40.0%
- **Days Left:** 6
- **Volume 24h:** $1,234,670
- **Liquidity:** $39,769

## Statistical Prior
- **p_base:** 35.2%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,748 (-0.6% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,805 (-0.5% 24h) → neutral
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
- → The Padres and Mariners close their weekend series Sunday night at T-Mobile Park, with San Diego going for a sweep after winning the first two games

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 35.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] Matt Waldron (SP): 15-Day-IL
INJURY [san diego padres] German Marquez (SP)
- `get_sports_data({'sport': 'mlb', 'team': 'Mariners'})` → INJURY [seattle mariners] Brendan Donovan (3B): 10-Day-IL
INJURY [seattle mariners] Cal Raleigh (C):
- `search_web({'query': 'San Diego Padres vs Seattle Mariners 2025 preview'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] San Diego Padres at Seattle Mariners odds, picks a
- `search_web({'query': 'Padres Mariners May 2026 prediction'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Padres vs. Mariners Prediction, MLB Picks for Sund
- `get_market_context({'keyword': 'Padres Mariners'})` → No related markets found for 'Padres Mariners'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Padres'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Padres Mariners odds moneyline May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Padres vs. Mariners prediction, odds, time: 2026 M

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*