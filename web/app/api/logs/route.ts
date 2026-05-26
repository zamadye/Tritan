import { NextResponse } from 'next/server'
import fs from 'fs'

const LOG_FILE = process.env.PM2_LOG_FILE || '/root/.pm2/logs/tritan-agent-out.log'
const ERR_FILE = process.env.PM2_ERR_FILE || '/root/.pm2/logs/tritan-agent-error.log'

// Strip ANSI escape codes
function stripAnsi(str: string): string {
  return str.replace(/\x1B\[[0-9;]*[mGKHF]/g, '').replace(/\x1B\[\d+;\d+m/g, '')
}

// Classify log line for frontend display
function classifyLine(line: string): { type: string; text: string } {
  const t = line.trim()
  if (!t) return { type: 'empty', text: '' }
  if (t.includes('LIVE') && t.includes('Filled')) return { type: 'bet', text: t }
  if (t.includes('DEMO') && t.includes('Simulated')) return { type: 'bet', text: t }
  if (t.includes('EXIT') && (t.includes('✅') || t.includes('❌'))) return { type: 'exit', text: t }
  if (t.includes('RESOLVER') && t.includes('WIN') || t.includes('RESOLVER') && t.includes('LOSS')) return { type: 'resolve', text: t }
  if (t.includes('RESOLVER')) return { type: 'resolver', text: t }
  if (t.includes('🔍 Scanning')) return { type: 'scan_start', text: t }
  if (t.includes('Found') && t.includes('candidate')) return { type: 'scan_found', text: t }
  if (t.includes('⛔ Gate fail')) return { type: 'gate_fail', text: t }
  if (t.includes('⛔ Corr limit') || t.includes('⛔ Exposure')) return { type: 'gate_limit', text: t }
  if (t.includes('⛔ High leverage') || t.includes('⛔ Extreme entry')) return { type: 'gate_catalyst', text: t }
  if (t.includes('MARKET ANALYSIS') || t.includes('p_true:')) return { type: 'analysis', text: t }
  if (t.includes('🧠 Evolution')) return { type: 'learning', text: t }
  if (t.includes('Next scan in')) return { type: 'waiting', text: t }
  if (t.includes('Bankroll:') || t.includes('Win Rate:')) return { type: 'stats', text: t }
  if (t.includes('SELL') || t.includes('sell')) return { type: 'sell', text: t }
  if (t.includes('error') || t.includes('Error') || t.includes('❌')) return { type: 'error', text: t }
  if (t.includes('[TWITTER]') || t.includes('[OSINT]')) return { type: 'data', text: t }
  if (t.includes('LLM') || t.includes('ANALYZER')) return { type: 'llm', text: t }
  return { type: 'info', text: t }
}

export async function GET(req: Request) {
  const url = new URL(req.url)
  const lines = parseInt(url.searchParams.get('lines') || '150')
  const since = url.searchParams.get('since') || ''

  try {
    // Read last N lines from out log
    let outContent = ''
    let errContent = ''

    if (fs.existsSync(LOG_FILE)) {
      const stat = fs.statSync(LOG_FILE)
      const size = stat.size
      const readSize = Math.min(size, 50000) // last 50KB
      const buf = Buffer.alloc(readSize)
      const fd = fs.openSync(LOG_FILE, 'r')
      fs.readSync(fd, buf, 0, readSize, size - readSize)
      fs.closeSync(fd)
      outContent = buf.toString('utf-8')
    }

    if (fs.existsSync(ERR_FILE)) {
      const stat = fs.statSync(ERR_FILE)
      const size = stat.size
      const readSize = Math.min(size, 10000)
      const buf = Buffer.alloc(readSize)
      const fd = fs.openSync(ERR_FILE, 'r')
      fs.readSync(fd, buf, 0, readSize, size - readSize)
      fs.closeSync(fd)
      errContent = buf.toString('utf-8')
    }

    // Parse and classify lines
    const outLines = outContent.split('\n')
      .map(l => stripAnsi(l).trim())
      .filter(l => l.length > 0)
      .slice(-lines)
      .map((l, i) => ({ id: i, ...classifyLine(l), source: 'out' }))

    // Only include critical errors from err log
    const errLines = errContent.split('\n')
      .map(l => stripAnsi(l).trim())
      .filter(l => l.length > 0 && (l.includes('error') || l.includes('Error')) && !l.includes('request error'))
      .slice(-20)
      .map((l, i) => ({ id: 10000 + i, ...classifyLine(l), source: 'err' }))

    const allLines = [...outLines, ...errLines]
      .sort((a, b) => a.id - b.id)

    return NextResponse.json({
      lines: allLines,
      total: allLines.length,
      timestamp: new Date().toISOString(),
    })
  } catch (e: any) {
    return NextResponse.json({ lines: [], error: e.message }, { status: 500 })
  }
}
