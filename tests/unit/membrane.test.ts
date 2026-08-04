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

test("maturity makes severe automatic defense more effective", () => {
  const early = new Membrane().respond(severeSignal, { score: 10, tier: "M0" });
  const mature = new Membrane().respond(severeSignal, { score: 90, tier: "M3" });

  assert.equal(early.strategy, "absorb");
  assert.equal(mature.strategy, "adapt");
  assert.ok(mature.mitigationRate > early.mitigationRate);
  assert.ok(mature.energyCost < early.energyCost);
});

test("Membrane enters recovery after an active response", () => {
  const membrane = new Membrane();

  membrane.respond(severeSignal, { score: 10, tier: "M0" });
  assert.equal(membrane.state, "defense");

  membrane.completeResponse();
  assert.equal(membrane.state, "recovery");
});

