# Market Analysis — 2026-05-20 10:51 UTC

## Market
- **Question:** GP SAR La Princesse Lalla Meryem: Alycia Parks vs Jil Teichmann
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 6
- **Volume 24h:** $68,304
- **Liquidity:** $100,648

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,473 (+0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,498 (+0.9% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: princesse lalla meryem: alycia parks
- [Bing News]
- [Wed, 20 May 2026] princesse lalla meryem: alycia parks
- → Subscribe to Sky Sports to watch live, or stream on NOW. WTA Tour: Alycia Parks versus Jil Teichmann in the 2nd Round at the Grand Prix Son Altesse 
- [Fri, 26 May 2023] A. Parks v J. Teichmann
- → Also known as the Morocco Open or Rabat Grand Prix, the Grand Prix Sar La Princesse Lalla Meryem is an international WTA 250 event played on outdoor
- [] Grand Prix Son Altesse Royale La Princesse Lalla Meryem
- [Metaculus]

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 56.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.35

### Reasoning
Small 2% gap below 5% gate threshold. Conflicting signals: base rate suggests +2% YES edge, but stat signal (n=13,967) suggests ~9% NO edge. However, 50-60% entry range has only 33% WR from 9 trades. No direct player form or H2H data to confirm edge. Insufficient actionable information to bet with confidence.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'nba'})` → INJURY [atlanta hawks] Keshon Gilbert (G): Out
INJURY [atlanta hawks] Jock Landale (C): Out
INJURY [
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Alycia Parks vs Jil Teichmann GP SAR La Princesse Lalla Meryem 2025'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] WTA Rabat Day 3 Predictions Including Alycia Parks
- `search_web({'query': 'Alycia Parks recent form results 2025 WTA clay'})` → [Wed, 01 Oct 2025] Google News
[Wed, 22 Apr 2026] China Open quarterfinals: Who's in, how they got h
- `get_market_context({'keyword': 'Alycia Parks Jil Teichmann tennis'})` → No related markets found for 'Alycia Parks Jil Teichmann tennis'
- `search_web({'query': 'Jil Teichmann form results 2025 clay court season'})` → [Mon, 21 Jul 2025] Google News
[Mon, 21 Jul 2025] Rankings Watch: Boisson cracks Top 50; Begu, Teich
- `search_web({'query': '"Alycia Parks" "Jil Teichmann" head to head H2H tennis'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] H2H Alycia Parks Vs Jil Teichmann stats, predictio
- `get_odds({'sport': 'mma_mixed_martial_arts'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*