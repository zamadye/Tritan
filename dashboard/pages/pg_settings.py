import os, sys, json, subprocess
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from pathlib import Path
import streamlit as st
from dashboard.components.shared import save_env, get_usdc_balance, load_bankroll, restart_agent

def render():
    st.subheader("⚙️ Settings")
    st.caption("Changes update .env and restart the agent automatically.")

    tab1,tab2,tab3,tab4,tab5 = st.tabs(["📈 Strategy","🚪 Exit","🎯 Compounding","⏱ Scan","🔑 API & Mode"])

    with tab1:
        min_conf = st.slider("Min Confidence",    0.50, 0.90, float(os.getenv("MIN_CONFIDENCE",0.65)), 0.01)
        edge_thr = st.slider("Min Edge",          0.03, 0.25, float(os.getenv("EDGE_THRESHOLD",0.08)), 0.01)
        min_bet  = st.number_input("Min Bet ($)", 0.5, 10.0,  float(os.getenv("MIN_BET_SIZE",0.5)),   0.5)
        max_bet  = st.number_input("Max Bet ($)", 1.0, 50.0,  float(os.getenv("MAX_BET_SIZE",3.0)),   0.5)
        max_open = st.number_input("Max Open Positions", 1, 50, int(os.getenv("MAX_OPEN_POSITIONS",20)))
        kelly    = st.slider("Kelly Fraction",    0.10, 1.00, float(os.getenv("KELLY_FRACTION",0.25)), 0.05)
        pref_cat = st.text_input("Preferred Categories", os.getenv("PREFERRED_CATEGORIES","politics,economics,crypto,science"))
        blk_cat  = st.text_input("Blacklisted Categories", os.getenv("BLACKLISTED_CATEGORIES",""))
        if st.button("💾 Save Strategy", type="primary", key="s1"):
            save_env({"MIN_CONFIDENCE":min_conf,"EDGE_THRESHOLD":edge_thr,"MIN_BET_SIZE":min_bet,
                      "MAX_BET_SIZE":max_bet,"MAX_OPEN_POSITIONS":int(max_open),"KELLY_FRACTION":kelly,
                      "PREFERRED_CATEGORIES":pref_cat,"BLACKLISTED_CATEGORIES":blk_cat})
            restart_agent(); st.success("✅ Saved & restarted!")

    with tab2:
        tp_ret = st.slider("Take Profit (return %)", 0.20, 3.00, float(os.getenv("EXIT_TAKE_PROFIT",1.0)),  0.10,
                           help="+100% = nilai posisi 2x modal")
        trail  = st.slider("Trailing Stop Distance", 0.10, 0.60, float(os.getenv("TRAILING_STOP_PCT",0.25)),0.05,
                           help="SL = peak × (1 - trail)")
        sl_ret = st.slider("Stop Loss (return %)",   0.10, 0.60, float(os.getenv("EXIT_STOP_LOSS",0.33)),   0.05)
        max_h  = st.number_input("Max Hold (hours)", 6, 168, int(float(os.getenv("EXIT_MAX_HOURS",48))))

        ex_entry = st.number_input("Example entry price", 0.10, 0.90, 0.30, 0.05)
        shares   = 2.0/ex_entry
        ex_tp    = min(ex_entry*(1+tp_ret), 0.99)
        ex_sl    = max(ex_entry*(1-sl_ret), 0.01)
        st.info(f"Entry **{ex_entry:.2f}** · TP at **{ex_tp:.2f}** (+${shares*ex_tp-2:.2f}) · SL at **{ex_sl:.2f}** (-${2-shares*ex_sl:.2f})")

        if st.button("💾 Save Exit Strategy", type="primary", key="s2"):
            save_env({"EXIT_TAKE_PROFIT":tp_ret,"TRAILING_STOP_PCT":trail,"EXIT_STOP_LOSS":sl_ret,"EXIT_MAX_HOURS":int(max_h)})
            restart_agent(); st.success("✅ Saved & restarted!")

    with tab3:
        bk       = load_bankroll()
        win_str  = st.number_input("Wins to Level Up (base)", 1, 10, int(os.getenv("WIN_STREAK_TO_INCREASE",3)))
        loss_str = st.number_input("Losses to Level Down",    1, 10, int(os.getenv("LOSS_STREAK_TO_DECREASE",3)))
        step_sz  = st.slider("Step Size per Level", 0.05, 0.30, float(os.getenv("BANKROLL_STEP_SIZE",0.10)), 0.05)
        max_lvl  = st.number_input("Max Level", 1, 10, int(os.getenv("MAX_BANKROLL_LEVEL",5)))
        min_lvl  = st.number_input("Min Level", -5, 0, int(os.getenv("MIN_BANKROLL_LEVEL",-2)))
        st.caption(f"Current: level={bk.get('level',0)} · win_streak={bk.get('win_streak',0)} · loss_streak={bk.get('loss_streak',0)}")
        if st.button("🔄 Reset Level to 0", key="reset_lvl"):
            p = Path("data/bankroll_state.json")
            state = json.loads(p.read_text()) if p.exists() else {}
            state.update({"level":0,"win_streak":0,"loss_streak":0})
            p.write_text(json.dumps(state,indent=2))
            st.cache_data.clear(); st.success("Reset!"); st.rerun()
        if st.button("💾 Save Compounding", type="primary", key="s3"):
            save_env({"WIN_STREAK_TO_INCREASE":int(win_str),"LOSS_STREAK_TO_DECREASE":int(loss_str),
                      "BANKROLL_STEP_SIZE":step_sz,"MAX_BANKROLL_LEVEL":int(max_lvl),"MIN_BANKROLL_LEVEL":int(min_lvl)})
            restart_agent(); st.success("✅ Saved & restarted!")

    with tab4:
        scan_int    = st.number_input("Scan Interval off-peak (min)", 5, 120, int(os.getenv("SCAN_INTERVAL_MINUTES",15)))
        scan_active = st.number_input("Scan Interval active 14-22 UTC (min)", 1, 30, int(os.getenv("SCAN_INTERVAL_ACTIVE_MINUTES",5)))
        min_vol     = st.number_input("Min Volume 24h ($)", 100, 50000, int(float(os.getenv("MIN_VOLUME_24H",2000))), 500)
        min_liq     = st.number_input("Min Liquidity ($)",  100, 20000, int(float(os.getenv("MIN_LIQUIDITY",500))),   100)
        max_days    = st.number_input("Max Days to Resolve", 1, 90, int(os.getenv("MAX_DAYS_TO_RESOLVE",30)))
        min_price   = st.slider("Min Market Price", 0.05, 0.40, float(os.getenv("MIN_MARKET_PRICE",0.15)), 0.01)
        max_price   = st.slider("Max Market Price", 0.60, 0.95, float(os.getenv("MAX_MARKET_PRICE",0.85)), 0.01)
        if st.button("💾 Save Scan Settings", type="primary", key="s4"):
            save_env({"SCAN_INTERVAL_MINUTES":int(scan_int),"SCAN_INTERVAL_ACTIVE_MINUTES":int(scan_active),
                      "MIN_VOLUME_24H":int(min_vol),"MIN_LIQUIDITY":int(min_liq),
                      "MAX_DAYS_TO_RESOLVE":int(max_days),"MIN_MARKET_PRICE":min_price,"MAX_MARKET_PRICE":max_price})
            restart_agent(); st.success("✅ Saved & restarted!")

    with tab5:
        st.text_input("AI Model",  os.getenv("AI_MODEL",""),  disabled=True)
        wallet = os.getenv("POLYGON_WALLET_ADDRESS","")
        st.text_input("Wallet",    wallet[:8]+"..."+wallet[-6:] if len(wallet)>14 else wallet, disabled=True)
        bal = get_usdc_balance()
        st.metric("USDC Balance (Live)", f"${bal:.2f}")
        demo_br = st.number_input("Demo Bankroll ($)", 1.0, 10000.0, float(os.getenv("DEMO_BANKROLL",20)), 1.0)
        dry_run = st.toggle("Dry Run Mode", os.getenv("DRY_RUN","false").lower()=="true")
        if st.button("💾 Save", type="primary", key="s5"):
            save_env({"DEMO_BANKROLL":demo_br,"DRY_RUN":str(dry_run).lower()})
            restart_agent(); st.success("✅ Saved!")

        st.divider()
        st.markdown("**⚠️ Danger Zone**")
        if st.button("🗑 Reset ALL Demo Trades", key="reset_trades"):
            st.session_state["confirm_reset"] = True
        if st.session_state.get("confirm_reset"):
            st.error("This will DELETE all demo trade history!")
            y, n = st.columns(2)
            if y.button("✅ Confirm Delete", key="del_yes"):
                Path("data/demo_trades.json").write_text("[]")
                st.session_state["confirm_reset"]=False
                st.cache_data.clear(); st.success("Deleted!"); st.rerun()
            if n.button("❌ Cancel", key="del_no"):
                st.session_state["confirm_reset"]=False; st.rerun()
