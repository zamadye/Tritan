'use client'
import { useState } from 'react'
import { useAuth } from '@/lib/auth'
import { Check, Star, Users, Zap, Clock, ArrowRight, Mail } from 'lucide-react'

const PLANS = [
  {
    name: 'Free',
    price: '$0',
    desc: 'Signal-only access',
    color: 'var(--muted)',
    features: [
      'Win/loss signal notifications',
      'Market analysis alerts',
      'Basic performance stats',
      'Community Discord access',
    ],
    cta: 'Join Waitlist',
    badge: null,
  },
  {
    name: 'Early Adopter',
    price: '$0',
    period: '1 month free',
    desc: 'Full platform access',
    color: 'var(--accent)',
    features: [
      'Everything in Free',
      'Full automated execution',
      'AI trade assistant',
      'Advanced analytics & proof',
      'Custom config tuning',
      'Priority support',
    ],
    cta: 'Apply for Early Access',
    badge: '50 spots',
    highlight: true,
  },
  {
    name: 'Pro',
    price: '$49',
    period: '/month',
    desc: 'Full access + priority',
    color: 'var(--yellow)',
    features: [
      'Everything in Early Adopter',
      'Unlimited AI analysis',
      'Multi-strategy support',
      'Priority execution',
      'API access',
      '1-on-1 onboarding call',
    ],
    cta: 'Coming Soon',
    badge: null,
    disabled: true,
  },
]

export default function SubscribePage() {
  const { user } = useAuth()
  const [email, setEmail] = useState(user?.email || '')
  const [submitted, setSubmitted] = useState(false)
  const [plan, setPlan] = useState('')

  const handleSubmit = (selectedPlan: string) => {
    if (!email.includes('@')) return
    setPlan(selectedPlan)
    // In production, this would call an API to register the waitlist
    localStorage.setItem('tritan_waitlist', JSON.stringify({ email, plan: selectedPlan, date: new Date().toISOString() }))
    setSubmitted(true)
  }

  if (submitted) {
    return (
      <div className="min-h-screen flex items-center justify-center p-4" style={{ background: 'var(--bg)' }}>
        <div className="text-center fade-in max-w-sm">
          <div className="text-5xl mb-4">🎉</div>
          <h1 className="text-lg font-bold mb-2" style={{ color: 'var(--text)' }}>You&apos;re on the list!</h1>
          <p className="text-sm mb-1" style={{ color: 'var(--muted)' }}>
            {plan === 'Early Adopter'
              ? 'We\'ll notify you when a spot opens up. Early adopters get 1 month full access free.'
              : 'We\'ll notify you when free signal access launches.'}
          </p>
          <p className="text-xs mono mb-6" style={{ color: 'var(--dim)' }}>{email}</p>
          <a href="/" className="btn btn-primary">
            Go to Dashboard <ArrowRight size={14} />
          </a>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen p-4 pb-20" style={{ background: 'var(--bg)' }}>
      <div className="max-w-3xl mx-auto fade-in">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-xl font-bold mb-2" style={{ color: 'var(--text)' }}>Choose Your Plan</h1>
          <p className="text-sm" style={{ color: 'var(--dim)' }}>
            Start free, upgrade when you&apos;re ready. Early adopters get full access for 1 month.
          </p>
        </div>

        {/* Stats banner */}
        <div className="flex justify-center gap-6 mb-8">
          <div className="flex items-center gap-2 text-xs" style={{ color: 'var(--muted)' }}>
            <Users size={14} style={{ color: 'var(--accent)' }} />
            <span><strong style={{ color: 'var(--text)' }}>50</strong> early adopter spots</span>
          </div>
          <div className="flex items-center gap-2 text-xs" style={{ color: 'var(--muted)' }}>
            <Users size={14} style={{ color: 'var(--green)' }} />
            <span><strong style={{ color: 'var(--text)' }}>1,000</strong> free signal spots</span>
          </div>
        </div>

        {/* Plans grid */}
        <div className="grid gap-4" style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))' }}>
          {PLANS.map(p => (
            <div key={p.name} className="section-card relative" style={{
              border: p.highlight ? `2px solid var(--accent)` : undefined,
              opacity: p.disabled ? 0.6 : 1,
            }}>
              {p.badge && (
                <div className="absolute -top-3 left-1/2 -translate-x-1/2">
                  <span className="badge" style={{
                    background: 'var(--accent-bg)', color: 'var(--accent-light)', borderColor: 'var(--accent-border)',
                  }}>
                    <Star size={10} className="mr-1" /> {p.badge}
                  </span>
                </div>
              )}
              <div className="p-5">
                <h3 className="text-sm font-bold mb-1" style={{ color: p.color }}>{p.name}</h3>
                <div className="flex items-baseline gap-1 mb-1">
                  <span className="text-2xl font-bold" style={{ color: 'var(--text)' }}>{p.price}</span>
                  {p.period && <span className="text-xs" style={{ color: 'var(--dim)' }}>{p.period}</span>}
                </div>
                <p className="text-xs mb-4" style={{ color: 'var(--dim)' }}>{p.desc}</p>

                <div className="flex flex-col gap-2 mb-5">
                  {p.features.map(f => (
                    <div key={f} className="flex items-start gap-2 text-xs">
                      <Check size={14} className="flex-shrink-0 mt-0.5" style={{ color: 'var(--green)' }} />
                      <span style={{ color: 'var(--text2)' }}>{f}</span>
                    </div>
                  ))}
                </div>

                {p.disabled ? (
                  <button disabled className="btn btn-secondary w-full text-xs">
                    <Clock size={12} /> {p.cta}
                  </button>
                ) : (
                  <div>
                    <input type="email" value={email} onChange={e => setEmail(e.target.value)}
                      placeholder="your@email.com" className="input mb-2 text-xs" />
                    <button onClick={() => handleSubmit(p.name)} disabled={!email.includes('@')}
                      className="btn btn-primary w-full text-xs">
                      <Mail size={12} /> {p.cta}
                    </button>
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>

        {/* FAQ */}
        <div className="mt-10 section-card p-5">
          <h3 className="text-sm font-bold mb-4" style={{ color: 'var(--text)' }}>Frequently Asked Questions</h3>
          <div className="flex flex-col gap-4">
            {[
              { q: 'What happens after the 1 month early adopter trial?', a: 'You\'ll be offered a discounted rate to continue. If you don\'t upgrade, you keep signal-only access for free.' },
              { q: 'Is my Polymarket API key safe?', a: 'Yes. Your keys are stored only on your server in the .env file. We never transmit them to any external service.' },
              { q: 'Can I switch between demo and live mode?', a: 'Yes. You can switch anytime from the Config tab. Demo mode uses real market prices but doesn\'t execute trades.' },
              { q: 'What markets does TRITAN trade?', a: 'Sports, crypto, geopolitics, and politics markets on Polymarket. The AI analyzes price movement patterns, not outcomes.' },
            ].map(({ q, a }) => (
              <div key={q}>
                <div className="text-xs font-semibold mb-1" style={{ color: 'var(--text2)' }}>{q}</div>
                <div className="text-[11px] leading-relaxed" style={{ color: 'var(--dim)' }}>{a}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
