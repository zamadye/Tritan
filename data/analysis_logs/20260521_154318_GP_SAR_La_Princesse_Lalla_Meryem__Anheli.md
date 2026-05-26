# Market Analysis — 2026-05-21 15:43 UTC

## Market
- **Question:** GP SAR La Princesse Lalla Meryem: Anhelina Kalinina vs Anna Bondar
- **Category:** sports
- **YES Price:** 93.0%
- **Days Left:** 6
- **Volume 24h:** $189,842
- **Liquidity:** $70,669

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,159 (-0.5% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,110 (-0.3% 24h) → neutral
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
- **Confidence:** 48%
- **p_true:** 92.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Despite a 5% gap between market (93%) and base rate (98%), the previous decision on this exact market already identified it as having no edge (gate=FAIL). Historical resolution data suggests 60% of similar markets OVERPRICE YES (only 44.7% historical resolution), meaning the 98% base rate may be inflated. No injuries, withdrawals, or form changes found for either player. The 5% edge is insufficient given: (1) match is 6 days away with time for information to change, (2) similar past decision showed no independent catalyst, (3) sports pattern suggests edges need to be more robust. Tennis at this level can produce upsets - Bondar is a capable clay court player. The risk/reward doesn't justify a bet at 93% pricing.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `search_web({'query': 'Anhelina Kalinina vs Anna Bondar GP SAR La Princesse Lalla Meryem'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] PREDICTION, PREVIEW, H2H: Bondar, Kalinina, Udvard
- `search_web({'query': 'Anhelina Kalinina injury status May 2026'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] WTA Rabat Day 3 Predictions Including Yuliia Staro
- `search_web({'query': 'Anna Bondar injury status May 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 05 May 2026] WTA Rabat Day 3 Predictions Including Alycia Parks
- `get_market_context({'keyword': 'GP SAR La Princesse Lalla Meryem'})` → No related markets found for 'GP SAR La Princesse Lalla Meryem'
- `search_web({'query': 'Kalinina vs Bondar head to head record 2026'})` → [Tue, 19 May 2026] Google News
[Thu, 21 May 2026] WTA Rabat Day 3 Predictions Including Alycia Parks
- `search_web({'query': 'GP SAR La Princesse Lalla Meryem 2026 draw results Kalinina Bondar quarterfinal'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] PREDICTION, PREVIEW, H2H: Bondar, Kalinina, Udvard
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Kalinina'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Kalinina vs Bondar odds betting lines Rabat 2026'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Anhelina Kalinina vs. Anna Bondar prediction, odds
- `search_web({'query': 'dimers.com Kalinina Bondar odds Morocco Open 2026'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Anhelina Kalinina vs. Anna Bondar prediction, odds

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*