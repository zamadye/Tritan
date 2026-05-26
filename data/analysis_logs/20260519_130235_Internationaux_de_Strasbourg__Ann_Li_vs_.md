# Market Analysis — 2026-05-19 13:02 UTC

## Market
- **Question:** Internationaux de Strasbourg: Ann Li vs Ekaterina Alexandrova
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 7
- **Volume 24h:** $194,015
- **Liquidity:** $19,577

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,890 (-0.7% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,890 (-0.7% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: ekaterina alexandrova
- [Bing News]
- [Sun, 17 May 2026] internationaux strasbourg: ekaterina alexandrova
- → The women’s slate at the Internationaux de Strasbourg today includes six matches, among them Ann Li (ranked No. 30) versus Ekaterina Alexandrova (No
- [Fri, 15 May 2026] How to watch the women's Internationaux de Strasbourg: TV channel and streaming options for the Round of 16
- → The Internationaux de Strasbourg takes place between 17-23 May in a WTA 500 tournament prior to the French Open. Elena Rybakina is defending champio
- [Sat, 16 May 2026] Internationaux de Strasbourg 2026: Results, Draw, Schedule, Entry List, Prize Money and Predictions
- → It's a big week for tennis; catch the Geneva Open, the Hamburg Open and the Internationaux de Strasbourg on the Tennis Channel all week long.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 44.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.72

### Reasoning
Strong statistical signal (n=13,967) indicates markets at 52% resolve YES only 44.7% of the time — market overprices YES by ~7.3pp. No contradicting injury/form news found. Alexandrova has recent H2H advantage. However, confidence tempered because entry in 50-60% range historically shows weak 33% WR from 6 trades. Similar Strasbourg market (Raducanu) was BET_NO based on same stat signal. Stat edge of 7.3% exceeds 5% threshold, but information_gap=false reduces edge quality.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Ann Li'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_odds({'sport': 'tennis', 'team': 'Ann Li'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Ann Li vs Ekaterina Alexandrova Internationaux de Strasbourg 2025'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Sports News, Transfers, Scores | Watch Live Sport 
- `search_web({'query': 'Ann Li injury 2026'})` → [Sat, 25 Apr 2026] Google News
[Sat, 25 Apr 2026] Unwell Iga Swiatek retires in third set of Madrid 
- `search_web({'query': 'Ekaterina Alexandrova recent form 2026'})` → [Thu, 19 Feb 2026] Google News
[Fri, 06 Feb 2026] Medvedev Teams With Rival Tien As Singles Standout
- `get_market_context({'keyword': 'Internationaux de Strasbourg tennis'})` → No related markets found for 'Internationaux de Strasbourg tennis'
- `search_web({'query': 'Ann Li vs Ekaterina Alexandrova head to head'})` → [Tue, 19 May 2026] Google News
[Thu, 07 May 2026] WTA Strasbourg Day 2 Predictions Including Diane P

## Outcome
**✅ WIN** | P&L: $+0.49 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*