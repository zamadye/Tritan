'use client'
import { useState, useRef, useEffect } from 'react'
import { MessageCircle, X, Send, Sparkles, Settings, TrendingUp, HelpCircle, Lightbulb } from 'lucide-react'

type Suggestion = { key: string; value: string; reason: string }
type Message = { role: 'user' | 'assistant'; text: string; suggestions?: Suggestion[]; type?: 'analysis' | 'config' | 'general' }

const QUICK_ACTIONS = [
  { icon: <TrendingUp size={12} />, label: 'Analyze recent trades', msg: 'Analyze my recent trades and tell me what patterns you see.' },
  { icon: <HelpCircle size={12} />, label: 'Why am I losing?', msg: 'Why am I losing? Analyze my loss patterns and suggest improvements.' },
  { icon: <Settings size={12} />, label: 'Optimize config', msg: 'Analyze my current config and suggest optimizations based on my trade history.' },
  { icon: <Lightbulb size={12} />, label: 'Strategy advice', msg: 'Based on my performance data, what strategy changes would you recommend?' },
]

interface Props {
  onApplySuggestion: (key: string, value: string) => void
}

export function AssistantChat({ onApplySuggestion }: Props) {
  const [open, setOpen] = useState(false)
  const [messages, setMessages] = useState<Message[]>([
    { role: 'assistant', text: '👋 Hi! I\'m your Trade Monitor Assistant.\n\nI can help you with:\n• Analyzing trade performance\n• Suggesting config improvements\n• Explaining strategy decisions\n• Debugging losing streaks\n\nAsk me anything or use the quick actions below.', type: 'general' }
  ])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [notification, setNotification] = useState<string | null>(null)
  const bottomRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  // Poll for new assistant lessons
  useEffect(() => {
    const check = async () => {
      try {
        const r = await fetch('/api/stats')
        const d = await r.json()
        const lessons = d.assistant_lessons
        if (lessons?.length) {
          const last = lessons[lessons.length - 1]
          const lastTs = localStorage.getItem('last_assistant_ts')
          if (last.timestamp !== lastTs) {
            localStorage.setItem('last_assistant_ts', last.timestamp)
            setNotification('New trade analysis available')
            setMessages(prev => [...prev, { role: 'assistant', text: `📊 **Trade closed:** ${last.summary}`, suggestions: last.suggestions, type: 'analysis' }])
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
      setMessages(prev => [...prev, {
        role: 'assistant',
        text: d.text || d.error || 'No response',
        suggestions: d.suggestions,
        type: d.suggestions?.length ? 'config' : 'general',
      }])
    } catch {
      setMessages(prev => [...prev, { role: 'assistant', text: '❌ Connection error. Please try again.', type: 'general' }])
    }
    setLoading(false)
  }

  return (
    <>
      {/* Notification badge */}
      {notification && !open && (
        <div className="fixed z-50 cursor-pointer fade-in"
          style={{ bottom: 'calc(80px + env(safe-area-inset-bottom, 0px) + 52px)', right: 16, background: 'var(--accent)', color: 'white', fontSize: 11, padding: '6px 14px', borderRadius: 'var(--radius-full)', boxShadow: '0 4px 12px rgba(99,102,241,0.4)' }}
          onClick={() => setOpen(true)}>
          {notification}
        </div>
      )}

      {/* Floating button */}
      <button onClick={() => setOpen(o => !o)}
        style={{
          position: 'fixed', bottom: 'calc(80px + env(safe-area-inset-bottom, 0px) + 8px)', right: 16,
          width: 52, height: 52, borderRadius: '50%',
          background: open ? 'var(--bg3)' : 'linear-gradient(135deg, var(--accent-dark), var(--accent))',
          color: 'white', border: 'none', cursor: 'pointer', zIndex: 200,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          boxShadow: '0 4px 20px rgba(99,102,241,0.4)', transition: 'all 0.2s',
        }}
        title="Trade Monitor Assistant">
        {open ? <X size={20} /> : <MessageCircle size={22} />}
      </button>

      {/* Chat panel */}
      {open && (
        <div className="assistant-chat-panel" style={{
          position: 'fixed', bottom: 'calc(80px + env(safe-area-inset-bottom, 0px) + 68px)', right: 16,
          width: 'min(340px, calc(100vw - 32px))', maxHeight: 'calc(100vh - 200px)', height: 500,
          background: 'var(--bg)', border: '1px solid var(--border)', borderRadius: 'var(--radius-lg)',
          boxShadow: 'var(--shadow-lg)', zIndex: 200,
          display: 'flex', flexDirection: 'column', overflow: 'hidden',
        }}>
          {/* Header */}
          <div className="flex items-center gap-2.5 px-4 py-3" style={{ borderBottom: '1px solid var(--border2)' }}>
            <div className="w-8 h-8 rounded-lg flex items-center justify-center" style={{ background: 'var(--accent-bg)' }}>
              <Sparkles size={16} style={{ color: 'var(--accent)' }} />
            </div>
            <div className="flex-1">
              <div className="text-xs font-semibold" style={{ color: 'var(--text)' }}>Trade Assistant</div>
              <div className="text-[10px]" style={{ color: 'var(--dim)' }}>AI-powered trade analysis & config advisor</div>
            </div>
            <button onClick={() => setOpen(false)} className="icon-btn" style={{ width: 28, height: 28, background: 'transparent' }}>
              <X size={14} style={{ color: 'var(--dim)' }} />
            </button>
          </div>

          {/* Messages */}
          <div className="flex-1 overflow-y-auto p-3 flex flex-col gap-3">
            {messages.map((m, i) => (
              <div key={i} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                <div style={{
                  maxWidth: '88%', borderRadius: 'var(--radius-md)', padding: '10px 12px',
                  fontSize: 12, lineHeight: 1.6,
                  ...(m.role === 'user'
                    ? { background: 'var(--accent)', color: 'white' }
                    : { background: 'var(--bg2)', border: '1px solid var(--border)', color: 'var(--text2)' }),
                }}>
                  <p className="whitespace-pre-wrap">{m.text}</p>

                  {/* Config suggestions */}
                  {m.suggestions?.length ? (
                    <div className="mt-2 pt-2 space-y-1.5" style={{ borderTop: '1px solid var(--border2)' }}>
                      <div className="text-[10px] font-semibold" style={{ color: 'var(--dim)' }}>Suggested config changes:</div>
                      {m.suggestions.map((s, j) => (
                        <div key={j} className="flex items-center justify-between gap-2 p-2 rounded-lg" style={{ background: 'var(--bg)' }}>
                          <div className="flex-1 min-w-0">
                            <span className="text-[10px] mono font-semibold" style={{ color: 'var(--accent-light)' }}>{s.key}={s.value}</span>
                            <p className="text-[9px] truncate" style={{ color: 'var(--dim)' }}>{s.reason}</p>
                          </div>
                          <button onClick={() => onApplySuggestion(s.key, s.value)}
                            className="btn btn-primary btn-sm flex-shrink-0" style={{ padding: '4px 8px', fontSize: 10 }}>
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
                <div className="px-3 py-2 rounded-xl text-xs" style={{ background: 'var(--bg2)', border: '1px solid var(--border)', color: 'var(--dim)' }}>
                  <span className="animate-pulse">⏳ Analyzing...</span>
                </div>
              </div>
            )}
            <div ref={bottomRef} />
          </div>

          {/* Quick actions */}
          <div className="px-3 py-2 flex gap-1.5 flex-wrap" style={{ borderTop: '1px solid var(--border2)' }}>
            {QUICK_ACTIONS.map(q => (
              <button key={q.label} onClick={() => send(q.msg)}
                className="flex items-center gap-1.5 text-[10px] px-2.5 py-1.5 rounded-lg transition-colors"
                style={{ background: 'var(--bg2)', border: '1px solid var(--border)', color: 'var(--muted)' }}>
                {q.icon} {q.label}
              </button>
            ))}
          </div>

          {/* Input */}
          <div className="px-3 pb-3 flex gap-2">
            <input value={input} onChange={e => setInput(e.target.value)}
              onKeyDown={e => e.key === 'Enter' && !e.shiftKey && send()}
              placeholder="Ask about your trades or config..."
              className="input" style={{ padding: '10px 12px', fontSize: 12 }} />
            <button onClick={() => send()} disabled={loading || !input.trim()}
              className="btn btn-primary" style={{ padding: '10px 12px', minWidth: 40 }}>
              <Send size={14} />
            </button>
          </div>
        </div>
      )}
    </>
  )
}
