# Market Analysis — 2026-05-21 17:42 UTC

## Market
- **Question:** GP SAR La Princesse Lalla Meryem: Jil Teichmann vs Yasmine Kabbaj
- **Category:** sports
- **YES Price:** 74.0%
- **Days Left:** 6
- **Volume 24h:** $117,846
- **Liquidity:** $33,196

## Statistical Prior
- **p_base:** 82.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,918 (+0.6% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,848 (+0.4% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: princesse lalla meryem: teichmann yasmine
- [Bing News]
- [Sat, 17 May 2025] princesse lalla meryem: teichmann yasmine
- → Our editors independently choose our recommendations. Some content is produced with paid support from a third party, however our editorial decisions
- [Wed, 20 May 2026] How to watch Grand Prix De Son Altesse Royale La Princesse Lalla Meryem Monday: TV coverage, streaming live, match times and more M
- → Surface: Red clay RABAT, MOROCCO (AP) _ Results Wednesday from Grand Prix De SAR La Princesse Lalla Meryem at Club d ...
- [Thu, 21 May 2026] WTA Grand Prix De SAR La Princesse Lalla Meryem Results
- → Live scores for the 2025 Grand Prix Son Altesse Royale La Princesse Lalla Meryem tennis tournament on ESPN. Includes daily schedules, live scores an

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 82.8%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Despite +9% gap between market (74%) and base rate (83%), cannot verify edge. Morocco article suggests Kabbaj in good form at home tournament. Entry 70-80% range has weak 29% WR historically. No concrete catalyst or injury news to confirm why market undervalues Teichmann. Confidence below 0.55 threshold.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'tennis_atp', 'team': 'Teichmann'})` → No injury data found for tennis_atp Teichmann
- `search_web({'query': 'Jil Teichmann vs Yasmine Kabbaj GP SAR La Princesse Lalla Meryem 2025'})` → [Mon, 19 May 2025] Google News
[Mon, 19 May 2025] Tennis, WTA – Rabat Open 2025: Volynets beats Alve
- `search_web({'query': 'Teichmann Kabbaj Rabat 2025 head to head odds'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] H2H, prediction of Jil Teichmann vs Yasmine Kabbaj
- `get_odds({'sport': 'tennis_atp', 'team': 'Teichmann'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Jil Teichmann current form ranking 2025'})` → [Thu, 21 May 2026] Google News
[Mon, 08 Sep 2025] Jil Teichmann vs Yasmine Kabbaj Prediction &amp; P
- `search_web({'query': 'Yasmine Kabbaj current form ranking 2025'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Morocco’s Yasmine Kabbaj Advances to Quarter-Final
- `get_market_context({'keyword': 'Teichmann Kabbaj'})` → No related markets found for 'Teichmann Kabbaj'
- `search_web({'query': 'Jil Teichmann injury status May 2025'})` → [Sat, 19 Jul 2025] Google News
[Sat, 09 Aug 2025] Tennis, WTA – Iasi Open 2025: Teichmann sees off C
- `search_web({'query': 'Yasmine Kabbaj recent results Rabat Open 2025'})` → [Thu, 21 May 2026] Google News
[Mon, 19 May 2025] Jil Teichmann vs Yasmine Kabbaj Prediction &amp; P

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*