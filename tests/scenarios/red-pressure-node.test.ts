import assert from "node:assert/strict";
import test from "node:test";

import { ElyxionCore } from "../../src/core/elyxion-core.js";
import { runFirstContact } from "../../src/simulation/first-contact.js";
import { RedPressureNode } from "../../src/threats/red-pressure-node/red-pressure-node.js";

test("first contact completes the pressure-defense-learning loop", () => {
  const result = runFirstContact(20);

  assert.equal(result.outcomes.length, 4);
  assert.equal(result.finalSnapshot.tick, 4);
  assert.equal(result.finalSnapshot.historySize, 4);
  assert.ok(result.finalSnapshot.whiteLine.score > 20);
  assert.equal(result.finalSnapshot.membraneState, "recovery");

  for (const outcome of result.outcomes) {
    assert.equal(outcome.signal.source, "red-pressure-node");
    assert.equal(
      outcome.preventedPressure + outcome.residualPressure,
      outcome.signal.intensity,
    );
    assert.ok(outcome.maturityAfter.score >= outcome.maturityBefore.score);
  }

  const severeOutcome = result.outcomes[2];
  assert.ok(severeOutcome);
  assert.equal(severeOutcome.action.state, "defense");
  assert.notEqual(severeOutcome.action.strategy, "observe");
});

test("the same initial state and signals produce the same history", () => {
  const signals = RedPressureNode.firstContact().emitAll();
  const first = new ElyxionCore({ initialWhiteLineScore: 20 }).run(signals);
  const second = new ElyxionCore({ initialWhiteLineScore: 20 }).run(signals);

  assert.deepEqual(first, second);
});

test("Core rejects signals that move simulation time backwards", () => {
  const core = new ElyxionCore();
  const [firstSignal] = RedPressureNode.firstContact().emitAll();

  assert.ok(firstSignal);
  core.process(firstSignal);
  assert.throws(() => core.process(firstSignal), RangeError);
});

