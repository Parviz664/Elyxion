import type { WhiteLineSnapshot } from "../core/contracts.js";
import { assertPercentage, clamp, round } from "../core/numbers.js";
import { maturityTierFor } from "./maturity.js";

export interface LearningInput {
  readonly preventedPressure: number;
  readonly residualPressure: number;
}

export class WhiteLine {
  private score: number;

  public constructor(initialScore = 0) {
    assertPercentage(initialScore, "Initial WhiteLine score");
    this.score = round(initialScore);
  }

  public snapshot(): WhiteLineSnapshot {
    return Object.freeze({
      score: this.score,
      tier: maturityTierFor(this.score),
    });
  }

  public learn(input: LearningInput): WhiteLineSnapshot {
    const totalExposure = input.preventedPressure + input.residualPressure;

    if (totalExposure <= 0) {
      return this.snapshot();
    }

    const weightedExperience =
      input.preventedPressure * 0.6 + input.residualPressure * 0.15;
    const gain = clamp(Math.round(weightedExperience / 10), 1, 5);

    this.score = round(clamp(this.score + gain, 0, 100));
    return this.snapshot();
  }
}

