# Market Analysis — 2026-05-21 12:07 UTC

## Market
- **Question:** Will the price of Bitcoin be above $76,000 on May 22?
- **Category:** crypto
- **YES Price:** 83.0%
- **Days Left:** 1
- **Volume 24h:** $51,828
- **Liquidity:** $18,948

## Statistical Prior
- **p_base:** 75.5%
- **Source:** logistic:crypto
- **N (historical):** 4092
- **Raw gap:** 7.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,174 (-0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,162 (-0.3% 24h) → neutral

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
- [MULTI-SOURCE NEWS] 4 sources for: price bitcoin above $76,000
- [Bing News]
- [Thu, 21 May 2026] price bitcoin above $76,000
- → SpaceX disclosed a $1.4B Bitcoin holding, boosting market confidence. Bitcoin above $72K on May 21 at 99.9% YES.
- [Wed, 20 May 2026] SpaceX reveals $1.4B Bitcoin holding, boosting market confidence
- → Bitcoin surged past $78,000, leading to $30M in short liquidations. Bitcoin above $72K on May 21 at 99.9% YES.
- [Tue, 21 Apr 2026] Bitcoin surges past $78,000, triggers $30M in short liquidations
- → Bitcoin price trades above $76,000 on Tuesday after gaining nearly 3% the previous day. US-listed spot ETFs recorded an inflow of over $238 million 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 75.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
BTC at $77,173 is already $1,174 (1.5%) above $76,000 threshold with only 1 day left. Market prices YES at 83% which appears efficiently priced given BTC would need to drop >1.5% in 24h. My estimated p_true is ~84%, providing negligible edge (1%). News mentions $76,000 support weakening but BTC has held above it. Fear sentiment improving (-0.28% 24h momentum is mild). Insufficient edge to justify bet given WEAK crypto pattern (25% WR).

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $77,173.00 | 24h: -0.28%
- `search_web({'query': 'Bitcoin price May 22 2024 news'})` → [2026-05-20] Sensex today | Stock Market Highlights: Stock markets rebound; Sensex climbs 117 points
- `search_web({'query': 'Bitcoin market analysis May 22 price prediction'})` → [2026-05-20] Sensex today | Stock Market Highlights: Stock markets rebound; Sensex climbs 117 points
- `search_web({'query': 'Bitcoin price movement today May 20 2026'})` → [2026-05-20] Sensex today | Stock Market Highlights: Stock markets rebound; Sensex climbs 117 points
- `search_web({'query': 'cryptocurrency market outlook Bitcoin support resistance'})` → [2026-05-20] Bitcoin Could Hit Near $95,000 If It Holds Above This Critical Support, Top Analyst Say
- `get_market_context({'keyword': 'Bitcoin'})` → [YES=50% vol=$5,821,653] Will Bitcoin hit $150k by June 30, 2026?
- `search_web({'query': 'Bitcoin price analysis May 20 2026 support level'})` → [2026-05-20] Sensex today | Stock Market Highlights: Stock markets rebound; Sensex climbs 117 points
- `search_web({'query': 'Bitcoin ETF flows institutional sentiment May 2026'})` → [2026-05-20] Sensex today | Stock Market Highlights: Stock markets rebound; Sensex climbs 117 points
- `get_market_context({'keyword': 'Bitcoin May 22'})` → No related markets found for 'Bitcoin May 22'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*