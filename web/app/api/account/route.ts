import { NextResponse } from 'next/server'
import { readEnvValue, readJSON } from '@/lib/paths'

export async function GET() {
  try {
    const mode = readEnvValue('AGENT_MODE') || 'demo'
    const wallet = readEnvValue('POLYGON_WALLET_ADDRESS')

    if (mode === 'live') {
      // Live mode: merge agent trades + synced account trades
      const agentTrades = readJSON('live_trades.json') || []
      const syncTrades = readJSON('live_sync.json') || []
      const seen = new Set<string>()
      const trades: any[] = []
      for (const t of [...syncTrades, ...agentTrades]) {
        const key = t.market_id || t.market_question
        if (!seen.has(key)) {
          seen.add(key)
          trades.push(t)
        }
      }

      const liveBalance = readJSON('live_balance.json') || {}
      const liveStats = readJSON('live_stats.json') || {}
      const livePositions = readJSON('live_positions.json') || []

      const open = trades.filter((t: any) => !t.actual_outcome)
      const resolved = trades.filter((t: any) => t.actual_outcome)
      const wins = resolved.filter((t: any) => t.prediction_correct || t.actual_outcome === 'WIN' || (t.pnl || 0) > 0)
      const losses = resolved.filter((t: any) => !t.prediction_correct && t.actual_outcome === 'LOSS' && (t.pnl || 0) < 0)
      const pnl = resolved.reduce((s: number, t: any) => s + (t.pnl || 0), 0)
      const deployed = open.reduce((s: number, t: any) => s + (t.size_usd || 0), 0)

      return NextResponse.json({
        wallet: wallet ? wallet.slice(0, 8) + '...' + wallet.slice(-6) : '—',
        usdc_balance: (liveBalance.balance || 0) + (liveBalance.portfolio_value || 0),
        positions: livePositions,
        mode: 'live',
        deployed: liveStats.deployed || deployed,
        total_trades: trades.length,
        open: open.length,
        resolved: resolved.length,
        wins: wins.length,
        losses: losses.length,
        total_pnl: pnl,
        win_rate: resolved.length ? wins.length / resolved.length : 0,
        last_sync: liveBalance.timestamp || null,
      })
    } else {
      // Demo mode: read from demo trades
      const trades = readJSON('demo_trades.json') || []
      const open = trades.filter((t: any) => !t.actual_outcome)
      const resolved = trades.filter((t: any) => t.actual_outcome)
      const wins = resolved.filter((t: any) => t.prediction_correct || (t.pnl || 0) > 0)
      const losses = resolved.filter((t: any) => !t.prediction_correct && (t.pnl || 0) < 0)
      const pnl = resolved.reduce((s: number, t: any) => s + (t.pnl || 0), 0)
      const deployed = open.reduce((s: number, t: any) => s + (t.size_usd || 0), 0)
      const baseBankroll = parseFloat(readEnvValue('DEMO_BANKROLL') || '500')
      const balance = Math.max(baseBankroll - deployed + pnl, 0)

      return NextResponse.json({
        wallet: 'Demo Account',
        usdc_balance: balance,
        positions: open,
        mode: 'demo',
        deployed: deployed,
        total_trades: trades.length,
        open: open.length,
        resolved: resolved.length,
        wins: wins.length,
        losses: losses.length,
        total_pnl: pnl,
        win_rate: resolved.length ? wins.length / resolved.length : 0,
        last_sync: null,
      })
    }
  } catch (e: any) {
    return NextResponse.json({
      usdc_balance: 0,
      positions: [],
      wallet: '—',
      mode: 'demo',
      error: e.message,
    })
  }
}
