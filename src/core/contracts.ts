export type ThreatPattern = "pulse" | "surge" | "sustained";

export type MembraneState = "stable" | "alert" | "defense" | "recovery";

export type DefenseStrategy = "observe" | "brace" | "selective-dampen";

export type FriendlyParticleState =
  | "dormant"
  | "recognizing"
  | "supporting";

export type VisualCueType =
  | "pressure-ripple"
  | "membrane-deformation"
  | "brief-desaturation"
  | "friendly-particle-awakening"
  | "friendly-particle-connection";

export interface ThreatSignal {
  readonly id: string;
  readonly source: string;
  readonly tick: number;
  readonly intensity: number;
  readonly pattern: ThreatPattern;
}

export interface VisualCue {
  readonly type: VisualCueType;
  readonly strength: number;
}

export interface FriendlyParticleSnapshot {
  readonly state: FriendlyParticleState;
  readonly accumulatedExposure: number;
}

export interface FriendlyParticleObservation {
  readonly before: FriendlyParticleSnapshot;
  readonly after: FriendlyParticleSnapshot;
  readonly supportRate: number;
}

export interface DefenseAction {
  readonly state: Exclude<MembraneState, "recovery">;
  readonly strategy: DefenseStrategy;
  readonly mitigationRate: number;
  readonly energyCost: number;
}

export interface MembraneSnapshot {
  readonly state: MembraneState;
  readonly integrity: number;
  readonly energy: number;
}

export interface PlanetSnapshot {
  readonly id: string;
  readonly evolutionaryStage: "cell";
  readonly membrane: MembraneSnapshot;
  readonly friendlyParticle: FriendlyParticleSnapshot;
}

export interface EncounterOutcome {
  readonly signal: ThreatSignal;
  readonly action: DefenseAction;
  readonly preventedPressure: number;
  readonly residualPressure: number;
  readonly damage: number;
  readonly defenseCost: number;
  readonly planetBefore: PlanetSnapshot;
  readonly planetAfter: PlanetSnapshot;
  readonly particleObservation: FriendlyParticleObservation;
  readonly visualCues: readonly VisualCue[];
}

export interface CoreSnapshot {
  readonly phase: "phase-1";
  readonly tick: number;
  readonly planetCount: 1;
  readonly friendlyParticleCount: 1;
  readonly enemyNodeCount: 1;
  readonly planet: PlanetSnapshot;
  readonly historySize: number;
}
