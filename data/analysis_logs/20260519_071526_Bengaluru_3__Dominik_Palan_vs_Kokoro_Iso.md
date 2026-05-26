# Market Analysis — 2026-05-19 07:15 UTC

## Market
- **Question:** Bengaluru 3: Dominik Palan vs Kokoro Isomura
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 5
- **Volume 24h:** $136,472
- **Liquidity:** $19,516

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,013 (+0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,013 (+0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: bengaluru dominik palan kokoro isomura
- [Bing News]
- [] bengaluru dominik palan kokoro isomura
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending
- [] Will the Senate of the Philippines remove Vice President Sara Duterte
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.60

### Reasoning
Strong statistical signal shows markets priced at 53% resolve YES only 44.7% of time (n=13,967), indicating systematic overpricing of YES. No concrete match-specific information (injuries, form, H2H) to justify current YES price. Entry price range (50-60%) historically has only 33% win rate.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `search_web({'query': 'Dominik Palan vs Kokoro Isomura Bengaluru 3 tennis'})` → [Mon, 18 May 2026] Google News
[Wed, 13 May 2026] Dominik Palan v Kokoro Isomura Odds - FanDuel Spor
- `search_web({'query': 'Palan Isomura tennis result 2025'})` → [Mon, 18 May 2026] Google News
[Mon, 11 May 2026] H2H, prediction of Dominik Palan vs Kokoro Isomura
- `get_market_context({'keyword': 'Palan Isomura'})` → No related markets found for 'Palan Isomura'
- `get_odds({'sport': 'tennis_atp_italian_open'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Dominik Palan tennis form 2026'})` → [Wed, 26 Nov 2025] Google News
[] A British teenager has just made his maiden ATP quarter-final at t
- `search_web({'query': 'Kokoro Isomura tennis form 2026'})` → [Wed, 25 Feb 2026] Google News
[] Pune ATP 75 Challenger: Manas Dhamne reaches quarter-finals - theb
- `search_web({'query': '"Bengaluru 3 Challenger" results'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] H2H, prediction of Ilya Ivashka vs S D Prajwal Dev
- `search_web({'query': 'Dominik Palan injury'})` → No search results for: Dominik Palan injury
- `search_web({'query': 'Kokoro Isomura injury'})` → [Wed, 25 Feb 2026] Google News
[Mon, 09 Oct 2023] Pune ATP Challenger 2026: Manas Dhamne reaches qua
- `search_web({'query': 'Dominik Palan recent results tennis 2026'})` → [Wed, 21 Jan 2026] Google News
[Tue, 12 May 2026] Dominik Palan Timofei Derepasko live score and H2H
- `search_web({'query': 'Kokoro Isomura recent results tennis 2026'})` → [Sat, 16 May 2026] Google News
[Tue, 12 May 2026] Kokoro Isomura/Makoto Ochi's draws, scores, stats,
- `search_web({'query': 'Palan Isomura head to head Bengaluru'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] H2H, prediction of Dominik Palan vs Kokoro Isomura
- `search_web({'query': '"Dominik Palan vs Kokoro Isomura" odds Tennis Tonic'})` → [Mon, 18 May 2026] Google News
[] H2H, prediction of Dominik Palan vs Kokoro Isomura in Bengaluru 3 
- `search_web({'query': 'Dominik Palan ranking ATP 2026'})` → [Mon, 05 Jan 2026] Google News
[Wed, 21 Jan 2026] Bengaluru Open 2026: Sumit Nagal cruises into seco
- `search_web({'query': 'Kokoro Isomura ranking ATP 2026'})` → [Sat, 16 May 2026] Google News
[Mon, 18 May 2026] Kokoro Isomura/Makoto Ochi's draws, scores, stats,
- `search_web({'query': 'Tennis Tonic Palan Isomura prediction pick Bengaluru 3'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] H2H, prediction of Dominik Palan vs Kokoro Isomura
- `search_web({'query': 'Bengaluru 3 Challenger 2026 draw results'})` → [Thu, 08 Jan 2026] Google News
[Mon, 05 Jan 2026] Bengaluru Open 2026 tennis: Manas Dhamne, Dhakshin

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*