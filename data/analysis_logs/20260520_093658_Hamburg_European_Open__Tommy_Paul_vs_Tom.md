# Market Analysis — 2026-05-20 09:36 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 6
- **Volume 24h:** $682,534
- **Liquidity:** $114,511

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,446 (+1.0% 24h) → neutral
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
- **Confidence:** 58%
- **p_true:** 57.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE_ONLY
- **Catalyst Strength:** 0.35

### Reasoning
Strong statistical signal (n=13,967) shows market overprices YES at 55% vs historical 44.7% resolution, but edge is small (2% gap < 5% gate), no concrete catalyst (injury/form/news) found, and past decisions for this exact market already SKIPPED. Pattern shows entry 50-60% has weak 33% WR. Insufficient verifiable edge for action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Tommy Paul'})` → No injury data found for tennis Tommy Paul
- `get_sports_data({'sport': 'tennis', 'team': 'Tomas Etcheverry'})` → No injury data found for tennis Tomas Etcheverry
- `search_web({'query': 'Tommy Paul Tomas Etcheverry Hamburg European Open 2025 head to head'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Hamburg Open 2026: Ben Shelton falls to Germany's 
- `search_web({'query': 'Tommy Paul Hamburg Open 2025 form results clay court'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `get_market_context({'keyword': 'Hamburg European Open Tommy Paul'})` → No related markets found for 'Hamburg European Open Tommy Paul'
- `search_web({'query': '"Tommy Paul" vs "Etcheverry" 2025 odds prediction'})` → [Fri, 03 Apr 2026] Google News
[Wed, 21 Jan 2026] ATP Houston QF Predictions and Odds, Paul vs Etche
- `search_web({'query': 'Hamburg Open 2025 results Tommy Paul Tomas Etcheverry tennis'})` → [Mon, 18 May 2026] Google News
[Fri, 09 Dec 2022] ATP Hamburg Day 3 Predictions Including Felix Auge

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*