# Market Analysis — 2026-05-21 14:53 UTC

## Market
- **Question:** Internationaux de Strasbourg: Shuai Zhang vs Emma Navarro
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 6
- **Volume 24h:** $241,382
- **Liquidity:** $46,545

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $76,836 (-0.8% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,028 (-0.5% 24h) → neutral
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
- **p_true:** 53.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market at 52% with only +1% gap from base rate (53%) fails the 5% gate threshold. No concrete catalyst or information edge identified. Stat signal suggests slight overpricing of YES but insufficient for profitable bet. Pattern shows 38% WR for 50-60% entries.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Navarro'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Zhang Navarro tennis Strasbourg'})` → No related markets found for 'Zhang Navarro tennis Strasbourg'
- `search_web({'query': 'Shuai Zhang vs Emma Navarro Internationaux de Strasbourg 2025 odds preview'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] H2H, prediction of Emma Navarro vs Shuai Zhang in 
- `search_web({'query': 'Emma Navarro Shuai Zhang head to head record 2025 2026'})` → [Tue, 19 May 2026] Google News
[Thu, 21 May 2026] WTA Strasbourg Day 4 Predictions Including Emma Na
- `search_web({'query': 'Emma Navarro current form ranking 2026'})` → [Sun, 08 Mar 2026] Google News
[Mon, 05 Jan 2026] Emma Navarro has a clear issue which is causing he
- `get_sports_data({'sport': 'tennis', 'team': 'Navarro'})` → No injury data found for tennis Navarro
- `search_web({'query': 'Tennis Tonic Emma Navarro vs Shuai Zhang Strasbourg 2026 prediction pick'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] H2H, prediction of Emma Navarro vs Shuai Zhang in 
- `search_web({'query': 'Shuai Zhang form 2026 ranking WTA'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Shuai Zhang Matches | Past Tournaments &amp; More 
- `search_web({'query': '"Emma Navarro" "Shuai Zhang" odds prediction Strasbourg May 2026'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] WTA Strasbourg Best Bets Including Emma Navarro vs
- `search_web({'query': 'Navarro poor form 2026 results clay court'})` → [Wed, 20 May 2026] Google News
[Thu, 26 Mar 2026] The Official Home of the Women's Tennis Associatio

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*