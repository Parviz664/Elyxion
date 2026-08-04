import assert from "node:assert/strict";
import test from "node:test";

import { ElyxionCore } from "../../src/core/elyxion-core.js";
import { runFirstContact } from "../../src/simulation/first-contact.js";
import { RedPressureNode } from "../../src/threats/red-pressure-node/red-pressure-node.js";

test("first contact preserves the one-to-one Phase 1 topology", () => {
  const result = runFirstContact();

  assert.equal(result.enemy.coreCount, 3);
  assert.equal(result.finalSnapshot.planetCount, 1);
  assert.equal(result.finalSnapshot.friendlyParticleCount, 1);
  assert.equal(result.finalSnapshot.enemyNodeCount, 1);
  assert.equal(result.finalSnapshot.planet.evolutionaryStage, "cell");
});

test("first contact completes the pressure-response-adaptation loop", () => {
  const result = runFirstContact();

  assert.equal(result.outcomes.length, 4);
  assert.equal(result.finalSnapshot.tick, 4);
  assert.equal(result.finalSnapshot.historySize, 4);
  assert.equal(
    result.finalSnapshot.planet.friendlyParticle.state,
    "supporting",
  );
  assert.equal(result.finalSnapshot.planet.membrane.state, "recovery");
  assert.ok(result.finalSnapshot.planet.membrane.integrity < 100);
  assert.ok(result.finalSnapshot.planet.membrane.integrity > 0);

  for (const outcome of result.outcomes) {
    assert.equal(outcome.signal.source, "red-pressure-node");
    assert.equal(
      outcome.preventedPressure + outcome.residualPressure,
      outcome.signal.intensity,
    );
    assert.ok(outcome.visualCues.length >= 2);
  }

  assert.ok(
    result.outcomes.some((outcome) =>
      outcome.visualCues.some(
        (cue) => cue.type === "friendly-particle-awakening",
      ),
    ),
  );
  assert.ok(
    result.outcomes.some((outcome) =>
      outcome.visualCues.some((cue) => cue.type === "brief-desaturation"),
    ),
  );
});

test("the same initial world and signals produce the same history", () => {
  const signals = RedPressureNode.firstContact().emitAll();
  const first = new ElyxionCore().run(signals);
  const second = new ElyxionCore().run(signals);

  assert.deepEqual(first, second);
});

test("Core rejects signals that move simulation time backwards", () => {
  const core = new ElyxionCore();
  const [firstSignal] = RedPressureNode.firstContact().emitAll();

  assert.ok(firstSignal);
  core.process(firstSignal);
  assert.throws(() => core.process(firstSignal), RangeError);
});

test("Red Pressure Node keeps its canonical three-core identity", () => {
  const threat = RedPressureNode.firstContact();

  assert.equal(threat.coreCount, 3);
  assert.equal(threat.visualSignature, "translucent-crimson");
  assert.equal(threat.emitAll().length, 4);
});
