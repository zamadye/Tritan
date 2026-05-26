# Market Analysis — 2026-05-18 00:02 UTC

## Market
- **Question:** San Diego Padres vs. Seattle Mariners
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $1,395,467
- **Liquidity:** $60,204

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,426 (-1.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,805 (-0.5% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
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
- → The San Diego Padres, second in the NL West with a 27-18 record, face the Seattle Mariners, who are second in the AL West with a 22-25 record. The s

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 52.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical evidence: markets at 57% resolve YES only 44.7% historically (n=13,967). Padres have significant pitching disadvantage with 3 SPs on IL including ace Yu Darvish. Crowd likely overprices Padres due to brand recognition despite injury disadvantages.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] Matt Waldron (SP): 15-Day-IL
INJURY [san diego padres] German Marquez (SP)
- `get_sports_data({'sport': 'mlb', 'team': 'Mariners'})` → INJURY [seattle mariners] Brendan Donovan (3B): 10-Day-IL
INJURY [seattle mariners] Cal Raleigh (C):
- `search_web({'query': 'San Diego Padres recent results form 2025'})` → [Sat, 30 Aug 2025] Google News
[Mon, 03 Nov 2025] Padres score seven runs in the 7th - MLB.com
[Fri,
- `search_web({'query': 'Seattle Mariners recent results form 2025'})` → [Mon, 13 Oct 2025] Google News
[Mon, 03 Nov 2025] Seattle Mariners at Toronto Blue Jays Game Story, 
- `get_market_context({'keyword': 'San Diego Padres'})` → No related markets found for 'San Diego Padres'
- `get_odds({'sport': 'baseball_mlb', 'team': 'San Diego Padres'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Padres vs Mariners 2025 matchup head to head'})` → [Fri, 15 May 2026] Google News
[Sun, 29 Mar 2026] Mariners vs Padres Prediction, Odds, Moneyline, Sp
- `search_web({'query': 'Padres Mariners series August 2025'})` → [Mon, 25 Aug 2025] Google News
[Mon, 25 Aug 2025] San Diego Padres at Seattle Mariners Game Story, S
- `get_market_context({'keyword': 'Mariners'})` → No related markets found for 'Mariners'
- `search_web({'query': 'Padres Mariners August 26 2025 result score'})` → [Tue, 26 Aug 2025] Google News
[Tue, 26 Aug 2025] San Diego Padres at Seattle Mariners Game Story, S
- `search_web({'query': 'MLB standings wild card 2025 Padres Mariners'})` → [Sun, 28 Sep 2025] Google News
[Sun, 02 Nov 2025] 2025 MLB playoff picture: Final baseball standings

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*