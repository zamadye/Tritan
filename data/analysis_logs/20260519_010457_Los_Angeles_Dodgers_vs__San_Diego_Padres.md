# Market Analysis — 2026-05-19 01:04 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $141,201
- **Liquidity:** $480,433

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,029 (-0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,117 (+0.1% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)
- ?: Max Muncy — 10-Day-IL (Fracture)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: angeles dodgers diego padres
- [Bing News]
- [Mon, 18 May 2026] angeles dodgers diego padres
- → The Los Angeles Dodgers (29-18) take a five-game winning streak down the coast on Monday night to open a three-game series for the National League W
- [Mon, 18 May 2026] How to live stream Dodgers vs Padres: MLB, TV channel
- → The Los Angeles Dodgers and the San Diego Padres open a 3-game series Monday at Petco Park in San Diego, California. First pitch is set for 9:40 p.m
- [Mon, 18 May 2026] LA Dodgers at San Diego Padres odds, picks and predictions
- → Your game thread for May 18, 2026.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal indicates markets priced at 57% resolve YES only 44.7% of the time (n=13,967), creating ~12% edge for NO. Supporting injury evidence: Dodgers missing two key starters (Blake Snell, Tyler Glasnow) on 15-Day-IL weakens their lineup. Crowd appears to be overpricing YES relative to historical resolution rates. However, entry range 50-60% shows historically weak WR (40%), slightly tempering conviction.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Blake Snell (SP): 15-Day-IL
INJURY [los angeles dodgers] Tyler Glasnow 
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `get_odds({'sport': 'baseball_mlb', 'team': 'Dodgers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres 2025 game preview'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Padres vs Dodgers Series Preview: Pitching Probabl
- `search_web({'query': 'Dodgers Padres May 2026 pitching matchup injuries'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Dodgers vs. Padres Series Injured List - May 18-20
- `get_market_context({'keyword': 'Dodgers Padres'})` → No related markets found for 'Dodgers Padres'
- `search_web({'query': 'Shohei Ohtani pitching change Dodgers Padres series May 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Padres, Dodgers separated by slimmest of margins e

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*