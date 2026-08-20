export const FRIENDLY_POINT_RULES = Object.freeze({
  initialScale: 2,
  firstThreshold: 3,
  firstThresholdScale: 3,
  finalThreshold: 5,
  finalThresholdScale: 5,
  initialBreathingIntervalSeconds: 2,
  finalBreathingIntervalSeconds: 3,
} as const);

export interface FriendlyPointEvolutionSnapshot {
  readonly absorbedFriendlyPoints: number;
  readonly membraneScale: number;
  readonly breathingIntervalSeconds: number;
}

export type EvolutionLogger = (message: string) => void;

/**
 * Contains only the state required by TASK 001. Rendering and point movement
 * stay in the browser adapter so the evolution thresholds are easy to test.
 */
export class FriendlyPointEvolution {
  private absorbedFriendlyPoints = 0;

  public constructor(
    private readonly log: EvolutionLogger = console.info,
  ) {}

  /** Records one completed absorption and returns the evolved membrane state. */
  public absorbFriendlyPoint(): FriendlyPointEvolutionSnapshot {
    this.absorbedFriendlyPoints += 1;

    // Log the exact threshold transition so it is also visible in DevTools.
    if (this.absorbedFriendlyPoints === FRIENDLY_POINT_RULES.firstThreshold) {
      this.log(
        "[Elyxion] Threshold 3 reached: membrane scale = 3.0",
      );
    }

    if (this.absorbedFriendlyPoints === FRIENDLY_POINT_RULES.finalThreshold) {
      this.log(
        "[Elyxion] Threshold 5 reached: membrane scale = 5.0, breathing interval = 3s",
      );
    }

    return this.snapshot();
  }

  public snapshot(): FriendlyPointEvolutionSnapshot {
    return Object.freeze({
      absorbedFriendlyPoints: this.absorbedFriendlyPoints,
      membraneScale: this.membraneScale(),
      breathingIntervalSeconds: this.breathingIntervalSeconds(),
    });
  }

  private membraneScale(): number {
    if (this.absorbedFriendlyPoints >= FRIENDLY_POINT_RULES.finalThreshold) {
      return FRIENDLY_POINT_RULES.finalThresholdScale;
    }

    if (this.absorbedFriendlyPoints >= FRIENDLY_POINT_RULES.firstThreshold) {
      return FRIENDLY_POINT_RULES.firstThresholdScale;
    }

    return FRIENDLY_POINT_RULES.initialScale;
  }

  private breathingIntervalSeconds(): number {
    if (this.absorbedFriendlyPoints >= FRIENDLY_POINT_RULES.finalThreshold) {
      return FRIENDLY_POINT_RULES.finalBreathingIntervalSeconds;
    }

    return FRIENDLY_POINT_RULES.initialBreathingIntervalSeconds;
  }
}
