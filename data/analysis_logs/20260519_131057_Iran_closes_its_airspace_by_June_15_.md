# Market Analysis — 2026-05-19 13:10 UTC

## Market
- **Question:** Iran closes its airspace by June 15?
- **Category:** geopolitik
- **YES Price:** 52.0%
- **Days Left:** 26
- **Volume 24h:** $5,774
- **Liquidity:** $33,683

## Statistical Prior
- **p_base:** 40.6%
- **Source:** logistic:geopolitik
- **N (historical):** 135
- **Raw gap:** 11.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,890 (-0.7% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,720 (-1.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Iran-US tension escalates → oil supply risk → WTI crude +5-15%
- → Iran nuclear deal progress → sanctions ease → oil supply increases → oil price falls
- → Iran ceasefire → oil price -5-10% → risk-ON → equities/crypto rally
- → Iran military strike → oil spike → global inflation → Fed hawkish

### Multi-Source
- [MULTI-SOURCE NEWS] 5 sources for: iran closes airspace june
- [Bing News]
- [Wed, 13 May 2026] iran closes airspace june
- → Saudi Arabia launched airstrikes on Iran, increasing tensions. Iran closing its airspace by May 31 at 38.5% YES.
- [Sun, 17 May 2026] Saudi Arabia launches airstrikes on Iran, escalating regional conflict
- → Israeli military strikes on Doha and Tehran escalate tensions. Permanent peace deal by June 30, 2026 at 13% YES.
- [] Israeli military strikes on Doha, Tehran escalate Iran conflict
- [Al Jazeera]

## LLM Decision
- **Action:** NO
- **Confidence:** 62%
- **p_true:** 38.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** DE-ESCALATION_SIGNAL
- **Catalyst Strength:** 0.55

### Reasoning
Market at 52% overprices YES vs historical base rate (41%) and stat signal (44.7% at this price). Key evidence: (1) UAE LIFTED all airspace restrictions on May 18 - de-escalation signal; (2) Iran reopened airspace May 14-15 with no concrete evidence of imminent new closure; (3) Peace deal market at 50% suggests negotiated outcome possible. GEOPOLITIK category has weak 17% WR pattern. While active US-Iran conflict exists, crowd appears to overweight recent headline volatility while ignoring base rates and de-escalation signals. NO offers ~8% edge (52% market vs 44% true prob).

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'Iran airspace closure June 15 2025'})` → [Sat, 16 May 2026] Google News
[Sun, 15 Jun 2025] Airspace closure: UAE airlines announce flight can
- `search_web({'query': 'Iran airspace closure news May 2026'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] Predicting Peace: Iran Deal Bets - StartupHub.ai
[
- `search_web({'query': 'Iran airspace restrictions May 2026'})` → [Tue, 05 May 2026] Google News
[Sun, 03 May 2026] UAE restricts airspace after Iranian missile, dron
- `search_web({'query': 'Iran war airspace closure civilian flights'})` → [Mon, 18 May 2026] Google News
[Sun, 03 May 2026] Dubai and Middle East flight disruption: the lates
- `get_market_context({'keyword': 'Iran airspace'})` → No related markets found for 'Iran airspace'
- `get_market_context({'keyword': 'Iran'})` → [YES=50% vol=$2,518,580] Will Trump say "Iran" during events with Xi Jinping?
[YES=50% vol=$1,673,35
- `search_web({'query': '"Iran airspace" closed June 2026'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Israeli military strikes on Doha, Tehran escalate 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*