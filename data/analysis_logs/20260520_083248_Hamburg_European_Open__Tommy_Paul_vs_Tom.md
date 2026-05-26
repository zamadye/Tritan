# Market Analysis — 2026-05-20 08:32 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $680,355
- **Liquidity:** $132,011

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: ? | trend: ?
- BTC: $77,178 (+0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,178 (+0.2% 24h) → neutral
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
- **Confidence:** 58%
- **p_true:** 59.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.60

### Reasoning
Strong statistical signal (n=13,967) suggests YES is overpriced at 56% — historical resolution rate at this price is only 44.7%, implying ~11% edge on NO. However, SKIP because: (1) gap of +3% is below the 5% gate threshold required for action, (2) entry range 50-60% shows historically weak 38% WR from 8 trades, (3) no direct catalyst found — Tommy Paul won Houston clay title in April (good form) but no injury/concern news on either player, (4) both previous decisions on this exact market were SKIP for same reason. Paul's recent clay success (first ATP clay title) may support his 56% pricing more than the stat signal suggests. Need either a wider gap or concrete injury/form info to act.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Tommy Paul Hamburg European Open 2025 results form'})` → [Mon, 04 May 2026] Google News
[Fri, 24 Oct 2025] Tennis 2026 schedule, Grand Slam dates and tournam
- `search_web({'query': 'Tomas Etcheverry Hamburg European Open 2025 results form'})` → [Mon, 04 May 2026] Google News
[Sun, 20 Jul 2025] Tennis 2026 schedule, Grand Slam dates and tournam
- `get_market_context({'keyword': 'Hamburg European Open tennis'})` → No related markets found for 'Hamburg European Open tennis'
- `search_web({'query': 'Tommy Paul tennis injury 2025 foot problem withdrawal'})` → [Fri, 24 Oct 2025] Google News
[Wed, 08 Oct 2025] Tommy Paul abruptly ends 2025 season after withdra
- `search_web({'query': 'Tomas Etcheverry tennis 2025 clay court results'})` → [Sat, 16 May 2026] Google News
[Tue, 07 Apr 2026] Jack Draper tennis results, next match, news, rank
- `get_sports_data({'sport': 'nba', 'team': 'Tommy Paul'})` → No injury data found for nba Tommy Paul
- `search_web({'query': '"Tommy Paul" "Etcheverry" Hamburg 2026 odds prediction'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] ATP Hamburg Best Bets Including Ben Shelton vs Dan
- `search_web({'query': '"Tommy Paul" tennis 2026 results form clay'})` → [Sun, 17 May 2026] Google News
[Sat, 04 Apr 2026] ATP Hamburg Day 1 Predictions Including Tommy Paul
- `get_market_context({'keyword': 'Tommy Paul Etcheverry'})` → No related markets found for 'Tommy Paul Etcheverry'
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg 2026 prediction odds'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Tommy Paul vs. Tomas Martin Etcheverry prediction,
- `search_web({'query': 'Tomas Etcheverry 2026 season results ranking clay'})` → [Sat, 16 May 2026] Google News
[Wed, 20 May 2026] Jack Draper - latest news and results - Sky Sports
- `search_web({'query': 'Tommy Paul Hamburg Open 2026 round result score'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Altmaier tops Shelton for Hamburg QF spot: 'It's a
- `search_web({'query': 'Etcheverry Hamburg Open 2026 first round result'})` → [Sat, 16 May 2026] Google News
[Tue, 19 May 2026] Jack Draper - latest news and results - Sky Sports

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*