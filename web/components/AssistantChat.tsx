'use client'
import { useState, useRef, useEffect } from 'react'

type Suggestion = { key: string; value: string; reason: string }
type Message = { role: 'user' | 'assistant'; text: string; suggestions?: Suggestion[] }

interface Props {
  onApplySuggestion: (key: string, value: string) => void
}

export function AssistantChat({ onApplySuggestion }: Props) {
  const [open, setOpen] = useState(false)
  const [messages, setMessages] = useState<Message[]>([
    { role: 'assistant', text: '👋 Hi! I\'m your Trade Monitor Assistant. I analyze your trades and suggest strategy improvements. Ask me anything or click the button below to get a quick analysis.' }
  ])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [notification, setNotification] = useState<string | null>(null)
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  // Poll for new assistant lessons (trade close triggers)
  useEffect(() => {
    const check = async () => {
      try {
        const r = await fetch('/api/stats')
        const d = await r.json()
        // Check if there's a new lesson saved
        const lessons = d.assistant_lessons
        if (lessons?.length) {
          const last = lessons[lessons.length - 1]
          const lastTs = localStorage.getItem('last_assistant_ts')
          if (last.timestamp !== lastTs) {
            localStorage.setItem('last_assistant_ts', last.timestamp)
            setNotification('📊 New trade analysis available')
            setMessages(prev => [...prev, { role: 'assistant', text: `📊 **Trade closed:** ${last.summary}`, suggestions: last.suggestions }])
            setTimeout(() => setNotification(null), 5000)
          }
        }
      } catch {}
    }
    const t = setInterval(check, 30000)
    return () => clearInterval(t)
  }, [])

  const send = async (msg?: string) => {
    const text = msg || input.trim()
    if (!text || loading) return
    setInput('')
    setMessages(prev => [...prev, { role: 'user', text }])
    setLoading(true)
    try {
      const r = await fetch('/api/assistant', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text }),
      })
      const d = await r.json()
      setMessages(prev => [...prev, { role: 'assistant', text: d.text || d.error || 'No response', suggestions: d.suggestions }])
    } catch {
      setMessages(prev => [...prev, { role: 'assistant', text: '❌ Connection error' }])
    }
    setLoading(false)
  }

  return (
    <>
      {/* Notification badge */}
      {notification && !open && (
        <div className="fixed z-50 cursor-pointer"
          style={{ bottom: 'calc(72px + env(safe-area-inset-bottom, 0px) + 52px)', right: 16, background: '#4f46e5', color: 'white', fontSize: 11, padding: '6px 12px', borderRadius: 20, boxShadow: '0 4px 12px rgba(79,70,229,0.4)' }}
          onClick={() => setOpen(true)}>
          {notification}
        </div>
      )}

      {/* Floating button */}
      <button onClick={() => setOpen(o => !o)}
        style={{ position: 'fixed', bottom: 'calc(72px + env(safe-area-inset-bottom, 0px) + 8px)', right: 16, width: 48, height: 48, borderRadius: '50%', background: open ? '#374151' : 'linear-gradient(135deg,#4f46e5,#6366f1)', color: 'white', fontSize: 20, border: 'none', cursor: 'pointer', zIndex: 200, display: 'flex', alignItems: 'center', justifyContent: 'center', boxShadow: '0 4px 16px rgba(79,70,229,0.4)', transition: 'all 0.2s' }}
        title="Trade Monitor Assistant">
        {open ? '✕' : '🤖'}
      </button>

      {/* Chat panel */}
      {open && (
        <div style={{ position: 'fixed', bottom: 'calc(72px + env(safe-area-inset-bottom, 0px) + 64px)', right: 16, width: 320, height: 460, background: '#0d0d1a', border: '1px solid #2a2a4a', borderRadius: 20, boxShadow: '0 8px 32px rgba(0,0,0,0.5)', zIndex: 200, display: 'flex', flexDirection: 'column', overflow: 'hidden' }}>
          {/* Header */}
          <div className="px-4 py-3 border-b border-[#1e1e3a] flex items-center gap-2">
            <span className="text-sm">🤖</span>
            <div>
              <div className="text-xs font-semibold text-[#e2e8f0]">Trade Monitor Assistant</div>
              <div className="text-[10px] text-[#4b5563]">Analyzes trades · Suggests config changes</div>
            </div>
          </div>

          {/* Messages */}
          <div className="flex-1 overflow-y-auto p-3 space-y-3">
            {messages.map((m, i) => (
              <div key={i} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                <div className={`max-w-[85%] rounded-xl px-3 py-2 text-xs leading-relaxed ${
                  m.role === 'user'
                    ? 'bg-[#4f46e5] text-white'
                    : 'bg-[#13132a] border border-[#2a2a4a] text-[#e2e8f0]'
                }`}>
                  <p className="whitespace-pre-wrap">{m.text}</p>

                  {/* Config suggestions */}
                  {m.suggestions?.length ? (
                    <div className="mt-2 space-y-1 border-t border-[#2a2a4a] pt-2">
                      <div className="text-[10px] text-[#6b7280] mb-1">Suggested config changes:</div>
                      {m.suggestions.map((s, j) => (
                        <div key={j} className="flex items-center justify-between gap-2 bg-[#0d0d1a] rounded-lg px-2 py-1">
                          <div className="flex-1 min-w-0">
                            <span className="text-[#a5b4fc] font-mono text-[10px]">{s.key}={s.value}</span>
                            <p className="text-[9px] text-[#6b7280] truncate">{s.reason}</p>
                          </div>
                          <button
                            onClick={() => onApplySuggestion(s.key, s.value)}
                            className="shrink-0 text-[10px] bg-[#4f46e5] hover:bg-[#4338ca] text-white px-2 py-0.5 rounded transition-colors">
                            Apply
                          </button>
                        </div>
                      ))}
                    </div>
                  ) : null}
                </div>
              </div>
            ))}
            {loading && (
              <div className="flex justify-start">
                <div className="bg-[#13132a] border border-[#2a2a4a] rounded-xl px-3 py-2 text-xs text-[#6b7280]">
                  ⏳ Analyzing...
                </div>
              </div>
            )}
            <div ref={bottomRef} />
          </div>

          {/* Quick actions */}
          <div className="px-3 py-2 border-t border-[#1e1e3a] flex gap-1 flex-wrap">
            {['Analyze recent trades', 'Why am I losing?', 'Optimize config'].map(q => (
              <button key={q} onClick={() => send(q)}
                className="text-[10px] bg-[#13132a] border border-[#2a2a4a] text-[#94a3b8] px-2 py-1 rounded-lg hover:border-[#4f46e5] hover:text-[#a5b4fc] transition-colors">
                {q}
              </button>
            ))}
          </div>

          {/* Input */}
          <div className="px-3 pb-3 flex gap-2">
            <input
              value={input}
              onChange={e => setInput(e.target.value)}
              onKeyDown={e => e.key === 'Enter' && !e.shiftKey && send()}
              placeholder="Ask about your trades..."
              className="flex-1 bg-[#13132a] border border-[#2a2a4a] rounded-lg px-3 py-2 text-xs text-[#e2e8f0] placeholder-[#4b5563] focus:border-[#4f46e5] outline-none"
            />
            <button onClick={() => send()}
              disabled={loading || !input.trim()}
              className="bg-[#4f46e5] hover:bg-[#4338ca] disabled:opacity-40 text-white text-xs px-3 py-2 rounded-lg transition-colors">
              ↑
            </button>
          </div>
        </div>
      )}
    </>
  )
}
