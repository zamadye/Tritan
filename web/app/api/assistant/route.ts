import { NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'

const DATA_DIR = path.join(process.cwd(), '..', 'data')
const ENV_FILE = path.join(process.cwd(), '..', '.env')

function readJSON(file: string) {
  try { return JSON.parse(fs.readFileSync(path.join(DATA_DIR, file), 'utf-8')) }
  catch { return null }
}

function readEnvValue(key: string): string {
  try {
    const m = fs.readFileSync(ENV_FILE, 'utf-8').match(new RegExp(`^${key}=(.+)$`, 'm'))
    return m?.[1] ?? ''
  } catch { return '' }
}

function buildContext(): string {
  const trades: any[] = readJSON('demo_trades.json') || []
  const evolution = readJSON('evolution_lessons.json') || {}
  const lessons = readJSON('assistant_lessons.json') || []

  const resolved = trades.filter(t => t.actual_outcome)
  const open = trades.filter(t => !t.actual_outcome)
  const wins = resolved.filter(t => t.prediction_correct)
  const pnl = resolved.reduce((s: number, t: any) => s + (t.pnl || 0), 0)
  const wr = resolved.length ? wins.length / resolved.length : 0

  // Recent 10 resolved trades
  const recent = [...resolved]
    .sort((a, b) => (b.resolved_at || '').localeCompare(a.resolved_at || ''))
    .slice(0, 10)
    .map((t: any) => `  [${t.prediction_correct ? 'WIN' : 'LOSS'}] ${t.side} @${(t.price_at_entry * 100).toFixed(0)}% pnl=$${(t.pnl || 0).toFixed(2)} exit=${t.exit_reason || 'RESOLVED'} cat=${t.category || '?'} conf=${((t.confidence_at_bet || 0) * 100).toFixed(0)}% edge=${((t.edge_at_bet || 0) * 100).toFixed(1)}% | ${(t.market_question || '').slice(0, 60)}`)
    .join('\n')

  // Key config
  const cfg = {
    MIN_CONFIDENCE: readEnvValue('MIN_CONFIDENCE'),
    MIN_STAT_EDGE: readEnvValue('MIN_STAT_EDGE'),
    EXIT_TAKE_PROFIT: readEnvValue('EXIT_TAKE_PROFIT'),
    EXIT_STOP_LOSS: readEnvValue('EXIT_STOP_LOSS'),
    TRAILING_STOP_PCT: readEnvValue('TRAILING_STOP_PCT'),
    MIN_HOLD_MINUTES: readEnvValue('MIN_HOLD_MINUTES'),
    MAX_BET_SIZE: readEnvValue('MAX_BET_SIZE'),
    MIN_BET_SIZE: readEnvValue('MIN_BET_SIZE'),
    EXIT_MAX_HOURS: readEnvValue('EXIT_MAX_HOURS'),
  }

  // Category breakdown
  const catMap: Record<string, { w: number; l: number; pnl: number }> = {}
  for (const t of resolved) {
    const cat = t.category || 'other'
    if (!catMap[cat]) catMap[cat] = { w: 0, l: 0, pnl: 0 }
    if (t.prediction_correct) catMap[cat].w++; else catMap[cat].l++
    catMap[cat].pnl += t.pnl || 0
  }
  const catStr = Object.entries(catMap)
    .map(([c, s]) => `${c}: WR=${s.w + s.l ? ((s.w / (s.w + s.l)) * 100).toFixed(0) : '?'}% pnl=$${s.pnl.toFixed(2)} (${s.w}W/${s.l}L)`)
    .join(', ')

  // Recent assistant lessons
  const lessonStr = lessons.slice(-3).map((l: any) => `  - ${l.summary}`).join('\n')

  return `TRITAN TRADE MONITOR CONTEXT
============================
Performance: ${resolved.length} resolved | WR=${(wr * 100).toFixed(1)}% | PnL=$${pnl.toFixed(2)} | Open=${open.length}
Category breakdown: ${catStr || 'no data yet'}

Current config:
  MIN_CONFIDENCE=${cfg.MIN_CONFIDENCE} | MIN_STAT_EDGE=${cfg.MIN_STAT_EDGE}
  TP=${cfg.EXIT_TAKE_PROFIT} | SL=${cfg.EXIT_STOP_LOSS} | Trail=${cfg.TRAILING_STOP_PCT}
  Min hold=${cfg.MIN_HOLD_MINUTES}min | Max hold=${cfg.EXIT_MAX_HOURS}h
  Bet size=$${cfg.MIN_BET_SIZE}-$${cfg.MAX_BET_SIZE}

Recent 10 trades:
${recent || '  No resolved trades yet'}

Evolution lessons: ${evolution.overall_win_rate ? `WR=${(evolution.overall_win_rate * 100).toFixed(0)}% (${evolution.total_resolved} trades)` : 'none yet'}
${evolution.recent_mistakes?.length ? 'Recent mistakes:\n' + evolution.recent_mistakes.slice(0, 2).map((m: any) => `  - ${m.lesson}`).join('\n') : ''}

Previous assistant insights:
${lessonStr || '  None yet'}
`
}

export async function POST(req: Request) {
  const { message, mode } = await req.json()
  if (!message?.trim()) return NextResponse.json({ error: 'No message' }, { status: 400 })

  const apiKey = readEnvValue('AI_API_KEY')
  const baseUrl = readEnvValue('AI_BASE_URL') || 'https://token-plan-sgp.xiaomimimo.com/v1'
  const model = readEnvValue('AI_MODEL') || 'mimo-v2.5'

  const context = buildContext()

  const systemPrompt = `You are TRITAN Trade Monitor Assistant. You analyze prediction market trading performance and give actionable advice.

CRITICAL: Always respond in the SAME language as the user's message. If user writes in English → respond in English. If user writes in Indonesian (Bahasa Indonesia) → respond in Indonesian. NEVER respond in Chinese.

Your role:
1. Monitor trade results (wins/losses) and identify patterns
2. Diagnose what caused losses — wrong confidence threshold? bad exit timing? wrong category?
3. Recommend specific config changes with exact values
4. When recommending config changes, always include a "config_suggestions" JSON array

IMPORTANT: Focus on PRICE MOVEMENT strategy, not outcome prediction.
- Sports: wait for resolved (fast resolution)
- Crypto/Geo: max 24h hold, exit via trailing stop or TP
- Dynamic TP: edge≥20%→40%, edge≥15%→30%, edge≥8%→20%, default→15%

When you suggest config changes, end your response with:
<config_suggestions>
[{"key": "MIN_CONFIDENCE", "value": "0.70", "reason": "Too many low-confidence losses"}]
</config_suggestions>

Be concise and direct. Use data from context.`

  try {
    const resp = await fetch(`${baseUrl}/chat/completions`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${apiKey}` },
      body: JSON.stringify({
        model,
        max_tokens: 800,
        messages: [
          { role: 'system', content: systemPrompt },
          { role: 'user', content: `${context}\n\nUser: ${message}` },
        ],
      }),
    })

    const data = await resp.json()
    const raw = data.choices?.[0]?.message?.content || ''

    // Parse config suggestions
    const suggestMatch = raw.match(/<config_suggestions>([\s\S]*?)<\/config_suggestions>/)
    let suggestions: { key: string; value: string; reason: string }[] = []
    if (suggestMatch) {
      try { suggestions = JSON.parse(suggestMatch[1].trim()) } catch {}
    }
    const text = raw.replace(/<config_suggestions>[\s\S]*?<\/config_suggestions>/, '').trim()

    // Save lesson if this was triggered by a trade close
    if (mode === 'trade_close' && text) {
      const lessons = readJSON('assistant_lessons.json') || []
      lessons.push({
        timestamp: new Date().toISOString(),
        summary: text.slice(0, 200),
        suggestions,
      })
      fs.writeFileSync(path.join(DATA_DIR, 'assistant_lessons.json'), JSON.stringify(lessons.slice(-50), null, 2))
    }

    return NextResponse.json({ text, suggestions })
  } catch (e: any) {
    return NextResponse.json({ error: e.message }, { status: 500 })
  }
}
