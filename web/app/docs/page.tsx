'use client'
import { BookOpen, Code, Settings, Shield, BarChart3, Brain, ExternalLink, ArrowLeft, Zap, HelpCircle } from 'lucide-react'

const DOC_SECTIONS = [
  {
    icon: <Zap size={18} />,
    title: 'Getting Started',
    desc: 'Quick start guide to set up and run TRITAN',
    links: [
      { title: 'Installation Guide', desc: 'Set up TRITAN on your VPS with PM2', url: '#' },
      { title: 'First Run Checklist', desc: 'Step-by-step for your first demo trade', url: '#' },
      { title: 'Demo vs Live Mode', desc: 'Understanding the difference and when to switch', url: '#' },
    ],
  },
  {
    icon: <Settings size={18} />,
    title: 'Configuration',
    desc: 'Detailed explanation of every config parameter',
    links: [
      { title: 'Mode & Bankroll', desc: 'AGENT_MODE, DEMO_BANKROLL, LIVE_BANKROLL', url: '#' },
      { title: 'Bet Sizing & Kelly', desc: 'MIN/MAX_BET, KELLY_FRACTION, position limits', url: '#' },
      { title: 'Edge & Signal Gate', desc: 'MIN_STAT_EDGE, confidence thresholds, edge filters', url: '#' },
      { title: 'Exit Strategy', desc: 'Take profit, stop loss, trailing stop, max hold', url: '#' },
      { title: 'Scan & Market Filter', desc: 'Scan intervals, volume/liquidity filters, resolve time', url: '#' },
      { title: 'AI & Cost Control', desc: 'LLM budget, max tokens, analysis limits', url: '#' },
      { title: 'Bankroll Compounding', desc: 'Win/loss streaks, level system, step sizes', url: '#' },
    ],
  },
  {
    icon: <BarChart3 size={18} />,
    title: 'Strategy',
    desc: 'How TRITAN makes trading decisions',
    links: [
      { title: 'Price Movement Strategy', desc: 'Why we bet on price movement, not outcome', url: '#' },
      { title: 'Sports Markets', desc: 'Wait-for-resolved approach', url: '#' },
      { title: 'Crypto & Geopolitics', desc: '24h max hold with dynamic TP/SL', url: '#' },
      { title: 'Edge Calculation', desc: 'How statistical edge is computed from model vs market', url: '#' },
      { title: 'Brier Score Explained', desc: 'What it means and why lower is better', url: '#' },
    ],
  },
  {
    icon: <Brain size={18} />,
    title: 'AI System',
    desc: 'How the AI analysis and learning works',
    links: [
      { title: 'AI Analysis Pipeline', desc: 'From market scan to trade signal', url: '#' },
      { title: 'Learning System', desc: 'How the system improves from resolved trades', url: '#' },
      { title: 'Model Calibration', desc: 'Logistic regression by category', url: '#' },
      { title: 'LLM Cost Management', desc: 'Token budgets and cost optimization', url: '#' },
    ],
  },
  {
    icon: <Shield size={18} />,
    title: 'Security & API',
    desc: 'Keeping your keys and funds safe',
    links: [
      { title: 'API Key Setup', desc: 'Getting Polymarket CLOB API credentials', url: '#' },
      { title: 'SAFE Wallet Integration', desc: 'Using Gnosis Safe for automated execution', url: '#' },
      { title: 'Environment Variables', desc: 'All .env keys explained', url: '#' },
      { title: 'Security Best Practices', desc: 'VPS hardening, key rotation, monitoring', url: '#' },
    ],
  },
  {
    icon: <Code size={18} />,
    title: 'Architecture',
    desc: 'Technical deep dive into the system',
    links: [
      { title: 'System Architecture', desc: 'Python agent + Next.js dashboard + PM2', url: '#' },
      { title: 'Data Flow', desc: 'From market scan to trade execution to dashboard', url: '#' },
      { title: 'API Reference', desc: 'Internal API routes and data formats', url: '#' },
      { title: 'Troubleshooting', desc: 'Common issues and solutions', url: '#' },
    ],
  },
]

export default function DocsPage() {
  return (
    <div className="min-h-screen p-4 pb-20" style={{ background: 'var(--bg)' }}>
      <div className="max-w-3xl mx-auto fade-in">
        {/* Header */}
        <div className="mb-6">
          <a href="/" className="flex items-center gap-1.5 text-xs mb-4" style={{ color: 'var(--dim)' }}>
            <ArrowLeft size={14} /> Back to Dashboard
          </a>
          <div className="flex items-center gap-2 mb-2">
            <BookOpen size={20} style={{ color: 'var(--accent)' }} />
            <h1 className="text-lg font-bold" style={{ color: 'var(--text)' }}>Documentation</h1>
          </div>
          <p className="text-sm" style={{ color: 'var(--dim)' }}>
            Everything you need to know about TRITAN — from setup to advanced configuration.
          </p>
        </div>

        {/* Quick links */}
        <div className="flex gap-2 mb-6 flex-wrap">
          <a href="/subscribe" className="btn btn-secondary btn-sm text-xs">
            <Zap size={12} /> Pricing Plans
          </a>
          <a href="/roadmap" className="btn btn-secondary btn-sm text-xs">
            <BarChart3 size={12} /> Roadmap
          </a>
          <button className="btn btn-ghost btn-sm text-xs">
            <HelpCircle size={12} /> Need Help?
          </button>
        </div>

        {/* Doc sections */}
        <div className="flex flex-col gap-4">
          {DOC_SECTIONS.map(section => (
            <div key={section.title} className="section-card">
              <div className="p-4 pb-0">
                <div className="flex items-center gap-2 mb-1">
                  <span style={{ color: 'var(--accent)' }}>{section.icon}</span>
                  <h2 className="text-sm font-bold" style={{ color: 'var(--text)' }}>{section.title}</h2>
                </div>
                <p className="text-xs" style={{ color: 'var(--dim)' }}>{section.desc}</p>
              </div>
              <div className="p-4">
                <div className="flex flex-col gap-0">
                  {section.links.map(link => (
                    <a key={link.title} href={link.url}
                      className="flex items-center justify-between py-2.5 group" style={{ borderBottom: '1px solid var(--border2)' }}>
                      <div>
                        <div className="text-xs font-medium group-hover:underline" style={{ color: 'var(--text2)' }}>{link.title}</div>
                        <div className="text-[10px]" style={{ color: 'var(--dim)' }}>{link.desc}</div>
                      </div>
                      <ExternalLink size={12} style={{ color: 'var(--dim)' }} />
                    </a>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Footer */}
        <div className="text-center mt-8 py-4" style={{ borderTop: '1px solid var(--border2)' }}>
          <p className="text-xs" style={{ color: 'var(--dim)' }}>
            Can&apos;t find what you&apos;re looking for? Check the <a href="/roadmap" style={{ color: 'var(--accent-light)' }}>roadmap</a> for upcoming features.
          </p>
        </div>
      </div>
    </div>
  )
}
