# Market Analysis — 2026-05-18 13:16 UTC

## Market
- **Question:** GP SAR La Princesse Lalla Meryem: Alycia Parks vs Moyuka Uchijima
- **Category:** sports
- **YES Price:** 74.0%
- **Days Left:** 6
- **Volume 24h:** $75,339
- **Liquidity:** $64,563

## Statistical Prior
- **p_base:** 82.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,574 (-1.0% 24h) → neutral
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,474 (-1.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: princesse lalla meryem: alycia parks
- [Bing News]
- [Fri, 26 May 2023] princesse lalla meryem: alycia parks
- → Also known as the Morocco Open or Rabat Grand Prix, the Grand Prix Sar La Princesse Lalla Meryem is an international WTA 250 event played on outdoor
- [] Grand Prix Son Altesse Royale La Princesse Lalla Meryem
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** YES
- **Confidence:** 65%
- **p_true:** 91.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.72

### Reasoning
Strong 9% gap between base rate (83%, n=6077) and market price (74%). Historical data from 6,077 similar scenarios shows Parks-level favorites win 83% of the time, but market only prices at 74%. No contradicting injury/form data found. Sports category has 88% historical win rate. The gap exceeds the 5% edge threshold. Crowd appears to be undervaluing the favorite's true probability.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET YES $1.00

## Tool Calls
- `get_sports_data({'team': 'Alycia Parks', 'sport': 'tennis_atp'})` → No injury data found for tennis_atp Alycia Parks
- `get_sports_data({'team': 'Moyuka Uchijima', 'sport': 'tennis_atp'})` → No injury data found for tennis_atp Moyuka Uchijima
- `search_web({'query': 'Alycia Parks vs Moyuka Uchijima GP SAR La Princesse Lalla Meryem 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] PREDICTION, PREVIEW, H2H: Parks, Ferro, Belen Teic
- `search_web({'query': 'Moyuka Uchijima recent form 2025 tennis results'})` → [Wed, 08 Oct 2025] Google News
[Mon, 22 Sep 2025] Tennis: Coco Gauff begins Wuhan Open campaign with
- `search_web({'query': 'Alycia Parks recent form clay court 2025 2026'})` → [Thu, 16 Apr 2026] Google News
[Wed, 22 Apr 2026] Alycia Parks faces Andreeva in Stuttgart Round of 
- `search_web({'query': 'Moyuka Uchijima recent form clay court 2025 2026'})` → [Thu, 16 Apr 2026] Google News
[Fri, 10 Apr 2026] Madrid 411: Dates, top players, prize money and mo
- `get_odds({'sport': 'tennis_atp', 'team': 'Parks'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Alycia Parks Moyuka Uchijima'})` → No related markets found for 'Alycia Parks Moyuka Uchijima'
- `search_web({'query': 'Alycia Parks ranking 2026 WTA clay specialist'})` → [Mon, 06 Apr 2026] Google News
[Tue, 21 Apr 2026] Alycia Parks takes on Galfi in Linz first round sh
- `search_web({'query': 'Moyuka Uchijima ranking 2026 WTA Japan clay'})` → [Mon, 02 Mar 2026] Google News
[Sun, 05 Apr 2026] Rankings Watch: Bucsa vaults 32 spots, Jimenez Kas
- `search_web({'query': '"Alycia Parks" "Uchijima" H2H prediction Rabat 2026'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] H2H, prediction of Alycia Parks vs Moyuka Uchijima
- `get_market_context({'keyword': 'GP SAR La Princesse Lalla Meryem'})` → No related markets found for 'GP SAR La Princesse Lalla Meryem'
- `search_web({'query': 'Tennis Tonic Parks Uchijima prediction Rabat odds pick winner'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] H2H, prediction of Alycia Parks vs Moyuka Uchijima

## Outcome
**✅ WIN** | P&L: $+0.47 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*