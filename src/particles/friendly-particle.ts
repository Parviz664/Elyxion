import type {
  FriendlyParticleObservation,
  FriendlyParticleSnapshot,
  FriendlyParticleState,
  ThreatSignal,
  VisualCue,
} from "../core/contracts.js";
import { assertPercentage, round } from "../core/numbers.js";

const RECOGNITION_THRESHOLD = 20;
const SUPPORTING_EXPOSURE_THRESHOLD = 100;

export interface FriendlyParticleResponse {
  readonly observation: FriendlyParticleObservation;
  readonly visualCues: readonly VisualCue[];
}

export class FriendlyParticle {
  private currentState: FriendlyParticleState = "dormant";
  private exposure = 0;

  public snapshot(): FriendlyParticleSnapshot {
    return Object.freeze({
      state: this.currentState,
      accumulatedExposure: this.exposure,
    });
  }

  public observe(signal: ThreatSignal): FriendlyParticleResponse {
    assertPercentage(signal.intensity, "Threat intensity");

    const before = this.snapshot();
    const supportRate = this.supportRateFor(before.state);

    if (signal.intensity >= RECOGNITION_THRESHOLD) {
      this.exposure = round(this.exposure + signal.intensity);

      if (this.currentState === "dormant") {
        this.currentState = "recognizing";
      } else if (
        this.currentState === "recognizing" &&
        this.exposure >= SUPPORTING_EXPOSURE_THRESHOLD
      ) {
        this.currentState = "supporting";
      }
    }

    const after = this.snapshot();
    const visualCues: VisualCue[] = [];

    if (before.state === "dormant" && after.state === "recognizing") {
      visualCues.push(
        Object.freeze({
          type: "friendly-particle-awakening",
          strength: 0.35,
        }),
      );
    }

    if (before.state === "recognizing" && after.state === "supporting") {
      visualCues.push(
        Object.freeze({
          type: "friendly-particle-connection",
          strength: 0.45,
        }),
      );
    }

    return Object.freeze({
      observation: Object.freeze({ before, after, supportRate }),
      visualCues: Object.freeze(visualCues),
    });
  }

  private supportRateFor(state: FriendlyParticleState): number {
    if (state === "recognizing") {
      return 0.03;
    }

    if (state === "supporting") {
      return 0.08;
    }

    return 0;
  }
}
