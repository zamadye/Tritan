# Market Analysis — 2026-05-18 12:23 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $64,284
- **Liquidity:** $232,591

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,405 (-1.3% 24h) → risk-OFF
- BTC: $77,253 (-1.4% 24h) → risk-OFF
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
- → Los Angeles Dodgers (29-18, first in the NL West) vs. San Diego Padres (28-18, second in the NL West) San Diego; Monday, 9:40 p.m. EDT. PITCHING PRO
- [Mon, 18 May 2026] Dodgers take win streak into matchup with the Padres
- → Here's how to watch Monday's San Diego Padres vs Los Angeles Dodgers game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Los Angeles Dodgers vs San Diego Padres: TV channel, start time, streaming for May 18
- → The Los Angeles Dodgers and San Diego Padres' pitching probables for this week's huge series, plus key injuries and how to watch.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_CALIBRATION
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) shows markets at 57% resolve YES only 44.7% of time, suggesting market overprices YES. However, gate fails: gap between base rate (60%) and market (57%) is only 3%, below 5% threshold. Past decisions show same analysis skipped for same reason. No new catalysts or injury news materially affecting this specific game outcome. Entry 50-60% pattern shows only 25% historical win rate.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Brusdar Graterol (RP): 60-Day-IL
INJURY [los angeles dodgers] Jack Drey
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres upcoming game predictions injury report'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Fantasy baseball: Gasser, Rodriguez called up for 
- `search_web({'query': 'Dodgers vs Padres May 18 2026 starting pitchers odds prediction'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] MLB Picks Today: Greg Peterson Best Bets Monday, M
- `search_web({'query': '"Dodgers" "Padres" "May 18" starting pitcher 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] MLB Gameday: Dodgers at Padres, Probable Pitchers,
- `get_market_context({'keyword': 'Dodgers Padres'})` → No related markets found for 'Dodgers Padres'
- `search_web({'query': 'Dodgers Padres May 18 2026 weather lineup announcement'})` → [Thu, 23 Apr 2026] Google News
[] Peacock May 2026 Movies, TV Shows, and Sports - Vital Thrills
- `search_web({'query': 'Dodgers Padres May 2026 series predictions odds'})` → [Sun, 17 May 2026] Google News
[Mon, 11 May 2026] San Diego Padres vs. Los Angeles Dodgers Series Ma

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*