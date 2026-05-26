# Market Analysis — 2026-05-19 03:00 UTC

## Market
- **Question:** Bengaluru 3: Karan Singh vs Mitsuki Wei Kang Leong
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $56,503
- **Liquidity:** $56,582

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,579 (-0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,721 (-0.2% 24h) → neutral

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
- **Confidence:** 65%
- **p_true:** 50.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_BIAS
- **Catalyst Strength:** 0.70

### Reasoning
Historical data shows markets at 56% YES price resolve YES only 44.7% of the time (n=13,967), indicating systematic overpricing of YES. No specific match evidence found to deviate from this pattern. Edge: 11.3% for NO.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Karan Singh'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Bengaluru tennis'})` → No related markets found for 'Bengaluru tennis'
- `search_web({'query': 'Karan Singh vs Mitsuki Wei Kang Leong Bengaluru tennis 2025'})` → [Mon, 05 Jan 2026] Google News
[Sun, 23 Feb 2025] Bengaluru Open 2026: Sumit Nagal cruises into seco
- `search_web({'query': 'Mitsuki Wei Kang Leong tennis ranking results 2025'})` → [Sat, 20 Dec 2025] Google News
[Wed, 19 Nov 2025] SEA Games 2025: All of Malaysia's medal winners - 
- `search_web({'query': 'Karan Singh tennis player India ranking'})` → [Wed, 09 Jul 2025] Google News
[Sat, 14 Feb 2026] Tennis: Karan Singh becomes India’s No. 2 ranked p
- `search_web({'query': 'Bengaluru Open 2025 Karan Singh Mitsuki Leong'})` → [Sun, 23 Feb 2025] Google News
[Mon, 24 Feb 2025] Bengaluru Open 2025 tennis: Rising teen star Manas
- `search_web({'query': '"Mitsuki Leong" tennis'})` → [Tue, 12 May 2026] Google News
[Tue, 12 May 2026] Mitsuki set to hit new career high in ATP rankings

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*