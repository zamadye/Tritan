# Market Analysis — 2026-05-21 14:19 UTC

## Market
- **Question:** Internationaux de Strasbourg: Shuai Zhang vs Emma Navarro
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 6
- **Volume 24h:** $151,384
- **Liquidity:** $54,670

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $76,919 (-0.6% 24h) → neutral
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
- **Confidence:** 48%
- **p_true:** 54.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.15

### Reasoning
Market at 53% YES with only +1% gap from base rate (54%) fails the 5% gate threshold. Stat signal strongly indicates market overprices YES (historical 53% markets resolve YES only 44.7% of time, n=13,967). While Zhang shows clay form (beat Parry, into QF) and Navarro has struggled in 2026, this information appears partially priced in. Previous decisions on identical market correctly SKIPped for similar reasons. No verifiable edge exists—confidence below 55% threshold for actionable bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Zhang Navarro'})` → No injury data found for tennis Zhang Navarro
- `get_odds({'sport': 'tennis_atp', 'team': 'Zhang Navarro Strasbourg'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Strasbourg tennis Zhang Navarro'})` → No related markets found for 'Strasbourg tennis Zhang Navarro'
- `search_web({'query': 'Shuai Zhang vs Emma Navarro Strasbourg 2025 tennis match preview'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Internationaux de Strasbourg presented by Mammotio
- `search_web({'query': 'Emma Navarro Shuai Zhang WTA Strasbourg odds head to head'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] H2H, prediction of Emma Navarro vs Shuai Zhang in 
- `search_web({'query': '"Emma Navarro" "Shuai Zhang" Strasbourg 2026 prediction preview head to head'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] WTA Strasbourg Quarterfinal Predictions Including 
- `search_web({'query': 'Emma Navarro form 2026 WTA results recent'})` → [Sun, 17 May 2026] Google News
[Wed, 04 Feb 2026] WTA Strasbourg Day 1 Predictions Including Sara Be
- `search_web({'query': 'Shuai Zhang form 2026 WTA results recent'})` → [Wed, 20 May 2026] Google News
[Sat, 31 Jan 2026] WTA Strasbourg Quarterfinal Predictions Including 
- `search_web({'query': 'site:tennistonic.com Emma Navarro Shuai Zhang Strasbourg 2026 prediction odds'})` → [Wed, 21 Nov 2012] Google News
[Fri, 24 Aug 2018] HOME - Tennis Tonic - News, Predictions, H2H, Live
- `search_web({'query': 'Emma Navarro 2026 season results WTA rankings'})` → [Wed, 20 May 2026] Google News
[Fri, 27 Feb 2026] The Official Home of the Women's Tennis Associatio
- `search_web({'query': '"Internationaux de Strasbourg 2026" draw results Zhang Navarro'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Internationaux de Strasbourg 2026: Results, Draw, 
- `search_web({'query': 'Emma Navarro tennis 2026 form struggles ranking'})` → [Sun, 08 Mar 2026] Google News
[Thu, 26 Mar 2026] Emma Navarro has a clear issue which is causing he
- `search_web({'query': 'Shuai Zhang WTA 2026 results ranking form clay'})` → [Wed, 20 May 2026] Google News
[Sat, 02 May 2026] Shuai Zhang Matches | Past Tournaments &amp; More 
- `search_web({'query': '"Emma Navarro" "2026" season results wins losses'})` → [Sun, 04 Jan 2026] Google News
[Tue, 06 Jan 2026] Emma Navarro 2025 Season Recap - Last Word On Spor
- `search_web({'query': 'Emma Navarro Shuai Zhang head to head record tennis'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] WTA Strasbourg Quarterfinal Predictions Including 
- `search_web({'query': 'Shuai Zhang clay court 2026 Strasbourg form'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Zhang bests Parry in Strasbourg; into first clay q

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*