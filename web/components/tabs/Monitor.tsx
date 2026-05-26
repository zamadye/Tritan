'use client'
import { useState, useEffect, useRef } from 'react'

type LogLine = { id: number; type: string; text: string }

// Terminal color map — like bash/zsh terminal colors
const COLOR: Record<string, string> = {
  bet:           '#00ff00',  // bright green — new bet
  exit:          '#00ffff',  // cyan — exit
  resolve:       '#00ff00',  // green — win
  resolver:      '#888888',  // gray
  scan_start:    '#ffff00',  // yellow — scanning
  scan_found:    '#87ceeb',  // light blue
  gate_fail:     '#555555',  // dark gray — skipped
  gate_limit:    '#555555',
  gate_catalyst: '#666666',
  analysis:      '#ff87ff',  // magenta — LLM analysis
  learning:      '#87ceeb',  // light blue
  waiting:       '#444444',  // very dark
  stats:         '#aaaaaa',  // light gray
  sell:          '#ffa500',  // orange — sell
  error:         '#ff4444',  // red — error
  data:          '#00cc88',  // teal — data fetch
  llm:           '#cc88ff',  // purple — LLM
  info:          '#888888',
}

const PREFIX: Record<string, string> = {
  bet:           '[TRADE]  ',
  exit:          '[EXIT]   ',
  resolve:       '[RESOLVE]',
  resolver:      '[RESOLVE]',
  scan_start:    '[SCAN]   ',
  scan_found:    '[SCAN]   ',
  gate_fail:     '[SKIP]   ',
  gate_limit:    '[SKIP]   ',
  gate_catalyst: '[SKIP]   ',
  analysis:      '[ANALYZE]',
  learning:      '[LEARN]  ',
  waiting:       '[WAIT]   ',
  stats:         '[STATS]  ',
  sell:          '[SELL]   ',
  error:         '[ERROR]  ',
  data:          '[DATA]   ',
  llm:           '[LLM]    ',
  info:          '[INFO]   ',
}

export function Monitor() {
  const [lines, setLines] = useState<LogLine[]>([])
  const [filter, setFilter] = useState('all')
  const [paused, setPaused] = useState(false)
  const [autoScroll, setAutoScroll] = useState(true)
  const [lastCount, setLastCount] = useState(0)
  const bottomRef = useRef<HTMLDivElement>(null)

  const fetchLogs = async () => {
    if (paused) return
    try {
      const r = await fetch('/api/logs?lines=300')
      const d = await r.json()
      if (d.lines?.length !== lastCount) {
        setLines(d.lines || [])
        setLastCount(d.lines?.length || 0)
      }
    } catch {}
  }

  useEffect(() => {
    fetchLogs()
    const t = setInterval(fetchLogs, 2000)
    return () => clearInterval(t)
  }, [paused, lastCount])

  useEffect(() => {
    if (autoScroll && bottomRef.current) {
      bottomRef.current.scrollIntoView({ behavior: 'smooth' })
    }
  }, [lines, autoScroll])

  const filtered = lines.filter(l => {
    if (l.type === 'empty') return false
    if (filter === 'all') return l.type !== 'waiting'
    if (filter === 'trades') return ['bet','exit','resolve','sell'].includes(l.type)
    if (filter === 'scan') return ['scan_start','scan_found','gate_fail','gate_limit','gate_catalyst'].includes(l.type)
    if (filter === 'errors') return l.type === 'error'
    if (filter === 'llm') return ['analysis','llm'].includes(l.type)
    return true
  })

  const now = new Date().toLocaleTimeString('en-US', { hour12: false })
  const bets = lines.filter(l => l.type === 'bet').length
  const errors = lines.filter(l => l.type === 'error').length

  return (
    <div style={{
      display: 'flex', flexDirection: 'column',
      height: 'calc(100dvh - 52px - 56px - 16px)', /* dvh - top header - bottom nav - padding */
      minHeight: 300,
      fontFamily: '"JetBrains Mono", "Fira Code", "Courier New", monospace',
      overflow: 'hidden',
    }}>
      {/* Terminal title bar */}
      <div style={{
        background: '#1a1a1a',
        borderBottom: '1px solid #333',
        padding: '6px 12px',
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        flexShrink: 0,
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <span style={{ color: '#ff5f56', fontSize: 10 }}>●</span>
          <span style={{ color: '#ffbd2e', fontSize: 10 }}>●</span>
          <span style={{ color: '#27c93f', fontSize: 10 }}>●</span>
          <span style={{ color: '#888', fontSize: 11, marginLeft: 8 }}>
            tritan-agent — system monitor
          </span>
        </div>
        <div style={{ display: 'flex', gap: 6, alignItems: 'center' }}>
          <span style={{ color: '#27c93f', fontSize: 10 }}>
            {bets > 0 && `${bets} bets`}
          </span>
          {errors > 0 && <span style={{ color: '#ff5f56', fontSize: 10 }}>{errors} errors</span>}
          <span style={{ color: '#555', fontSize: 10 }}>{now}</span>
        </div>
      </div>

      {/* Filter bar — terminal style */}
      <div style={{
        background: '#111',
        borderBottom: '1px solid #222',
        padding: '4px 12px',
        display: 'flex', gap: 4, alignItems: 'center',
        flexShrink: 0,
      }}>
        <span style={{ color: '#555', fontSize: 10, marginRight: 4 }}>filter:</span>
        {[
          { id: 'all', label: 'all' },
          { id: 'trades', label: 'trades' },
          { id: 'scan', label: 'scan' },
          { id: 'llm', label: 'llm' },
          { id: 'errors', label: 'errors' },
        ].map(f => (
          <button key={f.id} onClick={() => setFilter(f.id)} style={{
            padding: '1px 8px', fontSize: 10, border: 'none', cursor: 'pointer', borderRadius: 2,
            background: filter === f.id ? '#333' : 'transparent',
            color: filter === f.id ? '#00ff00' : '#555',
            fontFamily: 'inherit',
          }}>
            [{f.label}]
          </button>
        ))}
        <div style={{ marginLeft: 'auto', display: 'flex', gap: 8 }}>
          <button onClick={() => setPaused(p => !p)} style={{
            padding: '1px 8px', fontSize: 10, border: '1px solid #333', cursor: 'pointer', borderRadius: 2,
            background: 'transparent', color: paused ? '#ffbd2e' : '#555', fontFamily: 'inherit',
          }}>
            {paused ? '[resume]' : '[pause]'}
          </button>
          <button onClick={() => setAutoScroll(a => !a)} style={{
            padding: '1px 8px', fontSize: 10, border: '1px solid #333', cursor: 'pointer', borderRadius: 2,
            background: 'transparent', color: autoScroll ? '#27c93f' : '#555', fontFamily: 'inherit',
          }}>
            {autoScroll ? '[scroll:on]' : '[scroll:off]'}
          </button>
        </div>
      </div>

      {/* Terminal output */}
      <div style={{
        flex: 1, overflowY: 'auto', background: '#0d0d0d',
        padding: '8px 12px',
        scrollbarWidth: 'thin', scrollbarColor: '#333 #0d0d0d',
      }}>
        {/* Prompt header */}
        <div style={{ color: '#27c93f', fontSize: 11, marginBottom: 8 }}>
          <span style={{ color: '#87ceeb' }}>root@tritan</span>
          <span style={{ color: '#555' }}>:</span>
          <span style={{ color: '#87ceeb' }}>~</span>
          <span style={{ color: '#555' }}>$ </span>
          <span style={{ color: '#aaa' }}>tail -f /var/log/tritan-agent.log</span>
        </div>

        {filtered.length === 0 ? (
          <div style={{ color: '#444', fontSize: 11 }}>
            waiting for agent output...
            <span style={{ animation: 'blink 1s infinite' }}>_</span>
          </div>
        ) : (
          filtered.map(line => {
            const color = COLOR[line.type] || '#888'
            const prefix = PREFIX[line.type] || '[INFO]   '
            const ts = new Date().toLocaleTimeString('en-US', { hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' })

            return (
              <div key={line.id} style={{
                fontSize: 11, lineHeight: 1.7,
                display: 'flex', gap: 8, minWidth: 0,
              }}>
                <span style={{ color: '#444', flexShrink: 0, userSelect: 'none' }}>{ts}</span>
                <span style={{ color: color === '#555555' ? '#444' : '#555', flexShrink: 0, userSelect: 'none' }}>{prefix}</span>
                <span style={{ color, wordBreak: 'break-all', minWidth: 0, flex: 1 }}>{line.text}</span>
              </div>
            )
          })
        )}
        <div ref={bottomRef} />
      </div>

      {/* Status bar */}
      <div style={{
        background: '#1a1a1a', borderTop: '1px solid #222',
        padding: '3px 12px', fontSize: 10,
        display: 'flex', justifyContent: 'space-between',
        color: '#555', flexShrink: 0,
      }}>
        <span>{filtered.length} lines · {paused ? 'PAUSED' : 'LIVE'}</span>
        <span>tritan-agent · live mode · scan every 3min</span>
      </div>

      <style>{`
        @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
      `}</style>
    </div>
  )
}
