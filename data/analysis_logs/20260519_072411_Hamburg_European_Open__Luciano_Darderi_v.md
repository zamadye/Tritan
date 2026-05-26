# Market Analysis — 2026-05-19 07:24 UTC

## Market
- **Question:** Hamburg European Open: Luciano Darderi vs Roman Andres Burruchaga
- **Category:** sports
- **YES Price:** 68.0%
- **Days Left:** 6
- **Volume 24h:** $74,171
- **Liquidity:** $57,442

## Statistical Prior
- **p_base:** 75.6%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 7.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,013 (+0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,155 (+0.5% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → ECB rate cut → EUR weakens vs USD → EUR/USD falls
- → EU GDP beats expectations → EUR strengthens
- → EU political crisis (elections) → EUR uncertainty → falls
- → EUR/USD above 1.10 → European exports competitive → EU stocks rally

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: hamburg european open: luciano darderi
- [Bing News]
- [] hamburg european open: luciano darderi
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending
- [] Will the Senate of the Philippines remove Vice President Sara Duterte
- → Community: pending

## LLM Decision
- **Action:** YES
- **Confidence:** 65%
- **p_true:** 79.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** FORM
- **Catalyst Strength:** 0.60

### Reasoning
8% gap between base rate (76%) and market price (68%) with no contradicting evidence found. Darderi recently upset Tommy Paul in Rome, showing strong form on clay. Both players are clay court specialists, but Darderi has the statistical edge according to the base rate model (n=6077). The market appears to be underpricing Darderi's chances.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET YES $1.00

## Tool Calls
- `search_web({'query': 'Luciano Darderi vs Roman Andres Burruchaga head to head recent results Hamburg European Open 2024'})` → [Mon, 18 May 2026] Google News
[Sun, 28 Jan 2024] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Luciano Darderi recent form and results tennis 2024'})` → [Mon, 18 May 2026] Google News
[Wed, 13 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `get_market_context({'keyword': 'Hamburg European Open'})` → No related markets found for 'Hamburg European Open'
- `search_web({'query': 'Roman Andres Burruchaga recent results tennis Hamburg European Open'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge
- `search_web({'query': 'Luciano Darderi vs Roman Andres Burruchaga prediction Hamburg 2024'})` → [Mon, 18 May 2026] Google News
[Tue, 16 Apr 2024] ATP Hamburg Day 3 Predictions Including Felix Auge
- `get_odds({'sport': 'tennis_atp', 'team': 'Darderi'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': '"Luciano Darderi vs Roman Andres Burruchaga" "19th May 2026" prediction odds Hamburg'})` → [Mon, 18 May 2026] Google News
[] H2H, prediction of Luciano Darderi vs Roman Andres Burruchaga in H
- `get_sports_data({'sport': 'nba', 'team': 'Darderi'})` → No injury data found for nba Darderi
- `search_web({'query': 'Luciano Darderi 2026 form ranking Hamburg clay court results'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] Alex de Minaur suffers another setback right befor
- `search_web({'query': 'Roman Burruchaga tennis 2026 ranking form clay court'})` → [Mon, 06 Apr 2026] Google News
[Sun, 05 Apr 2026] Tommy Paul saves 3 championship points to win firs
- `search_web({'query': 'Hamburg European Open 2026 draw results Darderi Burruchaga first round'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] What is the Hamburg tennis schedule? - ATP Tour
[S
- `search_web({'query': '"Darderi" "Burruchaga" Hamburg 2026 odds head to head'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] ATP Hamburg Day 3 Predictions Including Felix Auge

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*