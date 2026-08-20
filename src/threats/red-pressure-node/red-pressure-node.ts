import type { ThreatPattern, ThreatSignal } from "../../core/contracts.js";
import { assertPercentage } from "../../core/numbers.js";

export interface RedPressurePhase {
  readonly intensity: number;
  readonly pattern: ThreatPattern;
}

export interface RedPressureNodeOptions {
  readonly id?: string;
  readonly phases: readonly RedPressurePhase[];
}

const FIRST_CONTACT_PHASES = [
  { intensity: 18, pattern: "pulse" },
  { intensity: 42, pattern: "sustained" },
  { intensity: 78, pattern: "surge" },
  { intensity: 28, pattern: "pulse" },
] as const satisfies readonly RedPressurePhase[];

export class RedPressureNode {
  public readonly id: string;
  public readonly coreCount = 3 as const;
  public readonly visualSignature = "translucent-crimson" as const;
  private readonly phases: readonly RedPressurePhase[];

  public constructor(options: RedPressureNodeOptions) {
    if (options.phases.length === 0) {
      throw new RangeError("Red Pressure Node requires at least one phase.");
    }

    this.id = options.id ?? "red-pressure-node";
    this.phases = options.phases.map((phase) => {
      assertPercentage(phase.intensity, "Red Pressure phase intensity");
      return Object.freeze({ ...phase });
    });
  }

  public static firstContact(): RedPressureNode {
    return new RedPressureNode({ phases: FIRST_CONTACT_PHASES });
  }

  public emitAll(startTick = 1): readonly ThreatSignal[] {
    if (!Number.isInteger(startTick) || startTick < 1) {
      throw new RangeError("Start tick must be a positive integer.");
    }

    return Object.freeze(
      this.phases.map((phase, index) => {
        const tick = startTick + index;
        return Object.freeze({
          id: `${this.id}:${tick}`,
          source: this.id,
          tick,
          intensity: phase.intensity,
          pattern: phase.pattern,
        });
      }),
    );
  }
}
