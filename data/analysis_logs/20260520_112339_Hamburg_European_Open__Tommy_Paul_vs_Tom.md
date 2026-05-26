# Market Analysis — 2026-05-20 11:23 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 6
- **Volume 24h:** $704,894
- **Liquidity:** $57,435

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,419 (+0.8% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,421 (+0.6% 24h) → neutral
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
- **p_true:** 52.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.70

### Reasoning
Statistical signal from 13,967 samples shows markets at 57% YES historically resolve YES only 44.7% of time, indicating YES is significantly overpriced. Edge is 12.3% for NO. No specific match information (injuries, recent form) contradicts this general pattern. Both players appear in form, but the strong historical statistical edge justifies betting against the overpriced YES.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Tommy Paul'})` → No injury data found for tennis Tommy Paul
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg European Open 2025 preview prediction'})` → [Mon, 18 May 2026] Google News
[Fri, 03 Apr 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `get_market_context({'keyword': 'Tommy Paul Etcheverry Hamburg'})` → No related markets found for 'Tommy Paul Etcheverry Hamburg'
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry odds Hamburg European Open 2026'})` → [Sun, 17 May 2026] Google News
[Fri, 03 Apr 2026] How to watch the men’s Hamburg European Open: TV c
- `search_web({'query': 'Tommy Paul recent form 2026 results'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] ATP Hamburg Day 1 Predictions Including Tommy Paul
- `search_web({'query': 'Tomas Etcheverry recent form 2026 results'})` → [Tue, 12 May 2026] Google News
[Mon, 18 May 2026] Argentina's in-form Etcheverry reaches new career 
- `search_web({'query': '"Tommy Paul" "Etcheverry" head to head'})` → [Mon, 18 May 2026] Google News
[Fri, 03 Apr 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Tommy Paul injury 2026'})` → [Mon, 19 Jan 2026] Google News
[Tue, 20 Jan 2026] Physically and philanthropically, Tommy Paul hits 
- `search_web({'query': 'Etcheverry injury 2026'})` → [Mon, 13 Apr 2026] Google News
[Sat, 16 May 2026] Draper: 'I will work my way out of this' - ATP Tou
- `search_web({'query': '"Hamburg European Open" 2026 draw Tommy Paul'})` → [Sun, 30 Jul 2023] Google News
[Mon, 04 May 2026] Zverev Downs Djere For Hometown Triumph In Hamburg
- `search_web({'query': 'Tommy Paul Hamburg 2026 round'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] What is the Hamburg tennis schedule? - ATP Tour
[M
- `search_web({'query': 'Hamburg Open 2026 Tommy Paul Tomas Etcheverry'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] What is the Hamburg tennis schedule? - ATP Tour
[M
- `search_web({'query': 'site:atptour.com Hamburg 2026 draw'})` → [Tue, 19 May 2026] Google News
[Fri, 15 May 2026] Roland Garros: When is the draw &amp; how to watch
- `search_web({'query': '"Bitpanda Hamburg Open 2026" Tommy Paul'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] What is the Hamburg tennis schedule? - ATP Tour
[S
- `search_web({'query': 'Hamburg Open 2026 round of 16 Paul Etcheverry'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] Tommy Paul vs Tomas Martin Etcheverry - Match ATP 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*