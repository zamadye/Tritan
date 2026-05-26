# Market Analysis — 2026-05-18 14:50 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $81,758
- **Liquidity:** $240,062

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,363 (-2.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,474 (-1.9% 24h) → risk-OFF
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
- → Yoshinobu Yamamoto can handle San Diego's bats in our Dodgers vs. Padres predictions and MLB picks on Monday, May 18.
- [Mon, 18 May 2026] Dodgers vs Padres Prediction, Picks &amp; Odds for Today's MLB Game
- → The Monday night series opener between the visiting Los Angeles Dodgers and the San Diego Padres could be billed as a hot team against a sizzling hi
- [Mon, 18 May 2026] Hot Dodgers meet even hotter Gavin Sheets vs. Padres in NL West clash
- → The Padres are a wonder. How in the name of Tony Gwynn are they winning games? They have the worst batting average in the major leagues and the seco

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 60.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.75

### Reasoning
Statistical signal (n=13,967) shows market overprices YES (57% market resolves YES 44.7% historically), but gate check fails: gap=3% < 5% threshold required. Past decisions for identical market also resulted in SKIP. Injury reports favor neither team decisively. Recent Padres victories provide some support for NO but insufficient to override gate failure.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Brusdar Graterol (RP): 60-Day-IL
INJURY [los angeles dodgers] Jack Drey
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres 2025 recent results'})` → [Fri, 22 Aug 2025] Google News
[Wed, 18 Mar 2026] Los Angeles Dodgers at San Diego Padres Game Story
- `search_web({'query': 'Dodgers Padres series August 2025 results score'})` → [Sat, 16 Aug 2025] Google News
[Fri, 22 Aug 2025] San Diego Padres at Los Angeles Dodgers Game Story
- `search_web({'query': 'Padres vs Dodgers score August 22 2025 shutout'})` → [Sat, 23 Aug 2025] Google News
[Sat, 23 Aug 2025] Padres 5-1 Dodgers (Aug 23, 2025) Final Score - ES
- `get_market_context({'keyword': 'Dodgers Padres'})` → No related markets found for 'Dodgers Padres'
- `search_web({'query': 'Dodgers vs Padres August 25 2025 pitching'})` → [Mon, 25 Aug 2025] Google News
[Mon, 25 Aug 2025] How to Watch Dodgers vs. Reds: TV Channel &amp; Li

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*