# Market Analysis — 2026-05-18 12:02 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $63,981
- **Liquidity:** $184,690

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,253 (-1.4% 24h) → risk-OFF
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
- → Here's how to watch Monday's San Diego Padres vs Los Angeles Dodgers game, including start times, TV channels, scores and how to stream.
- [Mon, 18 May 2026] Where to watch Los Angeles Dodgers vs San Diego Padres: TV channel, start time, streaming for May 18
- → Los Angeles Dodgers (29-18, first in the NL West) vs. San Diego Padres (28-18, second in the NL West) San Diego; Monday, 9:40 p.m. EDT. PITCHING PRO
- [Sun, 17 May 2026] Dodgers take win streak into matchup with the Padres
- → The Los Angeles Dodgers and San Diego Padres' pitching probables for this week's huge series, plus key injuries and how to watch.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 52.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical evidence (n=13,967) shows markets at 57% resolve YES only 44.7% of time, indicating market overprices YES by ~12.3 points. No specific catalyst found to justify higher YES price. Competitive matchup doesn't override large-sample historical resolution data.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Brusdar Graterol (RP): 60-Day-IL
INJURY [los angeles dodgers] Jack Drey
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres MLB 2025 recent results series'})` → [Sun, 17 Aug 2025] Google News
[Wed, 18 Mar 2026] San Diego Padres at Los Angeles Dodgers Game Story
- `search_web({'query': 'Dodgers Padres pitching matchup upcoming series 2025'})` → [Tue, 30 Sep 2025] Google News
[Tue, 30 Sep 2025] Padres-Cubs Wild Card Series Game 1 (ABC) - MLB.co
- `get_market_context({'keyword': 'Dodgers Padres'})` → No related markets found for 'Dodgers Padres'
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres series August 2025 prediction'})` → [Mon, 18 May 2026] Google News
[Fri, 22 Aug 2025] San Diego Padres vs Los Angeles Dodgers Prediction
- `search_web({'query': 'Dodgers Padres betting odds analysis August 2025'})` → [Sun, 17 May 2026] Google News
[Fri, 22 Aug 2025] MLB World Series Odds 2026 - Odds Shark
[Fri, 15 A
- `get_market_context({'keyword': 'MLB baseball'})` → No related markets found for 'MLB baseball'
- `search_web({'query': '"Dodgers" "Padres" August 2025 game series results'})` → [Mon, 25 Aug 2025] Google News
[Sat, 23 Aug 2025] After fierce Padres-Dodgers season set, only a tie
- `search_web({'query': 'MLB standings August 2025 NL West Dodgers Padres'})` → [Wed, 22 Apr 2026] Google News
[Fri, 15 Aug 2025] Dodgers not concerned with Padres in NL West stand

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*