# Market Analysis — 2026-05-18 12:37 UTC

## Market
- **Question:** GP SAR La Princesse Lalla Meryem: Jil Teichmann vs Julia Grabher
- **Category:** sports
- **YES Price:** 68.0%
- **Days Left:** 6
- **Volume 24h:** $75,899
- **Liquidity:** $114,051

## Statistical Prior
- **p_base:** 75.6%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,405 (-1.3% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,378 (-1.3% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: princesse lalla meryem: teichmann julia
- [Bing News]
- [Sun, 17 May 2026] princesse lalla meryem: teichmann julia
- → Clay-Court Swing 411: Dates, draws, prize money and everything you need to know Download on the app store Google play ...
- [Sat, 17 May 2025] Grand Prix Son Altesse Royale La Princesse Lalla Meryem
- → Our editors independently choose our recommendations. Some content is produced with paid support from a third party, however our editorial decisions
- [Mon, 19 May 2025] How to watch Grand Prix De Son Altesse Royale La Princesse Lalla Meryem Tuesday: TV coverage, streaming live, match times and more 
- → Our team of savvy editors independently handpicks all recommendations. If you purchase through our links, the USA TODAY Network may earn a commissio

## LLM Decision
- **Action:** YES
- **Confidence:** 65%
- **p_true:** 81.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.65

### Reasoning
Significant 8% gap between base rate (76%, n=6077) and market price (68%). Historical data suggests market is systematically underpricing Teichmann. Teichmann appears to be higher-ranked WTA player (Top 100) on clay against lower-ranked Grabher. No injury news or negative form indicators found. Prior similar market decisions at this tournament were SKIPPED for small gaps (1-4%); this 8% gap exceeds typical thresholds. Sports category shows strong 86% WR pattern. However, confidence capped at 0.68 due to limited direct head-to-head data and inability to confirm specific current form through available tools.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET YES $1.00

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Teichmann'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_sports_data({'sport': 'tennis', 'team': 'Teichmann'})` → No injury data found for tennis Teichmann
- `search_web({'query': 'Teichmann vs Grabher Morocco Open 2025 head to head odds'})` → No search results for: Teichmann vs Grabher Morocco Open 2025 head to head odds
- `search_web({'query': 'Jil Teichmann Julia Grabher recent form 2025'})` → [Mon, 19 May 2025] Google News
[Wed, 04 Jun 2025] Tennis, WTA – Rabat Open 2025: Bouzas Maneiro sees
- `search_web({'query': 'GP SAR La Princesse Lalla Meryem 2025 tennis draw results'})` → [Thu, 09 Oct 2025] Google News
[Wed, 07 May 2025] Grand Prix Son Altesse Royale La Princesse Lalla M
- `search_web({'query': 'Jil Teichmann WTA ranking form clay court 2025'})` → [Mon, 21 Jul 2025] Google News
[Mon, 21 Jul 2025] Rankings Watch: Boisson cracks Top 50; Begu, Teich
- `search_web({'query': 'Teichmann Grabher head to head record tennis'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] RABAT DRAW. Julia Grabher’s prediction with Teichm
- `search_web({'query': 'Julia Grabher WTA ranking 2025 results clay'})` → [Tue, 07 Apr 2026] Google News
[Mon, 06 Apr 2026] LOOK: Alex Eala opens her clay season against Juli
- `search_web({'query': '"Teichmann" "Grabher" Rabat 2025 prediction pick odds'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] H2H, prediction of Julia Grabher vs Jil Teichmann 
- `get_market_context({'keyword': 'Teichmann Grabher'})` → No related markets found for 'Teichmann Grabher'

## Outcome
**✅ WIN** | P&L: $+0.47 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*