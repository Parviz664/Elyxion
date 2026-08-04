export type {
  CoreSnapshot,
  DefenseAction,
  DefenseStrategy,
  EncounterOutcome,
  MaturityTier,
  MembraneState,
  ThreatPattern,
  ThreatSignal,
  WhiteLineSnapshot,
} from "./core/contracts.js";
export { ElyxionCore } from "./core/elyxion-core.js";
export { Membrane } from "./membrane/membrane.js";
export { runFirstContact } from "./simulation/first-contact.js";
export { RedPressureNode } from "./threats/red-pressure-node/red-pressure-node.js";
export { MATURITY_BANDS, maturityTierFor } from "./whiteline/maturity.js";
export { WhiteLine } from "./whiteline/white-line.js";

