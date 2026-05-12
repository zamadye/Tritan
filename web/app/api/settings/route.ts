import { NextResponse } from 'next/server'
import fs from 'fs'
import { exec } from 'child_process'
import { promisify } from 'util'
import { ENV_FILE } from '@/lib/paths'

const execAsync = promisify(exec)

// Keys that must never be exposed via API
const SENSITIVE_KEYS = new Set([
  'POLYGON_PRIVATE_KEY', 'AI_API_KEY', 'POLY_API_SECRET', 'POLY_API_PASSPHRASE',
  'POLY_API_KEY', 'SERPER_API_KEY', 'NEWS_API_KEY', 'TAVILY_API_KEY',
  'TWITTER_BEARER_TOKEN', 'TWITTER_CONSUMER_KEY', 'TWITTER_CONSUMER_SECRET',
  'TWITTER_ACCESS_TOKEN', 'TWITTER_ACCESS_TOKEN_SECRET', 'ODDS_API_KEY',
  'OPENWEATHER_API_KEY', 'FRED_API_KEY', 'API_SECRET_TOKEN',
])

// Only these keys are allowed to be updated via POST
const ALLOWED_UPDATE_KEYS = new Set([
  'AGENT_MODE', 'DEMO_BANKROLL', 'LIVE_BANKROLL',
  'MIN_BET_SIZE', 'MAX_BET_SIZE', 'KELLY_FRACTION', 'MAX_OPEN_POSITIONS', 'MAX_OPEN_PER_CATEGORY', 'MAX_CATEGORY_EXPOSURE_PCT',
  'MIN_STAT_EDGE', 'MIN_STAT_EDGE_HIGH_RISK', 'MIN_CONFIDENCE', 'MIN_CONFIDENCE_CRYPTO', 'MIN_CONFIDENCE_GEOPOLITIK', 'MIN_CONFIDENCE_POLITICS', 'EDGE_THRESHOLD',
  'EXIT_TAKE_PROFIT', 'EXIT_STOP_LOSS', 'EXIT_MAX_HOURS', 'TRAILING_STOP_PCT',
  'SCAN_INTERVAL_MINUTES', 'SCAN_INTERVAL_ACTIVE_MINUTES', 'MAX_MARKETS_TO_SCAN', 'MIN_VOLUME_24H', 'MIN_LIQUIDITY', 'MAX_DAYS_TO_RESOLVE',
  'MAX_LLM_CALLS_PER_CYCLE', 'LLM_DAILY_COST_LIMIT_USD', 'LLM_MAX_TOKENS',
  'WIN_STREAK_TO_INCREASE', 'LOSS_STREAK_TO_DECREASE', 'BANKROLL_STEP_SIZE', 'MAX_BANKROLL_LEVEL',
])

function readEnv(): Record<string, string> {
  const lines = fs.readFileSync(ENV_FILE, 'utf-8').split('\n')
  const env: Record<string, string> = {}
  for (const line of lines) {
    const m = line.match(/^([A-Z_]+)=(.*)$/)
    if (m && !SENSITIVE_KEYS.has(m[1])) env[m[1]] = m[2]
  }
  return env
}

export async function GET() {
  return NextResponse.json(readEnv())
}

export async function POST(req: Request) {
  const updates: Record<string, string> = await req.json()

  // Handle reset to defaults
  if (updates._reset) {
    try {
      await execAsync('cd /root/Tritan && cp .env.example .env')
      await execAsync('pm2 restart tritan-dashboard').catch(() => {})
      return NextResponse.json({ ok: true, updated: ['_reset'] })
    } catch (e: any) {
      return NextResponse.json({ ok: false, error: 'Reset failed' }, { status: 500 })
    }
  }

  // Only allow whitelisted keys
  const filtered: Record<string, string> = {}
  for (const [k, v] of Object.entries(updates)) {
    if (!ALLOWED_UPDATE_KEYS.has(k)) continue
    // Sanitize value: only allow safe characters
    if (!/^[\w\s.,\-+%:/]+$/.test(String(v))) continue
    filtered[k] = String(v).slice(0, 100)
  }

  if (Object.keys(filtered).length === 0) {
    return NextResponse.json({ ok: false, error: 'No valid keys to update' }, { status: 400 })
  }

  let content = fs.readFileSync(ENV_FILE, 'utf-8')
  for (const [k, v] of Object.entries(filtered)) {
    const re = new RegExp(`^${k}=.*`, 'm')
    if (re.test(content)) content = content.replace(re, `${k}=${v}`)
    else content += `\n${k}=${v}`
  }
  fs.writeFileSync(ENV_FILE, content)
  await execAsync('pm2 restart tritan-agent').catch(() => {})
  return NextResponse.json({ ok: true, updated: Object.keys(filtered) })
}
