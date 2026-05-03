export interface Stats {
  pnl: number; wr: number; rr: number; ev: number
  bankroll: number; deployed: number
  total: number; resolved: number; open: number
  wins: number; losses: number; avg_win: number; avg_loss: number; avg_brier: number
  new_arch: { total: number; wins: number; wr: number }
  stat_edge: { total: number; wins: number; wr: number }
}

export interface BrierProof {
  model: number; naive: number; improvement: number; our_avg: number
}

export interface Trade {
  market: string; side: string; entry: number
  p_base: string | null; p_true: number; confidence: number; edge: number
  outcome: string; pnl: number; correct: boolean; brier: number
  exit_reason: string; catalyst: string; calibration: string
  category: string; date: string
}

export interface CalibrationModel {
  cat: string; n: number; improvement: number
  a: number; b: number; brier: number; naive_brier: number
}

export interface DashboardData {
  stats: Stats
  brier: BrierProof
  bankroll_state: { level: number; win_streak: number; loss_streak: number }
  evolution: any
  pnl_series: { i: number; pnl: number; correct: boolean; date: string }[]
  cat_breakdown: Record<string, { w: number; l: number; pnl: number; brier: number; n_brier: number }>
  exit_breakdown: Record<string, number>
  open_positions: any[]
  recent_full: Trade[]
  llm: { daily: { calls: number; cost_usd: number; input: number; output: number } }
  calibration_model: CalibrationModel[]
  data_sources: { markets_analyzed: number; espn: boolean; newsapi: boolean; twitter: boolean; coingecko: boolean; fear_greed: boolean }
}
