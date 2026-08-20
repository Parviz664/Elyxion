import assert from "node:assert/strict";
import test from "node:test";

import { FriendlyPointEvolution } from "../../src/prototype/friendly-point-evolution.js";

test("Friendly Points prototype starts at scale 2.0 with a 2s breath", () => {
  const evolution = new FriendlyPointEvolution(() => undefined);

  assert.deepEqual(evolution.snapshot(), {
    absorbedFriendlyPoints: 0,
    membraneScale: 2,
    breathingIntervalSeconds: 2,
  });
});

test("absorbing point 3 changes membrane scale to 3.0", () => {
  const logs: string[] = [];
  const evolution = new FriendlyPointEvolution((message) => logs.push(message));

  evolution.absorbFriendlyPoint();
  evolution.absorbFriendlyPoint();
  const atThree = evolution.absorbFriendlyPoint();

  assert.deepEqual(atThree, {
    absorbedFriendlyPoints: 3,
    membraneScale: 3,
    breathingIntervalSeconds: 2,
  });
  assert.deepEqual(logs, [
    "[Elyxion] Threshold 3 reached: membrane scale = 3.0",
  ]);
});

test("absorbing point 5 changes scale to 5.0 and breathing to 3s", () => {
  const logs: string[] = [];
  const evolution = new FriendlyPointEvolution((message) => logs.push(message));

  let atFour = evolution.snapshot();
  for (let point = 1; point <= 4; point += 1) {
    atFour = evolution.absorbFriendlyPoint();
  }

  assert.deepEqual(atFour, {
    absorbedFriendlyPoints: 4,
    membraneScale: 3,
    breathingIntervalSeconds: 2,
  });

  const atFive = evolution.absorbFriendlyPoint();
  assert.deepEqual(atFive, {
    absorbedFriendlyPoints: 5,
    membraneScale: 5,
    breathingIntervalSeconds: 3,
  });
  assert.equal(
    logs.at(-1),
    "[Elyxion] Threshold 5 reached: membrane scale = 5.0, breathing interval = 3s",
  );
});
