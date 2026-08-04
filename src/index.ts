export type {
  CoreSnapshot,
  DefenseAction,
  DefenseStrategy,
  EncounterOutcome,
  FriendlyParticleObservation,
  FriendlyParticleSnapshot,
  FriendlyParticleState,
  MembraneSnapshot,
  MembraneState,
  PlanetSnapshot,
  ThreatPattern,
  ThreatSignal,
  VisualCue,
  VisualCueType,
} from "./core/contracts.js";
export { ElyxionCore } from "./core/elyxion-core.js";
export { Membrane } from "./membrane/membrane.js";
export { FriendlyParticle } from "./particles/friendly-particle.js";
export { runFirstContact } from "./simulation/first-contact.js";
export { RedPressureNode } from "./threats/red-pressure-node/red-pressure-node.js";
export { ProtoPlanet } from "./world/proto-planet.js";
