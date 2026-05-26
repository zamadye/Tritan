# Market Analysis — 2026-05-21 19:51 UTC

## Market
- **Question:** Will the Iran ceasefire continue through July 31?
- **Category:** geopolitik
- **YES Price:** 51.0%
- **Days Left:** None
- **Volume 24h:** $5,455
- **Liquidity:** $10,566

## Statistical Prior
- **p_base:** 39.2%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 11.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,551 (-0.0% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,578 (+0.0% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%
- → Iran nuclear deal progress → sanctions ease → oil supply increases → oil price falls
- → Iran ceasefire → oil price -5-10% → risk-ON → equities/crypto rally
- → Iran military strike → oil spike → global inflation → Fed hawkish

### Multi-Source
- [MULTI-SOURCE NEWS] 5 sources for: iran ceasefire continue through july
- [Bing News]
- [] iran ceasefire continue through july
- [Al Jazeera]
- [Thu, 21 May 2026] Trump shifts between diplomacy and threats in Iran standoff
- [Thu, 21 May 2026] Iran’s World Cup hopes hit US visa hurdles
- [The Guardian]
- [Thu, 21 May 2026] Macron under pressure over reparatory justice for France’s role in slave trade

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 35.2%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** GEOPOLITICAL_STALEMATE
- **Catalyst Strength:** 0.60

### Reasoning
Market overprices YES at 51% vs historical resolution rate of 44.7% (n=13,967) and base rate of 39% (gap -12%). News indicates stalled talks and uncertainty about ceasefire extension. Past decisions on very similar markets (June 15 and June 30) recommend NO with 62-65% confidence, citing consistent overpricing. Geopolitics category shows weak win rate (20%), and news context suggests potential for breakdown with Iran stating 'fully prepared for war' as deadline looms.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'Iran ceasefire July 2025 news'})` → [Wed, 11 Feb 2026] Google News
[Sat, 28 Feb 2026] Israel and Iran agree to ceasefire to bring end to
- `search_web({'query': 'Iran ceasefire extension July 31 2025'})` → [Tue, 19 May 2026] Google News
[Sat, 16 May 2026] Israel-Hamas War (Gaza Conflict) | Explanation, Su
- `get_market_context({'keyword': 'Iran ceasefire'})` → No related markets found for 'Iran ceasefire'
- `get_market_context({'keyword': 'Iran'})` → [YES=50% vol=$8,009,028] Will Trump say "Iran" during events with Xi Jinping?
[YES=50% vol=$4,975,14
- `search_web({'query': 'Iran ceasefire status July 2025'})` → [Tue, 21 Apr 2026] Google News
[Mon, 21 Jul 2025] Ceasefire deadline looms as talks with Iran remain
- `search_web({'query': 'Iran Israel ceasefire news today 2025'})` → [Sat, 16 May 2026] Google News
[Tue, 24 Mar 2026] BBC Learning English - Learning English from the N
- `search_web({'query': '"Ceasefire deadline looms" Iran talks uncertain July 2025'})` → [Tue, 21 Apr 2026] Google News
[Tue, 21 Apr 2026] Ceasefire deadline looms as talks with Iran remain
- `search_web({'query': 'site:thecentersquare.com ceasefire deadline looms Iran talks uncertain'})` → [Tue, 21 Apr 2026] Google News
[Mon, 24 Nov 2025] Ceasefire deadline looms as talks with Iran remain

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*