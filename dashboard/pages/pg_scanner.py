import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import streamlit as st
from dashboard.components.shared import get_current_mode, compute_stats

def render():
    mode = get_current_mode()
    s    = compute_stats(mode)

    st.subheader("🔍 Market Scanner")
    if st.button("🔍 Scan Markets Now", type="primary"):
        with st.spinner("Fetching candidates..."):
            from agent.scanner import get_candidate_markets
            st.session_state["scan_markets"] = get_candidate_markets()

    markets = st.session_state.get("scan_markets", [])
    if not markets:
        st.info("Click 'Scan Markets Now' to fetch live candidates."); return

    st.caption(f"{len(markets)} candidates found")
    for m in markets:
        with st.expander(f"p={m['price']:.2%}  vol=${m['volume_24h']:,.0f}  d+{m.get('days_left','?')}  |  {m['question'][:60]}"):
            c1,c2,c3 = st.columns(3)
            c1.metric("Market Price", f"{m['price']:.2%}")
            c2.metric("Volume 24h",   f"${m['volume_24h']:,.0f}")
            c3.metric("Days Left",    str(m.get("days_left","?")))

            if st.button("🧠 Analyze", key=f"ana_{m['id']}"):
                with st.spinner("Analyzing..."):
                    from agent.analyzer import estimate_probability, fetch_news
                    from agent.learner import get_evolution_context
                    news    = fetch_news(m)
                    evo_ctx = get_evolution_context(mode)
                    result  = estimate_probability(m, news, evo_ctx)
                st.session_state[f"res_{m['id']}"] = result

            result = st.session_state.get(f"res_{m['id']}")
            if result:
                side = result.get("recommended_side","SKIP")
                col  = "green" if side!="SKIP" else "orange"
                st.markdown(f"**Decision:** :{col}[**{side}**]")
                r1,r2,r3 = st.columns(3)
                r1.metric("p_true",     f"{result.get('p_true',0):.2%}")
                r2.metric("Edge",       f"{result.get('edge',0):+.2%}")
                r3.metric("Confidence", f"{result.get('confidence',0):.0%}")
                if result.get("reasoning_summary"): st.info(result["reasoning_summary"])

                if side != "SKIP" and st.button(f"💰 Place Bet {side}", key=f"bet_{m['id']}"):
                    from agent.executor import execute_trade
                    from agent.sizer import calculate_position
                    sz, sd, _ = calculate_position(result["p_true"], m["price"], s["bankroll"])
                    if sd != "SKIP":
                        execute_trade(m, sd, sz, mode, None)
                        st.cache_data.clear(); st.success(f"✅ Bet {sd} ${sz:.2f}"); st.rerun()
                    else:
                        st.warning("Sizer returned SKIP — edge/RR too low.")
