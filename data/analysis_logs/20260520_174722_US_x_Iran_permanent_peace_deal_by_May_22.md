# Market Analysis — 2026-05-20 17:47 UTC

## Market
- **Question:** US x Iran permanent peace deal by May 22, 2026?
- **Category:** geopolitik
- **YES Price:** 6.6%
- **Days Left:** 1
- **Volume 24h:** $1,023,206
- **Liquidity:** $74,271

## Statistical Prior
- **p_base:** 1.1%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 5.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,523 (+0.9% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,586 (+1.1% 24h) → risk-ON

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%
- → Iran nuclear deal progress → sanctions ease → oil supply increases → oil price falls
- → Iran ceasefire → oil price -5-10% → risk-ON → equities/crypto rally
- → Iran military strike → oil spike → global inflation → Fed hawkish

### Multi-Source
- [MULTI-SOURCE NEWS] 4 sources for: iran permanent peace deal 2026
- [Bing News]
- [Tue, 19 May 2026] iran permanent peace deal 2026
- → Trump told reporters at the White House that he had been just &quot;an hour away&quot; from relaunching Washington's attacks on Iran before postponi
- [Wed, 13 May 2026] US, Iran trade threats but Trump says Tehran wants peace deal
- → Israeli strikes on Iranian universities escalate tensions. Permanent peace deal by June 30, 2026 at 16.5% YES.
- [Mon, 18 May 2026] Israeli strikes on Iranian universities escalate conflict, impact peace deal prospects
- → US President Donald Trump said Tehran repeatedly expressed interest in signing an agreement but accused Iranian leaders of changing their position d

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 1.1%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** DIPLOMATIC_PROGRESS
- **Catalyst Strength:** 0.30

### Reasoning
Market expires TOMORROW with negotiations still incomplete. While talks are 'in final stages,' permanent peace deal is far broader than nuclear agreement. Previous SKIP decisions with 35% confidence remain valid. Edge on NO is only 2-4% - too thin for risky final-day liquidity. GEOPOLITIK pattern weak (11% WR).

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'US Iran peace deal negotiations May 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Trump says negotiations with Iran in final stages,
- `search_web({'query': 'Iran nuclear deal agreement latest news May 22 2026'})` → [Fri, 15 May 2026] Google News
[Wed, 20 May 2026] Trump says he’s OK with Iran suspending nuke enric
- `get_market_context({'keyword': 'Iran deal peace'})` → No related markets found for 'Iran deal peace'
- `search_web({'query': '"US Iran deal" signed agreement May 21 22 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] US-Israel-Iran War Latest Update: ‘Hit Iran Even H
- `search_web({'query': 'Iran nuclear enrichment uranium deal Trump 2026 latest'})` → [Wed, 20 May 2026] Google News
[Fri, 15 May 2026] Trump says Iran attack on ‘hold’: What we know abo

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*