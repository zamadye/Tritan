# Market Analysis — 2026-05-18 13:46 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $70,281
- **Liquidity:** $265,490

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,916 (-1.7% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,331 (-1.1% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: angeles dodgers diego padres
- [Bing News]
- [Mon, 18 May 2026] angeles dodgers diego padres
- → The Monday night series opener between the visiting Los Angeles Dodgers and the San Diego Padres could be billed as a hot team against a sizzling hi
- [Mon, 18 May 2026] Hot Dodgers meet even hotter Gavin Sheets vs. Padres in NL West clash
- → Los Angeles Dodgers (29-18, first in the NL West) vs. San Diego Padres (28-18, second in the NL West) San Diego; Monday, 9:40 p.m. EDT. PITCHING PRO
- [Mon, 18 May 2026] Dodgers take win streak into matchup with the Padres
- → Starting Monday night, one of the best rivalries in Major League Baseball will return. The Los Angeles Dodgers and the […] ...

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 52.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) shows markets priced at 57% YES resolve YES only 44.7% of the time, indicating significant overpricing of YES by approximately 12 percentage points. While the gap between base rate (60%) and market (57%) is only 3%, the historical resolution data provides a concrete, verifiable edge for a NO bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Brusdar Graterol (RP): 60-Day-IL
INJURY [los angeles dodgers] Jack Drey
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres recent news'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Where to watch Los Angeles Dodgers vs San Diego Pa
- `search_web({'query': 'Dodgers Padres game outcome news May 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Los Angeles Dodgers at Los Angeles Angels Game Sto
- `get_market_context({'keyword': 'Dodgers Padres'})` → No related markets found for 'Dodgers Padres'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'sport': 'baseball_mlb'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*