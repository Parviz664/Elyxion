import type { CoreSnapshot, EncounterOutcome } from "../core/contracts.js";
import { ElyxionCore } from "../core/elyxion-core.js";
import { RedPressureNode } from "../threats/red-pressure-node/red-pressure-node.js";

export interface FirstContactResult {
  readonly enemy: {
    readonly id: string;
    readonly coreCount: 3;
    readonly visualSignature: "translucent-crimson";
  };
  readonly outcomes: readonly EncounterOutcome[];
  readonly finalSnapshot: CoreSnapshot;
}

export function runFirstContact(): FirstContactResult {
  const core = new ElyxionCore();
  const threat = RedPressureNode.firstContact();
  const outcomes = core.run(threat.emitAll());

  return Object.freeze({
    enemy: Object.freeze({
      id: threat.id,
      coreCount: threat.coreCount,
      visualSignature: threat.visualSignature,
    }),
    outcomes,
    finalSnapshot: core.snapshot(),
  });
}
