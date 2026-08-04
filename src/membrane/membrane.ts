import type {
  DefenseAction,
  MaturityTier,
  MembraneState,
  ThreatSignal,
  WhiteLineSnapshot,
} from "../core/contracts.js";
import { assertPercentage, round } from "../core/numbers.js";

interface DefenseProfile {
  readonly alertMitigation: number;
  readonly defenseMitigation: number;
  readonly costRate: number;
}

const DEFENSE_PROFILES: Readonly<Record<MaturityTier, DefenseProfile>> = {
  M0: { alertMitigation: 0.15, defenseMitigation: 0.25, costRate: 0.08 },
  M1: { alertMitigation: 0.25, defenseMitigation: 0.4, costRate: 0.07 },
  M2: { alertMitigation: 0.4, defenseMitigation: 0.58, costRate: 0.06 },
  M3: { alertMitigation: 0.55, defenseMitigation: 0.75, costRate: 0.05 },
};

export class Membrane {
  private currentState: MembraneState = "stable";

  public get state(): MembraneState {
    return this.currentState;
  }

  public respond(
    signal: ThreatSignal,
    maturity: WhiteLineSnapshot,
  ): DefenseAction {
    assertPercentage(signal.intensity, "Threat intensity");
    const profile = DEFENSE_PROFILES[maturity.tier];

    if (signal.intensity < 20) {
      this.currentState = "stable";
      return Object.freeze({
        state: "stable",
        strategy: "observe",
        mitigationRate: 0.05,
        energyCost: 0,
      });
    }

    if (signal.intensity < 50) {
      this.currentState = "alert";
      return Object.freeze({
        state: "alert",
        strategy: "brace",
        mitigationRate: profile.alertMitigation,
        energyCost: round(signal.intensity * profile.costRate),
      });
    }

    this.currentState = "defense";
    return Object.freeze({
      state: "defense",
      strategy:
        maturity.tier === "M2" || maturity.tier === "M3" ? "adapt" : "absorb",
      mitigationRate: profile.defenseMitigation,
      energyCost: round(signal.intensity * profile.costRate * 1.5),
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
}

