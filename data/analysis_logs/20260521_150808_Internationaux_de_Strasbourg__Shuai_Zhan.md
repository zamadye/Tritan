# Market Analysis — 2026-05-21 15:08 UTC

## Market
- **Question:** Internationaux de Strasbourg: Shuai Zhang vs Emma Navarro
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 6
- **Volume 24h:** $278,128
- **Liquidity:** $48,181

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $76,959 (-0.4% 24h) → neutral
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
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.7%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.78

### Reasoning
Strong statistical edge: Markets at 58% YES historically resolve YES only 44.7% of the time (n=13,967), indicating market systematically overprices YES at this level. This creates ~13.3% edge on NO (true NO prob ~55.3% vs market NO price 42%). No specific injury or form news found for either player, suggesting market inefficiency is driven by general overpricing pattern rather than new information. Sports trading pattern shows strong 77% WR from 31 trades. Confidence limited to 0.72 due to lack of match-specific catalyst, but statistical pattern with large sample size provides reliable edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Zhang'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_sports_data({'sport': 'nba', 'team': 'Zhang'})` → No injury data found for nba Zhang
- `search_web({'query': 'Shuai Zhang vs Emma Navarro Internationaux de Strasbourg 2025 tennis prediction'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Internationaux de Strasbourg 2026: Results, Draw, 
- `search_web({'query': 'Emma Navarro recent form 2025 clay court results'})` → [Sun, 17 May 2026] Google News
[Thu, 09 Apr 2026] WTA Strasbourg Day 1 Predictions Including Sara Be
- `get_market_context({'keyword': 'Strasbourg tennis Zhang Navarro'})` → No related markets found for 'Strasbourg tennis Zhang Navarro'
- `search_web({'query': 'Emma Navarro 2025 season results clay court ranking'})` → [Wed, 20 May 2026] Google News
[Tue, 03 Mar 2026] The Official Home of the Women's Tennis Associatio
- `search_web({'query': 'Shuai Zhang 2025 season results form WTA ranking'})` → [Thu, 21 May 2026] Google News
[Sat, 31 Jan 2026] Wang Xinyu leads Chinese charge into French Open a
- `search_web({'query': '"Emma Navarro" injury 2025 clay court Strasbourg'})` → [Sun, 17 May 2026] Google News
[Tue, 24 Mar 2026] Injured Madison Keys retires from WTA 125 Paris Ch
- `search_web({'query': '"Shuai Zhang" injury 2025 Strasbourg form'})` → [Mon, 06 Oct 2025] Google News
[Sun, 17 May 2026] China Open champion Anisimova pulls out of Wuhan, 

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*