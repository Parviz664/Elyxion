import assert from "node:assert/strict";
import test from "node:test";

import { maturityTierFor } from "../../src/whiteline/maturity.js";
import { WhiteLine } from "../../src/whiteline/white-line.js";

test("WhiteLine maps every maturity boundary to one tier", () => {
  assert.equal(maturityTierFor(0), "M0");
  assert.equal(maturityTierFor(24), "M0");
  assert.equal(maturityTierFor(25), "M1");
  assert.equal(maturityTierFor(49), "M1");
  assert.equal(maturityTierFor(50), "M2");
  assert.equal(maturityTierFor(74), "M2");
  assert.equal(maturityTierFor(75), "M3");
  assert.equal(maturityTierFor(100), "M3");
});

test("WhiteLine learns from an outcome without exceeding 100", () => {
  const whiteLine = new WhiteLine(98);

  const snapshot = whiteLine.learn({
    preventedPressure: 80,
    residualPressure: 20,
  });

  assert.deepEqual(snapshot, { score: 100, tier: "M3" });
});

test("WhiteLine rejects scores outside its contract", () => {
  assert.throws(() => new WhiteLine(-1), RangeError);
  assert.throws(() => new WhiteLine(101), RangeError);
});

