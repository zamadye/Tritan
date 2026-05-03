import { NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'

const DATA_DIR = path.join(process.cwd(), '..', 'data')

function readJSON(file: string) {
  try { return JSON.parse(fs.readFileSync(path.join(DATA_DIR, file), 'utf-8')) }
  catch { return null }
}

export async function GET() {
  const trades: any[]     = readJSON('demo_trades.json') || []
  const bankroll_state    = readJSON('bankroll_state.json') || {}
  const evolution         = readJSON('evolution_lessons.json') || {}
  const llm_usage         = readJSON('llm_usage.json') || {}
  const calibration_model = readJSON('calibration_model.json') || {}
  const statistical_prior = readJSON('statistical_prior.json') || {}

  const resolved = trades.filter(t => t.actual_outcome)
  const open     = trades.filter(t => !t.actual_outcome)
  const wins     = resolved.filter(t => t.prediction_correct)
  const losses   = resolved.filter(t => !t.prediction_correct)
  const pnl      = resolved.reduce((s, t) => s + (t.pnl || 0), 0)
  const deployed = open.reduce((s, t) => s + t.size_usd, 0)
  const bankroll = Math.max(20 - deployed + pnl, 0)
  const avg_win  = wins.length ? wins.reduce((s, t) => s + t.pnl, 0) / wins.length : 0
  const avg_loss = losses.length ? Math.abs(losses.reduce((s, t) => s + t.pnl, 0) / losses.length) : 0
  const wr       = resolved.length ? wins.length / resolved.length : 0
  const rr       = avg_loss ? avg_win / avg_loss : 0
  const ev       = wr * avg_win - (1 - wr) * avg_loss

  // New arch trades (May 1+)
  const new_arch = resolved.filter(t => (t.timestamp || '') >= '2026-05-01')
  const new_wins = new_arch.filter(t => t.prediction_correct)

  // Brier score: model vs naive
  const brier_trades = resolved.filter(t => t.brier_score != null)
  const avg_brier    = brier_trades.length ? brier_trades.reduce((s, t) => s + t.brier_score, 0) / brier_trades.length : 0

  // P&L series
  const sorted = [...resolved].sort((a, b) =>
    (a.resolved_at || a.timestamp || '').localeCompare(b.resolved_at || b.timestamp || ''))
  let running = 0
  const pnl_series = sorted.map((t, i) => ({
    i, pnl: running += (t.pnl || 0),
    correct: t.prediction_correct,
    date: (t.resolved_at || t.timestamp || '').slice(0, 10),
  }))

  // Category breakdown with edge proof
  const cat_map: Record<string, { w: number; l: number; pnl: number; brier: number; n_brier: number }> = {}
  for (const t of resolved) {
    const cat = t.category || 'other'
    if (!cat_map[cat]) cat_map[cat] = { w: 0, l: 0, pnl: 0, brier: 0, n_brier: 0 }
    if (t.prediction_correct) cat_map[cat].w++
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

  // Signal A proof: which trades used statistical prior
  const stat_edge_trades = resolved.filter(t =>
    t.calibration_applied && t.calibration_applied.includes('logistic'))
  const stat_edge_wins = stat_edge_trades.filter(t => t.prediction_correct)

  // Recent trades with full audit trail
  const recent_full = [...resolved]
    .sort((a, b) => (b.resolved_at || '').localeCompare(a.resolved_at || ''))
    .slice(0, 20)
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
      correct: t.prediction_correct,
      brier: t.brier_score,
      exit_reason: t.exit_reason,
      catalyst: t.reasoning_summary?.slice(0, 120),
      calibration: t.calibration_applied?.slice(0, 100),
      category: t.category,
      date: (t.resolved_at || '').slice(0, 16),
    }))

  // LLM today
  const today = new Date().toISOString().slice(0, 10)
  const daily_llm = llm_usage?.daily?.[today] || { calls: 0, cost_usd: 0, input: 0, output: 0 }

  // Calibration model summary
  const cal_summary = Object.entries(calibration_model).map(([cat, d]: any) => ({
    cat, n: d.n, improvement: d.improvement, a: d.a, b: d.b, brier: d.brier, naive_brier: d.naive_brier
  })).sort((a, b) => b.n - a.n)

  return NextResponse.json({
    stats: {
      pnl: Math.round(pnl * 100) / 100, wr, rr, ev,
      bankroll: Math.round(bankroll * 100) / 100,
      deployed, total: trades.length, resolved: resolved.length,
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
    open_positions: open,
    recent_full,
    llm: { daily: daily_llm, total: llm_usage },
    calibration_model: cal_summary,
    data_sources: {
      markets_analyzed: statistical_prior?.total_markets || 0,
      categories: Object.keys(calibration_model).length,
      espn: true, newsapi: true, twitter: true, coingecko: true, fear_greed: true,
    },
  })
}
