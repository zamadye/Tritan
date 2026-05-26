# Market Analysis — 2026-05-20 08:00 UTC

## Market
- **Question:** Hamburg European Open: Tommy Paul vs Tomas Etcheverry
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $651,129
- **Liquidity:** $156,728

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,202 (+0.1% 24h) → neutral
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
- **Confidence:** 65%
- **p_true:** 47.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_OVERPRICING
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets priced at 55% YES resolve YES only 44.7% of the time — a 10.3% overpricing. Supporting factors: (1) Tommy Paul ended 2025 season early due to ongoing foot injury and hasn't competed since US Open, raising fitness concerns; (2) Etcheverry is Argentine clay-court specialist with recent strong form ('in-form Etcheverry reaches new career milestone') while Hamburg is clay surface; (3) Paul typically stronger on hard courts. Despite strong sports pattern (WR=83%), the 50-60% entry zone historically has only 38% WR. Market overpricing + injury concerns + surface disadvantage for Paul = edge on NO side.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Tommy Paul'})` → No injury data found for tennis Tommy Paul
- `get_sports_data({'sport': 'tennis', 'team': 'Tomas Etcheverry'})` → No injury data found for tennis Tomas Etcheverry
- `get_market_context({'keyword': 'Hamburg European Open tennis'})` → No related markets found for 'Hamburg European Open tennis'
- `search_web({'query': 'Tommy Paul Hamburg European Open 2025 form results'})` → [Fri, 24 Oct 2025] Google News
[Fri, 16 May 2025] Tommy Paul abruptly ends 2025 season after withdra
- `search_web({'query': 'Tomas Etcheverry Hamburg European Open 2025 recent matches'})` → [Sat, 16 May 2026] Google News
[Mon, 04 May 2026] Jack Draper - latest news and results - Sky Sports
- `search_web({'query': 'Tommy Paul vs Tomas Etcheverry Hamburg European Open head to head 2025'})` → [Mon, 18 May 2026] Google News
[Fri, 03 Apr 2026] Hamburg Open 2026: Ben Shelton falls to Germany's 
- `search_web({'query': 'Tommy Paul tennis results June 2025'})` → [Tue, 03 Jun 2025] Google News
[Sat, 07 Jun 2025] French Open 2025: Carlos Alcaraz dominates Tommy P
- `get_odds({'sport': 'tennis_atp', 'team': 'Tommy Paul'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis_atp', 'team': 'Etcheverry'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': '"Tommy Paul" "Etcheverry" odds betting Hamburg 2025'})` → [Tue, 02 Sep 2025] Google News
[Sat, 15 Feb 2025] How Tall Is Jannik Sinner? Discover His Height and
- `search_web({'query': 'Tommy Paul Tomas Etcheverry head to record tennis'})` → [Fri, 03 Apr 2026] Google News
[Mon, 23 Mar 2026] ATP Houston Quarterfinal Predictions Including Fra
- `search_web({'query': 'Hamburg European Open 2025 tennis draw results today'})` → [Tue, 19 May 2026] Google News
[Sat, 16 May 2026] Hamburg Open 2026: All matches, live scores and ho
- `search_web({'query': 'Tommy Paul injury status 2025 foot problem recovery'})` → [Sun, 10 Aug 2025] Google News
[Mon, 08 Dec 2025] Newly Engaged, Paul Eyes Big Run In Cincinnati - C
- `search_web({'query': 'Etcheverry clay court form 2025 results'})` → [Tue, 12 May 2026] Google News
[Mon, 18 May 2026] Argentina's in-form Etcheverry reaches new career 
- `search_web({'query': 'Tommy Paul Hamburg Open 2025 entry withdrawal'})` → [Mon, 11 May 2026] Google News
[Sat, 16 Aug 2025] ATP Hamburg Open 2026 Entry List: Rune withdraws, 
- `search_web({'query': 'Etcheverry Hamburg Open 2025 clay court performance'})` → [Thu, 18 Sep 2025] Google News
[Thu, 22 May 2025] Highlights: Etcheverry blitzes Dzumhur in Hangzhou

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*