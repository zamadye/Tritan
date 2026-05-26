# Market Analysis — 2026-05-21 15:30 UTC

## Market
- **Question:** Internationaux de Strasbourg: Shuai Zhang vs Emma Navarro
- **Category:** sports
- **YES Price:** 75.0%
- **Days Left:** 6
- **Volume 24h:** $339,051
- **Liquidity:** $48,788

## Statistical Prior
- **p_base:** 83.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,131 (-0.6% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $76,959 (-0.4% 24h) → neutral
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
- **Action:** YES
- **Confidence:** 65%
- **p_true:** 87.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** PLAYER_FORM_DIVERGENCE
- **Catalyst Strength:** 0.60

### Reasoning
Market priced 9% below base rate (75% vs 84%). Emma Navarro on 5-match losing streak while Shuai Zhang has recent positive form (AO doubles title, R1 win at Strasbourg). Gap suggests YES (Zhang) is undervalued. However, limited head-to-head data and weak historical pattern for this price range (40% WR) reduces confidence.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET YES $1.00

## Tool Calls
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Zhang Navarro'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Strasbourg tennis'})` → No related markets found for 'Strasbourg tennis'
- `search_web({'query': 'Shuai Zhang Emma Navarro Strasbourg 2025 match preview'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Internationaux de Strasbourg presented by Mammotio
- `search_web({'query': 'Internationaux de Strasbourg Zhang vs Navarro odds prediction'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions 
- `search_web({'query': 'Emma Navarro vs Shuai Zhang Strasbourg head to head 2026'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] WTA Strasbourg Quarterfinal Predictions Including 
- `get_market_context({'keyword': 'Navarro Zhang'})` → No related markets found for 'Navarro Zhang'
- `search_web({'query': 'site:tennistonic.com "Emma Navarro vs Shuai Zhang" Strasbourg 2026'})` → [Wed, 21 Nov 2012] Google News
[Fri, 24 Aug 2018] HOME - Tennis Tonic - News, Predictions, H2H, Live
- `search_web({'query': 'Shuai Zhang Strasbourg 2026 results form'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] WTA Strasbourg Quarterfinal Predictions Including 
- `search_web({'query': 'Emma Navarro Strasbourg 2026 results form'})` → [Wed, 20 May 2026] Google News
[Sun, 17 May 2026] The Official Home of the Women's Tennis Associatio
- `search_web({'query': 'Shuai Zhang WTA ranking May 2026'})` → [Wed, 20 May 2026] Google News
[Tue, 05 May 2026] Shuai Zhang Matches | Past Tournaments &amp; More 
- `search_web({'query': 'Emma Navarro WTA ranking May 2026'})` → [Mon, 18 May 2026] Google News
[Fri, 08 May 2026] WTA Rankings Update: Rome champion Svitolina rises
- `search_web({'query': '"Emma Navarro" "Shuai Zhang" Strasbourg quarterfinal 2026 prediction'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] WTA Strasbourg Quarterfinal Predictions Including 
- `search_web({'query': 'WTA Strasbourg 2026 quarterfinals draw results'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] Zhang vs. Navarro | Quarterfinals Internationaux d

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*