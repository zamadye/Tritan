import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import streamlit as st
import plotly.graph_objects as go
from collections import defaultdict
from dashboard.components.shared import (
    compute_stats, load_evolution, load_bankroll,
    service_active, get_current_mode, switch_mode,
    save_env, badge
)

def render():
    mode   = get_current_mode()
    active = service_active()
    s      = compute_stats(mode)
    bk     = load_bankroll()
    evo    = load_evolution()
    oc     = len(evo.get("overconfidence_patterns", []))

    # ── agent controls ────────────────────────────────────────────────────────
    c1,c2,c3,c4,c5 = st.columns([1,1,1,1.6,1])
    if c1.button("▶ Start",    use_container_width=True): subprocess.run(["systemctl","start","polymarket-agent"]);   st.rerun()
    if c2.button("⏹ Stop",     use_container_width=True): subprocess.run(["systemctl","stop","polymarket-agent"]);    st.rerun()
    if c3.button("🔄 Restart", use_container_width=True): subprocess.run(["systemctl","restart","polymarket-agent"]); st.rerun()
    new_mode = "live" if mode=="demo" else "demo"
    if c4.button(f"⇄ Switch to {'LIVE 💰' if mode=='demo' else 'DEMO 📝'}", use_container_width=True):
        st.session_state["confirm_switch"] = True
    if c5.button("🗑 Refresh", use_container_width=True):
        st.cache_data.clear(); st.rerun()

    if st.session_state.get("confirm_switch"):
        col_warn, col_y, col_n = st.columns([4,1,1])
        col_warn.warning(f"⚠️ Switch to **{new_mode.upper()}**? Agent will restart.")
        if col_y.button("✅ Yes", key="sw_yes"): switch_mode(new_mode); st.session_state["confirm_switch"]=False; st.cache_data.clear(); st.rerun()
        if col_n.button("❌ No",  key="sw_no"):  st.session_state["confirm_switch"]=False; st.rerun()

    st.divider()

    # ── alerts ────────────────────────────────────────────────────────────────
    if oc >= 30:
        st.markdown(f"<div class='alert-banner'>⚠️ OVERCONFIDENCE {oc}x — hard cap 68%, penalty -{min(0.25,oc*0.005):.0%} active on all bets</div>", unsafe_allow_html=True)
    elif oc >= 10:
        st.warning(f"⚠️ Overconfidence {oc}x — penalty -{min(0.25,oc*0.005):.0%} applied")

    # ── KPI row with trend ────────────────────────────────────────────────────
    res = s["resolved"]
    last10 = res[-10:]; prev10 = res[-20:-10] if len(res)>=20 else []
    wr_l10 = sum(1 for t in last10 if t.get("prediction_correct"))/len(last10) if last10 else 0
    wr_p10 = sum(1 for t in prev10 if t.get("prediction_correct"))/len(prev10) if prev10 else wr_l10
    pnl_l10 = sum(t.get("pnl",0) for t in last10)
    pnl_p10 = sum(t.get("pnl",0) for t in prev10)

    m1,m2,m3,m4,m5,m6 = st.columns(6)
    m1.metric("💰 P&L",      f"${s['pnl']:+.2f}",  f"last10: ${pnl_l10:+.2f}")
    m2.metric("🎯 Win Rate", f"{s['wr']:.0%}",      f"last10: {wr_l10:.0%} {'↑' if wr_l10>wr_p10 else '↓' if wr_l10<wr_p10 else '→'}")
    m3.metric("⚖️ R:R",      f"{s['rr']:.2f}:1")
    m4.metric("📈 EV/trade", f"${s['ev']:+.3f}")
    m5.metric("🏦 Bankroll", f"${s['bankroll']:.2f}", f"-${s['deployed']:.2f} deployed")
    m6.metric("📂 Open",     str(len(s['open_t'])))

    st.divider()
    left, right = st.columns([3, 1])

    with left:
        st.subheader("Cumulative P&L")
        if res:
            srt = sorted(res, key=lambda x: x.get("resolved_at", x.get("timestamp","")))
            cum, colors, run = [], [], 0
            for t in srt:
                run += t.get("pnl",0); cum.append(round(run,2))
                colors.append("#00cc88" if t.get("prediction_correct") else "#ff4444")
            fig = go.Figure()
            fig.add_trace(go.Scatter(y=cum, mode="lines+markers",
                line=dict(color="#00cc88",width=2), marker=dict(color=colors,size=6),
                fill="tozeroy", fillcolor="rgba(0,204,136,0.07)",
                hovertemplate="Trade #%{x}<br>P&L: $%{y:.2f}<extra></extra>"))
            fig.add_hline(y=0, line_dash="dash", line_color="#444")
            fig.update_layout(height=240, margin=dict(l=0,r=0,t=4,b=0),
                plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#aaa"), xaxis_title="Trade #", yaxis_title="P&L ($)")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No resolved trades yet.")

        st.subheader("Performance by Category")
        cat_w, cat_l = defaultdict(int), defaultdict(int)
        for t in res:
            cat = t.get("category","") or "other"
            if t.get("prediction_correct"): cat_w[cat]+=1
            else: cat_l[cat]+=1
        cats = sorted(set(list(cat_w)+list(cat_l)))
        if cats:
            fig2 = go.Figure([
                go.Bar(name="Wins",   x=cats, y=[cat_w[c] for c in cats], marker_color="#00cc88"),
                go.Bar(name="Losses", x=cats, y=[cat_l[c] for c in cats], marker_color="#ff4444"),
            ])
            fig2.update_layout(barmode="group", height=200, margin=dict(l=0,r=0,t=4,b=0),
                plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#aaa"), legend=dict(orientation="h",y=1.1))
            st.plotly_chart(fig2, use_container_width=True)

    with right:
        level = bk.get("level",0)
        lc    = "#22c55e" if level>0 else "#ef4444" if level<0 else "#94a3b8"
        step  = float(os.getenv("BANKROLL_STEP_SIZE",0.10))
        mult  = max(0.5, min(2.0, 1.0+level*step))
        eff_k = round(float(os.getenv("KELLY_FRACTION",0.25))*mult, 4)
        need  = 3 if level<=0 else 2 if level==1 else 1
        ws, ls = bk.get("win_streak",0), bk.get("loss_streak",0)

        st.markdown(f"""
<div class='card'>
  <div class='card-title'>Compounding Level</div>
  <div class='card-value' style='color:{lc}'>{level:+d}</div>
  <div class='card-sub'>Kelly {eff_k:.4f} &nbsp;·&nbsp; ×{mult:.2f} base</div>
</div>""", unsafe_allow_html=True)

        st.markdown(f"<div style='font-size:12px;color:#6b7280;margin-bottom:4px'>Win streak {ws}/{need} → level up</div>", unsafe_allow_html=True)
        st.progress(min(ws/need,1.0))
        st.markdown(f"<div style='font-size:12px;color:#6b7280;margin:4px 0'>Loss streak {ls}/3 → level down</div>", unsafe_allow_html=True)
        st.progress(min(ls/3,1.0))

        st.markdown("""<div style='height:1px;background:#1e1e3a;margin:16px 0'></div>""", unsafe_allow_html=True)

        tp = float(os.getenv("EXIT_TAKE_PROFIT",1.0))
        sl = float(os.getenv("EXIT_STOP_LOSS",0.33))
        tr = float(os.getenv("TRAILING_STOP_PCT",0.25))
        mh = float(os.getenv("EXIT_MAX_HOURS",48))
        st.markdown(f"""
<div class='card'>
  <div class='card-title'>Exit Rules</div>
  <div style='display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px'>
    <div><div style='font-size:10px;color:#6b7280'>TAKE PROFIT</div><div style='font-size:15px;font-weight:600;color:#22c55e'>+{tp:.0%}</div></div>
    <div><div style='font-size:10px;color:#6b7280'>STOP LOSS</div><div style='font-size:15px;font-weight:600;color:#ef4444'>-{sl:.0%}</div></div>
    <div><div style='font-size:10px;color:#6b7280'>TRAIL DIST</div><div style='font-size:15px;font-weight:600;color:#a5b4fc'>{tr:.0%}</div></div>
    <div><div style='font-size:10px;color:#6b7280'>MAX HOLD</div><div style='font-size:15px;font-weight:600;color:#94a3b8'>{mh:.0f}h</div></div>
  </div>
</div>""", unsafe_allow_html=True)

        st.markdown("""<div style='height:1px;background:#1e1e3a;margin:16px 0'></div>""", unsafe_allow_html=True)

        osint_items = [("Tavily","TAVILY_API_KEY"),("Odds API","ODDS_API_KEY"),("FRED","FRED_API_KEY")]
        osint_html = "".join(
            f"<div style='display:flex;align-items:center;gap:6px;padding:4px 0;font-size:12px;color:#94a3b8'>"
            f"<span style='color:{'#22c55e' if os.getenv(k) else '#ef4444'}'>{'●' if os.getenv(k) else '○'}</span>{n}</div>"
            for n,k in osint_items
        )
        st.markdown(f"<div class='card'><div class='card-title'>OSINT Sources</div>{osint_html}</div>", unsafe_allow_html=True)

        st.markdown("""<div style='height:1px;background:#1e1e3a;margin:16px 0'></div>""", unsafe_allow_html=True)
        if st.button("🔍 Trigger Scan", use_container_width=True, type="primary"):
            with st.spinner("Scanning..."): subprocess.run(["python3","main.py","--mode",mode,"scan"], capture_output=True, timeout=120)
            st.cache_data.clear(); st.success("Done!"); st.rerun()

    # ── Recent activity feed ──────────────────────────────────────────────────
    st.divider()
    st.subheader("Recent Activity")
    recent = sorted(res, key=lambda x: x.get("resolved_at",""), reverse=True)[:8]
    if recent:
        rows = ""
        for t in recent:
            correct = t.get("prediction_correct")
            pnl     = t.get("pnl",0) or 0
            dot_c   = "#22c55e" if correct else ("#f59e0b" if t.get("actual_outcome")=="EXIT" else "#ef4444")
            pnl_c   = "#22c55e" if pnl>0 else "#ef4444"
            ts      = (t.get("resolved_at","") or "")[:10]
            rows += (
                f"<div class='stat-row'>"
                f"<span style='color:{dot_c};font-size:16px;width:20px'>{'✓' if correct else '✗'}</span>"
                f"<span style='flex:1;color:#cbd5e1;font-size:12px'>{t['market_question'][:55]}</span>"
                f"<span style='color:#6b7280;font-size:11px;margin:0 12px'>{t['side']}</span>"
                f"<span style='color:{pnl_c};font-weight:600;font-size:13px;min-width:60px;text-align:right'>${pnl:+.2f}</span>"
                f"<span style='color:#4b5563;font-size:11px;margin-left:12px'>{ts}</span>"
                f"</div>"
            )
        st.markdown(f"<div class='card' style='padding:8px 16px'>{rows}</div>", unsafe_allow_html=True)
    else:
        st.caption("No resolved trades yet.")
