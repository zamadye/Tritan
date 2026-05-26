import { NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'

const LOG_DIR = path.join(process.cwd(), '..', 'data', 'analysis_logs')

function parseLogs(files: string[], filter?: { category?: string; gate?: string; search?: string }) {
  const records = []
  for (const f of files) {
    try {
      const content = fs.readFileSync(path.join(LOG_DIR, f), 'utf-8')
      const r: any = { file: f }

      const get = (pattern: RegExp) => content.match(pattern)?.[1]?.trim() || ''

      r.question    = get(/\*\*Question:\*\* (.+)/)
      r.category    = get(/\*\*Category:\*\* (.+)/)
      r.yes_price   = get(/\*\*YES Price:\*\* (.+)/)
      r.p_base      = get(/\*\*p_base:\*\* (.+)/)
      r.raw_gap     = get(/\*\*Raw gap:\*\* (.+)/)
      r.action      = get(/\*\*Action:\*\* (.+)/)
      r.confidence  = get(/\*\*Confidence:\*\* (.+)/)
      r.info_gap    = get(/\*\*Information Gap:\*\* (.+)/)
      r.catalyst    = get(/\*\*Catalyst Type:\*\* (.+)/)
      r.reasoning   = get(/### Reasoning\n(.+)/)
      r.gate_passed = content.includes('**Passed:** ✅')
      r.gate_reason = get(/\*\*Reason:\*\* (.+)/)
      r.timestamp   = f.slice(0, 15).replace('_', ' ').replace(/_/g, ':')

      const outcome = content.match(/\*\*(WIN|LOSS)\*\*.*P&L: \$([+-][\d.]+)/)
      if (outcome) { r.result = outcome[1]; r.pnl = parseFloat(outcome[2]) }

      // Count news sources
      const sources = (content.match(/\[Bing News\]|\[Metaculus\]|\[CoinTelegraph\]|\[BBC Sport\]|\[Al Jazeera\]|\[Guardian\]/g) || [])
      r.news_sources = sources.length

      // Apply filters
      if (filter?.category && r.category !== filter.category) continue
      if (filter?.gate === 'pass' && !r.gate_passed) continue
      if (filter?.gate === 'fail' && r.gate_passed) continue
      if (filter?.search && !r.question.toLowerCase().includes(filter.search.toLowerCase())) continue

      records.push(r)
    } catch { continue }
  }
  return records
}

export async function GET(req: Request) {
  const { searchParams } = new URL(req.url)
  const category = searchParams.get('category') || undefined
  const gate     = searchParams.get('gate') || undefined
  const search   = searchParams.get('search') || undefined
  const limit    = parseInt(searchParams.get('limit') || '50')

  if (!fs.existsSync(LOG_DIR)) {
    return NextResponse.json({ records: [], stats: {}, total: 0 })
  }

  const files = fs.readdirSync(LOG_DIR).filter(f => f.endsWith('.md')).sort().reverse()
  const records = parseLogs(files, { category, gate, search }).slice(0, limit)

  // Stats
  const all = parseLogs(files)
  const passed = all.filter(r => r.gate_passed)
  const resolved = all.filter(r => r.result)
  const wins = resolved.filter(r => r.result === 'WIN')

  const catStats: Record<string, any> = {}
  for (const r of all) {
    const c = r.category || 'other'
    if (!catStats[c]) catStats[c] = { pass: 0, fail: 0 }
    r.gate_passed ? catStats[c].pass++ : catStats[c].fail++
  }

  return NextResponse.json({
    records,
    total: files.length,
    filtered: records.length,
    stats: {
      total: all.length,
      gate_pass_rate: passed.length / Math.max(all.length, 1),
      resolved: resolved.length,
      wr: wins.length / Math.max(resolved.length, 1),
      by_category: catStats,
    }
  })
}
