# Market Analysis — 2026-05-18 10:45 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $57,440
- **Liquidity:** $193,288

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,785 (-2.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,788 (-2.1% 24h) → risk-OFF
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
- → Here's how to watch Monday's San Diego Padres vs Los Angeles Dodgers game, including start times, TV channels, scores and how to stream.
- [Mon, 18 May 2026] Where to watch Los Angeles Dodgers vs San Diego Padres: TV channel, start time, streaming for May 18
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
Markets at 57% YES resolve YES only 44.7% historically (n=13,967). Large-sample statistical evidence shows systematic overpricing of YES. Despite 3% gap being below typical 5% threshold, the direct statistical signal provides a clear edge for betting NO. Injuries slightly favor Padres, but the primary edge is the market inefficiency revealed by historical resolution patterns.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Los Angeles Dodgers'})` → INJURY [los angeles dodgers] Brusdar Graterol (RP): 60-Day-IL
INJURY [los angeles dodgers] Jack Drey
- `get_sports_data({'sport': 'mlb', 'team': 'San Diego Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Dodgers vs Padres 2025 MLB series odds prediction'})` → [Thu, 02 Oct 2025] Google News
[Sun, 24 Aug 2025] 2025 MLB playoffs: World Series odds, postseason p
- `search_web({'query': 'Los Angeles Dodgers San Diego Padres head to head 2025 season'})` → [Mon, 18 May 2026] Google News
[Wed, 18 Mar 2026] San Diego Padres vs Los Angeles Dodgers Prediction
- `get_market_context({'keyword': 'Dodgers Padres'})` → No related markets found for 'Dodgers Padres'
- `search_web({'query': 'Dodgers Padres 2025 season record standings'})` → [Tue, 05 May 2026] Google News
[Wed, 22 Apr 2026] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Padres Dodgers series game 1 October 2025'})` → [Wed, 01 Oct 2025] Google News
[Sun, 02 Nov 2025] In pivotal moment, Machado makes Cubs pay as Padre

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*