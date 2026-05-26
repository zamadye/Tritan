# Market Analysis — 2026-05-20 08:12 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $652,340
- **Liquidity:** $132,589

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,188 (+0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,298 (+0.1% 24h) → neutral
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
- **Confidence:** 52%
- **p_true:** 59.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN_ONLY
- **Catalyst Strength:** 0.40

### Reasoning
While the statistical signal (n=13,967) suggests YES is overpriced at 56% vs 44.7% historical resolution — implying a NO edge — no new catalyst, injury news, or form information was found to act on. The gap vs base rate is only +3% (<5% gate). Entry 50-60% bucket historically has poor 38% WR. Two prior SKIP decisions on this exact market reached the same conclusion. Without an information edge beyond the statistical pattern, risk/reward doesn't justify a bet with 6 days remaining.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_sports_data({'sport': 'tennis', 'team': 'Tommy Paul'})` → No injury data found for tennis Tommy Paul
- `search_web({'query': 'Tommy Paul Hamburg European Open 2025 recent form'})` → [Mon, 18 May 2026] Google News
[Mon, 04 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Tomas Etcheverry Hamburg European Open 2025 recent results'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `get_market_context({'keyword': 'Hamburg European Open tennis'})` → No related markets found for 'Hamburg European Open tennis'
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry head to head tennis record'})` → [Fri, 03 Apr 2026] Google News
[Mon, 23 Mar 2026] ATP Houston Quarterfinal Predictions Including Fra
- `search_web({'query': 'Tommy Paul tennis results May 2025'})` → [Sat, 07 Jun 2025] Google News
[Wed, 28 May 2025] 2025 French Open: Results, schedule as Jannik Sinn
- `get_market_context({'keyword': 'Tommy Paul tennis'})` → No related markets found for 'Tommy Paul tennis'
- `search_web({'query': 'Hamburg European Open 2025 draw Tommy Paul Tomas Etcheverry'})` → [Fri, 19 Jul 2019] Google News
[Thu, 07 Mar 2024] Hamburg | Draws | ATP Tour | Tennis - ATP Tour
[Mo
- `search_web({'query': 'Tomas Etcheverry recent form clay court 2025'})` → [Tue, 12 May 2026] Google News
[Sat, 16 May 2026] Argentina's in-form Etcheverry reaches new career 
- `search_web({'query': 'Hamburg European Open 2025 draw Tommy Paul Tomas Etcheverry'})` → [Fri, 19 Jul 2019] Google News
[Thu, 07 Mar 2024] Hamburg | Draws | ATP Tour | Tennis - ATP Tour
[Mo
- `search_web({'query': 'Tomas Etcheverry recent form clay court 2025'})` → [Tue, 12 May 2026] Google News
[Sat, 16 May 2026] Argentina's in-form Etcheverry reaches new career 
- `search_web({'query': 'Tommy Paul Hamburg European Open 2025 clay results'})` → [Mon, 18 May 2026] Google News
[Mon, 04 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Tomas Etcheverry 2025 clay season results win loss'})` → [Thu, 16 Oct 2025] Google News
[Sat, 16 May 2026] Top seed Rune escapes late jam to win Stockholm op
- `get_market_context({'keyword': 'Etcheverry'})` → No related markets found for 'Etcheverry'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*