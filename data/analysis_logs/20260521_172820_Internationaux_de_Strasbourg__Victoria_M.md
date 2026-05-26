# Market Analysis — 2026-05-21 17:28 UTC

## Market
- **Question:** Internationaux de Strasbourg: Victoria Mboko vs Leylah Fernandez
- **Category:** sports
- **YES Price:** 84.0%
- **Days Left:** 6
- **Volume 24h:** $146,725
- **Liquidity:** $87,928

## Statistical Prior
- **p_base:** 92.3%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 8.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,682 (+0.3% 24h) → neutral
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
- **Confidence:** 48%
- **p_true:** 92.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** FORM_INDIRECT
- **Catalyst Strength:** 0.35

### Reasoning
Market at 84% is 8% below 92% base rate, but no concrete evidence supports value. Fernandez's poor 2026 form is indirect signal. No H2H data, no bookmaker odds, no injury reports found. Previous similar markets were skipped due to insufficient evidence. The 92% base rate may be inflated for a WTA QF on clay - market may be accurately priced.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 48%<52%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Fernandez Mboko Strasbourg'})` → No injury data found for tennis Fernandez Mboko Strasbourg
- `get_odds({'sport': 'tennis_atp', 'team': 'Fernandez Mboko'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Strasbourg tennis Mboko Fernandez'})` → No related markets found for 'Strasbourg tennis Mboko Fernandez'
- `search_web({'query': 'Victoria Mboko vs Leylah Fernandez Strasbourg 2025 head to head prediction'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Victoria Mboko vs. Leylah Fernandez: Predictions, 
- `search_web({'query': 'Internationaux de Strasbourg 2025 draw results Mboko Fernandez'})` → [Tue, 19 May 2026] Google News
[Thu, 21 May 2026] Mboko, Fernandez set all-Canadian quarterfinal mee
- `search_web({'query': 'Victoria Mboko Leylah Fernandez Strasbourg quarterfinal 2026 prediction odds'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Victoria Mboko vs Leylah Fernandez Preview: Head-t
- `search_web({'query': 'Leylah Fernandez form 2026 WTA results recent matches'})` → [Tue, 19 May 2026] Google News
[Sun, 17 May 2026] Mboko, Fernandez set all-Canadian quarterfinal mee
- `search_web({'query': '"Leylah Fernandez" "2026" ranking form results clay court'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Emma Raducanu: British No 1 in line to face Diane 
- `search_web({'query': '"Victoria Mboko" 2026 clay court results form rising'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Mboko, Fernandez set all-Canadian quarterfinal mee
- `search_web({'query': 'Victoria Mboko vs Leylah Fernandez head to head record wins losses'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] [UPDATED QF]. Prediction, H2H of Victoria Mboko’s 
- `search_web({'query': 'Leylah Fernandez WTA ranking 2026 recent form'})` → [Sun, 17 May 2026] Google News
[Fri, 16 Jan 2026] WTA Strasbourg Day 1 Predictions Including Leolia 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*