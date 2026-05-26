# Market Analysis — 2026-05-21 14:21 UTC

## Market
- **Question:** GP SAR La Princesse Lalla Meryem: Anhelina Kalinina vs Anna Bondar
- **Category:** sports
- **YES Price:** 60.0%
- **Days Left:** 6
- **Volume 24h:** $72,114
- **Liquidity:** $49,276

## Statistical Prior
- **p_base:** 64.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.7%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $76,919 (-0.6% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $76,891 (-0.7% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: princesse lalla meryem: anhelina kalinina
- [Bing News]
- [Wed, 20 May 2026] princesse lalla meryem: anhelina kalinina
- → Yasmine Kabbaj continued her run through her home tournament with a 6-2, 6-4 upset of third-seeded German Tatjana Maria in the Grand Prix SAR La Pri
- [Wed, 20 May 2026] WTA roundup: Camila Osorio knocks off No. 1 seed Janice Tjen in Rabat
- → Janice Tjen Gagal ke Perempat Final Grand Prix SAR La Princesse Lalla Meryem di Rabat Usai Dikalahkan Camila Osorio - Menyandang status unggulan per
- [Tue, 19 May 2026] Janice Tjen Gagal ke Perempat Final Grand Prix SAR La Princesse Lalla Meryem di Rabat Usai Dikalahkan Camila Osorio
- → Live scores for the 2025 Grand Prix Sar La Princesse Lalla Meryem tennis tournament on ESPN. Includes daily schedules, live scores and match results

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 64.8%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Stat signal suggests 60% markets overprice YES (44.7% historical resolution), but no independent catalyst or verifiable edge to act on. Kalinina's fatigue from 3-set previous match is a mild concern, and Bondar has upset capability, but insufficient data to place confident bet. Market appears to have crowd bias toward favorite, but SKIP due to low confidence.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_sports_data({'team': 'Kalinina', 'sport': 'tennis'})` → No injury data found for tennis Kalinina
- `get_sports_data({'team': 'Bondar', 'sport': 'tennis'})` → No injury data found for tennis Bondar
- `get_odds({'team': 'Kalinina', 'sport': 'tennis_atp_italian_open'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_odds({'team': 'Bondar', 'sport': 'tennis_atp_italian_open'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'GP SAR La Princesse Lalla Meryem'})` → No related markets found for 'GP SAR La Princesse Lalla Meryem'
- `search_web({'query': 'Kalinina vs Bondar GP SAR La Princesse Lalla Meryem 2025'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] On sixth match point, Kalinina wins all-Ukrainian 
- `search_web({'query': 'Anhelina Kalinina recent results 2025 form'})` → [Wed, 20 May 2026] Google News
[Tue, 13 Jan 2026] The Official Home of the Women's Tennis Associatio
- `search_web({'query': 'Anna Bondar 2025 results form Morocco Open'})` → [Fri, 18 Jul 2025] Google News
[Wed, 17 Sep 2025] Bondar upsets Alexandrova in Hamburg quarters for 
- `search_web({'query': 'Kalinina Bondar head to head tennis'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] WTA Rabat Quarterfinal Predictions Including Jessi
- `search_web({'query': 'Bondar vs Kalinina prediction odds Morocco Open quarterfinal 2026'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Anhelina Kalinina vs. Anna Bondar prediction, odds
- `search_web({'query': 'Kalinina form recent matches 2026 results'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] The Official Home of the Women's Tennis Associatio
- `search_web({'query': '"Kalinina" "Bondar" prediction winner Morocco Open quarterfinal'})` → [Wed, 20 May 2026] Google News
[Thu, 21 May 2026] WTA Rabat Quarterfinal Predictions Including Jessi
- `search_web({'query': 'Bondar tennis 2026 results ranking'})` → [Thu, 23 Apr 2026] Google News
[Mon, 02 Feb 2026] Swiatek enjoys 61-minute opening win, Bondar stuns

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*