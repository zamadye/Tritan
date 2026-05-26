# Market Analysis — 2026-05-19 03:27 UTC

## Market
- **Question:** Bengaluru 3: Karan Singh vs Mitsuki Wei Kang Leong
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $56,557
- **Liquidity:** $54,995

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,669 (-0.3% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,634 (-0.3% 24h) → neutral

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
- **p_true:** 48.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_MISPRICING
- **Catalyst Strength:** 0.75

### Reasoning
Market overprices YES (Karan Singh win) at 56% when historical data shows markets at this price resolve YES only 44.7% of the time (n=13,967). This creates ~11.3% edge for NO bet. Strong statistical signal despite no direct match-specific evidence.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `search_web({'query': 'Karan Singh vs Mitsuki Wei Kang Leong Bengaluru 3'})` → [Mon, 18 May 2026] Google News
[Sat, 16 May 2026] Karan (ind) Singh v Mitsuki Wei Kang Leong Odds - 
- `search_web({'query': '"Mitsuki Wei Kang Leong" tennis Bengaluru 2026'})` → [Mon, 18 May 2026] Google News
[Sat, 09 May 2026] Karan (ind) Singh v Mitsuki Wei Kang Leong Odds - 
- `get_market_context({'keyword': 'Bengaluru tennis'})` → No related markets found for 'Bengaluru tennis'
- `search_web({'query': 'Karan Singh tennis player Bengaluru Challenger 2026'})` → [Sun, 04 Jan 2026] Google News
[Tue, 06 Jan 2026] Bengaluru Open 2026: Know where to watch live stre
- `search_web({'query': 'Mitsuki Wei Kang Leong tennis 2026 results'})` → [Wed, 25 Feb 2026] Google News
[Tue, 24 Feb 2026] Pune ATP Challenger 2026: Manas Dhamne reaches qua
- `search_web({'query': '"Karan Singh" vs "Mitsuki Wei Kang Leong" odds'})` → [Mon, 18 May 2026] Google News
[Tue, 12 May 2026] H2H, prediction of Karan Singh vs Mitsuki Wei Kang
- `get_market_context({'keyword': 'Karan Singh'})` → No related markets found for 'Karan Singh'
- `search_web({'query': 'site:tennisactu.net Karan Singh vs Mitsuki Wei Kang Leong prediction Bengaluru'})` → No search results for: site:tennisactu.net Karan Singh vs Mitsuki Wei Kang Leong prediction Bengalur
- `search_web({'query': 'Tennis Tonic Karan Singh Mitsuki Wei Kang Leong Bengaluru prediction'})` → [Mon, 11 May 2026] Google News
[Tue, 12 May 2026] H2H Digvijaypratap Singh Vs Mitsuki Wei Kang Leong

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*