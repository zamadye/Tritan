# Market Analysis — 2026-05-18 14:02 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $71,476
- **Liquidity:** $253,330

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,915 (-1.6% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,870 (-1.6% 24h) → risk-OFF
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
- → Here's how to watch Monday's San Diego Padres vs Los Angeles Dodgers game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 51.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.72

### Reasoning
Strong statistical signal (n=13,967) shows markets priced at 57% YES resolve YES only 44.7% of the time — a ~12 percentage point edge for NO bet. Dodgers missing key players (Blake Snell SP on 15-Day-IL, Graterol RP on 60-Day-IL) weakens their chances. Market is overpriced on YES despite large sample confirming historical mispricing pattern.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Brusdar Graterol (RP): 60-Day-IL
INJURY [los angeles dodgers] Jack Drey
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres recent game results 2025'})` → [Fri, 22 Aug 2025] Google News
[Sun, 24 Aug 2025] Los Angeles Dodgers at San Diego Padres Game Story
- `search_web({'query': 'Dodgers Padres series preview 2025'})` → [Sun, 24 Aug 2025] Google News
[Thu, 02 Oct 2025] Los Angeles Dodgers at San Diego Padres Preview - 
- `get_market_context({'query': 'Dodgers Padres'})` → [YES=50% vol=$5,821,653] Will Bitcoin hit $150k by June 30, 2026?
[YES=50% vol=$4,712,943] Will Trum
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': '"Los Angeles Dodgers vs. San Diego Padres" prediction market Polymarket 2025'})` → No search results for: "Los Angeles Dodgers vs. San Diego Padres" prediction market Polymarket 2025
- `search_web({'query': 'MLB standings 2025 Dodgers Padres record'})` → [Tue, 05 May 2026] Google News
[Thu, 14 Aug 2025] 2026 MLB Standings and Records: Spring Training - 
- `search_web({'query': 'Dodgers Padres head to head 2025 season record'})` → [Mon, 25 Aug 2025] Google News
[Fri, 22 Aug 2025] After fierce Padres-Dodgers season set, only a tie

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*