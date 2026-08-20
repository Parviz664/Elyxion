import assert from "node:assert/strict";
import test from "node:test";

import {
  runFirstContactExperience,
  scoreFirstContact,
} from "../../src/presentation/first-contact-score.js";
import { runFirstContact } from "../../src/simulation/first-contact.js";

test("the first-contact score forms one continuous 31-second arc", () => {
  const experience = runFirstContactExperience();

  assert.equal(experience.durationMs, 31_000);
  assert.equal(experience.beats.length, 7);
  assert.equal(experience.beats[0]?.startMs, 0);

  for (const [index, beat] of experience.beats.entries()) {
    const nextBeat = experience.beats[index + 1];
    if (nextBeat !== undefined) {
      assert.equal(beat.startMs + beat.durationMs, nextBeat.startMs);
    }
  }

  const lastBeat = experience.beats.at(-1);
  assert.ok(lastBeat);
  assert.equal(lastBeat.startMs + lastBeat.durationMs, experience.durationMs);
});

test("all four domain impacts receive synchronized visual, audio, and camera cues", () => {
  const experience = runFirstContactExperience();
  const signalIds = [
    "red-pressure-node:1",
    "red-pressure-node:2",
    "red-pressure-node:3",
    "red-pressure-node:4",
  ];

  for (const signalId of signalIds) {
    const signalCues = experience.cues.filter(
      (cue) => cue.sourceSignalId === signalId,
    );
    assert.ok(signalCues.some((cue) => cue.modality === "visual"));
    assert.ok(signalCues.some((cue) => cue.modality === "audio"));
    assert.ok(signalCues.some((cue) => cue.modality === "camera"));
  }
});

test("recognition, connection, and later support remain separate moments", () => {
  const experience = runFirstContactExperience();
  const awakening = experience.cues.find(
    (cue) => cue.type === "particle-awakening",
  );
  const connection = experience.cues.find(
    (cue) => cue.type === "particle-connection",
  );
  const support = experience.cues.find((cue) => cue.type === "support-flow");

  assert.equal(awakening?.sourceSignalId, "red-pressure-node:2");
  assert.equal(connection?.sourceSignalId, "red-pressure-node:3");
  assert.equal(support?.sourceSignalId, "red-pressure-node:4");
  assert.ok((awakening?.atMs ?? 0) < (connection?.atMs ?? 0));
  assert.ok((connection?.atMs ?? 0) < (support?.atMs ?? 0));
});

test("the presentation score is deterministic and keeps every cue render-safe", () => {
  const first = scoreFirstContact(runFirstContact());
  const second = scoreFirstContact(runFirstContact());

  assert.deepEqual(first, second);

  for (const cue of first.cues) {
    assert.ok(cue.atMs >= 0);
    assert.ok(cue.durationMs > 0);
    assert.ok(cue.atMs + cue.durationMs <= first.durationMs);
    assert.ok(cue.strength >= 0 && cue.strength <= 1);
  }
});
