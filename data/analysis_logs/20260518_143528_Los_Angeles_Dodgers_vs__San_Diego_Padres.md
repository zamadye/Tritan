# Market Analysis — 2026-05-18 14:35 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $81,294
- **Liquidity:** $234,881

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,630 (-1.7% 24h) → risk-OFF
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
- → Here's how to watch Monday's San Diego Padres vs Los Angeles Dodgers game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 57% YES resolve YES only 44.7% of the time, indicating a 12.3% overpricing of YES. While past decisions cited the 3% gap (below 5% gate) as reason to skip, the fundamental question is whether YES will resolve - and the data strongly suggests NO. Injury data is balanced (both teams have key players on IL). Macro risk-off environment unlikely to directly affect sports outcomes. Sports category has strong 91% WR overall. The crowd is paying 57% for an outcome that historically occurs only 44.7% of the time.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Dodgers'})` → INJURY [los angeles dodgers] Brusdar Graterol (RP): 60-Day-IL
INJURY [los angeles dodgers] Jack Drey
- `get_sports_data({'sport': 'mlb', 'team': 'Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres upcoming series 2025'})` → [Wed, 18 Mar 2026] Google News
[Sun, 24 Aug 2025] Dodgers vs. Padres: Upcoming Game Info &amp; Rival
- `search_web({'query': 'Dodgers vs Padres today 2026 injury update'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Padres vs. Dodgers: Injury Report, Updates &amp; P
- `search_web({'query': 'Padres vs Dodgers May 18 2026 probable pitchers'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] MLB Gameday: Dodgers at Padres, Probable Pitchers,
- `get_market_context({'keyword': 'Los Angeles Dodgers'})` → No related markets found for 'Los Angeles Dodgers'
- `get_market_context({'keyword': 'Dodgers Padres'})` → No related markets found for 'Dodgers Padres'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*