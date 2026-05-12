import { NextResponse } from 'next/server'
import fs from 'fs'
import { DATA_DIR, readJSON, readEnvValue } from '@/lib/paths'

export async function GET() {
  const mode = readEnvValue('AGENT_MODE') || 'demo'

  let trades: any[] = []
  let balance = 0
  let deployed = 0
  let wallet = ''

  if (mode === 'live') {
    // Live mode: merge agent trades + synced account trades
    const agentTrades = readJSON('live_trades.json') || []
    const syncTrades = readJSON('live_sync.json') || []
    // Merge by market_id — sync trades first (have resolution data from API), then agent trades
    const seen = new Set<string>()
    trades = []
    for (const t of [...syncTrades, ...agentTrades]) {
      const key = t.market_id || t.market_question
      if (!seen.has(key)) {
        seen.add(key)
        trades.push(t)
      }
    }
    const liveStats = readJSON('live_stats.json') || {}
    const liveBalance = readJSON('live_balance.json') || {}

    // Total portfolio = available balance + positions value (matches Polymarket "Portfolio")
    const avail = liveBalance.balance || liveStats.balance || 0
    const portVal = liveBalance.portfolio_value || 0
    balance = avail + portVal
    deployed = liveStats.deployed || 0
    wallet = liveBalance.wallet || ''
  } else {
    // Demo mode: read from demo trades
    trades = readJSON('demo_trades.json') || []
    const baseBankroll = parseFloat(readEnvValue('DEMO_BANKROLL') || '500')
    const open = trades.filter(t => !t.actual_outcome)
    const resolved = trades.filter(t => t.actual_outcome)
    deployed = open.reduce((s, t) => s + (t.size_usd || 0), 0)
    const pnl = resolved.reduce((s, t) => s + (t.pnl || 0), 0)
    balance = Math.max(baseBankroll - deployed + pnl, 0)
  }

  const bankroll_state = readJSON('bankroll_state.json') || {}
  const evolution = readJSON('evolution_lessons.json') || {}
  const llm_usage = readJSON('llm_usage.json') || {}
  const calibration_model = readJSON('calibration_model.json') || {}
  const statistical_prior = readJSON('statistical_prior.json') || {}
  const assistant_lessons = (readJSON('assistant_lessons.json') || []).slice(-5)

  const resolved = trades.filter(t => t.actual_outcome)
  const open = trades.filter(t => !t.actual_outcome)
  const wins = resolved.filter(t => t.prediction_correct || (t.pnl || 0) > 0)
  const losses = resolved.filter(t => !t.prediction_correct && (t.pnl || 0) < 0)
  const pnl = resolved.reduce((s, t) => s + (t.pnl || 0), 0)
  const avg_win = wins.length ? wins.reduce((s, t) => s + (t.pnl || 0), 0) / wins.length : 0
  const avg_loss = losses.length ? Math.abs(losses.reduce((s, t) => s + (t.pnl || 0), 0) / losses.length) : 0
  const wr = resolved.length ? wins.length / resolved.length : 0
  const rr = avg_loss ? avg_win / avg_loss : 0
  const ev = wr * avg_win - (1 - wr) * avg_loss

  // New arch trades (May 1+)
  const new_arch = resolved.filter(t => (t.timestamp || '') >= '2026-05-01')
  const new_wins = new_arch.filter(t => t.prediction_correct || (t.pnl || 0) > 0)

  // Brier score
  const brier_trades = resolved.filter(t => t.brier_score != null)
  const avg_brier = brier_trades.length ? brier_trades.reduce((s, t) => s + t.brier_score, 0) / brier_trades.length : 0

  // P&L series
  const sorted = [...resolved].sort((a, b) =>
    (a.resolved_at || a.timestamp || '').localeCompare(b.resolved_at || b.timestamp || ''))
  let running = 0
  const pnl_series = sorted.map((t, i) => ({
    i, pnl: running += (t.pnl || 0),
    correct: t.prediction_correct || (t.pnl || 0) > 0,
    date: (t.resolved_at || t.timestamp || '').slice(0, 10),
  }))

  // Category breakdown
  const cat_map: Record<string, { w: number; l: number; pnl: number; brier: number; n_brier: number }> = {}
  for (const t of resolved) {
    const cat = t.category || 'other'
    if (!cat_map[cat]) cat_map[cat] = { w: 0, l: 0, pnl: 0, brier: 0, n_brier: 0 }
    if (t.prediction_correct || (t.pnl || 0) > 0) cat_map[cat].w++
    else cat_map[cat].l++
    cat_map[cat].pnl += t.pnl || 0
    if (t.brier_score != null) { cat_map[cat].brier += t.brier_score; cat_map[cat].n_brier++ }
  }

  // Exit breakdown
  const exit_map: Record<string, number> = {}
  for (const t of resolved) {
    const r = t.exit_reason || 'RESOLVED'
    const k = r.includes('TAKE_PROFIT') ? 'TAKE_PROFIT'
            : r.includes('TRAILING') ? 'TRAILING_STOP'
            : r.includes('STOP_LOSS') ? 'STOP_LOSS'
            : r.includes('TIME') || r.includes('EVENT') ? 'TIME/EVENT'
            : 'RESOLVED'
    exit_map[k] = (exit_map[k] || 0) + 1
  }

  // Signal A proof
  const stat_edge_trades = resolved.filter(t =>
    t.calibration && t.calibration.includes('logistic'))
  const stat_edge_wins = stat_edge_trades.filter(t => t.prediction_correct || (t.pnl || 0) > 0)

  // Recent trades with full audit trail
  const recent_full = [...resolved]
    .sort((a, b) => (b.resolved_at || b.timestamp || '').localeCompare(a.resolved_at || a.timestamp || ''))
    .map(t => ({
      market: t.market_question,
      side: t.side,
      entry: t.price_at_entry,
      p_base: t.calibration_applied?.match(/p_base=([\d.]+%)/)?.[1] || null,
      p_true: t.p_true_estimated,
      confidence: t.confidence_at_bet,
      edge: t.edge_at_bet,
      outcome: t.actual_outcome,
      pnl: t.pnl,
      correct: t.prediction_correct || (t.pnl || 0) > 0,
      brier: t.brier_score,
      exit_reason: t.exit_reason,
      catalyst: t.reasoning_summary?.slice(0, 120),
      calibration: t.calibration_applied?.slice(0, 100),
      category: t.category,
      date: (t.resolved_at || t.timestamp || '').slice(0, 16),
      reasoning: t.reasoning_summary,
      base_rate: t.base_rate,
      tool_calls_log: t.tool_calls_log,
      news_context: t.news_context,
      information_gap: t.information_gap,
      information_gap_reason: t.information_gap_reason,
    }))

  // LLM today
  const today = new Date().toISOString().slice(0, 10)
  const daily_llm = llm_usage?.daily?.[today] || { calls: 0, cost_usd: 0, input: 0, output: 0 }

  // Calibration model summary
  const cal_summary = Object.entries(calibration_model).map(([cat, d]: any) => ({
    cat, n: d.n, improvement: d.improvement, a: d.a, b: d.b, brier: d.brier, naive_brier: d.naive_brier
  })).sort((a, b) => b.n - a.n)

  // Enrich open positions with current price and unrealized P&L
  const enrichedPositions = await Promise.all(open.map(async (t: any) => {
    try {
      const nid = t.market_numeric_id || ''
      if (!nid) return t
      const r = await fetch(`https://gamma-api.polymarket.com/markets/${nid}`, { signal: AbortSignal.timeout(4000) })
      const m = await r.json()
      const opRaw = m.outcomePrices || '[]'
      const op = Array.isArray(opRaw) ? opRaw : JSON.parse(String(opRaw))
      const yesP = op[0] ? parseFloat(op[0]) : null
      if (yesP === null) return t
      const entry = t.price_at_entry || 0
      const size = t.size_usd || 0
      const side = t.side
      let currentValue = 0
      if (side === 'YES') {
        const shares = size / entry
        currentValue = shares * yesP
      } else {
        const noEntry = 1 - entry
        const noShares = noEntry > 0 ? size / noEntry : size / entry
        currentValue = noShares * (1 - yesP)
      }
      const unrealizedPnl = Math.round((currentValue - size) * 100) / 100
      const unrealizedPct = Math.round((currentValue - size) / size * 10000) / 100
      return { ...t, current_yes_price: yesP, unrealized_pnl: unrealizedPnl, unrealized_pct: unrealizedPct }
    } catch {
      return t
    }
  }))

  return NextResponse.json({
    stats: {
      pnl: Math.round(pnl * 100) / 100, wr, rr, ev,
      bankroll: Math.round(balance * 100) / 100,
      deployed: Math.round(deployed * 100) / 100,
      total: trades.length, resolved: resolved.length,
      open: open.length, wins: wins.length, losses: losses.length,
      avg_win, avg_loss, avg_brier,
      new_arch: { total: new_arch.length, wins: new_wins.length, wr: new_arch.length ? new_wins.length / new_arch.length : 0 },
      stat_edge: { total: stat_edge_trades.length, wins: stat_edge_wins.length, wr: stat_edge_trades.length ? stat_edge_wins.length / stat_edge_trades.length : 0 },
    },
    brier: { model: 0.1788, naive: 0.1874, improvement: 4.6, our_avg: Math.round(avg_brier * 10000) / 10000 },
    bankroll_state,
    evolution,
    pnl_series,
    cat_breakdown: cat_map,
    exit_breakdown: exit_map,
    open_positions: enrichedPositions,
    recent_full,
    llm: { daily: daily_llm, total: llm_usage },
    calibration_model: cal_summary,
    assistant_lessons,
    data_sources: {
      markets_analyzed: statistical_prior?.total_markets || 0,
      categories: Object.keys(calibration_model).length,
      espn: true, newsapi: true, twitter: true, coingecko: true, fear_greed: true,
    },
    agent_mode: mode,
    wallet: wallet,
  })
}
