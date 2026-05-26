# Market Analysis — 2026-05-20 09:09 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $680,486
- **Liquidity:** $121,379

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,370 (+0.5% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,370 (+0.5% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → ECB rate cut → EUR weakens vs USD → EUR/USD falls
- → EU GDP beats expectations → EUR strengthens
- → EU political crisis (elections) → EUR uncertainty → falls
- → EUR/USD above 1.10 → European exports competitive → EU stocks rally

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: hamburg european open: tommy paul
- [Bing News]
- [Fri, 15 May 2026] hamburg european open: tommy paul
- → Hamburg Open 2026 (ATP 500): stacked clay-field before Roland Garros. Defending champ Flavio Cobolli, Zverev, Auger-Aliassime, Shelton, Fonseca, Men
- [] Hamburg Open 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 60%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal shows markets at 55% YES historically resolve YES only 44.7% of time (n=13,967), suggesting ~10% overpricing of YES. However, the gap is only +2% (below 5% threshold), the 50-60% entry pattern shows weak 33% WR from 9 trades, and no concrete catalyst or injury news found. Past decisions also rejected this trade. While crowd_bias is present, the small edge and poor entry-level pattern performance make this a skip.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Tommy Paul'})` → No injury data found for tennis Tommy Paul
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp_italian_open'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg European Open 2025 head to head form'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Tommy Paul injury status Hamburg 2025'})` → [Sun, 17 May 2026] Google News
[Thu, 23 Oct 2025] ATP tennis Hamburg and Geneva previews, picks, and
- `get_market_context({'keyword': 'Hamburg European Open Tommy Paul'})` → No related markets found for 'Hamburg European Open Tommy Paul'
- `search_web({'query': 'Tommy Paul tennis form 2026 recent results'})` → [Sun, 17 May 2026] Google News
[Tue, 10 Mar 2026] ATP Hamburg Day 1 Predictions Including Tommy Paul
- `search_web({'query': 'Tomas Etcheverry tennis form 2026 recent results Hamburg'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Altmaier tops Shelton for Hamburg QF spot: 'It's a
- `get_market_context({'keyword': 'Etcheverry Hamburg'})` → No related markets found for 'Etcheverry Hamburg'
- `search_web({'query': '"Tommy Paul" "Tomas Etcheverry" 2026 head to head'})` → [Sat, 09 May 2026] Google News
[Tue, 07 Apr 2026] Tommy Paul 1 - 2 Luciano Darderi (05/10) - Match R
- `search_web({'query': 'Hamburg European Open 2026 draw Tommy Paul Etcheverry'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] What is the Hamburg tennis schedule? - ATP Tour
[T
- `search_web({'query': 'Tommy Paul results May 2026 tennis'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] What were the Hamburg tennis results? - ATP Tour
[
- `search_web({'query': 'Tomas Etcheverry results May 2026 tennis'})` → [Mon, 04 May 2026] Google News
[Thu, 12 Feb 2026] Tennis 2026 schedule, Grand Slam dates and tournam

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*