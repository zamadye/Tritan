import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import streamlit as st
from dashboard.components.shared import load_evolution, load_trades, get_current_mode

def render():
    mode = get_current_mode()
    evo  = load_evolution()

    st.markdown("<h2>🧠 Evolution Learning</h2>", unsafe_allow_html=True)

    if not evo:
        st.info("No evolution data yet."); return

    oc = len(evo.get("overconfidence_patterns",[]))
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Resolved Trades",  evo.get("total_resolved",0))
    c2.metric("Win Rate",         f"{evo.get('overall_win_rate',0):.0%}")
    c3.metric("Momentum Lessons", len(evo.get("momentum_lessons",[])))
    c4.metric("Overconfidence",   f"{oc}x")

    st.divider()
    left, right = st.columns(2)

    with left:
        # Exit breakdown
        ep = evo.get("exit_patterns",{})
        if ep:
            st.markdown("<div class='card-title'>Exit Breakdown</div>", unsafe_allow_html=True)
            total_ep = sum(ep.values()) or 1
            colors = {"TAKE_PROFIT":"#22c55e","TRAILING_STOP":"#a5b4fc",
                      "STOP_LOSS":"#ef4444","TIME_LIMIT":"#f59e0b","RESOLVED":"#6b7280"}
            rows = ""
            for k, v in sorted(ep.items(), key=lambda x: -x[1]):
                c = colors.get(k,"#94a3b8"); pct = v/total_ep
                rows += (
                    f"<div class='stat-row'>"
                    f"<span style='color:{c};font-weight:600;width:130px'>{k}</span>"
                    f"<span style='flex:1;background:#1e1e3a;border-radius:4px;height:8px;margin:0 12px'>"
                    f"<span style='display:block;background:{c};width:{pct:.0%};height:8px;border-radius:4px'></span></span>"
                    f"<span style='color:#94a3b8;font-size:12px'>{v} ({pct:.0%})</span></div>"
                )
            st.markdown(f"<div class='card' style='padding:12px 16px'>{rows}</div>", unsafe_allow_html=True)

        # Price movement patterns
        pmp = evo.get("price_movement_patterns",{})
        if pmp:
            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
            st.markdown("<div class='card-title'>Entry Price Range Performance</div>", unsafe_allow_html=True)
            rows = ""
            for b, d in sorted(pmp.items()):
                wr = d["win_rate"]; pnl = d["avg_pnl"]; n = d["n"]
                wc = "#22c55e" if wr>=0.55 else "#f59e0b" if wr>=0.45 else "#ef4444"
                pc = "#22c55e" if pnl>0 else "#ef4444"
                rows += (
                    f"<div class='stat-row'>"
                    f"<span style='color:#94a3b8;width:80px'>{b}</span>"
                    f"<span style='color:{wc};font-weight:600'>WR {wr:.0%}</span>"
                    f"<span style='color:{pc};margin-left:12px'>avg ${pnl:+.2f}</span>"
                    f"<span style='color:#4b5563;margin-left:auto;font-size:11px'>n={n}</span></div>"
                )
            st.markdown(f"<div class='card' style='padding:12px 16px'>{rows}</div>", unsafe_allow_html=True)

    with right:
        # What worked
        ml = evo.get("momentum_lessons",[])
        if ml:
            st.markdown("<div class='card-title'>What Worked (Profitable Catalysts)</div>", unsafe_allow_html=True)
            for m in ml:
                pnl = m.get("pnl",0) or 0
                with st.expander(f"✓ [{m.get('category','?')}] entry={m.get('entry_price',0):.2f} → ${pnl:+.2f} via {m.get('exit_reason','?')}"):
                    st.markdown(f"<div style='font-size:12px;color:#94a3b8'>{m.get('catalyst','')}</div>", unsafe_allow_html=True)

        # Recent mistakes
        rm = evo.get("recent_mistakes",[])
        if rm:
            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
            st.markdown("<div class='card-title'>Recent Losses</div>", unsafe_allow_html=True)
            for m in rm:
                with st.expander(f"✗ [{m.get('category','?')}] entry={m.get('entry_price',0):.2f} — {m.get('question','')[:45]}"):
                    st.warning(m.get("lesson","?"))
                    st.markdown(f"<div style='font-size:11px;color:#6b7280'>{m.get('reasoning','')}</div>", unsafe_allow_html=True)

        # LLM context preview
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        st.markdown("<div class='card-title'>LLM Context</div>", unsafe_allow_html=True)
        from agent.learner import get_evolution_context
        ctx = get_evolution_context(mode)
        st.code(ctx[:600] if ctx else "Empty", language=None)

    st.divider()
    if st.button("🔄 Regenerate Lessons", type="primary"):
        trades = load_trades(mode)
        from agent.learner import _generate_evolution_lessons
        _generate_evolution_lessons(trades, mode)
        st.cache_data.clear(); st.success("Regenerated!"); st.rerun()
