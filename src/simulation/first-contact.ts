import type { CoreSnapshot, EncounterOutcome } from "../core/contracts.js";
import { ElyxionCore } from "../core/elyxion-core.js";
import { RedPressureNode } from "../threats/red-pressure-node/red-pressure-node.js";

export interface FirstContactResult {
  readonly outcomes: readonly EncounterOutcome[];
  readonly finalSnapshot: CoreSnapshot;
}

export function runFirstContact(initialWhiteLineScore = 20): FirstContactResult {
  const core = new ElyxionCore({ initialWhiteLineScore });
  const threat = RedPressureNode.firstContact();
  const outcomes = core.run(threat.emitAll());

  return Object.freeze({
    outcomes,
    finalSnapshot: core.snapshot(),
  });
}

