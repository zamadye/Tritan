# Market Analysis — 2026-05-21 14:36 UTC

## Market
- **Question:** Internationaux de Strasbourg: Shuai Zhang vs Emma Navarro
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 6
- **Volume 24h:** $183,974
- **Liquidity:** $75,345

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,028 (-0.5% 24h) → neutral
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
- **Confidence:** 52%
- **p_true:** 56.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.15

### Reasoning
Multiple factors prevent a profitable bet: (1) Gap of only +2% (market 54% vs base 56%) fails the 5% gate threshold; (2) Stat signal suggests YES overpricing (44.7% historical resolution vs 54% price), but no concrete evidence to exploit this; (3) Entry zone 50-60% has weak 38% WR from 16 trades - historically poor zone; (4) Two prior analyses of this exact same market concluded SKIP at 48% confidence; (5) Search revealed no injury news, form changes, or head-to-head insights to create an information edge; (6) No catalyst within 6-day window identified. While crowd may slightly overprice YES, the gap is too narrow and entry zone too weak to justify a bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Zhang'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_sports_data({'sport': 'tennis', 'team': 'Navarro'})` → No injury data found for tennis Navarro
- `search_web({'query': 'Shuai Zhang vs Emma Navarro Internationaux de Strasbourg 2025'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Internationaux de Strasbourg presented by Mammotio
- `search_web({'query': 'Emma Navarro recent form 2025 tennis results'})` → [Wed, 04 Feb 2026] Google News
[Wed, 20 Aug 2025] Emma Navarro fans should be worried after her star
- `search_web({'query': 'Zhang Shuai Emma Navarro tennis match 2025 head to head'})` → [Wed, 20 May 2026] Google News
[Thu, 26 Feb 2026] Internationaux de Strasbourg presented by Mammotio
- `get_market_context({'keyword': 'tennis Zhang Navarro Strasbourg'})` → No related markets found for 'tennis Zhang Navarro Strasbourg'
- `search_web({'query': 'Shuai Zhang WTA ranking 2025 form results'})` → [Sat, 31 Jan 2026] Google News
[Fri, 09 Jan 2026] Reunited and it feels so good! Mertens and Zhang w
- `search_web({'query': 'Internationaux de Strasbourg 2025 draw tennis'})` → [Wed, 20 May 2026] Google News
[Thu, 09 Oct 2025] The Official Home of the Women's Tennis Associatio
- `search_web({'query': 'Emma Navarro 2025 WTA ranking win loss record clay'})` → [Thu, 12 Mar 2026] Google News
[Wed, 20 May 2026] Alexandra Eala and Emma Raducanu confirm their fir
- `search_web({'query': 'Zhang Shuai 2025 clay court form WTA'})` → [Tue, 19 May 2026] Google News
[Thu, 16 Apr 2026] WTA Strasbourg Day 4 Predictions Including Emma Na
- `get_market_context({'keyword': 'Internationaux Strasbourg tennis'})` → No related markets found for 'Internationaux Strasbourg tennis'

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*