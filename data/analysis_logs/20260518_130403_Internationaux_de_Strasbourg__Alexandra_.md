# Market Analysis — 2026-05-18 13:04 UTC

## Market
- **Question:** Internationaux de Strasbourg: Alexandra Eala vs Oleksandra Oliynykova
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $110,425
- **Liquidity:** $119,975

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,574 (-1.0% 24h) → neutral
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $77,574 (-1.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: alexandra eala oleksandra
- [Bing News]
- [Sun, 17 May 2026] internationaux strasbourg: alexandra eala oleksandra
- → ALEX Eala drew Ukraine’s Oleksandra Oliynykova in the opening round of the WTA 500 Internationaux de Strasbourg - her fifth tournament of the clay s
- [Sun, 17 May 2026] Eala draws world No. 68 Oliynykova in final French Open tuneup
- → Filipina tennis star Alex Eala will play Ukraine's Oleksandra Oliynykova in the first round of the Internationaux de Strasbourg, a WTA 500 tournamen
- [Sun, 17 May 2026] Tennis: Alex Eala to play Ukraine's Oliynykova in first round of Strasbourg Open
- → MANILA, Philippines — Alex Eala begins her campaign at the Internationaux de Strasbourg with a first-round clash against Ukrainian qualifier Oleksan

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 54.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MISPRICING
- **Catalyst Strength:** 0.60

### Reasoning
Strong statistical signal: markets at 56% historically resolve YES only 44.7% of the time (n=13,967), indicating YES is overpriced by 11.3 percentage points. While base rate (59%) suggests slight underpricing, the stat signal's larger sample and direct calibration to this price level is more reliable. Eala (WTA #38) is the clear favorite against lower-ranked Oliynykova, but the crowd appears to be overvaluing her win probability. Entry in 50-60% range has historically shown poor performance (WR=25%). No direct injury or form catalyst identified, but the statistical edge is sufficient for a moderate-confidence NO bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `search_web({'query': 'Alexandra Eala vs Oleksandra Oliynykova Strasbourg 2025 odds'})` → [Mon, 15 Dec 2025] Google News
[Mon, 18 May 2026] Lee Victor, Iñigo Jose reveal Big Four bets for ‘P
- `search_web({'query': 'Alexandra Eala recent form injury 2025'})` → [Sun, 07 Sep 2025] Google News
[Tue, 28 Oct 2025] Biggest upsets of the 2025 US Open - US Open.org
[
- `get_odds({'sport': 'tennis_atp', 'team': 'Eala'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Strasbourg'})` → No related markets found for 'Strasbourg'
- `search_web({'query': 'Internationaux de Strasbourg 2026 Alexandra Eala Oleksandra Oliynykova prediction'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] WTA Strasbourg Day 2 Predictions Including Daria K
- `search_web({'query': 'Alexandra Eala WTA ranking 2026 recent results'})` → [Mon, 18 May 2026] Google News
[Fri, 24 Apr 2026] WTA Strasbourg Best Bets Including Marie Bouzkova 
- `get_market_context({'keyword': 'Eala'})` → No related markets found for 'Eala'
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Eala vs Oliynykova prediction odds Strasbourg 2026 Tennis Tonic'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] H2H, prediction of Alexandra Eala vs Oleksandra Ol
- `search_web({'query': 'Alexandra Eala form 2026 clay season results'})` → [Thu, 14 May 2026] Google News
[Wed, 13 May 2026] Italian Open 2026: Coco Gauff reaches back-to-back
- `search_web({'query': 'Alexandra Eala vs Oleksandra Oliynykova odds head to head'})` → [Mon, 18 May 2026] Google News
[Tue, 21 Apr 2026] WTA Strasbourg Best Bets Including Marie Bouzkova 
- `search_web({'query': 'Oleksandra Oliynykova WTA ranking 2026 form clay'})` → [Sun, 17 May 2026] Google News
[Wed, 22 Apr 2026] WTA Strasbourg Day 1 Predictions Including Sara Be
- `search_web({'query': 'Alexandra Eala WTA ranking May 2026'})` → [Mon, 18 May 2026] Google News
[Thu, 14 May 2026] Alex Eala rises to No. 38 in WTA rankings ahead of
- `search_web({'query': 'Oleksandra Oliynykova WTA ranking May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Ukrainian tennis players rise in WTA rankings afte
- `get_market_context({'keyword': 'tennis'})` → No related markets found for 'tennis'
- `search_web({'query': '"Oleksandra Oliynykova" WTA ranking 2026'})` → [Mon, 18 May 2026] Google News
[Fri, 08 May 2026] Who is Oleksandra Oliynykova? Alex Eala's Round of
- `search_web({'query': 'Alex Eala injury 2026 Strasbourg'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] WTA Strasbourg draw: Mboko and Fernandez clash on 
- `search_web({'query': 'Internationaux de Strasbourg 2026 draw results'})` → [Sat, 16 May 2026] Google News
[Mon, 18 May 2026] Internationaux de Strasbourg 2026: Draw, Schedule,
- `search_web({'query': 'Alex Eala results May 2026 WTA'})` → [Fri, 08 May 2026] Google News
[Sat, 16 May 2026] Italian Open 2026: Alexandra Eala advances past Wa
- `search_web({'query': 'Oleksandra Oliynykova results May 2026 WTA'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Yulia Putintseva vs Oleksandra Oliynykova: Scores,
- `search_web({'query': 'Oliynykova saves 21 break points Cluj-Napoca Raducanu'})` → [Thu, 05 Feb 2026] Google News
[Fri, 06 Feb 2026] Oliynykova saves 21 break points in Cluj-Napoca; t

## Outcome
**❌ LOSS** | P&L: $-1.00 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*