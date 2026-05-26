# Market Analysis — 2026-05-18 23:34 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $127,633
- **Liquidity:** $458,281

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,999 (-1.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,980 (-1.1% 24h) → risk-OFF

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)
- ?: Max Muncy — 10-Day-IL (Fracture)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: angeles dodgers diego padres
- [Bing News]
- [Mon, 18 May 2026] angeles dodgers diego padres
- → Siani only spent three months with the Dodgers organization after being claimed in February. The 26-year-old outfielder never appeared in a Major Le
- [Mon, 18 May 2026] Dodgers Lose Player to Orioles Before Padres Game
- → Petco Park is the location where the San Diego Padres (27-18) will take on the Los Angeles Dodgers (28-18) on Tuesday. The moneyline on this game ha
- [Mon, 18 May 2026] Los Angeles Dodgers vs San Diego Padres Prediction, 5/19/2026 MLB Picks, Best Bets &amp; Odds
- → The Los Angeles Dodgers (29-18) meet the San Diego Padres( 28-18) to start a three-game series between the NL West rivals. The Dodgers have won five

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_REVERSION
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 57% YES historically resolve YES only 44.7% of the time — a 12.3pp overpricing edge. Dodgers have 3 key injuries (Snell, Graterol, Dreyer) vs Padres injuries (Marquez, Brito, Campusano). Prior SKIP decisions on same market had weaker confidence (62-65%) due to 3% gap gate failure, but the underlying stat edge (12.3pp) significantly exceeds that threshold. SPORTS pattern shows 85% WR overall. However, 50-60% entry range historically weak (25% WR, n=4), and no direct game-specific catalyst found. Macro fear environment (F&G=28) is irrelevant to individual game outcomes.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Brusdar Graterol (RP): 60-Day-IL
INJURY [los angeles dodgers] Jack Drey
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres game 2024'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Tom Krasovic: Playoff regulars Padres, Dodgers see
- `search_web({'query': 'Dodgers Padres injury report May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] How to watch Dodgers vs. Padres: TV channel and st
- `get_market_context({'keyword': 'Dodgers Padres'})` → No related markets found for 'Dodgers Padres'
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*