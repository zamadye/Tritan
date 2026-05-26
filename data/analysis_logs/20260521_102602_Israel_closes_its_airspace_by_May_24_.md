# Market Analysis — 2026-05-21 10:26 UTC

## Market
- **Question:** Israel closes its airspace by May 24?
- **Category:** geopolitik
- **YES Price:** 9.0%
- **Days Left:** 2
- **Volume 24h:** $70,200
- **Liquidity:** $51,759

## Statistical Prior
- **p_base:** 1.8%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 7.1%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,573 (+0.1% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,568 (+0.0% 24h) → neutral

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
- [Sat, 09 May 2026] Iran Closes Airspace as Israel Launches Attack
- → Israel demands strikes on Iran's energy sites amid peace deal doubts. Permanent peace deal by June 30, 2026 at 16.5% YES.
- [Sun, 10 May 2026] Israel demands strikes on Iran’s energy sites amid peace deal doubts
- → Iran deployed drones in the Strait of Hormuz amid rising tensions. Iran closes its airspace by May 31 at 29.5% YES, Israel at 22.5% YES.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 1.8%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Ongoing Iran conflict explains elevated price (9% vs 2% base rate), but de-escalation signals (Trump calling off attacks, serious negotiations) reduce near-term probability. No direct evidence of imminent full Israeli airspace closure within 2 days. Mixed signals with weak edge - market appears approximately fairly priced.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `search_web({'query': 'Israel airspace closure May 2025'})` → [Mon, 27 Apr 2026] Google News
[Tue, 17 Mar 2026] Middle East Airspace – Current Operational Picture
- `search_web({'query': 'Israel Iran conflict airspace closure 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] El Al posts loss in first quarter of 2026 amid air
- `get_market_context({'keyword': 'Israel airspace'})` → No related markets found for 'Israel airspace'
- `get_market_context({'keyword': 'Israel Iran war'})` → No related markets found for 'Israel Iran war'
- `search_web({'query': 'Israel airspace closed Iran attack April 2026'})` → [Mon, 27 Apr 2026] Google News
[Wed, 13 May 2026] Middle East Airspace – Current Operational Picture
- `search_web({'query': 'Israel closes airspace 2026 Iran war'})` → [Thu, 07 May 2026] Google News
[Mon, 30 Mar 2026] Trump reportedly paused Hormuz op after Saudis den
- `search_web({'query': 'Israel airspace status today April 27 2026'})` → [Mon, 27 Apr 2026] Google News
[Mon, 11 May 2026] Middle East Airspace – Current Operational Picture
- `search_web({'query': 'Israel Iran conflict latest news escalation 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Trump calls off scheduled attack on Iran amid "ser

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*