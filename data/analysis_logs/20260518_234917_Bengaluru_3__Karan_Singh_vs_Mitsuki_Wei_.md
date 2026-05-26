# Market Analysis — 2026-05-18 23:49 UTC

## Market
- **Question:** Bengaluru 3: Karan Singh vs Mitsuki Wei Kang Leong
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 6
- **Volume 24h:** $55,900
- **Liquidity:** $47,821

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $77,037 (-0.1% 24h) → neutral
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,975 (-1.1% 24h) → risk-OFF

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening

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
- **p_true:** 51.9%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.75

### Reasoning
Stat signal shows markets at 58% resolve YES only 44.7% of the time (n=13,967), indicating systematic overpricing of YES. Market at 58% vs true probability ~45% creates ~13% edge for NO. No specific match information contradicts this statistical edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `search_web({'query': 'Karan Singh vs Mitsuki Wei Kang Leong Bengaluru'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Karan (ind) Singh v Mitsuki Wei Kang Leong Odds - 
- `search_web({'query': 'ATP Bengaluru Karan Singh Mitsuki Wei Kang Leong 2025'})` → [Mon, 05 Jan 2026] Google News
[Sun, 23 Feb 2025] Bengaluru Open 2026: Sumit Nagal cruises into seco
- `get_market_context({'keyword': 'Karan Singh'})` → No related markets found for 'Karan Singh'
- `get_market_context({'keyword': 'Mitsuki Wei Kang Leong'})` → No related markets found for 'Mitsuki Wei Kang Leong'
- `get_market_context({'keyword': 'Bengaluru Open tennis'})` → No related markets found for 'Bengaluru Open tennis'
- `search_web({'query': '"Karan Singh" "Mitsuki Wei Kang Leong" tennis 2026'})` → [Tue, 24 Feb 2026] Google News
[Tue, 06 Jan 2026] Pune ATP Challenger 2026: Sumit Nagal enters singl
- `search_web({'query': 'Bengaluru Open 2026 tennis draw results round'})` → [Sat, 10 Jan 2026] Google News
[Mon, 05 Jan 2026] Bengaluru Open 2026 tennis: Pedro Martinez bags si
- `get_odds({'sport': 'tennis_atp_italian_open', 'team': 'Singh'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Karan Singh tennis player ranking 2026'})` → [Fri, 20 Feb 2026] Google News
[Sun, 15 Feb 2026] Delhi Open 2026 tennis: Siddhant Banthia and Alexa
- `search_web({'query': 'Mitsuki Wei Kang Leong tennis ranking 2026 form'})` → [Tue, 24 Feb 2026] Google News
[Tue, 24 Feb 2026] Pune ATP Challenger 2026: Sumit Nagal enters singl

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*