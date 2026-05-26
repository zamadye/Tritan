# Market Analysis — 2026-05-21 12:24 UTC

## Market
- **Question:** Will the price of Bitcoin be above $78,000 on May 22?
- **Category:** crypto
- **YES Price:** 31.0%
- **Days Left:** 1
- **Volume 24h:** $55,401
- **Liquidity:** $19,920

## Statistical Prior
- **p_base:** 26.5%
- **Source:** logistic:crypto
- **N (historical):** 4092
- **Raw gap:** 4.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,130 (-0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,128 (-0.3% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving

### Bing/Google News
- 6 articles found:
- [NewsAPI] Binance Bitcoin Wallets Show 85% Quantum Exposure, Glassnode Says: Binance Bitcoin wallets show 85% public-key exposure in Glassnode’s quant
- [NewsAPI] Bitcoin’s ‘momentum is fading’: Traders have these support levels in mind: Bitcoin momentum is fading following drop to $76,000 as analysts 
- [NewsAPI] Before You Invest in Crypto, Watch This Film: A version of the below article first appeared in David Corn’s newsletter, Our Land. The newsle
- [NewsAPI] Sensex today | Stock Market Highlights: Stock markets rebound; Sensex climbs 117: Sensex Today, Nifty 50 | Stock Market Highlights - Find he
- [NewsAPI] New Bitcoin ETF outflows are exposing BTC to Wall Street’s most crowded trade: Bitcoin ETF outflows are turning rising Treasury yields into 
- [NewsAPI] Bitcoin Fall Under $77,000 Triggers Spike In Social Media FUD: Data shows sentiment around Bitcoin among social media users has turned negat
- [CAUSAL CHAINS] Relevant cause-effect patterns:

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
- **Confidence:** 52%
- **p_true:** 26.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market slightly overpriced (31% vs estimated 27%), but edge is <5% threshold. No concrete catalyst identified. BTC needs +1.2% in 1 day with neutral/negative momentum. Previous decisions for same market also SKIP. Crypto pattern performance is WEAK (25% WR).

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $77,074.00 | 24h: -0.32%
- `get_market_context({'keyword': 'Bitcoin price May 22'})` → No related markets found for 'Bitcoin price May 22'
- `search_web({'query': 'Bitcoin price prediction May 22 2025'})` → [Sat, 16 May 2026] Google News
[Tue, 19 Aug 2025] XRP Price Prediction 2026, 2027, 2028-2032 - Crypt
- `search_web({'query': 'Bitcoin crypto market news today May 2025'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Top 10 Cryptocurrencies Of May 20, 2026 - Forbes
[
- `get_market_context({'keyword': 'Bitcoin crypto prediction market'})` → No related markets found for 'Bitcoin crypto prediction market'
- `search_web({'query': 'Bitcoin price momentum technical analysis this week'})` → [Sun, 19 Apr 2026] Google News
[Mon, 18 May 2026] Crypto Technical Analysis: Bullish momentum return

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*