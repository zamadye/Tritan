# Market Analysis — 2026-05-20 12:55 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 59.0%
- **Days Left:** 6
- **Volume 24h:** $711,607
- **Liquidity:** $22,600

## Statistical Prior
- **p_base:** 63.3%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,474 (+0.8% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,474 (+0.8% 24h) → neutral
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
- **Confidence:** 65%
- **p_true:** 63.3%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Stat signal is very strong (n=13,967) showing YES at 59% resolves only 44.7% historically — market overprices Paul. However, gate FAILS: gap of +4% is below 5% threshold. Paul won Houston clay title recently (good form), but Etcheverry is Argentine with natural clay advantage. Pattern data shows 50-60% entries have only 33% WR (weak zone). Third consecutive SKIP — same market with consistent analysis. No breaking news or direct catalyst to change assessment.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_sports_data({'sport': 'nba', 'team': 'Tommy Paul'})` → No injury data found for nba Tommy Paul
- `search_web({'query': 'Tommy Paul Tomas Etcheverry Hamburg European Open 2025 head to head'})` → [Mon, 18 May 2026] Google News
[Fri, 19 Jul 2019] Hamburg Open 2026: Ben Shelton falls to Germany's 
- `search_web({'query': 'Tommy Paul recent form tennis 2025'})` → [Sun, 31 Aug 2025] Google News
[Thu, 28 Aug 2025] Tennis, ATP – US Open 2025: Bublik beats Paul - te
- `search_web({'query': 'Tomas Etcheverry recent results tennis 2025'})` → [Sat, 04 Oct 2025] Google News
[Sun, 14 Sep 2025] Holger Rune - Tomas Martin Etcheverry 2:1 - Flashs
- `get_market_context({'keyword': 'Tommy Paul Etcheverry Hamburg tennis'})` → No related markets found for 'Tommy Paul Etcheverry Hamburg tennis'
- `search_web({'query': 'Hamburg European Open 2026 Tommy Paul Tomas Etcheverry quarterfinal'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] Hamburg Open 2026: Ben Shelton falls to Germany's 
- `search_web({'query': 'Tommy Paul form 2026 clay court season results'})` → [Mon, 18 May 2026] Google News
[Sat, 04 Apr 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Tomas Etcheverry form 2026 clay results'})` → [Mon, 18 May 2026] Google News
[Thu, 09 Apr 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `get_market_context({'keyword': 'Hamburg European Open tennis'})` → No related markets found for 'Hamburg European Open tennis'
- `search_web({'query': '"Tommy Paul" vs "Tomas Etcheverry" Hamburg 2026'})` → [Tue, 19 May 2026] Google News
[Wed, 22 Apr 2026] Tommy Paul vs. Tomas Martin Etcheverry prediction,
- `search_web({'query': 'Tommy Paul clay court ranking 2026 ATP'})` → [Mon, 06 Apr 2026] Google News
[Sat, 04 Apr 2026] Tommy Paul saves 3 championship points to win firs
- `get_market_context({'keyword': 'ATP Hamburg tennis prediction'})` → No related markets found for 'ATP Hamburg tennis prediction'
- `search_web({'query': 'dimers.com Tommy Paul Etcheverry Hamburg Open 2026 prediction odds'})` → [Tue, 19 May 2026] Google News
[Sun, 17 May 2026] Tommy Paul vs. Tomas Martin Etcheverry prediction,
- `search_web({'query': 'Tommy Paul Hamburg Open 2026 results round'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Altmaier tops Shelton for Hamburg QF spot: 'It's a
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg 2026 odds head to head betting preview'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Etcheverry Hamburg 2026 round 2 match'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] ATP Hamburg Day 2 Predictions Including Marcos Gir

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*