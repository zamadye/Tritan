# Market Analysis — 2026-05-17 20:07 UTC

## Market
- **Question:** San Diego Padres vs. Seattle Mariners
- **Category:** sports
- **YES Price:** 41.0%
- **Days Left:** 7
- **Volume 24h:** $218,399
- **Liquidity:** $520,070

## Statistical Prior
- **p_base:** 36.7%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,359 (+0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,350 (+0.1% 24h) → neutral
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
- → SportsLine expert Angelo &quot;Amags&quot; Magliocca has dug up some value bets for a same-game parlay for Padres vs. Mariners on the May 17 edition
- [Sun, 17 May 2026] Padres vs. Mariners same-game parlay for Sunday Night Baseball matchup on May 17 from proven MLB expert
- → The San Diego Padres, second in the NL West with a 27-18 record, face the Seattle Mariners, who are second in the AL West with a 22-25 record. The s
- [Sun, 17 May 2026] Where to watch San Diego Padres vs. Seattle Mariners: Live stream, TV channel, odds for Sunday, May 17
- → Randy Arozarena and Julio Rodriguez will be dialed in when they face Lucas Giolito and the Padres tonight. Free Padres vs. Mariners props for Sunday

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 36.7%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Prediction market aligns with bookmaker consensus (~42%). Historical pattern shows 9% win rate for 40-50% entries. No verifiable edge or catalyst exists. Padres' pitching injuries and Mariners' lineup concerns are already priced in.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] Matt Waldron (SP): 15-Day-IL
INJURY [san diego padres] German Marquez (SP)
- `get_sports_data({'sport': 'mlb', 'team': 'Mariners'})` → INJURY [seattle mariners] Brendan Donovan (3B): Day-To-Day
INJURY [seattle mariners] Cal Raleigh (C)
- `get_odds({'sport': 'baseball_mlb', 'team': 'Padres'})` → [ODDS] baseball_mlb — 2 events
  Seattle Mariners vs San Diego Padres (2026-05-17)
    [FanDuel] San
- `search_web({'query': 'Padres Mariners prediction May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Padres vs Mariners Prediction, Picks &amp; Odds fo
- `search_web({'query': 'injury report Padres Mariners May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Seattle Mariners vs. San Diego Padres - May 17, 20
- `get_market_context({'keyword': 'Padres'})` → No related markets found for 'Padres'
- `get_market_context({'keyword': 'Mariners'})` → No related markets found for 'Mariners'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*