#!/usr/bin/env python3
"""Static regression sentinel for Elyxion P Control Point.

This validator checks machine-verifiable control invariants only.
It does not pretend to validate semantic truth or owner intent.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
PCP = ROOT / "channels" / "p-control-point"

REGISTRY = PCP / "P_CHANNEL_REGISTRY_V0_2.yaml"
FROZEN = PCP / "P_CONTROL_POINT_V0_2_FROZEN.md"
FREEZE_DECISION = PCP / "decisions" / "P_CONTROL_POINT_V0_2_FREEZE_DECISION_2026_10_07.md"
INVARIANTS = PCP / "P_CONTROL_POINT_INVARIANTS_V0_1.yaml"
GAPS = PCP / "P_CONTROL_POINT_V0_2_GAP_REGISTER.md"
CASES = PCP / "tests" / "P_CONTROL_POINT_FALSIFICATION_CASES_V0_1.json"

POLICY_MAP = [
    ("edits_locked_raw", "RAW_OVERWRITE"),
    ("correction_without_delta", "HISTORY_REWRITE"),
    ("lower_overwrites_higher", "AUTHORITY_INVERSION"),
    ("resolves_unknown_without_authority", "UNKNOWN_CLOSURE_WITHOUT_AUTHORITY"),
    ("automatic_canonization", "STATUS_PROMOTION_DRIFT"),
    ("contracted_without_source", "UNSOURCED_CONTRACT"),
    ("material_output_without_lineage", "UNSUPPORTED_CREATION"),
    ("material_input_dropped_without_reason", "MATERIAL_LOSS"),
    ("normalizes_ambiguous_raw", "SILENT_NORMALIZATION"),
    ("role_escape", "ROLE_ESCAPE"),
    ("provenance_overclaim", "PROVENANCE_OVERCLAIM"),
    ("assistant_rationale_as_owner", "ASSISTANT_RATIONALE_PROMOTION"),
    ("node_function_conflation", "NODE_FUNCTION_CONFLATION"),
    ("functional_similarity_as_absorption", "FALSE_ABSORPTION_INFERENCE"),
    ("freeze_current_route", "ROUTE_HOLD_BREACH"),
    ("gameplay_conversion_without_bridge", "DOMAIN_BOUNDARY_BREACH"),
    ("requires_live_dream_classification", "CREATIVITY_CONTROL_DRIFT"),
    ("p2_item_without_p1_binding", "P2_SOURCE_ORPHAN"),
    ("p3_strengthens_semantics", "P3_SEMANTIC_MUTATION"),
    ("p4_rewrites_candidate", "P4_SELECTION_MUTATION"),
    ("p4_bypasses_author_selection", "AUTHOR_SELECTION_BYPASS"),
    ("uncertainty_promoted", "UNCERTAINTY_PROMOTION"),
    ("source_order_changed_without_authority", "SOURCE_ORDER_DRIFT"),
    ("known_gap_erased", "GAP_ERASURE"),
]

REQUIRED_INVARIANT_IDS = {f"PCP-I{i:03d}" for i in range(1, 26)}

def classify(facts: dict[str, bool]) -> str:
    for key, violation in POLICY_MAP:
        if facts.get(key):
            return violation
    return "PASS"

def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)

def main() -> int:
    errors: list[str] = []

    for path in (REGISTRY, FROZEN, FREEZE_DECISION, INVARIANTS, GAPS, CASES):
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}", errors)

    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors))
        return 1

    registry = REGISTRY.read_text(encoding="utf-8")
    frozen = FROZEN.read_text(encoding="utf-8")
    freeze_decision = FREEZE_DECISION.read_text(encoding="utf-8")
    invariants = INVARIANTS.read_text(encoding="utf-8")
    gaps = GAPS.read_text(encoding="utf-8")
    data = json.loads(CASES.read_text(encoding="utf-8"))

    # Frozen control-layer state must be explicit.
    require("status: FROZEN_CONTROL_LAYER_ROUTE_HOLD" in registry,
            "registry lost frozen control-layer status", errors)
    require("FROZEN_CONTROL_LAYER / ROUTE_HOLD" in frozen,
            "frozen contract lost route-HOLD scope", errors)
    require("FROZEN_WITH_ROUTE_HOLD" in freeze_decision,
            "freeze decision record missing frozen-with-HOLD status", errors)

    # Current owner Decision C / HOLD must remain explicit until changed by a
    # new versioned route decision.
    require("status: HOLD_UNRESOLVED" in registry,
            "registry lost HOLD_UNRESOLVED current-route state", errors)
    require("owner_decision: C" in registry,
            "registry lost owner Decision C", errors)
    require("implementation_boundary_blocked: true" in registry,
            "registry no longer blocks disputed route implementation", errors)

    # Merge and implementation are not authorized by the freeze itself.
    require("merge_authorized: false" in registry,
            "freeze silently authorized merge", errors)
    require("route_implementation_authorized: false" in registry,
            "freeze silently authorized disputed route implementation", errors)

    # Authority boundaries.
    require("mutation_authority: NONE" in registry,
            "mutation authority changed from NONE", errors)
    require("canonization_authority: NONE" in registry,
            "canonization authority changed from NONE", errors)
    require("automatic_canonization_forbidden: true" in registry,
            "automatic canonization guard missing", errors)

    # Core domain / creativity boundary.
    require("free_author_dream_outside_continuous_p_control: true" in registry,
            "free-author-dream boundary missing", errors)
    require("p_channels_are_ai_work_architecture: true" in registry,
            "P-channel work-architecture boundary missing", errors)
    require("not_automatically_gameplay_systems: true" in registry,
            "gameplay-boundary guard missing", errors)

    # Known route families must both remain in history while HOLD is active.
    require("P0 -> -P1 -> P1 -> P2 -> P3 -> P4" in registry,
            "historical route containing -P1 disappeared", errors)
    require("P0 -> P1 -> P2 -> P3 -> P4" in registry,
            "historical NO_-P1 route disappeared", errors)

    # Gap visibility.
    require("GAP-G0-001" in gaps and "INTENTIONALLY_OPEN" in gaps,
            "G0 route-authority gap no longer visibly open", errors)

    # Invariant inventory.
    seen = {inv_id for inv_id in REQUIRED_INVARIANT_IDS if inv_id in invariants}
    missing = sorted(REQUIRED_INVARIANT_IDS - seen)
    require(not missing, f"missing invariant IDs: {missing}", errors)

    # Falsification fixtures.
    cases = data.get("cases", [])
    require(len(cases) >= 25, "falsification case set unexpectedly shrank", errors)
    for case in cases:
        actual = classify(case.get("facts", {}))
        expected = case.get("expected")
        require(
            actual == expected,
            f"{case.get('id')}: expected {expected}, got {actual}",
            errors,
        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("PASS: frozen v0.2 control-layer state preserved")
    print(f"PASS: {len(cases)} falsification cases")
    print(f"PASS: {len(REQUIRED_INVARIANT_IDS)} invariant IDs present")
    print("PASS: Decision C / HOLD route guard preserved")
    print("PASS: historical route families preserved")
    print("PASS: free-author-dream and domain boundaries preserved")
    print("PASS: merge/runtime route implementation remain unauthorized")
    return 0

if __name__ == "__main__":
    sys.exit(main())
