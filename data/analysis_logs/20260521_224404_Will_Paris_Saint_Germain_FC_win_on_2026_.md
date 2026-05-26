# Market Analysis — 2026-05-21 22:44 UTC

## Market
- **Question:** Will Paris Saint-Germain FC win on 2026-05-30?
- **Category:** other
- **YES Price:** 41.0%
- **Days Left:** 8
- **Volume 24h:** $53,893
- **Liquidity:** $254,822

## Statistical Prior
- **p_base:** 32.0%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 9.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,633 (+0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,517 (+0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- [CAUSAL CHAINS] Relevant cause-effect patterns:
- → Major AI model release → benchmark competition → sector excitement
- → AI regulation proposed → uncertainty → AI stocks fall short-term
- → AI chip shortage → NVIDIA revenue beats → AI infrastructure stocks rally
- → AI energy demand → data center power stocks rally

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: paris saint-germain 2026-05-30
- [Bing News]
- [Wed, 13 May 2026] paris saint-germain 2026-05-30
- → The goalkeepers are training specifically to anticipate Arsenal's set-piece plays, fine-tuning details ahead of the Champions League final in Budape
- [Sun, 10 May 2026] The Incredible Training of Paris Saint-Germain Goalkeepers for the Champions League Final Against Arsenal
- → There is growing optimism inside Paris Saint-Germain that Achraf Hakimi could be fit in time for the UEFA Champions League final on May 30.
- [Sun, 17 May 2026] Paris Saint-Germain Optimistic About Hakimi’s Return for Champions League Final
- → Ousmane Demb&#233;l&#233; left the pitch prematurely during Paris Saint-Germain’s last championship match. Big alert for Paris Saint-Germain. Establ

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 32.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** SPORTS_MATCH_FINAL
- **Catalyst Strength:** 0.30

### Reasoning
Market identifies PSG vs Arsenal Champions League Final on May 30, 2026. YES priced at 41% appears reasonably calibrated for an underdog in a CL final (base rate 32% suggests slight upward movement). Research confirms: (1) PSG clinched Ligue 1 title April 28, (2) PSG beat Bayern Munich in semi-finals to reach final, (3) PSG lost to Paris FC before final (mixed recent form). No concrete evidence found that 41% significantly misprices PSG's true win probability. Champions League finals between top clubs typically have 35-45% underdog probability. The 82% win rate for 'OTHER' category trades is from small sample (n=11) and may not apply to high-profile sports finals. Without specific injury news, tactical analysis, or venue advantage data that would shift probability >5% from current pricing, no actionable edge exists. SKIP as market appears efficient.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'soccer', 'team': 'Paris Saint-Germain'})` → No injury data found for soccer Paris Saint-Germain
- `search_web({'query': 'Paris Saint-Germain match May 30 2026 fixture schedule'})` → [Wed, 06 May 2026] Google News
[Thu, 14 May 2026] 2025/26 Champions League: All the fixtures and res
- `search_web({'query': 'PSG upcoming match May 2026 opponent'})` → [Thu, 07 May 2026] Google News
[Thu, 14 May 2026] PSG can win Ligue 1 if rival Lens drops points whi
- `search_web({'query': 'Champions League final 2026 date venue'})` → [Tue, 19 May 2026] Google News
[Mon, 11 May 2026] UEFA Women’s Champions League Final 2026 at a glan
- `search_web({'query': 'PSG Champions League semi-final 2026 opponent'})` → [Tue, 28 Apr 2026] Google News
[Wed, 15 Apr 2026] Champions League semi-finals: Head-to-head records
- `search_web({'query': '"Paris Saint-Germain" "May 30" 2026 match'})` → [Thu, 07 May 2026] Google News
[Sun, 17 May 2026] Paris Saint-Germain returns to Champions League fi
- `search_web({'query': 'UEFA Super Cup 2026 date PSG'})` → [Wed, 20 May 2026] Google News
[Mon, 11 May 2026] When and where is the 2026 UEFA Super Cup? Date, t
- `get_odds({'sport': 'soccer_epl'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'PSG vs Arsenal Champions League final May 30 2026 odds prediction'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Champions League final predictions: Arsenal vs PSG
- `search_web({'query': 'Arsenal vs PSG Champions League final 2026 form team news'})` → [Wed, 06 May 2026] Google News
[Mon, 27 Apr 2026] Champions League final 2026: Date, time, venue, &a
- `search_web({'query': '"PSG" "Arsenal" Champions League final 2026 favorite odds winner prediction'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Champions League final predictions: Arsenal vs PSG
- `get_market_context({'keyword': 'PSG Arsenal Champions League'})` → No related markets found for 'PSG Arsenal Champions League'
- `search_web({'query': 'Arsenal vs PSG Champions League final 2026 who is favorite to win'})` → [Wed, 20 May 2026] Google News
[Fri, 08 May 2026] Champions League final predictions: Arsenal vs PSG
- `search_web({'query': 'PSG vs Arsenal form 2026 recent results'})` → [Wed, 20 May 2026] Google News
[Wed, 06 May 2026] Champions League final predictions: Arsenal vs PSG

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*