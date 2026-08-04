export type FirstContactBeatId =
  | "ancient-stillness"
  | "node-approach"
  | "probe"
  | "recognition"
  | "surge"
  | "support"
  | "recovery";

export type ExperienceModality = "visual" | "audio" | "camera";

export type ExperienceTarget =
  | "environment"
  | "red-pressure-node"
  | "membrane"
  | "friendly-particle"
  | "world";

export type ExperienceCueType =
  | "ambient-drift"
  | "subaquatic-bed"
  | "membrane-breath"
  | "red-node-reveal"
  | "red-core-rotation"
  | "triple-core-throb"
  | "red-core-flare"
  | "pressure-hit"
  | "frequency-muffle"
  | "pressure-ripple"
  | "membrane-deformation"
  | "palette-desaturation"
  | "particle-awakening"
  | "particle-tone"
  | "particle-connection"
  | "connection-harmonic"
  | "support-flow"
  | "impact-impulse"
  | "recovery-breath"
  | "recovery-resonance";

export interface ExperienceBeat {
  readonly id: FirstContactBeatId;
  readonly startMs: number;
  readonly durationMs: number;
  readonly signalTick: number | null;
  readonly emotionalIntent: string;
}

export interface ExperienceCue {
  readonly id: string;
  readonly beatId: FirstContactBeatId;
  readonly atMs: number;
  readonly durationMs: number;
  readonly modality: ExperienceModality;
  readonly target: ExperienceTarget;
  readonly type: ExperienceCueType;
  readonly strength: number;
  readonly sourceSignalId: string | null;
}

export interface FirstContactExperience {
  readonly version: "phase-1-first-contact-v1";
  readonly durationMs: number;
  readonly beats: readonly ExperienceBeat[];
  readonly cues: readonly ExperienceCue[];
}
