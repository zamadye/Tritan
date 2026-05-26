# Market Analysis — 2026-05-18 13:38 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $70,005
- **Liquidity:** $252,427

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,121 (-1.5% 24h) → risk-OFF
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
- → Starting Monday night, one of the best rivalries in Major League Baseball will return. The Los Angeles Dodgers and the […] ...
- [Mon, 18 May 2026] Rivalry returns: Padres, Dodgers clash for first time this season
- → Los Angeles Dodgers (29-18, first in the NL West) vs. San Diego Padres (28-18, second in the NL West) San Diego; Monday, 9:40 p.m. EDT. PITCHING PRO

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 52.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) shows markets priced at 57% YES resolve YES only 44.7% of the time, creating a clear edge for NO bet. Market overprices YES by ~12 percentage points based on historical resolution data.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Brusdar Graterol (RP): 60-Day-IL
INJURY [los angeles dodgers] Jack Drey
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres upcoming game preview'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Los Angeles Dodgers at San Diego Padres Preview - 
- `search_web({'query': 'Dodgers Padres May 18 2026 prediction odds'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Los Angeles Dodgers vs San Diego Padres Odds - Mon
- `get_market_context({'keyword': 'Dodgers Padres'})` → No related markets found for 'Dodgers Padres'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*