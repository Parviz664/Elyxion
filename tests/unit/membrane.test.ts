import assert from "node:assert/strict";
import test from "node:test";

import type { ThreatSignal } from "../../src/core/contracts.js";
import { Membrane } from "../../src/membrane/membrane.js";

const severeSignal: ThreatSignal = {
  id: "test:1",
  source: "test",
  tick: 1,
  intensity: 80,
  pattern: "surge",
};

test("friendly support improves mitigation without becoming a full shield", () => {
  const unsupported = new Membrane().respond(severeSignal, 0);
  const supported = new Membrane().respond(severeSignal, 0.08);

  assert.equal(unsupported.action.strategy, "selective-dampen");
  assert.ok(supported.action.mitigationRate > unsupported.action.mitigationRate);
  assert.ok(supported.action.mitigationRate <= 0.25);
  assert.ok(supported.damage < unsupported.damage);
});

test("an impact consumes energy and membrane integrity", () => {
  const membrane = new Membrane();
  const resolution = membrane.respond(severeSignal, 0);
  const snapshot = membrane.snapshot();

  assert.ok(resolution.damage > 0);
  assert.ok(snapshot.integrity < 100);
  assert.ok(snapshot.energy < 100);
});

test("Membrane enters recovery after an active response", () => {
  const membrane = new Membrane();

  membrane.respond(severeSignal, 0);
  assert.equal(membrane.snapshot().state, "defense");

  membrane.completeResponse();
  assert.equal(membrane.snapshot().state, "recovery");
});

test("pressure accounting preserves higher-precision incoming intensity", () => {
  const preciseSignal: ThreatSignal = {
    ...severeSignal,
    id: "test:precise",
    intensity: 42.123,
  };

  const resolution = new Membrane().respond(preciseSignal, 0);

  assert.equal(
    resolution.preventedPressure + resolution.residualPressure,
    preciseSignal.intensity,
  );
});
