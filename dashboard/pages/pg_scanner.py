import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import streamlit as st
from dashboard.components.shared import get_current_mode, compute_stats

def render():
    mode = get_current_mode()
    s    = compute_stats(mode)

    st.markdown("<h2>🔍 Market Scanner</h2>", unsafe_allow_html=True)

    c1, c2 = st.columns([1,4])
    if c1.button("🔍 Scan Now", type="primary", use_container_width=True):
        with st.spinner("Fetching candidates..."):
            from agent.scanner import get_candidate_markets
            st.session_state["scan_markets"] = get_candidate_markets()

    markets = st.session_state.get("scan_markets", [])
    if not markets:
        st.markdown("<div style='color:#6b7280;font-size:13px;margin-top:12px'>Click Scan Now to fetch live market candidates.</div>", unsafe_allow_html=True)
        return

    c2.markdown(f"<div style='font-size:12px;color:#6b7280;padding-top:10px'>{len(markets)} candidates found</div>", unsafe_allow_html=True)
    st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

    for m in markets:
        days = m.get("days_left","?")
        with st.expander(f"p={m['price']:.2%}  ·  vol ${m['volume_24h']:,.0f}  ·  d+{days}  ·  {m['question'][:62]}"):
            c1,c2,c3 = st.columns(3)
            c1.metric("Market Price", f"{m['price']:.2%}")
            c2.metric("Volume 24h",   f"${m['volume_24h']:,.0f}")
            c3.metric("Days Left",    str(days))

            col_a, col_b = st.columns([1,4])
            if col_a.button("🧠 Analyze", key=f"ana_{m['id']}", use_container_width=True):
                with st.spinner("Analyzing..."):
                    from agent.analyzer import estimate_probability, fetch_news
                    from agent.learner import get_evolution_context
                    result = estimate_probability(m, fetch_news(m), get_evolution_context(mode))
                st.session_state[f"res_{m['id']}"] = result

            result = st.session_state.get(f"res_{m['id']}")
            if result:
                side = result.get("recommended_side","SKIP")
                sc   = "#22c55e" if side=="YES" else "#ef4444" if side=="NO" else "#f59e0b"
                st.markdown(
                    f"<div style='display:flex;gap:16px;align-items:center;margin:8px 0'>"
                    f"<span style='font-size:18px;font-weight:700;color:{sc}'>{side}</span>"
                    f"<span style='font-size:13px;color:#94a3b8'>p_true {result.get('p_true',0):.2%} · "
                    f"edge {result.get('edge',0):+.2%} · conf {result.get('confidence',0):.0%}</span></div>",
                    unsafe_allow_html=True
                )
                if result.get("reasoning_summary"):
                    st.info(result["reasoning_summary"])
                if result.get("calibration_applied"):
                    st.markdown(f"<div style='font-size:11px;color:#6b7280'>⚙️ {result['calibration_applied']}</div>", unsafe_allow_html=True)

                if side != "SKIP":
                    if st.button(f"💰 Place Bet {side}", key=f"bet_{m['id']}", type="primary"):
                        from agent.executor import execute_trade
                        from agent.sizer import calculate_position
                        sz, sd, _ = calculate_position(result["p_true"], m["price"], s["bankroll"])
                        if sd != "SKIP":
                            execute_trade(m, sd, sz, mode, None)
                            st.cache_data.clear(); st.success(f"✅ Bet {sd} ${sz:.2f}"); st.rerun()
                        else:
                            st.warning("Sizer returned SKIP — edge/RR too low.")
