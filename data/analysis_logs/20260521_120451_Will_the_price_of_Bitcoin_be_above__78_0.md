# Market Analysis — 2026-05-21 12:04 UTC

## Market
- **Question:** Will the price of Bitcoin be above $78,000 on May 22?
- **Category:** crypto
- **YES Price:** 33.0%
- **Days Left:** 1
- **Volume 24h:** $54,630
- **Liquidity:** $20,294

## Statistical Prior
- **p_base:** 28.1%
- **Source:** logistic:crypto
- **N (historical):** 4092
- **Raw gap:** 4.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,174 (-0.2% 24h) → neutral
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
- → SpaceX disclosed a $1.4B Bitcoin holding, boosting market confidence. Bitcoin above $72K on May 21 at 99.9% YES.
- [Sat, 02 May 2026] SpaceX reveals $1.4B Bitcoin holding, boosting market confidence
- → Bitcoin prices climbed during early morning trade on Saturday, extending a bullish streak as the market absorbed record-breaking institutional deman

## LLM Decision
- **Action:** SKIP
- **Confidence:** 50%
- **p_true:** 28.1%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** MACRO
- **Catalyst Strength:** 0.20

### Reasoning
BTC at $77,147 needs +1.1% in 1 day to reach $78,000. Current momentum is neutral (-0.29% 24h) with mixed signals: Fear & Greed improving but macro headwinds (rising bond yields, oil spike). Market priced at 33% vs base rate 28% gives slight edge but not strong enough. Past similar markets skipped due to no statistical edge. Entry pattern at 30-40% shows 46% win rate, below profitable threshold. No clear catalyst for imminent move.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $77,147.00 | 24h: -0.29%
- `search_web({'query': 'Bitcoin price today May 22 2025'})` → [2026-05-20] Sensex today | Stock Market Highlights: Stock markets rebound; Sensex climbs 117 points
- `search_web({'query': 'Bitcoin news May 22 2025 price movement'})` → [2026-05-20] Sensex today | Stock Market Highlights: Stock markets rebound; Sensex climbs 117 points
- `get_market_context({'keyword': 'Bitcoin'})` → [YES=50% vol=$5,821,653] Will Bitcoin hit $150k by June 30, 2026?

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*