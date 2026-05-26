# Market Analysis — 2026-05-20 09:49 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $697,227
- **Liquidity:** $75,643

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,428 (+0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,428 (+0.9% 24h) → neutral
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
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.15

### Reasoning
Statistical signal suggests YES is overpriced (57% market vs 44.7% historical resolution at this price, n=13,967), implying ~12% edge for NO. However: (1) gap is only 3%, below the 5% gate threshold; (2) pattern data shows 50-60% entry range has only 33% WR from 9 trades; (3) Paul won Houston 2026 clay title (good form), Etcheverry is a clay specialist — match could go either way; (4) no specific news/injury/catalyst found; (5) previous decisions on identical market were both SKIP. Strong stat edge exists but gap too small and historical pattern at this entry range is weak. Wait for better price or catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Tommy Paul'})` → No injury data found for tennis Tommy Paul
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg European Open 2025 odds'})` → [Mon, 18 May 2026] Google News
[Fri, 03 Apr 2026] Hamburg Open 2026: Ben Shelton falls to Germany's 
- `search_web({'query': 'Tommy Paul recent form ATP 2025 results'})` → [Thu, 21 Aug 2025] Google News
[Thu, 21 Aug 2025] US Open 2025: Laver Cup Form Guide - Laver Cup
[Mo
- `get_market_context({'keyword': 'Hamburg European Open tennis'})` → No related markets found for 'Hamburg European Open tennis'
- `get_odds({'sport': 'tennis_atp', 'team': 'Paul Etcheverry'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Tommy Paul vs Etcheverry Hamburg Open 2025 predictions head to head'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] PREDICTION, PREVIEW, H2H: Tiafoe, Paul, De Minaur 
- `search_web({'query': 'Tomas Etcheverry ATP ranking form clay court 2025'})` → [Sun, 12 Apr 2026] Google News
[Tue, 07 Apr 2026] What the Barcelona Open could reveal about Jack Dr
- `get_market_context({'keyword': 'Tommy Paul tennis'})` → No related markets found for 'Tommy Paul tennis'
- `search_web({'query': '"Tommy Paul" "Etcheverry" Hamburg 2026 match preview prediction'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] ATP Hamburg Best Bets Including Ben Shelton vs Dan
- `search_web({'query': 'Tommy Paul clay court record 2025 2026'})` → [Tue, 31 Mar 2026] Google News
[Sun, 05 Apr 2026] Tommy Paul, “a week-to-week kind of guy,” moves pa
- `search_web({'query': 'Hamburg Open 2026 Tommy Paul results draw'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] Hamburg Open 2026: Results, Draw, Schedule, Entry 
- `search_web({'query': 'Etcheverry Hamburg Open 2026 clay form'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] What is the Hamburg tennis schedule? - ATP Tour
[T
- `search_web({'query': 'Paul Etcheverry head to head record tennis'})` → [Fri, 03 Apr 2026] Google News
[Mon, 23 Mar 2026] ATP Houston Quarterfinal Predictions Including Fra
- `search_web({'query': '"Tommy Paul" 2026 season results ranking'})` → [Mon, 06 Apr 2026] Google News
[Thu, 26 Mar 2026] “It's one none of the Americans want to miss”: Tom
- `search_web({'query': 'Tommy Paul Hamburg 2026 clay court form match result'})` → [Mon, 18 May 2026] Google News
[Tue, 19 May 2026] What were the Hamburg tennis results? - ATP Tour
[
- `search_web({'query': 'Etcheverry clay court specialist form 2026'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] ATP Hamburg Best Bets Including Ben Shelton vs Dan
- `search_web({'query': 'site:tennisnerd.com Paul Etcheverry Houston quarterfinal'})` → No search results for: site:tennisnerd.com Paul Etcheverry Houston quarterfinal
- `search_web({'query': 'Tomas Etcheverry clay court 2026 ranking results form'})` → [Tue, 07 Apr 2026] Google News
[Sun, 12 Apr 2026] Monte-Carlo Masters: Carlos Alcaraz and Jannik Sin

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*