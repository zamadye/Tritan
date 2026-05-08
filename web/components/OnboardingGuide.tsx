'use client'
import { useState, useEffect } from 'react'

type Lang = 'en' | 'id'

const CONTENT = {
  en: {
    title: '👋 Welcome to TRITAN',
    subtitle: 'AI-powered prediction market trading system',
    steps: [
      {
        icon: '⚙️',
        title: 'Configure Your Strategy',
        desc: 'Go to the Config tab to set your bankroll, bet sizes, confidence thresholds, and exit rules. Each field has a description explaining what it does.',
        action: 'Open Config',
        tab: 'Config',
      },
      {
        icon: '🤖',
        title: 'Ask the AI Assistant',
        desc: 'Click the 🤖 button (bottom right) to chat with your Trade Monitor Assistant. It analyzes your trades and recommends strategy improvements.',
        action: null,
        tab: null,
      },
      {
        icon: '📊',
        title: 'Monitor Performance',
        desc: 'The Overview tab shows your P&L, win rate, and open positions. Trades tab shows full history with entry price, edge, confidence, and exit reason.',
        action: 'View Overview',
        tab: 'Overview',
      },
      {
        icon: '🎯',
        title: 'Strategy: Price Movement',
        desc: 'TRITAN bets on price movement, not final outcome. Sports: wait for resolved. Crypto/Geo: max 24h hold. Dynamic TP: 15-40% based on edge.',
        action: null,
        tab: null,
      },
    ],
    dismiss: "Got it, let's start",
    lang: 'ID',
  },
  id: {
    title: '👋 Selamat Datang di TRITAN',
    subtitle: 'Sistem trading prediction market berbasis AI',
    steps: [
      {
        icon: '⚙️',
        title: 'Konfigurasi Strategi',
        desc: 'Buka tab Config untuk set bankroll, ukuran bet, threshold confidence, dan aturan exit. Setiap field ada deskripsi yang menjelaskan fungsinya.',
        action: 'Buka Config',
        tab: 'Config',
      },
      {
        icon: '🤖',
        title: 'Tanya AI Assistant',
        desc: 'Klik tombol 🤖 (pojok kanan bawah) untuk chat dengan Trade Monitor Assistant. AI ini analisis trade kamu dan rekomendasikan perbaikan strategi.',
        action: null,
        tab: null,
      },
      {
        icon: '📊',
        title: 'Monitor Performa',
        desc: 'Tab Overview menampilkan P&L, win rate, dan posisi terbuka. Tab Trades menampilkan histori lengkap dengan entry price, edge, confidence, dan alasan exit.',
        action: 'Lihat Overview',
        tab: 'Overview',
      },
      {
        icon: '🎯',
        title: 'Strategi: Price Movement',
        desc: 'TRITAN bet pada pergerakan harga, bukan outcome akhir. Sports: tunggu resolved. Crypto/Geo: max 24 jam. Dynamic TP: 15-40% berdasarkan edge.',
        action: null,
        tab: null,
      },
    ],
    dismiss: 'Mengerti, mulai sekarang',
    lang: 'EN',
  },
}

interface Props {
  onNavigate: (tab: string) => void
}

export function OnboardingGuide({ onNavigate }: Props) {
  const [visible, setVisible] = useState(false)
  const [lang, setLang] = useState<Lang>('en')

  useEffect(() => {
    const dismissed = localStorage.getItem('tritan_onboarding_dismissed')
    if (!dismissed) setVisible(true)
  }, [])

  const dismiss = () => {
    localStorage.setItem('tritan_onboarding_dismissed', '1')
    setVisible(false)
  }

  if (!visible) return null

  const c = CONTENT[lang]

  return (
    <div className="fixed inset-0 bg-black/60 backdrop-blur-sm z-50 flex items-center justify-center p-4">
      <div className="bg-[#0d0d1a] border border-[#2a2a4a] rounded-2xl w-full max-w-lg shadow-2xl">
        {/* Header */}
        <div className="p-6 border-b border-[#1e1e3a] flex items-start justify-between">
          <div>
            <h2 className="text-base font-bold text-[#e2e8f0]">{c.title}</h2>
            <p className="text-xs text-[#6b7280] mt-1">{c.subtitle}</p>
          </div>
          <button
            onClick={() => setLang(l => l === 'en' ? 'id' : 'en')}
            className="text-[10px] bg-[#1e1e3a] border border-[#2a2a4a] text-[#94a3b8] px-2 py-1 rounded-lg hover:border-[#4f46e5] transition-colors">
            {c.lang}
          </button>
        </div>

        {/* Steps */}
        <div className="p-6 space-y-4">
          {c.steps.map((step, i) => (
            <div key={i} className="flex gap-3">
              <span className="text-xl shrink-0 mt-0.5">{step.icon}</span>
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-xs font-semibold text-[#e2e8f0]">{step.title}</span>
                  {step.action && step.tab && (
                    <button
                      onClick={() => { onNavigate(step.tab!); dismiss() }}
                      className="text-[10px] bg-[#4f46e5]/20 text-[#a5b4fc] border border-[#4f46e5]/30 px-2 py-0.5 rounded hover:bg-[#4f46e5]/40 transition-colors">
                      {step.action} →
                    </button>
                  )}
                </div>
                <p className="text-[11px] text-[#6b7280] leading-relaxed">{step.desc}</p>
              </div>
            </div>
          ))}
        </div>

        {/* Footer */}
        <div className="px-6 pb-6 flex items-center justify-between">
          <button
            onClick={() => { onNavigate('Config'); dismiss() }}
            className="text-xs bg-[#4f46e5] hover:bg-[#4338ca] text-white px-4 py-2 rounded-lg transition-colors font-medium">
            ⚙️ {lang === 'en' ? 'Setup Config First' : 'Setup Config Dulu'}
          </button>
          <button onClick={dismiss} className="text-xs text-[#6b7280] hover:text-[#94a3b8] transition-colors">
            {c.dismiss}
          </button>
        </div>
      </div>
    </div>
  )
}
