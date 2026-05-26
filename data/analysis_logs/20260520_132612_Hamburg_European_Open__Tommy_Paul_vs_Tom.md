# Market Analysis — 2026-05-20 13:26 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 6
- **Volume 24h:** $877,686
- **Liquidity:** $131,142

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,407 (+0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,407 (+0.9% 24h) → neutral
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
- **Confidence:** 62%
- **p_true:** 54.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Statistical signal confirms YES overpricing (44.7% vs 53%), but the 1% gap is below the 5% threshold needed for reliable edge. Past decisions for this exact market already skipped. Tommy Paul has decent clay form (Houston final), but no concrete evidence tips the balance. Entry zone 50-60% historically has poor 33% win rate.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Hamburg European Open 2025 Tommy Paul Tomas Etcheverry'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] Sports News, Transfers, Scores | Watch Live Sport 
- `search_web({'query': 'Tommy Paul Hamburg Open 2025 form injury'})` → [Sun, 17 May 2026] Google News
[Wed, 22 Apr 2026] ATP tennis Hamburg and Geneva previews, picks, and
- `get_market_context({'keyword': 'Hamburg European Open tennis'})` → No related markets found for 'Hamburg European Open tennis'
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Tommy Paul injury foot 2026 form results'})` → [Wed, 21 Jan 2026] Google News
[Sat, 21 Feb 2026] Tommy Paul confirms if he's still feeling any pain
- `search_web({'query': 'Tomas Etcheverry 2026 results form clay'})` → [Mon, 18 May 2026] Google News
[Thu, 09 Apr 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `get_market_context({'keyword': 'Tommy Paul'})` → No related markets found for 'Tommy Paul'
- `search_web({'query': '"Tommy Paul" vs "Etcheverry" Hamburg 2026 head to head'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'ATP Hamburg European Open 2026 results scores May'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Hamburg Open 2026: All matches, live scores and ho
- `search_web({'query': 'Paul vs Etcheverry prediction H2H Hamburg 2026 tennis odds'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] ATP Hamburg Best Bets Including Ben Shelton vs Dan
- `search_web({'query': 'Tommy Paul clay court 2026 season results'})` → [Sat, 04 Apr 2026] Google News
[Sun, 05 Apr 2026] Paul survives Tiafoe &amp; rain, reaches first ATP

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*