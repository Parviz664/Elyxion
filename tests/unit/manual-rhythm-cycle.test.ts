import assert from "node:assert/strict";
import test from "node:test";

import { ManualRhythmCycle } from "../../src/prototype/manual-rhythm-cycle.js";

test("manual rhythm starts ready for the lower-point inhale gesture", () => {
  const cycle = new ManualRhythmCycle();

  assert.deepEqual(cycle.snapshot(), {
    stage: "awaiting-inhale",
    cycleStartedAtMs: null,
    cycleCompletedAtMs: null,
    inhaleTravelMs: null,
    centerHoldMs: null,
    exhaleTravelMs: null,
    totalCycleMs: null,
  });
});

test("manual rhythm records raw timing for the canonical gesture order", () => {
  const cycle = new ManualRhythmCycle();

  cycle.beginInhale(100);
  cycle.completeInhale(500);
  cycle.beginHold(650);
  cycle.completeHold(1_150);
  cycle.beginExhale(1_300);
  const complete = cycle.completeExhale(1_900);

  assert.deepEqual(complete, {
    stage: "complete",
    cycleStartedAtMs: 100,
    cycleCompletedAtMs: 1_900,
    inhaleTravelMs: 400,
    centerHoldMs: 500,
    exhaleTravelMs: 600,
    totalCycleMs: 1_800,
  });
  assert.equal(Object.hasOwn(complete, "score"), false);
});

test("manual rhythm rejects actions attempted in the wrong order", () => {
  const cycle = new ManualRhythmCycle();

  assert.throws(
    () => cycle.beginHold(100),
    /requires stage "awaiting-hold"; current stage is "awaiting-inhale"/,
  );
  assert.equal(cycle.snapshot().stage, "awaiting-inhale");

  cycle.beginInhale(100);
  assert.throws(
    () => cycle.beginExhale(200),
    /requires stage "awaiting-exhale"; current stage is "inhaling"/,
  );
  assert.equal(cycle.snapshot().stage, "inhaling");
});

test("manual rhythm rejects invalid or backwards timestamps", () => {
  const cycle = new ManualRhythmCycle();

  assert.throws(() => cycle.beginInhale(Number.NaN), /finite and non-negative/);
  cycle.beginInhale(100);
  assert.throws(() => cycle.completeInhale(99), /cannot move backwards/);

  const afterValidCompletion = cycle.completeInhale(100);
  assert.equal(afterValidCompletion.inhaleTravelMs, 0);
});

test("manual rhythm reset clears an incomplete or completed measurement", () => {
  const cycle = new ManualRhythmCycle();

  cycle.beginInhale(100);
  cycle.completeInhale(200);

  const reset = cycle.reset();

  assert.equal(reset.stage, "awaiting-inhale");
  assert.equal(reset.inhaleTravelMs, null);
  assert.equal(reset.totalCycleMs, null);
  assert.equal(Object.isFrozen(reset), true);
});
