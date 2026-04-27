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
    c1,c2,c3,c4,_ = st.columns([1,1,1,1,3])
    if c1.button("▶ Start",   use_container_width=True): subprocess.run(["systemctl","start","polymarket-agent"]);   st.rerun()
    if c2.button("⏹ Stop",    use_container_width=True): subprocess.run(["systemctl","stop","polymarket-agent"]);    st.rerun()
    if c3.button("🔄 Restart", use_container_width=True): subprocess.run(["systemctl","restart","polymarket-agent"]); st.rerun()
    new_mode = "live" if mode=="demo" else "demo"
    if c4.button(f"⇄ →{'LIVE' if mode=='demo' else 'DEMO'}", use_container_width=True):
        st.session_state["confirm_switch"] = True

    if st.session_state.get("confirm_switch"):
        st.warning(f"Switch to **{new_mode.upper()}**? This will restart the agent.")
        y, n = st.columns(2)
        if y.button("✅ Confirm", key="sw_yes"): switch_mode(new_mode); st.session_state["confirm_switch"]=False; st.cache_data.clear(); st.rerun()
        if n.button("❌ Cancel",  key="sw_no"):  st.session_state["confirm_switch"]=False; st.rerun()

    st.divider()

    # ── alerts ────────────────────────────────────────────────────────────────
    if oc >= 30:
        st.error(f"⚠️ OVERCONFIDENCE {oc}x — hard cap 70%, penalty -{min(0.25,oc*0.005):.0%} active")
    elif oc >= 10:
        st.warning(f"⚠️ Overconfidence {oc}x — penalty -{min(0.25,oc*0.005):.0%} applied")

    # ── KPI row ───────────────────────────────────────────────────────────────
    m1,m2,m3,m4,m5,m6 = st.columns(6)
    m1.metric("💰 P&L",       f"${s['pnl']:+.2f}")
    m2.metric("🎯 Win Rate",  f"{s['wr']:.0%}", f"{len(s['wins'])}W/{len(s['losses'])}L")
    m3.metric("⚖️ R:R",       f"{s['rr']:.2f}:1")
    m4.metric("📈 EV/trade",  f"${s['ev']:+.3f}")
    m5.metric("🏦 Bankroll",  f"${s['bankroll']:.2f}", f"-${s['deployed']:.2f} deployed")
    m6.metric("📂 Open",      str(len(s['open_t'])))

    st.divider()
    left, right = st.columns([3, 1])

    with left:
        st.subheader("Cumulative P&L")
        res = s["resolved"]
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
        lc    = "#00cc88" if level>0 else "#ff4444" if level<0 else "#888"
        step  = float(os.getenv("BANKROLL_STEP_SIZE",0.10))
        mult  = max(0.5, min(2.0, 1.0+level*step))
        eff_k = round(float(os.getenv("KELLY_FRACTION",0.25))*mult, 4)
        need  = 3 if level<=0 else 2 if level==1 else 1
        ws, ls = bk.get("win_streak",0), bk.get("loss_streak",0)

        st.markdown(f"""<div style='background:#1e1e2e;border:1px solid #313155;border-radius:10px;padding:16px;margin-bottom:12px'>
<div style='font-size:11px;color:#888;text-transform:uppercase;letter-spacing:.5px'>Compounding Level</div>
<div style='font-size:36px;font-weight:700;color:{lc}'>{level:+d}</div>
<div style='font-size:12px;color:#aaa'>Kelly {eff_k:.4f} &nbsp;×{mult:.2f}</div>
</div>""", unsafe_allow_html=True)
        st.progress(min(ws/need,1.0), text=f"🏆 Win streak {ws}/{need} → up")
        st.progress(min(ls/3,1.0),   text=f"💀 Loss streak {ls}/3 → down")

        st.divider()
        st.markdown("**🛡 Exit Rules**")
        tp = float(os.getenv("EXIT_TAKE_PROFIT",1.0))
        sl = float(os.getenv("EXIT_STOP_LOSS",0.33))
        tr = float(os.getenv("TRAILING_STOP_PCT",0.25))
        mh = float(os.getenv("EXIT_MAX_HOURS",48))
        st.markdown(f"- TP **+{tp:.0%}** return\n- Trail **{tr:.0%}** from peak\n- SL **-{sl:.0%}** return\n- Max **{mh:.0f}h**")

        st.divider()
        st.markdown("**🔌 OSINT**")
        for name, key in [("Tavily","TAVILY_API_KEY"),("Odds API","ODDS_API_KEY"),("FRED","FRED_API_KEY")]:
            st.markdown(f"{'✅' if os.getenv(key) else '❌'} {name}")

        st.divider()
        if st.button("🔍 Trigger Scan", use_container_width=True):
            with st.spinner("Scanning..."): subprocess.run(["python3","main.py","--mode",mode,"scan"], capture_output=True, timeout=120)
            st.cache_data.clear(); st.success("Done!"); st.rerun()
        if st.button("🗑 Refresh Data", use_container_width=True):
            st.cache_data.clear(); st.rerun()
