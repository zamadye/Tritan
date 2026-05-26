# Market Analysis — 2026-05-21 10:57 UTC

## Market
- **Question:** Will the price of Bitcoin be above $78,000 on May 22?
- **Category:** crypto
- **YES Price:** 31.0%
- **Days Left:** 1
- **Volume 24h:** $52,714
- **Liquidity:** $26,233

## Statistical Prior
- **p_base:** 26.5%
- **Source:** logistic:crypto
- **N (historical):** 4092
- **Raw gap:** 4.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,240 (-0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,192 (-0.3% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → BTC within 3% of round number ($80k/$90k) → gamma squeeze → price accelerates
- → BTC ETF inflows spike → institutional buying → price +5-15%
- → BTC ETF outflows → selling pressure → price -5-10%
- → BTC halving approaching → supply shock narrative → price rally

### Multi-Source
- [MULTI-SOURCE NEWS] 4 sources for: price bitcoin above $78,000
- [Bing News]
- [Wed, 20 May 2026] price bitcoin above $78,000
- → Bitcoin surged past $78,000, leading to $30M in short liquidations. Bitcoin above $72K on May 21 at 99.9% YES.
- [Thu, 21 May 2026] Bitcoin surges past $78,000, triggers $30M in short liquidations
- → Overview: Bitcoin holds strong support near the $75,000 price zone.Institutional investors continue to increase Bitcoin exposure.Market volatility r
- [Wed, 20 May 2026] Bitcoin Price Near $78K as ETF Outflows Shake Cryptocurrency Market
- → Bitcoin (BTC) is embarking on a recovery, trading above $78,000 on Thursday after support around the key Exponential Moving Averages (EMAs) earlier 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 26.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $77,200.00 | 24h: -0.31%
- `search_web({'query': 'Bitcoin price news May 21 2025'})` → [Thu, 21 May 2026] Google News
[Fri, 21 Nov 2025] Bitcoin Spot CVD Chart Analysis: Key Levels Emerge
- `search_web({'query': 'BTC crypto market analysis May 2025'})` → [Fri, 26 Dec 2025] Google News
[Wed, 06 May 2026] December 2025: Winter Freeze - Grayscale
[Tue, 09 
- `get_market_context({'keyword': 'Bitcoin price'})` → No related markets found for 'Bitcoin price'
- `search_web({'query': 'Bitcoin price today May 21 2025 rally catalyst'})` → [Fri, 08 May 2026] Google News
[Wed, 06 May 2026] XRP Price Analysis: Should You Cut Your Losses or 
- `search_web({'query': 'BTC $78000 resistance level technical analysis'})` → [Sat, 02 May 2026] Google News
[Sat, 16 May 2026] Bitcoin Clings To Key Support: EMA Reclaim Vs $78,
- `get_market_context({'keyword': 'Bitcoin above'})` → No related markets found for 'Bitcoin above'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*