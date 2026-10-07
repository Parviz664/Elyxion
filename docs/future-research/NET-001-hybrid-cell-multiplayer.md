# NET-001 — Hybrid Cell-Stage Multiplayer Architecture

**Project:** Elyxion  
**Status:** FUTURE_RESEARCH_QUESTION / NOT_CANON / NOT_IMPLEMENTED  
**Scope:** Cell phases 1–6  
**Priority:** High future architecture question  
**Intent:** Preserve the multiplayer direction now without prematurely locking a specific vendor, engine replication stack, or server topology.

## Core question

How should Elyxion build an ultra-modern hybrid multiplayer system for Cell Phases 1–6 where nearby players can coexist in real time, while more distant parts of the world can behave asynchronously, with a realistic local target around **50 players** and a stretch target of roughly **140 players in one nearby environmental area**?

The desired solution is **not** “one giant server.” The design target is a hybrid of realtime simulation, asynchronous world state, interest management, procedural reconstruction, regional hosting, persistence, and orchestration.

## Working architecture direction

### 1. Realtime Bubble
Players and interactions that are truly near and causally relevant are simulated and replicated at high fidelity.

Examples:
- nearby organisms;
- direct collisions;
- immediate attacks/defense;
- membrane interactions;
- locally important resources;
- short-range environmental events.

### 2. Near Async
Players and systems that are nearby enough to matter, but not important enough for full-rate updates, are replicated at lower frequency and lower detail.

Possible techniques:
- reduced update rate;
- lower network LOD;
- coarse movement/state;
- event summaries instead of continuous state.

### 3. World Async
Distant areas do not require continuous realtime replication.

The world may preserve:
- changed chemistry;
- consumed resources;
- structures;
- population effects;
- traces of previous player activity;
- larger environmental changes.

A player can go offline while some consequences of their life remain in the world.

**Conceptual model:**

```
Realtime Bubble
      ↓
Near Async
      ↓
World Async
```

This is preferable to a simple binary “online/offline” world model.

## Core systems to research

- **Authoritative dedicated simulation server**  
  Important gameplay truth remains server-authoritative.

- **Spatial interest management / area of relevance**  
  Each player receives only the state that can materially affect them.

- **Network LOD**  
  Nearby entities update frequently; distant entities update less frequently or in compressed form.

- **Client prediction + interpolation**  
  Preserve smooth local motion between authoritative updates.

- **Procedural reconstruction**  
  The server should not necessarily replicate every visible particle or micro-object. It can send compact state, parameters, seeds, or field summaries that clients reconstruct locally.

- **Regional instances / simulation cells**  
  Different local environments can run as separate server processes or allocations.

- **Seamless handoff**  
  Moving between areas should ideally not feel like manually changing servers.

- **Persistent backend**  
  Character/organism state, evolution, long-lived world effects, and global persistence must not depend on one realtime server process surviving forever.

- **Asynchronous event layer**  
  Distant changes can propagate as events rather than frame-by-frame replication.

- **Game-server orchestrator**  
  Server processes should be started, allocated, scaled, and retired according to real load.

## Elyxion-specific scaling principle

### Simulation truth != graphical detail

Elyxion may eventually display enormous numbers of:
- particles;
- chemical fields;
- organisms;
- membrane changes;
- currents;
- threats;
- visual effects.

The network must **not** naively synchronize every visual object as authoritative shared state.

Example:

Bad:
> “Particle #829173 moved by 0.03 cm.”

Better:
> “This region has nutrient-field parameters X/Y/Z, seed S, plus these meaningful deltas.”

The client can reconstruct rich visual detail locally while the server preserves only the shared truth required for gameplay correctness.

## Player-count target

The current future target is:

- **Normal local target:** ~50 simultaneous players in one nearby environment.
- **Stretch target:** up to ~140 players in one local environment.

These are **research targets, not promises**.

The real engineering gate is not:

> “Can the server host 140 players?”

It is:

> “Can the system host 140 players while remaining within the defined Elyxion Simulation Budget, latency target, replication budget, server frame-time budget, client frame-time budget, memory budget, and bandwidth budget?”

A 140-player scene with simple entities and a 140-player scene where every player owns thousands of particles, complex physics, AI, chemistry, and collisions are completely different workloads.

## Unreal replication candidates

Do not lock a replication stack yet.

Two important Unreal directions to benchmark later:

### Replication Graph
Designed for large numbers of replicated actors and connections. It is a mature candidate for interest-management-heavy multiplayer.

### Iris
A newer replication system intended for larger interactive worlds and greater scale. Its maturity and production readiness must be re-evaluated at the time of implementation.

**Important:** Iris and Replication Graph are alternative replication approaches; do not assume they will be used together. Benchmark against Elyxion workloads before selection.

## Hosting / orchestration candidates

These are **candidates, not commitments**:

- Amazon GameLift / equivalent managed game-server hosting;
- Agones + Kubernetes;
- another future orchestration platform;
- hybrid regional/edge hosting.

The correct choice must be based on:
- latency;
- cost;
- operational complexity;
- geographic coverage;
- autoscaling behavior;
- observability;
- failure recovery;
- vendor lock-in;
- data/persistence architecture;
- Elyxion’s actual simulation profile.

## Possible high-level topology

```
Unreal Dedicated Simulation Server
              ↕
Replication / Interest Layer
              ↕
Game Server Orchestrator
              ↕
Regional / Edge Compute
              ↕
Persistent State + Event System
              ↕
Global Elyxion World
```

A local area with 140 players does **not** imply that the entire Elyxion planet or world must live inside one process.

## Core design law

> **Elyxion Multiplayer should scale by reducing unnecessary shared truth, not by reducing the richness perceived by the player.**

Human version:

> The player should perceive a rich living world, while the server should only compute and transmit the subset of truth that must actually be shared.

## Open research questions

1. What exact radius or relevance model defines the realtime bubble?
2. Which gameplay systems require authoritative per-entity replication, and which can be reconstructed procedurally?
3. What is the maximum acceptable update delay for Near Async entities?
4. How should environmental fields be represented: grids, sparse volumes, events, deterministic seeds, or another model?
5. How should migration/handoff between regional simulation cells work?
6. Which state survives server shutdown, and at what granularity?
7. How is conflict resolved when async regions later interact?
8. How many actors/entities can one Elyxion server instance sustain under realistic simulation load?
9. What are the latency, bandwidth, CPU, GPU, memory, and tick-rate targets?
10. How should mobile clients differ from PC clients without changing shared gameplay truth?
11. Which replication stack wins under Elyxion-specific benchmark scenarios?
12. Which hosting/orchestration platform gives the best cost/reliability tradeoff?
13. How should cheating and client-authority boundaries work?
14. How do we test recovery from server crash, regional outage, packet loss, high latency, and split-brain state?
15. How can offline player consequences remain meaningful without requiring the offline player to stay connected?

## Required future benchmark

Before any architecture becomes CANON, build a representative benchmark containing:

- realistic number of players;
- realistic membrane/organism complexity;
- representative particle/field density;
- representative collision/physics cost;
- representative AI/environment activity;
- realistic client hardware classes;
- realistic server hardware;
- realistic network conditions.

Measure at minimum:

- server frame time;
- client frame time;
- p50/p95/p99 latency;
- bandwidth per player;
- replication bytes/sec;
- relevant entity count per player;
- CPU;
- GPU where applicable;
- memory;
- persistence write load;
- recovery time;
- handoff interruption;
- cost per concurrent player.

Only benchmark evidence can promote a candidate architecture toward CANON.

## Current verdict

**Direction:** KEEP / RESEARCH LATER  
**Architecture status:** CANDIDATE  
**50-player local goal:** PLAUSIBLE TARGET, NOT YET PROVEN  
**~140-player local goal:** STRETCH TARGET, NOT YET PROVEN  
**Vendor choice:** UNKNOWN  
**Replication choice:** UNKNOWN  
**Persistence model:** UNKNOWN  
**Final topology:** UNKNOWN

The purpose of NET-001 is to preserve the direction now so future Elyxion engineering can investigate it rigorously without pretending the architecture is already solved.

## References to re-verify during future research

- Unreal Engine Replication Graph documentation
- Unreal Engine Iris Replication System documentation
- Unreal Engine Iris migration documentation
- Amazon GameLift Servers documentation
- Agones GameServer allocation/autoscaling documentation

These references are discovery anchors only. Their exact capabilities, maturity, limits, pricing, and compatibility must be freshly re-verified when NET-001 enters active research.
