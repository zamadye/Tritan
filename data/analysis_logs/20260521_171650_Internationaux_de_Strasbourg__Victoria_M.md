# Market Analysis — 2026-05-21 17:16 UTC

## Market
- **Question:** Internationaux de Strasbourg: Victoria Mboko vs Leylah Fernandez
- **Category:** sports
- **YES Price:** 79.0%
- **Days Left:** 6
- **Volume 24h:** $119,555
- **Liquidity:** $80,474

## Statistical Prior
- **p_base:** 87.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,163 (-0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,355 (+0.1% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: victoria mboko leylah
- [Bing News]
- [Thu, 21 May 2026] internationaux strasbourg: victoria mboko leylah
- → Victoria Mboko and Leylah Fernandez will battle it out in the Strasbourg Open quarterfinals on Thursday in what will be an all-Canadian showdown. Mb
- [Fri, 15 May 2026] Victoria Mboko vs Leylah Fernandez Preview: Head-to-Head, Prediction for Strasbourg Open 2026
- → The Internationaux de Strasbourg takes place between 17-23 May in a WTA 500 tournament prior to the French Open. Elena Rybakina is defending champio
- [Fri, 15 May 2026] Internationaux de Strasbourg 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- → The sponsors of the Internationaux de Strasbourg have made a financial commitment of $1,206,446 for the 2026 edition of the tournament.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 87.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market at 79% is 9% below base rate of 88%, suggesting potential value on YES. However, historical pattern shows 29% win rate for 70-80% entry range (WEAK). No concrete catalyst or breaking news found for this specific match. Mboko appears stronger (breaking into Top 10) but insufficient verifiable edge for confident bet given poor historical performance in this betting range.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Mboko Fernandez'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Victoria Mboko vs Leylah Fernandez Internationaux de Strasbourg 2025'})` → [Thu, 21 May 2026] Google News
[Mon, 11 May 2026] Victoria Mboko vs. Leylah Fernandez: Predictions, 
- `search_web({'query': "Internationaux de Strasbourg 2025 women's singles draw Mboko Fernandez"})` → [Thu, 09 Oct 2025] Google News
[Sat, 01 Nov 2025] Internationaux de Strasbourg presented by Mammotio
- `search_web({'query': 'Leylah Fernandez recent form 2025 results WTA ranking'})` → [Sun, 27 Jul 2025] Google News
[Fri, 16 Jan 2026] Fernandez storms to Washington crown for fourth ca
- `search_web({'query': 'Victoria Mboko recent results 2025 WTA ranking'})` → [Sun, 02 Nov 2025] Google News
[Sat, 03 Jan 2026] Tennis: Victoria Mboko triumphs in Hong Kong, defe
- `search_web({'query': 'Internationaux de Strasbourg 2025 May results schedule'})` → [Thu, 21 May 2026] Google News
[Tue, 18 Nov 2025] Internationaux de Strasbourg 2026: Results, Draw, 
- `search_web({'query': 'WTA Strasbourg 2025 Mboko Fernandez match'})` → [Tue, 19 May 2026] Google News
[Thu, 21 May 2026] Mboko, Fernandez set all-Canadian quarterfinal mee
- `get_sports_data({'sport': 'tennis', 'team': 'Mboko'})` → No injury data found for tennis Mboko
- `get_sports_data({'sport': 'tennis', 'team': 'Fernandez'})` → No injury data found for tennis Fernandez
- `get_market_context({'keyword': 'Internationaux de Strasbourg'})` → No related markets found for 'Internationaux de Strasbourg'
- `get_market_context({'keyword': 'Mboko Fernandez tennis'})` → No related markets found for 'Mboko Fernandez tennis'
- `search_web({'query': 'Victoria Mboko WTA ranking May 2025'})` → [Mon, 16 Feb 2026] Google News
[Fri, 13 Feb 2026] Rankings Watch: Mboko makes Top 10 debut, Muchova 
- `search_web({'query': 'Leylah Fernandez WTA ranking May 2025'})` → [Mon, 22 Dec 2025] Google News
[Tue, 04 Nov 2025] At 5'5", Leylah Fernandez stood tall through late-

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*