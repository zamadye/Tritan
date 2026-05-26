# Market Analysis — 2026-05-20 16:17 UTC

## Market
- **Question:** US x Iran permanent peace deal by May 22, 2026?
- **Category:** geopolitik
- **YES Price:** 6.5%
- **Days Left:** 1
- **Volume 24h:** $970,782
- **Liquidity:** $85,110

## Statistical Prior
- **p_base:** 1.1%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 5.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,392 (+1.2% 24h) → risk-ON
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,443 (+1.3% 24h) → risk-ON

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%
- → Iran nuclear deal progress → sanctions ease → oil supply increases → oil price falls
- → Iran ceasefire → oil price -5-10% → risk-ON → equities/crypto rally
- → Iran military strike → oil spike → global inflation → Fed hawkish

### Multi-Source
- [MULTI-SOURCE NEWS] 5 sources for: iran permanent peace deal 2026
- [Bing News]
- [Tue, 19 May 2026] iran permanent peace deal 2026
- → Trump told reporters at the White House that he had been just &quot;an hour away&quot; from relaunching Washington's attacks on Iran before postponi
- [Wed, 13 May 2026] US, Iran trade threats but Trump says Tehran wants peace deal
- → Israeli strikes on Iranian universities escalate tensions. Permanent peace deal by June 30, 2026 at 16.5% YES.
- [Mon, 18 May 2026] Israeli strikes on Iranian universities escalate conflict, impact peace deal prospects
- → President Trump has considered himself an effective dealmaker above all else, but he appears to have hit a wall with Iran as his tough talk, threats

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 1.1%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market expires TOMORROW (May 22). News flow is NEGATIVE: Trump rejected Iran's proposal as 'unacceptable' (May 11), called ceasefire 'life support' (May 6), said he's in 'no hurry'. Only positive signal is May 18 attack cancellation for 'serious negotiations' but nothing materialized in 3 days since. For a PERMANENT peace deal to be signed in 24 hours would require sudden major breakthrough with zero current indication. Market at 6% appears overpriced vs my ~2% estimate, but edge (~4pp) is too small given: (1) GEOPOLITIK pattern WR=11% (WEAK), (2) potential for sudden unexpected announcement, (3) low confidence below 0.55 threshold. Previous decision was also SKIP at 45% confidence - situation hasn't materially changed.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'US Iran permanent peace deal negotiations May 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 11 May 2026] Iran has responded to latest US peace proposal, Te
- `search_web({'query': 'US Iran peace talks May 21 2026 latest news'})` → [Tue, 05 May 2026] Google News
[Tue, 21 Apr 2026] U.S. And Iran Fail to Agree on Peace Deal After 21
- `get_market_context({'keyword': 'Iran peace deal'})` → No related markets found for 'Iran peace deal'
- `search_web({'query': '"May 21 2026" Iran US deal signed agreement'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Holland &amp; Knight Health Dose: May 19, 2026 - H
- `search_web({'query': 'Trump Iran peace deal announcement today'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] Trump calls off scheduled attack on Iran amid "ser
- `get_market_context({'keyword': 'Iran'})` → [YES=50% vol=$2,580,615] Will Trump say "Iran" during events with Xi Jinping?
- `get_market_context({'keyword': 'Iran'})` → [YES=50% vol=$2,580,615] Will Trump say "Iran" during events with Xi Jinping?

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*