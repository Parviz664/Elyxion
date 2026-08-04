import type {
  CoreSnapshot,
  EncounterOutcome,
  ThreatSignal,
} from "./contracts.js";
import { round } from "./numbers.js";
import { Membrane } from "../membrane/membrane.js";
import { WhiteLine } from "../whiteline/white-line.js";

export interface ElyxionCoreOptions {
  readonly initialWhiteLineScore?: number;
  readonly membrane?: Membrane;
  readonly whiteLine?: WhiteLine;
}

export class ElyxionCore {
  private readonly membrane: Membrane;
  private readonly whiteLine: WhiteLine;
  private readonly outcomes: EncounterOutcome[] = [];
  private currentTick = 0;

  public constructor(options: ElyxionCoreOptions = {}) {
    this.membrane = options.membrane ?? new Membrane();
    this.whiteLine =
      options.whiteLine ?? new WhiteLine(options.initialWhiteLineScore ?? 0);
  }

  public process(signal: ThreatSignal): EncounterOutcome {
    if (!Number.isInteger(signal.tick) || signal.tick <= this.currentTick) {
      throw new RangeError(
        `Signal tick must be an integer greater than ${this.currentTick}.`,
      );
    }

    const maturityBefore = this.whiteLine.snapshot();
    const action = this.membrane.respond(signal, maturityBefore);
    const preventedPressure = round(signal.intensity * action.mitigationRate);
    const residualPressure = round(signal.intensity - preventedPressure);
    const maturityAfter = this.whiteLine.learn({
      preventedPressure,
      residualPressure,
    });

    this.currentTick = signal.tick;

    const outcome: EncounterOutcome = Object.freeze({
      signal: Object.freeze({ ...signal }),
      action,
      preventedPressure,
      residualPressure,
      defenseCost: action.energyCost,
      maturityBefore,
      maturityAfter,
    });

    this.outcomes.push(outcome);
    this.membrane.completeResponse();
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
      tick: this.currentTick,
      membraneState: this.membrane.state,
      whiteLine: this.whiteLine.snapshot(),
      historySize: this.outcomes.length,
    });
  }

  public stabilize(): CoreSnapshot {
    this.membrane.stabilize();
    return this.snapshot();
  }
}

