import type {
  DefenseAction,
  MembraneSnapshot,
  MembraneState,
  ThreatSignal,
  VisualCue,
} from "../core/contracts.js";
import { assertPercentage, clamp, round } from "../core/numbers.js";

export interface MembraneResolution {
  readonly action: DefenseAction;
  readonly preventedPressure: number;
  readonly residualPressure: number;
  readonly damage: number;
  readonly visualCues: readonly VisualCue[];
}

export class Membrane {
  private currentState: MembraneState = "stable";
  private integrity = 100;
  private energy = 100;

  public snapshot(): MembraneSnapshot {
    return Object.freeze({
      state: this.currentState,
      integrity: this.integrity,
      energy: this.energy,
    });
  }

  public respond(
    signal: ThreatSignal,
    friendlySupportRate: number,
  ): MembraneResolution {
    assertPercentage(signal.intensity, "Threat intensity");
    assertPercentage(friendlySupportRate * 100, "Friendly support rate");

    const response = this.responseProfileFor(signal.intensity);
    const mitigationRate = round(
      clamp(response.baseMitigation + friendlySupportRate, 0, 0.25),
      3,
    );
    const energyCost = round(signal.intensity * response.costRate);
    const preventedPressure = round(signal.intensity * mitigationRate);
    // Keep the balancing remainder instead of rounding both sides separately.
    // This preserves the documented accounting invariant for any valid input
    // precision: prevented + residual === incoming intensity.
    const residualPressure = signal.intensity - preventedPressure;
    const damage = round(residualPressure * 0.1);

    this.currentState = response.state;
    this.energy = round(clamp(this.energy - energyCost, 0, 100));
    this.integrity = round(clamp(this.integrity - damage, 0, 100));

    const action: DefenseAction = Object.freeze({
      state: response.state,
      strategy: response.strategy,
      mitigationRate,
      energyCost,
    });

    return Object.freeze({
      action,
      preventedPressure,
      residualPressure,
      damage,
      visualCues: this.visualCuesFor(signal.intensity, residualPressure),
    });
  }

  public completeResponse(): void {
    if (this.currentState === "alert" || this.currentState === "defense") {
      this.currentState = "recovery";
    }
  }

  public stabilize(): void {
    this.currentState = "stable";
  }

  private responseProfileFor(intensity: number): {
    readonly state: Exclude<MembraneState, "recovery">;
    readonly strategy: DefenseAction["strategy"];
    readonly baseMitigation: number;
    readonly costRate: number;
  } {
    if (intensity < 20) {
      return {
        state: "stable",
        strategy: "observe",
        baseMitigation: 0.03,
        costRate: 0,
      };
    }

    if (intensity < 50) {
      return {
        state: "alert",
        strategy: "brace",
        baseMitigation: 0.07,
        costRate: 0.025,
      };
    }

    return {
      state: "defense",
      strategy: "selective-dampen",
      baseMitigation: 0.12,
      costRate: 0.05,
    };
  }

  private visualCuesFor(
    intensity: number,
    residualPressure: number,
  ): readonly VisualCue[] {
    const cues: VisualCue[] = [
      Object.freeze({
        type: "pressure-ripple",
        strength: round(intensity / 100, 3),
      }),
      Object.freeze({
        type: "membrane-deformation",
        strength: round(residualPressure / 100, 3),
      }),
    ];

    if (intensity >= 50) {
      cues.push(
        Object.freeze({
          type: "brief-desaturation",
          strength: round(residualPressure / 100, 3),
        }),
      );
    }

    return Object.freeze(cues);
  }
}
