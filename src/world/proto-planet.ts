import type {
  EncounterOutcome,
  PlanetSnapshot,
  ThreatSignal,
} from "../core/contracts.js";
import { Membrane } from "../membrane/membrane.js";
import { FriendlyParticle } from "../particles/friendly-particle.js";

export interface ProtoPlanetOptions {
  readonly id?: string;
  readonly membrane?: Membrane;
  readonly friendlyParticle?: FriendlyParticle;
}

export class ProtoPlanet {
  public readonly id: string;
  private readonly membrane: Membrane;
  private readonly friendlyParticle: FriendlyParticle;

  public constructor(options: ProtoPlanetOptions = {}) {
    this.id = options.id ?? "origin-planet";
    this.membrane = options.membrane ?? new Membrane();
    this.friendlyParticle =
      options.friendlyParticle ?? new FriendlyParticle();
  }

  public receive(signal: ThreatSignal): EncounterOutcome {
    const planetBefore = this.snapshot();
    const particleResponse = this.friendlyParticle.observe(signal);
    const membraneResolution = this.membrane.respond(
      signal,
      particleResponse.observation.supportRate,
    );

    this.membrane.completeResponse();
    const planetAfter = this.snapshot();

    return Object.freeze({
      signal: Object.freeze({ ...signal }),
      action: membraneResolution.action,
      preventedPressure: membraneResolution.preventedPressure,
      residualPressure: membraneResolution.residualPressure,
      damage: membraneResolution.damage,
      defenseCost: membraneResolution.action.energyCost,
      planetBefore,
      planetAfter,
      particleObservation: particleResponse.observation,
      visualCues: Object.freeze([
        ...membraneResolution.visualCues,
        ...particleResponse.visualCues,
      ]),
    });
  }

  public snapshot(): PlanetSnapshot {
    return Object.freeze({
      id: this.id,
      evolutionaryStage: "cell",
      membrane: this.membrane.snapshot(),
      friendlyParticle: this.friendlyParticle.snapshot(),
    });
  }

  public stabilize(): void {
    this.membrane.stabilize();
  }
}
