# Market Analysis — 2026-05-21 13:41 UTC

## Market
- **Question:** GP SAR La Princesse Lalla Meryem: Camila Osorio vs Panna Udvardy
- **Category:** sports
- **YES Price:** 7.8%
- **Days Left:** 6
- **Volume 24h:** $342,035
- **Liquidity:** $129,643

## Statistical Prior
- **p_base:** 2.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,200 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $76,896 (-0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: princesse lalla meryem: camila osorio
- [Bing News]
- [Wed, 20 May 2026] princesse lalla meryem: camila osorio
- → Yasmine Kabbaj continued her run through her home tournament with a 6-2, 6-4 upset of third-seeded German Tatjana Maria in the Grand Prix SAR La Pri
- [Wed, 20 May 2026] WTA roundup: Camila Osorio knocks off No. 1 seed Janice Tjen in Rabat
- → Subscribe to Sky Sports to watch live, or stream on NOW. WTA Tour: Janice Tjen versus Camila Osorio in the 2nd Round at the Grand Prix Son Altesse R
- [Wed, 20 May 2026] J. Tjen v C. Osorio
- → Janice Tjen Gagal ke Perempat Final Grand Prix SAR La Princesse Lalla Meryem di Rabat Usai Dikalahkan Camila Osorio - Menyandang status unggulan per

## LLM Decision
- **Action:** SKIP
- **Confidence:** 25%
- **p_true:** 5.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** AMBIGUOUS_SEARCH_RESULTS
- **Catalyst Strength:** 0.10

### Reasoning
Search results contradict each other - one suggests Udvardy already defeated Osorio, another suggests they haven't played yet. Cannot verify match status, exact market question, or current odds. No related markets for crowd consensus. Insufficient verifiable information to identify an edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 25%<52%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Camila Osorio'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Camila Osorio vs Panna Udvardy Grand Prix SAR La Princesse Lalla Meryem 2025'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Udvardy defeats Osorio in Rabat to make second sem
- `search_web({'query': 'Grand Prix SAR La Princesse Lalla Meryem 2026 results today'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] WTA Grand Prix De SAR La Princesse Lalla Meryem Re
- `search_web({'query': 'Osorio Udvardy head to head tennis 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] WTA Rabat Quarterfinal Predictions Including Jessi
- `search_web({'query': '"Udvardy defeats Osorio" Rabat semifinal 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 09 Oct 2025] Udvardy defeats Osorio in Rabat to make second sem
- `get_market_context({'keyword': 'Osorio Udvardy Grand Prix SAR La Princesse Lalla Meryem'})` → No related markets found for 'Osorio Udvardy Grand Prix SAR La Princesse Lalla Meryem'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*