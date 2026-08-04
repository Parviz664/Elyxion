import type {
  CoreSnapshot,
  EncounterOutcome,
  ThreatSignal,
} from "./contracts.js";
import { ProtoPlanet } from "../world/proto-planet.js";

export interface ElyxionCoreOptions {
  readonly planet?: ProtoPlanet;
}

export class ElyxionCore {
  private readonly planet: ProtoPlanet;
  private readonly outcomes: EncounterOutcome[] = [];
  private currentTick = 0;

  public constructor(options: ElyxionCoreOptions = {}) {
    this.planet = options.planet ?? new ProtoPlanet();
  }

  public process(signal: ThreatSignal): EncounterOutcome {
    if (!Number.isInteger(signal.tick) || signal.tick <= this.currentTick) {
      throw new RangeError(
        `Signal tick must be an integer greater than ${this.currentTick}.`,
      );
    }

    const outcome = this.planet.receive(signal);
    this.currentTick = signal.tick;
    this.outcomes.push(outcome);
    return outcome;
  }

  public run(signals: Iterable<ThreatSignal>): readonly EncounterOutcome[] {
    return Array.from(signals, (signal) => this.process(signal));
  }

  public history(): readonly EncounterOutcome[] {
    return Object.freeze([...this.outcomes]);
  }

  public snapshot(): CoreSnapshot {
    return Object.freeze({
      phase: "phase-1",
      tick: this.currentTick,
      planetCount: 1,
      friendlyParticleCount: 1,
      enemyNodeCount: 1,
      planet: this.planet.snapshot(),
      historySize: this.outcomes.length,
    });
  }

  public stabilize(): CoreSnapshot {
    this.planet.stabilize();
    return this.snapshot();
  }
}
