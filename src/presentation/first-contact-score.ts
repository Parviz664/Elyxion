import type { VisualCue } from "../core/contracts.js";
import { clamp, round } from "../core/numbers.js";
import type { FirstContactResult } from "../simulation/first-contact.js";
import { runFirstContact } from "../simulation/first-contact.js";
import type {
  ExperienceBeat,
  ExperienceCue,
  ExperienceCueType,
  ExperienceModality,
  ExperienceTarget,
  FirstContactBeatId,
  FirstContactExperience,
} from "./contracts.js";

const EXPERIENCE_DURATION_MS = 31_000;

const FIRST_CONTACT_BEATS: readonly ExperienceBeat[] = Object.freeze([
  beat(
    "ancient-stillness",
    0,
    4_000,
    null,
    "Establish fragile life before the threat has a name.",
  ),
  beat(
    "node-approach",
    4_000,
    3_000,
    null,
    "Let the three-core rhythm enter the scene before any impact.",
  ),
  beat(
    "probe",
    7_000,
    3_500,
    1,
    "A weak pulse disturbs the membrane but does not wake recognition.",
  ),
  beat(
    "recognition",
    10_500,
    5_000,
    2,
    "Sustained pressure makes the friendly particle notice the danger.",
  ),
  beat(
    "surge",
    15_500,
    6_000,
    3,
    "The largest impact causes real damage and a fragile connection.",
  ),
  beat(
    "support",
    21_500,
    4_000,
    4,
    "A final pulse reveals weak support without becoming a shield.",
  ),
  beat(
    "recovery",
    25_500,
    5_500,
    null,
    "End in altered survival and uneven breathing, not victory.",
  ),
]);

const IMPACT_TIMES_MS = [8_000, 12_000, 17_000, 22_500] as const;
const IMPACT_BEATS = [
  "probe",
  "recognition",
  "surge",
  "support",
] as const satisfies readonly FirstContactBeatId[];

export function scoreFirstContact(
  result: FirstContactResult,
): FirstContactExperience {
  if (result.outcomes.length !== IMPACT_TIMES_MS.length) {
    throw new RangeError(
      `The experimental first-contact score requires ${IMPACT_TIMES_MS.length} outcomes.`,
    );
  }

  const cues: ExperienceCue[] = baselineCues();

  result.outcomes.forEach((outcome, index) => {
    const atMs = IMPACT_TIMES_MS[index];
    const beatId = IMPACT_BEATS[index];

    if (atMs === undefined || beatId === undefined) {
      throw new RangeError("First-contact impact timing is incomplete.");
    }

    const expectedTick = index + 1;
    if (outcome.signal.tick !== expectedTick) {
      throw new RangeError(
        `Expected first-contact signal tick ${expectedTick}, received ${outcome.signal.tick}.`,
      );
    }

    const signalId = outcome.signal.id;
    const intensity = round(outcome.signal.intensity / 100, 3);
    const cameraStrength = round(
      clamp(outcome.residualPressure / 100, 0, 1) * 0.5,
      3,
    );

    cues.push(
      cue(
        `signal-${expectedTick}-core-flare`,
        beatId,
        atMs - 600,
        600,
        "visual",
        "red-pressure-node",
        "red-core-flare",
        intensity,
        signalId,
      ),
      cue(
        `signal-${expectedTick}-pressure-hit`,
        beatId,
        atMs - 80,
        Math.round(650 + intensity * 500),
        "audio",
        "membrane",
        "pressure-hit",
        intensity,
        signalId,
      ),
      cue(
        `signal-${expectedTick}-camera`,
        beatId,
        atMs,
        Math.round(180 + cameraStrength * 500),
        "camera",
        "world",
        "impact-impulse",
        cameraStrength,
        signalId,
      ),
    );

    outcome.visualCues.forEach((domainCue, cueIndex) => {
      cues.push(
        mapDomainCue(
          domainCue,
          cueIndex,
          expectedTick,
          beatId,
          atMs,
          signalId,
        ),
      );

      if (domainCue.type === "friendly-particle-awakening") {
        cues.push(
          cue(
            `signal-${expectedTick}-particle-tone`,
            beatId,
            atMs + 720,
            1_600,
            "audio",
            "friendly-particle",
            "particle-tone",
            domainCue.strength,
            signalId,
          ),
        );
      }

      if (domainCue.type === "brief-desaturation") {
        cues.push(
          cue(
            `signal-${expectedTick}-frequency-muffle`,
            beatId,
            atMs + 120,
            1_250,
            "audio",
            "world",
            "frequency-muffle",
            domainCue.strength,
            signalId,
          ),
        );
      }

      if (domainCue.type === "friendly-particle-connection") {
        cues.push(
          cue(
            `signal-${expectedTick}-connection-harmonic`,
            beatId,
            atMs + 950,
            2_600,
            "audio",
            "friendly-particle",
            "connection-harmonic",
            domainCue.strength,
            signalId,
          ),
        );
      }
    });

    if (
      outcome.particleObservation.before.state === "supporting" &&
      outcome.particleObservation.supportRate > 0
    ) {
      cues.push(
        cue(
          `signal-${expectedTick}-support-flow`,
          beatId,
          atMs - 450,
          2_800,
          "visual",
          "friendly-particle",
          "support-flow",
          round(outcome.particleObservation.supportRate / 0.25, 3),
          signalId,
        ),
      );
    }
  });

  const orderedCues = Object.freeze(
    cues
      .map((item) => validateCue(item))
      .sort(
        (left, right) =>
          left.atMs - right.atMs || left.id.localeCompare(right.id),
      ),
  );

  return Object.freeze({
    version: "phase-1-first-contact-v1",
    durationMs: EXPERIENCE_DURATION_MS,
    beats: FIRST_CONTACT_BEATS,
    cues: orderedCues,
  });
}

export function runFirstContactExperience(): FirstContactExperience {
  return scoreFirstContact(runFirstContact());
}

function baselineCues(): ExperienceCue[] {
  return [
    cue(
      "world-ambient-drift",
      "ancient-stillness",
      0,
      EXPERIENCE_DURATION_MS,
      "visual",
      "environment",
      "ambient-drift",
      0.22,
      null,
    ),
    cue(
      "world-subaquatic-bed",
      "ancient-stillness",
      0,
      EXPERIENCE_DURATION_MS,
      "audio",
      "environment",
      "subaquatic-bed",
      0.18,
      null,
    ),
    cue(
      "membrane-opening-breath",
      "ancient-stillness",
      350,
      6_200,
      "visual",
      "membrane",
      "membrane-breath",
      0.16,
      null,
    ),
    cue(
      "red-node-reveal",
      "node-approach",
      4_200,
      2_600,
      "visual",
      "red-pressure-node",
      "red-node-reveal",
      0.38,
      null,
    ),
    cue(
      "red-core-rotation",
      "node-approach",
      4_700,
      20_300,
      "visual",
      "red-pressure-node",
      "red-core-rotation",
      0.42,
      null,
    ),
    cue(
      "red-core-audio-rhythm",
      "node-approach",
      5_000,
      19_600,
      "audio",
      "red-pressure-node",
      "triple-core-throb",
      0.24,
      null,
    ),
    cue(
      "membrane-recovery-breath",
      "recovery",
      25_500,
      5_500,
      "visual",
      "membrane",
      "recovery-breath",
      0.32,
      null,
    ),
    cue(
      "membrane-recovery-resonance",
      "recovery",
      26_000,
      5_000,
      "audio",
      "membrane",
      "recovery-resonance",
      0.2,
      null,
    ),
  ];
}

function mapDomainCue(
  domainCue: VisualCue,
  cueIndex: number,
  signalTick: number,
  beatId: FirstContactBeatId,
  impactAtMs: number,
  signalId: string,
): ExperienceCue {
  const id = `signal-${signalTick}-domain-${cueIndex}`;

  switch (domainCue.type) {
    case "pressure-ripple":
      return cue(
        id,
        beatId,
        impactAtMs,
        Math.round(1_000 + domainCue.strength * 900),
        "visual",
        "membrane",
        "pressure-ripple",
        domainCue.strength,
        signalId,
      );
    case "membrane-deformation":
      return cue(
        id,
        beatId,
        impactAtMs + 100,
        Math.round(900 + domainCue.strength * 1_600),
        "visual",
        "membrane",
        "membrane-deformation",
        domainCue.strength,
        signalId,
      );
    case "brief-desaturation":
      return cue(
        id,
        beatId,
        impactAtMs + 160,
        Math.round(700 + domainCue.strength * 800),
        "visual",
        "world",
        "palette-desaturation",
        domainCue.strength,
        signalId,
      );
    case "friendly-particle-awakening":
      return cue(
        id,
        beatId,
        impactAtMs + 520,
        1_900,
        "visual",
        "friendly-particle",
        "particle-awakening",
        domainCue.strength,
        signalId,
      );
    case "friendly-particle-connection":
      return cue(
        id,
        beatId,
        impactAtMs + 780,
        3_200,
        "visual",
        "friendly-particle",
        "particle-connection",
        domainCue.strength,
        signalId,
      );
    default: {
      const unreachable: never = domainCue.type;
      throw new TypeError(`Unsupported domain cue: ${unreachable}`);
    }
  }
}

function beat(
  id: FirstContactBeatId,
  startMs: number,
  durationMs: number,
  signalTick: number | null,
  emotionalIntent: string,
): ExperienceBeat {
  return Object.freeze({
    id,
    startMs,
    durationMs,
    signalTick,
    emotionalIntent,
  });
}

function cue(
  id: string,
  beatId: FirstContactBeatId,
  atMs: number,
  durationMs: number,
  modality: ExperienceModality,
  target: ExperienceTarget,
  type: ExperienceCueType,
  strength: number,
  sourceSignalId: string | null,
): ExperienceCue {
  return Object.freeze({
    id,
    beatId,
    atMs,
    durationMs,
    modality,
    target,
    type,
    strength: round(strength, 3),
    sourceSignalId,
  });
}

function validateCue(item: ExperienceCue): ExperienceCue {
  if (!Number.isInteger(item.atMs) || item.atMs < 0) {
    throw new RangeError(
      `Cue ${item.id} must start at a non-negative millisecond.`,
    );
  }

  if (!Number.isInteger(item.durationMs) || item.durationMs <= 0) {
    throw new RangeError(`Cue ${item.id} must have a positive duration.`);
  }

  if (item.atMs + item.durationMs > EXPERIENCE_DURATION_MS) {
    throw new RangeError(`Cue ${item.id} exceeds the experience duration.`);
  }

  if (
    !Number.isFinite(item.strength) ||
    item.strength < 0 ||
    item.strength > 1
  ) {
    throw new RangeError(`Cue ${item.id} strength must be from 0 to 1.`);
  }

  return item;
}
