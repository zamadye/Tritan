# Market Analysis — 2026-05-17 22:15 UTC

## Market
- **Question:** US x Iran permanent peace deal by June 30, 2026?
- **Category:** geopolitik
- **YES Price:** 26.0%
- **Days Left:** 13
- **Volume 24h:** $119,203
- **Liquidity:** $354,654

## Statistical Prior
- **p_base:** 11.2%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 14.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,250 (+0.1% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,061 (-0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%
- → Iran nuclear deal progress → sanctions ease → oil supply increases → oil price falls
- → Iran ceasefire → oil price -5-10% → risk-ON → equities/crypto rally
- → Iran military strike → oil spike → global inflation → Fed hawkish

### Multi-Source
- [MULTI-SOURCE NEWS] 5 sources for: iran permanent peace deal june
- [Bing News]
- [Sun, 17 May 2026] iran permanent peace deal june
- → Trump hints at military action against Iran, reducing peace deal odds. Permanent peace deal by June 30, 2026 at 12.5% YES.
- [Sun, 17 May 2026] Trump hints at military action against Iran, impacting peace deal odds
- → Trump warns Iran, escalating tensions and reducing peace deal prospects. Israel-Iran peace deal by June 30, 2026 at 12.5% YES.
- [Sun, 17 May 2026] Trump warns Iran, escalating tensions and impacting peace deal prospects
- → Donald Trump said Chinese President Xi Jinping offered to help the US negotiate with Iran to reopen the Strait of Hormuz. Trump told Fox News that C

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 1.2%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** GEOPOLITICAL_DETERIORATION
- **Catalyst Strength:** 0.75

### Reasoning
Market at 26% overprices probability given: (1) Trump's May 17 escalation directly impacting peace prospects, (2) ceasefire fragile and facing collapse, (3) only ~40 days remain for comprehensive permanent deal, (4) gap between ceasefire and permanent peace is enormous, (5) war costs at $29B create domestic political pressure against concessions. Crowd appears anchored to ceasefire news without fully discounting escalatory trajectory and implausibility of permanent deal timeline.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'US Iran peace deal negotiations 2025 2026'})` → [Tue, 21 Apr 2026] Google News
[Tue, 21 Apr 2026] Tehran and Trump Send Mixed Signals Ahead of Poten
- `search_web({'query': 'Iran US nuclear deal latest news June 2025'})` → [Tue, 12 May 2026] Google News
[Tue, 24 Feb 2026] The Iran Strikes, Explained: How We Got Here and W
- `get_market_context({'keyword': 'Iran'})` → [YES=50% vol=$2,310,420] Will Reza Pahlavi lead Iran in 2026?
- `search_web({'query': 'US Iran ceasefire deal April May 2026 status'})` → [Tue, 12 May 2026] Google News
[Mon, 04 May 2026] Pakistan scrambles to salvage US-Iran diplomacy as
- `search_web({'query': 'Trump Iran negotiations permanent peace agreement'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Trump warns Iran, escalating tensions and impactin

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*