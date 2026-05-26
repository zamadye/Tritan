# Market Analysis — 2026-05-19 10:47 UTC

## Market
- **Question:** Internationaux de Strasbourg: Shuai Zhang vs Cristina Bucsa
- **Category:** sports
- **YES Price:** 59.7%
- **Days Left:** 6
- **Volume 24h:** $162,398
- **Liquidity:** $57,605

## Statistical Prior
- **p_base:** 64.3%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.6%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,710 (-0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,710 (-0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Major AI model release → benchmark competition → sector excitement
- → AI regulation proposed → uncertainty → AI stocks fall short-term
- → AI chip shortage → NVIDIA revenue beats → AI infrastructure stocks rally
- → AI energy demand → data center power stocks rally

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: internationaux strasbourg: shuai zhang cristina
- [Bing News]
- [] internationaux strasbourg: shuai zhang cristina
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending
- [] Will the Senate of the Philippines remove Vice President Sara Duterte
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 50%
- **p_true:** 64.3%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Conflicting signals between base rate (64% suggests YES underpriced) and stat signal (60% markets resolve YES only 44.7% suggests YES overpriced). No injury/form data found for either player. Poor historical win rate in 50-60% entry bracket (33%). Without independent catalyst to break tie between conflicting signals, edge is unclear.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `get_market_context({'keyword': 'Strasbourg Zhang Bucsa'})` → No related markets found for 'Strasbourg Zhang Bucsa'
- `search_web({'query': 'Shuai Zhang Cristina Bucsa Strasbourg 2025'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Sports News, Transfers, Scores | Watch Live Sport 
- `search_web({'query': 'Internationaux de Strasbourg Zhang Bucsa tennis'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Sports News, Transfers, Scores | Watch Live Sport 
- `search_web({'query': 'Shuai Zhang vs Cristina Bucsa head to head 2026'})` → [Tue, 19 May 2026] Google News
[Sun, 01 Mar 2026] WTA Strasbourg Day 2 Predictions Including Victori
- `search_web({'query': 'Shuai Zhang injury status 2026'})` → [Tue, 19 May 2026] Google News
[Fri, 24 Apr 2026] Madison Keys Pulls Out of Internationaux de Strasb
- `search_web({'query': '"Zhang" "Bucsa" Strasbourg 2026 prediction'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] WTA Strasbourg Day 2 Predictions Including Victori
- `search_web({'query': 'Tennis Tonic Bucsa Zhang Strasbourg prediction odds'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] H2H, prediction of Cristina Bucsa vs Shuai Zhang i
- `search_web({'query': 'Shuai Zhang current form 2026 WTA results'})` → [Sat, 31 Jan 2026] Google News
[Wed, 22 Apr 2026] Reunited and it feels so good! Mertens and Zhang w
- `search_web({'query': 'Cristina Bucsa current form 2026 WTA results'})` → [Sun, 17 May 2026] Google News
[Mon, 02 Mar 2026] Italian Open 2026: All results live - full scores,

## Outcome
**✅ WIN** | P&L: $+0.49 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*