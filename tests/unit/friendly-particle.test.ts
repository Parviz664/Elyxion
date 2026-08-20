import assert from "node:assert/strict";
import test from "node:test";

import type { ThreatSignal } from "../../src/core/contracts.js";
import { FriendlyParticle } from "../../src/particles/friendly-particle.js";

function signal(tick: number, intensity: number): ThreatSignal {
  return {
    id: `test:${tick}`,
    source: "test",
    tick,
    intensity,
    pattern: "pulse",
  };
}

test("the friendly particle begins dormant and ignores weak noise", () => {
  const particle = new FriendlyParticle();
  const response = particle.observe(signal(1, 18));

  assert.deepEqual(response.observation.after, {
    state: "dormant",
    accumulatedExposure: 0,
  });
  assert.equal(response.observation.supportRate, 0);
});

test("meaningful pressure wakes recognition before protection", () => {
  const particle = new FriendlyParticle();
  const response = particle.observe(signal(1, 42));

  assert.equal(response.observation.before.state, "dormant");
  assert.equal(response.observation.after.state, "recognizing");
  assert.equal(response.observation.supportRate, 0);
  assert.equal(response.visualCues[0]?.type, "friendly-particle-awakening");
});

test("repeated exposure creates only subtle membrane support", () => {
  const particle = new FriendlyParticle();
  particle.observe(signal(1, 42));
  const connection = particle.observe(signal(2, 78));
  const supporting = particle.observe(signal(3, 28));

  assert.equal(connection.observation.after.state, "supporting");
  assert.equal(connection.observation.supportRate, 0.03);
  assert.equal(supporting.observation.supportRate, 0.08);
});
