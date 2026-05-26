# Market Analysis — 2026-05-21 17:57 UTC

## Market
- **Question:** GP SAR La Princesse Lalla Meryem: Jil Teichmann vs Yasmine Kabbaj
- **Category:** sports
- **YES Price:** 66.0%
- **Days Left:** 6
- **Volume 24h:** $143,444
- **Liquidity:** $96,703

## Statistical Prior
- **p_base:** 73.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,772 (+0.3% 24h) → neutral
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
- **Action:** YES
- **Confidence:** 63%
- **p_true:** 77.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** RANKING_EXPERIENCE_ADVANTAGE
- **Catalyst Strength:** 0.60

### Reasoning
Market (66%) is 7% below base rate (73%) for Teichmann win. Teichmann is the higher-ranked, more experienced player (recently back in Top 100) facing a lower-ranked local wildcard Kabbaj who had a 'surprise' win to reach this round. The 7% gap combined with the 60-70% entry range (83% WR from 12 trades in pattern data) suggests market is slightly overpricing Kabbaj's chances, possibly due to her momentum and home crowd. However, limited verifiable current form data prevents higher confidence. This is a moderate edge bet on the more skilled player being underpriced.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET YES $1.00

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Jil Teichmann'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Jil Teichmann'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Jil Teichmann vs Yasmine Kabbaj GP SAR La Princesse Lalla Meryem 2025'})` → [Tue, 19 May 2026] Google News
[Mon, 19 May 2025] WTA Rabat Day 3 Predictions Including Alycia Parks
- `search_web({'query': 'Jil Teichmann recent form 2025'})` → [Mon, 18 Aug 2025] Google News
[Mon, 21 Jul 2025] Tennis, WTA – Cleveland Open 2025: Teichmann defea
- `search_web({'query': 'Yasmine Kabbaj recent form 2025'})` → [Thu, 21 May 2026] Google News
[Fri, 18 Jul 2025] Jil Teichmann vs Yasmine Kabbaj Prediction &amp; P
- `get_market_context({'keyword': 'GP SAR La Princesse Lalla Meryem'})` → No related markets found for 'GP SAR La Princesse Lalla Meryem'
- `search_web({'query': 'WTA Rabat 2025 Jil Teichmann Yasmine Kabbaj head to head'})` → [Tue, 19 May 2026] Google News
[Thu, 21 May 2026] WTA Rabat Day 3 Predictions Including Alycia Parks

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*