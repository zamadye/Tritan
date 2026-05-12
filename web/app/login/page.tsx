'use client'
import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/lib/auth'
import { Mail, Key, ArrowRight, SkipForward, Shield, Zap } from 'lucide-react'

export default function LoginPage() {
  const { user, login, setupPoly, skipPoly } = useAuth()
  const router = useRouter()
  const [step, setStep] = useState<'email' | 'poly'>(user ? 'poly' : 'email')
  const [email, setEmail] = useState('')
  const [apiKey, setApiKey] = useState('')
  const [secret, setSecret] = useState('')
  const [passphrase, setPassphrase] = useState('')
  const [serverMode, setServerMode] = useState<string>('demo')

  useEffect(() => {
    // Fetch current server mode
    fetch('/api/agent').then(r => r.json()).then(d => {
      setServerMode(d.mode || 'demo')
    }).catch(() => {})
  }, [])

  const handleEmail = () => {
    if (!email.includes('@')) return
    login(email)
    // Sync with server mode
    const stored = localStorage.getItem('tritan_user')
    if (stored) {
      const u = JSON.parse(stored)
      u.mode = serverMode
      localStorage.setItem('tritan_user', JSON.stringify(u))
    }
    setStep('poly')
  }

  const handlePoly = () => {
    if (!apiKey || !secret || !passphrase) return
    setupPoly(apiKey, secret, passphrase)
    // Sync with server mode
    const stored = localStorage.getItem('tritan_user')
    if (stored) {
      const u = JSON.parse(stored)
      u.mode = 'live'
      localStorage.setItem('tritan_user', JSON.stringify(u))
    }
    router.push('/')
  }

  const handleSkip = () => {
    skipPoly()
    // Sync with server mode
    const stored = localStorage.getItem('tritan_user')
    if (stored) {
      const u = JSON.parse(stored)
      u.mode = serverMode
      localStorage.setItem('tritan_user', JSON.stringify(u))
    }
    router.push('/')
  }

  return (
    <div className="min-h-screen flex items-center justify-center p-4" style={{ background: 'var(--bg)' }}>
      <div className="w-full max-w-md fade-in">
        {/* Logo */}
        <div className="text-center mb-8">
          <div className="text-3xl mb-2">⚡</div>
          <h1 className="text-xl font-bold" style={{ color: 'var(--accent-light)' }}>TRITAN</h1>
          <p className="text-xs mt-1" style={{ color: 'var(--dim)' }}>AI-Powered Prediction Market Trading</p>
        </div>

        {step === 'email' ? (
          /* ── Step 1: Email ── */
          <div className="section-card p-6">
            <div className="flex items-center gap-2 mb-4">
              <Mail size={18} style={{ color: 'var(--accent)' }} />
              <h2 className="text-sm font-bold" style={{ color: 'var(--text)' }}>Sign in to continue</h2>
            </div>
            <p className="text-xs mb-4" style={{ color: 'var(--dim)' }}>
              Enter your email to access the TRITAN trading dashboard. No password needed — we&apos;ll remember your device.
            </p>
            <input type="email" value={email} onChange={e => setEmail(e.target.value)}
              onKeyDown={e => e.key === 'Enter' && handleEmail()}
              placeholder="your@email.com" className="input mb-3" autoFocus />
            <button onClick={handleEmail} disabled={!email.includes('@')}
              className="btn btn-primary w-full">
              Continue <ArrowRight size={14} />
            </button>
            <button onClick={handleSkip} className="btn btn-ghost w-full mt-2 text-xs">
              <SkipForward size={12} /> Skip — try demo first
            </button>
          </div>
        ) : (
          /* ── Step 2: Polymarket Setup ── */
          <div className="section-card p-6">
            <div className="flex items-center gap-2 mb-2">
              <Key size={18} style={{ color: 'var(--accent)' }} />
              <h2 className="text-sm font-bold" style={{ color: 'var(--text)' }}>Polymarket Account Setup</h2>
            </div>
            <p className="text-xs mb-4" style={{ color: 'var(--dim)' }}>
              Connect your Polymarket account for automated trade execution. Skip if you want to try demo mode first.
            </p>

            {/* Info box */}
            <div className="flex items-start gap-2 p-3 rounded-xl mb-4" style={{ background: 'var(--accent-bg)', border: '1px solid var(--accent-border)' }}>
              <Shield size={14} className="flex-shrink-0 mt-0.5" style={{ color: 'var(--accent)' }} />
              <div className="text-[11px] leading-relaxed" style={{ color: 'var(--accent-light)' }}>
                <strong>Your keys stay local.</strong> API credentials are stored only in your server&apos;s .env file. We never send them to any external service.
              </div>
            </div>

            <div className="flex flex-col gap-3">
              <input value={apiKey} onChange={e => setApiKey(e.target.value)}
                placeholder="API Key" className="input" />
              <input value={secret} onChange={e => setSecret(e.target.value)} type="password"
                placeholder="API Secret" className="input" />
              <input value={passphrase} onChange={e => setPassphrase(e.target.value)} type="password"
                placeholder="API Passphrase" className="input" />
            </div>

            <button onClick={handlePoly} disabled={!apiKey || !secret || !passphrase}
              className="btn btn-primary w-full mt-4">
              <Zap size={14} /> Connect & Start Trading
            </button>
            <button onClick={handleSkip} className="btn btn-ghost w-full mt-2 text-xs">
              <SkipForward size={12} /> Skip — use demo mode
            </button>
          </div>
        )}

        {/* Footer links */}
        <div className="flex justify-center gap-4 mt-6 text-xs" style={{ color: 'var(--dim)' }}>
          <a href="/docs" className="hover:underline" style={{ color: 'var(--muted)' }}>Documentation</a>
          <a href="/roadmap" className="hover:underline" style={{ color: 'var(--muted)' }}>Roadmap</a>
          <a href="/subscribe" className="hover:underline" style={{ color: 'var(--muted)' }}>Plans</a>
        </div>
      </div>
    </div>
  )
}
