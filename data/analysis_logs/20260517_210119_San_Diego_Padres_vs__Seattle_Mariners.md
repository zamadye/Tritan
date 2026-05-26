# Market Analysis — 2026-05-17 21:01 UTC

## Market
- **Question:** San Diego Padres vs. Seattle Mariners
- **Category:** sports
- **YES Price:** 41.0%
- **Days Left:** 7
- **Volume 24h:** $228,326
- **Liquidity:** $431,495

## Statistical Prior
- **p_base:** 36.7%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,245 (+0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,242 (+0.0% 24h) → neutral
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
- → The San Diego Padres, second in the NL West with a 27-18 record, face the Seattle Mariners, who are second in the AL West with a 22-25 record. The s
- [Sun, 17 May 2026] Where to watch San Diego Padres vs. Seattle Mariners: Live stream, TV channel, odds for Sunday, May 17
- → SportsLine expert Angelo &quot;Amags&quot; Magliocca has dug up some value bets for a same-game parlay for Padres vs. Mariners on the May 17 edition
- [Sun, 17 May 2026] Padres vs. Mariners same-game parlay for Sunday Night Baseball matchup on May 17 from proven MLB expert
- → Randy Arozarena and Julio Rodriguez will be dialed in when they face Lucas Giolito and the Padres tonight. Free Padres vs. Mariners props for Sunday

## LLM Decision
- **Action:** SKIP
- **Confidence:** 35%
- **p_true:** 36.7%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market price (41%) is essentially identical to bookmaker consensus (FanDuel 42.4%, BetOnline 41.7%). No information gap exists. Injury reports (Padres: Darvish, Waldron, Marquez out; Mariners: Raleigh IL, Donovan DTD) are already priced into bookmaker odds. Gap of -4% is below 5% statistical edge threshold. Critical pattern warning: entry at 40-50% range historically yields only 9% win rate (n=11). Two prior decisions on identical market correctly skipped for same reasons. No new catalysts identified.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] Matt Waldron (SP): 15-Day-IL
INJURY [san diego padres] German Marquez (SP)
- `get_sports_data({'sport': 'mlb', 'team': 'Mariners'})` → INJURY [seattle mariners] Brendan Donovan (3B): Day-To-Day
INJURY [seattle mariners] Cal Raleigh (C)
- `search_web({'query': 'San Diego Padres vs Seattle Mariners 2025'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] San Diego Padres vs Seattle Mariners Live Stream: 
- `search_web({'query': 'Padres Mariners pitching injuries 2025'})` → [Sat, 20 Sep 2025] Google News
[Tue, 16 Sep 2025] The latest on Mariners starter Bryan Woo’s injury 
- `get_market_context({'keyword': 'Padres Mariners'})` → No related markets found for 'Padres Mariners'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Padres'})` → [ODDS] baseball_mlb — 2 events
  Seattle Mariners vs San Diego Padres (2026-05-17)
    [FanDuel] San
- `search_web({'query': 'Padres Mariners odds May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Padres vs. Mariners (May 17, 2026) Live Score - ES

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*