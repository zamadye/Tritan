# Market Analysis — 2026-05-17 12:52 UTC

## Market
- **Question:** Iran closes its airspace by May 21?
- **Category:** geopolitik
- **YES Price:** 12.0%
- **Days Left:** 3
- **Volume 24h:** $114,423
- **Liquidity:** $69,077

## Statistical Prior
- **p_base:** 3.0%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 9.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,425 (+0.5% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,381 (+0.5% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%
- → Iran nuclear deal progress → sanctions ease → oil supply increases → oil price falls
- → Iran ceasefire → oil price -5-10% → risk-ON → equities/crypto rally
- → Iran military strike → oil spike → global inflation → Fed hawkish

### Multi-Source
- [MULTI-SOURCE NEWS] 5 sources for: iran closes airspace
- [Bing News]
- [Thu, 15 Jan 2026] iran closes airspace
- → TEMPO.CO, Jakarta - Iran temporarily closed its airspace to all flights except international flights to and from Iran with official permission on We
- [Sun, 03 May 2026] Iran Closes Airspace Amid Rising Protests and Regional Tensions
- → Red Cross warns of renewed Iran attacks amid airspace closure concerns. Iran closes its airspace by May 8 at 14.5% YES, by May 31 at 39% YES.
- [Tue, 05 May 2026] Red Cross warns of renewed Iran attacks amid airspace closure concerns
- → The market for “Iran closes its airspace by May 8?” is currently priced at 15.5% YES, down from 20% over the past 24 hours. The market for “Iran clo

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 1.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.15

### Reasoning
Iran airspace closure at 12% represents 4x the base rate (3%), suggesting narrative/fear premium. Search reveals only historical past closures (2025-2026 events), no breaking news indicating imminent closure by May 21. This is a multi-outcome geopolitical longshot where crowd overprices tail risk. Pattern shows 87% WR on geopolitik NO bets. Past decisions correctly flagged no statistical edge. Fear sentiment may be inflating price without specific catalyst. Longshot strategy applies: 3-15% range with no specific evidence = BET_NO.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=9%<10%

## Tool Calls
- `search_web({'query': 'Iran airspace closure May 2025'})` → [Thu, 23 Apr 2026] Google News
[Mon, 02 Mar 2026] India extends airspace closure for Pakistan till M
- `search_web({'query': 'Iran aviation news today 2025'})` → [Wed, 01 Apr 2026] Google News
[Mon, 23 Jun 2025] What happened to Middle East air travel in just 33
- `search_web({'query': 'Iran airspace closure flight ban April 2025'})` → [Mon, 02 Mar 2026] Google News
[Thu, 05 Mar 2026] Airlines are being squeezed into this sliver of sk
- `search_web({'query': 'Iran US tensions airspace risk commercial flights'})` → [Wed, 14 Jan 2026] Google News
[Wed, 18 Feb 2026] Iran closes airspace to commercial aircraft for ho
- `get_market_context({'keyword': 'Iran airspace'})` → No related markets found for 'Iran airspace'
- `search_web({'query': 'Iran military airspace closure commercial flights 2025'})` → [Thu, 15 Jan 2026] Google News
[Thu, 15 Jan 2026] Iran temporarily closes airspace with US attack 'i

## Outcome
**❌ LOSS** | P&L: $-0.06 | Resolved: EXIT

---
*Mode: LIVE | DRY_RUN: true*