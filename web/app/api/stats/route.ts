import { NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'

const DATA_DIR = path.join(process.cwd(), '..', 'data')

function readJSON(file: string) {
  try {
    return JSON.parse(fs.readFileSync(path.join(DATA_DIR, file), 'utf-8'))
  } catch {
    return null
  }
}

export async function GET() {
  const trades: any[] = readJSON('demo_trades.json') || []
  const bankroll_state = readJSON('bankroll_state.json') || {}
  const evolution = readJSON('evolution_lessons.json') || {}
  const llm_usage = readJSON('llm_usage.json') || {}
  const pnl_summary = readJSON('pnl_summary.json') || {}

  const resolved = trades.filter(t => t.actual_outcome)
  const open = trades.filter(t => !t.actual_outcome)
  const wins = resolved.filter(t => t.prediction_correct)
  const losses = resolved.filter(t => !t.prediction_correct)
  const pnl = resolved.reduce((s, t) => s + (t.pnl || 0), 0)
  const deployed = open.reduce((s, t) => s + t.size_usd, 0)
  const bankroll = Math.max(20 - deployed + pnl, 0)
  const avg_win = wins.length ? wins.reduce((s, t) => s + t.pnl, 0) / wins.length : 0
  const avg_loss = losses.length ? Math.abs(losses.reduce((s, t) => s + t.pnl, 0) / losses.length) : 0
  const wr = resolved.length ? wins.length / resolved.length : 0
  const rr = avg_loss ? avg_win / avg_loss : 0
  const ev = wr * avg_win - (1 - wr) * avg_loss

  // Cumulative P&L series
  const sorted = [...resolved].sort((a, b) =>
    (a.resolved_at || a.timestamp || '').localeCompare(b.resolved_at || b.timestamp || '')
  )
  let running = 0
  const pnl_series = sorted.map((t, i) => ({
    i,
    pnl: running += (t.pnl || 0),
    correct: t.prediction_correct,
    date: (t.resolved_at || t.timestamp || '').slice(0, 10),
  }))

  // Category breakdown
  const cat_map: Record<string, { w: number; l: number; pnl: number }> = {}
  for (const t of resolved) {
    const cat = t.category || 'other'
    if (!cat_map[cat]) cat_map[cat] = { w: 0, l: 0, pnl: 0 }
    if (t.prediction_correct) cat_map[cat].w++
    else cat_map[cat].l++
    cat_map[cat].pnl += t.pnl || 0
  }

  // Today's LLM usage
  const today = new Date().toISOString().slice(0, 10)
  const daily_llm = llm_usage?.daily?.[today] || { calls: 0, cost_usd: 0, input: 0, output: 0 }

  return NextResponse.json({
    stats: { pnl: Math.round(pnl * 100) / 100, wr, rr, ev, bankroll: Math.round(bankroll * 100) / 100, deployed, total: trades.length, resolved: resolved.length, open: open.length, wins: wins.length, losses: losses.length },
    bankroll_state,
    evolution,
    pnl_series,
    cat_breakdown: cat_map,
    open_positions: open,
    recent: [...resolved].sort((a, b) => (b.resolved_at || '').localeCompare(a.resolved_at || '')).slice(0, 10),
    llm: { daily: daily_llm, total: llm_usage },
    brier: { model: 0.1788, naive: 0.1874, improvement: 4.6 },
  })
}
