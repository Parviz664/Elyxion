# CHANNEL_CONTRACT

Strongest-known supplied contract:
- version `3.2.4`;
- channel `ELYX_P1_MAP_PLANNER_v3.2.4`;
- output `ELYX_MAP_PLAN_PACKET_V3_2_4`;
- observed input family `ELYX_P1_INPUT_V1`.

Mission: build overview map, causal blocks, seed+linear order, micro-stage catalog, quality/readiness reports, P2 handoff, A compact handoff, and resume state.

Core per-node fields include:
`micro_stage_id`, `belongs_to_block_id`, `node_role`, `scope_entities_used`, `minimal_conditions`, `pressure`, `pressure_axis`, `pressure_vector`, `transition_trigger`, `trigger_type`, `mechanism_class`, `micro_transition`, `stabilized_state_after`, plausibility/confidence, anti-repeat, anti-boredom, `felt_inevitability_hint`, handoff tags, and P2 split permission.

Node roles:
`causal_core | bridge | closure | terminal_lock`.

Bridge nodes require proof/support fields. Closure and terminal nodes have split restrictions.

Entity discipline:
- preferred contract budget 8..18;
- out-of-list references fail;
- forbidden entity classes remain forbidden.

Range discipline:
`range_semantics = index_range`;
count hints belong in `output_size_hint`.

Block namespace:
preferred `BL###`; legacy `B###` only with explicit legacy namespace tag because P3 canon B### is reserved.

Required top-level output families do **not** list `final_hard_verdict`. Recent assistant P1 outputs added that field due upstream single-verdict task requests; generic P1 authority for it is therefore **NOT PROVED**.

Runtime implementation is not verified.
