# Market Analysis — 2026-05-19 05:58 UTC

## Market
- **Question:** Bengaluru 3: Karan Singh vs Mitsuki Wei Kang Leong
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 5
- **Volume 24h:** $54,467
- **Liquidity:** $47,175

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,877 (-0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,794 (-0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: bengaluru karan singh mitsuki kang
- [Bing News]
- [Tue, 06 Jan 2026] bengaluru karan singh mitsuki kang
- → Dhakshineswar Suresh came up with a power-packed performance to oust Croatia’s Duje Ajdukovic 6-4, 6-4 in the opening round of the Dafa News Bengalu
- [] Bengaluru Open: Dhakshineswar packs off Ajdukovic; Karan, Aryan bow out
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 59.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MEAN_REVERSION
- **Catalyst Strength:** 0.40

### Reasoning
Strong statistical signal (n=13,967) indicates markets at 56% resolve YES only 44.7% of time, suggesting YES is overpriced by ~11%. However, gap is only +3% (below 5% threshold), Karan Singh is India's No. 2 ranked player with recent strong form, no concrete injury/news catalyst found to confirm the statistical edge. Previous decisions on same market were SKIP. Entry 50-60% bracket shows weak 33% WR historically. Need stronger information edge to act on statistical mean reversion alone.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'tennis', 'team': 'Leong'})` → No injury data found for tennis Leong
- `get_odds({'sport': 'tennis_atp', 'team': 'Karan Singh'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Bengaluru tennis'})` → No related markets found for 'Bengaluru tennis'
- `search_web({'query': 'Karan Singh vs Mitsuki Wei Kang Leong tennis 2025'})` → [Sun, 23 Feb 2025] Google News
[Mon, 18 May 2026] Bengaluru Open 2025 tennis: Rising teen star Manas
- `search_web({'query': 'Bengaluru ATP tennis tournament results 2025'})` → [Sun, 08 Feb 2026] Google News
[Wed, 10 Dec 2025] World No. 457 Suresh propels India past Netherland
- `search_web({'query': 'Karan Singh tennis player ranking 2026'})` → [Fri, 20 Feb 2026] Google News
[Wed, 09 Jul 2025] Delhi Open 2026 tennis: Siddhant Banthia and Alexa
- `search_web({'query': 'Mitsuki Wei Kang Leong tennis player ranking form 2026'})` → [Sun, 17 May 2026] Google News
[Tue, 24 Feb 2026] SM Krishna Memorial: Upbeat Keegan Smith seeks two
- `search_web({'query': 'Karan Singh tennis India number 2 ranking 2026 results'})` → [Tue, 24 Feb 2026] Google News
[Tue, 03 Feb 2026] Pune ATP Challenger 2026: Sumit Nagal enters singl
- `search_web({'query': 'Mitsuki Wei Kang Leong tennis ATP ranking record 2026'})` → [Mon, 05 Jan 2026] Google News
[Mon, 11 May 2026] Bengaluru Open 2026: Sumit Nagal cruises into seco
- `search_web({'query': '"Karan Singh" "Mitsuki Wei Kang Leong" head to head Bengaluru 2026'})` → [Tue, 12 May 2026] Google News
[Tue, 12 May 2026] H2H, prediction of Hamish Stewart vs Mukund Sasiku
- `search_web({'query': 'Bengaluru Challenger tennis 2026 draw results Karan Singh'})` → [Tue, 06 Jan 2026] Google News
[Mon, 05 Jan 2026] Bengaluru Open 2026: Dhakshineswar Suresh powers i
- `search_web({'query': 'Tennis Tonic Karan Singh vs Mitsuki Wei Kang Leong prediction Bengaluru 3'})` → [Mon, 11 May 2026] Google News
[Tue, 12 May 2026] H2H Digvijaypratap Singh Vs Mitsuki Wei Kang Leong
- `search_web({'query': 'Mitsuki Wei Kang Leong tennis ranking Challenger results recent form'})` → [Tue, 24 Feb 2026] Google News
[Wed, 25 Feb 2026] Pune ATP Challenger 2026: Sumit Nagal enters singl
- `search_web({'query': 'Mitsuki Wei Kang Leong ATP ranking current 2026'})` → [Fri, 08 May 2026] Google News
[Mon, 05 Jan 2026] Leong vs Dev - Nakhon Pathom 2026 - Tennis Temple 
- `search_web({'query': 'Karan Singh ATP ranking current 2026 India number 2'})` → [Thu, 19 Feb 2026] Google News
[Mon, 16 Feb 2026] Delhi Open 2026 tennis: Sumit Nagal’s second-round

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*