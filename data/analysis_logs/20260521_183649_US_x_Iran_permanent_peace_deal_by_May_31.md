# Market Analysis — 2026-05-21 18:36 UTC

## Market
- **Question:** US x Iran permanent peace deal by May 31, 2026?
- **Category:** geopolitik
- **YES Price:** 21.0%
- **Days Left:** 9
- **Volume 24h:** $4,752,565
- **Liquidity:** $359,550

## Statistical Prior
- **p_base:** 7.7%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 13.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,751 (+0.4% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,716 (+0.3% 24h) → neutral
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
- [MULTI-SOURCE NEWS] 5 sources for: iran permanent peace deal 2026
- [Bing News]
- [Thu, 21 May 2026] iran permanent peace deal 2026
- → Iran says it's considering the latest U.S. peace offer, as President Trump says he's willing to wait &quot;a couple of days&quot; for a response.
- [Tue, 19 May 2026] Live Updates: Iran says it's mulling latest U.S. peace proposal, Trump says he'll wait &quot;a couple of days&quot;
- → Trump told reporters at the White House that he had been just &quot;an hour away&quot; from relaunching Washington's attacks on Iran before postponi
- [Wed, 13 May 2026] US, Iran trade threats but Trump says Tehran wants peace deal
- → Israeli strikes on Iranian universities escalate tensions. Permanent peace deal by June 30, 2026 at 16.5% YES.

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 1.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** HARD_LINE_STANCE
- **Catalyst Strength:** 0.80

### Reasoning
Supreme Leader's May 21 statement (enriched uranium must stay in Iran) creates direct obstacle; 9 days insufficient for permanent deal complexity; market overpriced at 21% vs 8% base rate; previous similar market decided NO with same reasoning

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'US Iran permanent peace deal negotiations May 2026'})` → [Thu, 21 May 2026] Google News
[Mon, 18 May 2026] Iran reviews US proposal to end war as Pakistan st
- `search_web({'query': 'Iran Supreme Leader enriched uranium stance May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Exclusive: Supreme Leader says enriched uranium mu
- `get_market_context({'keyword': 'Iran peace deal'})` → No related markets found for 'Iran peace deal'
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $77,714.00 | 24h: +0.33%

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*