# Market Analysis — 2026-05-21 09:30 UTC

## Market
- **Question:** Israel closes its airspace by May 24?
- **Category:** geopolitik
- **YES Price:** 10.0%
- **Days Left:** 2
- **Volume 24h:** $72,680
- **Liquidity:** $35,600

## Statistical Prior
- **p_base:** 2.2%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,871 (+0.7% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,850 (+0.6% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Major AI model release → benchmark competition → sector excitement
- → AI regulation proposed → uncertainty → AI stocks fall short-term
- → AI chip shortage → NVIDIA revenue beats → AI infrastructure stocks rally
- → AI energy demand → data center power stocks rally

### Multi-Source
- [MULTI-SOURCE NEWS] 5 sources for: israel closes airspace
- [Bing News]
- [Sat, 28 Feb 2026] israel closes airspace
- → TEMPO.CO, Jakarta Majid Akhavan, the spokesperson of the Iran Civil Aviation Organization, announced in an interview with the Mehr news agency on Sa
- [Sun, 17 May 2026] Iran Closes Airspace as Israel Launches Attack
- → Key Takeaways – The movement of the Turkish flotilla towards Israel appears to increase the potential for Israeli airspace closure. – Market pricing
- [Fri, 08 May 2026] Turkish flotilla nears Israel, Netanyahu to discuss defense response
- → When a corridor closes, replacement routings add anywhere from forty minutes to three hours per sector, which translates into extra fuel burn, paylo

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 2.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
No verifiable edge. Market at 10% appropriately prices ongoing US-Israel-Iran conflict risk (precedent: Feb 2026 airspace closure). However, no breaking catalyst suggests imminent closure within 2 days. Iran appears in negotiation phase ('reviewing' US response) rather than imminent escalation. GEOPOLITIK category shows weak 17% WR. Market likely fairly priced at current level.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'Israel airspace closure May 2025'})` → [Mon, 27 Apr 2026] Google News
[Tue, 17 Mar 2026] Middle East Airspace – Current Operational Picture
- `search_web({'query': 'Israel airspace closed threat missile attack'})` → [Mon, 27 Apr 2026] Google News
[Sat, 28 Feb 2026] Middle East Airspace – Current Operational Picture
- `search_web({'query': 'Israel Iran conflict May 2025 airspace'})` → [Thu, 07 May 2026] Google News
[Sun, 01 Mar 2026] Trump reportedly paused Hormuz op after Saudis den
- `get_market_context({'keyword': 'Israel airspace'})` → No related markets found for 'Israel airspace'
- `search_web({'query': 'Israel closes airspace May 2026 threat'})` → [Mon, 27 Apr 2026] Google News
[Sat, 02 May 2026] Middle East Airspace – Current Operational Picture
- `search_web({'query': 'Iran missile attack Israel airspace closure 2026'})` → [Mon, 27 Apr 2026] Google News
[Sat, 28 Feb 2026] Middle East Airspace – Current Operational Picture
- `search_web({'query': 'Israel Iran tensions latest news May 2026'})` → [Thu, 21 May 2026] Google News
[Wed, 20 May 2026] Iran war day 83: Tehran ‘reviewing’ latest US resp

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*