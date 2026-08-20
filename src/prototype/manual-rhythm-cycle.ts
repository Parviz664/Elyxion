export type ManualRhythmStage =
  | "awaiting-inhale"
  | "inhaling"
  | "awaiting-hold"
  | "holding"
  | "awaiting-exhale"
  | "exhaling"
  | "complete";

export interface ManualRhythmCycleSnapshot {
  readonly stage: ManualRhythmStage;
  readonly cycleStartedAtMs: number | null;
  readonly cycleCompletedAtMs: number | null;
  readonly inhaleTravelMs: number | null;
  readonly centerHoldMs: number | null;
  readonly exhaleTravelMs: number | null;
  readonly totalCycleMs: number | null;
}

/**
 * Records one creator-defined Elyxionpad rhythm cycle.
 *
 * This class deliberately measures raw time only. It does not grade a player,
 * prescribe a target duration, or turn prototype measurements into canon.
 */
export class ManualRhythmCycle {
  private stage: ManualRhythmStage = "awaiting-inhale";
  private cycleStartedAtMs: number | null = null;
  private cycleCompletedAtMs: number | null = null;
  private segmentStartedAtMs: number | null = null;
  private lastEventAtMs: number | null = null;
  private inhaleTravelMs: number | null = null;
  private centerHoldMs: number | null = null;
  private exhaleTravelMs: number | null = null;

  beginInhale(atMs: number): ManualRhythmCycleSnapshot {
    this.assertStage("awaiting-inhale");
    this.recordEventTime(atMs);
    this.cycleStartedAtMs = atMs;
    this.segmentStartedAtMs = atMs;
    this.stage = "inhaling";
    return this.snapshot();
  }

  completeInhale(atMs: number): ManualRhythmCycleSnapshot {
    this.assertStage("inhaling");
    this.recordEventTime(atMs);
    this.inhaleTravelMs = atMs - this.requireSegmentStart();
    this.segmentStartedAtMs = null;
    this.stage = "awaiting-hold";
    return this.snapshot();
  }

  beginHold(atMs: number): ManualRhythmCycleSnapshot {
    this.assertStage("awaiting-hold");
    this.recordEventTime(atMs);
    this.segmentStartedAtMs = atMs;
    this.stage = "holding";
    return this.snapshot();
  }

  completeHold(atMs: number): ManualRhythmCycleSnapshot {
    this.assertStage("holding");
    this.recordEventTime(atMs);
    this.centerHoldMs = atMs - this.requireSegmentStart();
    this.segmentStartedAtMs = null;
    this.stage = "awaiting-exhale";
    return this.snapshot();
  }

  beginExhale(atMs: number): ManualRhythmCycleSnapshot {
    this.assertStage("awaiting-exhale");
    this.recordEventTime(atMs);
    this.segmentStartedAtMs = atMs;
    this.stage = "exhaling";
    return this.snapshot();
  }

  completeExhale(atMs: number): ManualRhythmCycleSnapshot {
    this.assertStage("exhaling");
    this.recordEventTime(atMs);
    this.exhaleTravelMs = atMs - this.requireSegmentStart();
    this.segmentStartedAtMs = null;
    this.cycleCompletedAtMs = atMs;
    this.stage = "complete";
    return this.snapshot();
  }

  reset(): ManualRhythmCycleSnapshot {
    this.stage = "awaiting-inhale";
    this.cycleStartedAtMs = null;
    this.cycleCompletedAtMs = null;
    this.segmentStartedAtMs = null;
    this.lastEventAtMs = null;
    this.inhaleTravelMs = null;
    this.centerHoldMs = null;
    this.exhaleTravelMs = null;
    return this.snapshot();
  }

  snapshot(): ManualRhythmCycleSnapshot {
    const totalCycleMs =
      this.cycleStartedAtMs === null || this.cycleCompletedAtMs === null
        ? null
        : this.cycleCompletedAtMs - this.cycleStartedAtMs;

    return Object.freeze({
      stage: this.stage,
      cycleStartedAtMs: this.cycleStartedAtMs,
      cycleCompletedAtMs: this.cycleCompletedAtMs,
      inhaleTravelMs: this.inhaleTravelMs,
      centerHoldMs: this.centerHoldMs,
      exhaleTravelMs: this.exhaleTravelMs,
      totalCycleMs,
    });
  }

  private assertStage(expected: ManualRhythmStage): void {
    if (this.stage !== expected) {
      throw new Error(
        `Manual rhythm event requires stage "${expected}"; current stage is "${this.stage}".`,
      );
    }
  }

  private recordEventTime(atMs: number): void {
    if (!Number.isFinite(atMs) || atMs < 0) {
      throw new RangeError(
        "Manual rhythm timestamps must be finite and non-negative.",
      );
    }

    if (this.lastEventAtMs !== null && atMs < this.lastEventAtMs) {
      throw new RangeError(
        "Manual rhythm timestamps cannot move backwards between events.",
      );
    }

    this.lastEventAtMs = atMs;
  }

  private requireSegmentStart(): number {
    if (this.segmentStartedAtMs === null) {
      throw new Error("Manual rhythm segment has no start timestamp.");
    }

    return this.segmentStartedAtMs;
  }
}
