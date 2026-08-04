export type MaturityTier = "M0" | "M1" | "M2" | "M3";

export type ThreatPattern = "pulse" | "surge" | "sustained";

export type MembraneState = "stable" | "alert" | "defense" | "recovery";

export type DefenseStrategy = "observe" | "brace" | "absorb" | "adapt";

export interface ThreatSignal {
  readonly id: string;
  readonly source: string;
  readonly tick: number;
  readonly intensity: number;
  readonly pattern: ThreatPattern;
}

export interface WhiteLineSnapshot {
  readonly score: number;
  readonly tier: MaturityTier;
}

export interface DefenseAction {
  readonly state: Exclude<MembraneState, "recovery">;
  readonly strategy: DefenseStrategy;
  readonly mitigationRate: number;
  readonly energyCost: number;
}

export interface EncounterOutcome {
  readonly signal: ThreatSignal;
  readonly action: DefenseAction;
  readonly preventedPressure: number;
  readonly residualPressure: number;
  readonly defenseCost: number;
  readonly maturityBefore: WhiteLineSnapshot;
  readonly maturityAfter: WhiteLineSnapshot;
}

export interface CoreSnapshot {
  readonly tick: number;
  readonly membraneState: MembraneState;
  readonly whiteLine: WhiteLineSnapshot;
  readonly historySize: number;
}

