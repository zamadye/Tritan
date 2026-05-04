import { NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'

// Load .env from parent directory
function getEnv(key: string): string {
  try {
    const envFile = fs.readFileSync(path.join(process.cwd(), '..', '.env'), 'utf-8')
    const match = envFile.match(new RegExp(`^${key}=(.*)$`, 'm'))
    return match ? match[1].trim() : ''
  } catch { return '' }
}

export async function GET() {
  try {
    const wallet = getEnv('POLYGON_WALLET_ADDRESS')
    const rpc    = 'https://polygon-mainnet.g.alchemy.com/v2/-LJWrAuXvUC8QszJzGzs0'
    const USDC   = '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'
    const data   = '0x70a08231000000000000000000000000' + wallet.slice(2).padStart(64, '0')

    const res = await fetch(rpc, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ jsonrpc: '2.0', method: 'eth_call', params: [{ to: USDC, data }, 'latest'], id: 1 }),
      signal: AbortSignal.timeout(8000),
    })
    const json = await res.json()
    const balance = parseInt(json.result || '0x0', 16) / 1e6

    // Polymarket positions
    let positions: any[] = []
    try {
      if (wallet) {
        const posRes = await fetch(
          `https://data-api.polymarket.com/positions?user=${wallet}&sizeThreshold=.1&limit=50`,
          { signal: AbortSignal.timeout(8000) }
        )
        if (posRes.ok) positions = await posRes.json()
      }
    } catch { /* optional */ }

    const mode = getEnv('AGENT_MODE') || 'demo'

    return NextResponse.json({
      wallet: wallet ? wallet.slice(0, 8) + '...' + wallet.slice(-6) : '—',
      usdc_balance: Math.round(balance * 100) / 100,
      positions,
      mode,
    })
  } catch (e: any) {
    return NextResponse.json({ usdc_balance: 0, positions: [], wallet: '—', error: e.message })
  }
}
