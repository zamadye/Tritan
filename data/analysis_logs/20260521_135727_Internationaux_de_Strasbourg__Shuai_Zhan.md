# Market Analysis — 2026-05-21 13:57 UTC

## Market
- **Question:** Internationaux de Strasbourg: Shuai Zhang vs Emma Navarro
- **Category:** sports
- **YES Price:** 33.0%
- **Days Left:** 6
- **Volume 24h:** $78,194
- **Liquidity:** $52,512

## Statistical Prior
- **p_base:** 25.7%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $76,772 (-0.5% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $76,984 (-0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Major AI model release → benchmark competition → sector excitement
- → AI regulation proposed → uncertainty → AI stocks fall short-term
- → AI chip shortage → NVIDIA revenue beats → AI infrastructure stocks rally
- → AI energy demand → data center power stocks rally

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: shuai zhang emma
- [Bing News]
- [Wed, 20 May 2026] internationaux strasbourg: shuai zhang emma
- → Emma Navarro seeks to rediscover form vs rising American Iva Jovic. Get draw, schedule, entry list, prize money and expert predictions.
- [Wed, 20 May 2026] Internationaux de Strasbourg Day Four Round-up | Emma Navarro rallies to defeat Iva Jovic and advance to quarterfinals
- → None ...
- [Fri, 15 May 2026] WTA Internationaux de Strasbourg Results
- → The Internationaux de Strasbourg takes place between 17-23 May in a WTA 500 tournament prior to the French Open. Elena Rybakina is defending champio

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 25.7%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Market overprices YES (33%) vs. base rate (26%) by 7%, suggesting crowd bias toward Navarro. However, no direct evidence found through search regarding current form, injuries, or head-to-head that would confirm or refute this edge. Past similar market (Navarro vs. Jovic) was also skipped due to insufficient statistical edge. Without verifiable catalyst or current data, cannot confirm profitability.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Shuai Zhang'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Shuai Zhang vs Emma Navarro Internationaux de Strasbourg 2024 form injury'})` → [Sat, 04 Oct 2025] Google News
[Wed, 20 May 2026] Wuhan draw: Sabalenka returns for title defense, O
- `search_web({'query': 'Emma Navarro recent form results 2024 WTA'})` → [Sun, 17 May 2026] Google News
[Tue, 17 Feb 2026] WTA Strasbourg Day 1 Predictions Including Sara Be
- `get_market_context({'keyword': 'Internationaux de Strasbourg'})` → No related markets found for 'Internationaux de Strasbourg'
- `search_web({'query': 'Internationaux de Strasbourg 2024 Zhang Navarro prediction'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions 
- `search_web({'query': 'Shuai Zhang tennis 2025 results ranking'})` → [Tue, 07 Oct 2025] Google News
[Sun, 17 Aug 2025] Wuhan whiplash: Zhang loses 32 out of 37 points ..
- `search_web({'query': '"Internationaux de Strasbourg" 2025 Zhang Navarro'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Zhang vs. Navarro | Quarterfinals Internationaux d

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*