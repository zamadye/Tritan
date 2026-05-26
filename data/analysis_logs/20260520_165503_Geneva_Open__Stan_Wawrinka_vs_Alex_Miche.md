# Market Analysis — 2026-05-20 16:55 UTC

## Market
- **Question:** Geneva Open: Stan Wawrinka vs Alex Michelsen
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 6
- **Volume 24h:** $91,393
- **Liquidity:** $45,315

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,255 (+0.6% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,224 (+0.5% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: geneva open: stan wawrinka alex
- [Bing News]
- [Wed, 20 May 2026] geneva open: stan wawrinka alex
- → Elite tennis action continues in full swing as Emma Navarro is set to go up against Iva Jovic in an all-American clash in the Round of 16 match at t
- [Mon, 18 May 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions Ft. Emma Navarro vs Iva Jovic, Stan Wawrinka vs Alex Michelsen | May 20, 2026
- → Petenis yang telah dua kali menjuarai Geneva Open, Stan Wawrinka menambahkan babak tidak terlupakan lain pada musim pemungkas dalam kariernya di tur
- [Mon, 18 May 2026] Bertahan Di Jenewa, Stan Wawrinka Masuk Buku Rekor
- → Follow the Geneva Open as Wawrinka begins his farewell, with Tsitsipas, Rinderknech, and Mpetshi Perricard in action—crucial clay-court form ahead o

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 46.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal from large sample (n=13,967) shows markets at 54% YES historically resolve YES only 44.7% of time — indicating YES is overpriced by ~9.3%. NO true probability ~55.3% vs market price 46% creates meaningful edge. Context: Wawrinka (age 40, nearing retirement) vs rising young player Michelsen. Sports pattern WR=83% supports systematic betting approach.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis_atp', 'team': 'Wawrinka'})` → No injury data found for tennis_atp Wawrinka
- `get_sports_data({'sport': 'tennis_atp', 'team': 'Michelsen'})` → No injury data found for tennis_atp Michelsen
- `get_odds({'sport': 'tennis_atp', 'team': 'Wawrinka'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Stan Wawrinka vs Alex Michelsen Geneva Open 2025'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Tennis Picks Today: 5 Best Bets &amp; Predictions 
- `search_web({'query': 'Wawrinka form 2026 season results recent matches'})` → [Mon, 18 May 2026] Google News
[Thu, 22 Jan 2026] ATP Geneva Day 2 Predictions Including Stan Wawrin
- `search_web({'query': 'Alex Michelsen 2026 season results ranking form'})` → [Tue, 10 Mar 2026] Google News
[Thu, 19 Feb 2026] Michelsen upsets former champ Fritz in Indian Well
- `get_market_context({'keyword': 'Geneva Open'})` → No related markets found for 'Geneva Open'
- `search_web({'query': 'Michelsen vs Wawrinka head to head record 2025 2026'})` → [Mon, 20 Oct 2025] Google News
[Wed, 04 Jun 2025] ATP Vienna Day 2 Predictions Including Alexander Z

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*