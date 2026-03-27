# Roadmap: Discord AI DM

## Overview

Milestone `v1.0` established the Discord-first local-DM runtime with deterministic rules, persistence, diagnostics, and a starter packaged adventure. Milestone `v1.1` introduced a formal module runtime and shipped `疯狂之馆` as the first structured full-length module. Milestone `v1.2` added ready-gated startup, mature dice integration, and true Discord streaming. Milestone `v1.3` polished live-play feel through structured judgement, bounded guidance, and keeper-style scene framing. Milestone `v1.4` introduced room graphs, AI-first extraction drafts, and location-driven play. Milestone `v1.5` now focuses on the missing execution layer: a reusable trigger tree and consequence engine that can drive chained outcomes across many adventures.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [x] **Phase 1: Discord Runtime & Dual-Model Control** - Establish the Discord session surface, async interaction flow, and local dual-model orchestration.
- [x] **Phase 2: Character Import & Rules Authority** - Add one low-friction character path and a deterministic 2014 SRD rules backbone.
- [x] **Phase 3: Gameplay Loop & Combat Play** - Deliver DM narration, multi-character scenes, and heavy-rules combat inside Discord.
- [x] **Phase 4: Persistence, Recovery & Diagnostics** - Harden the runtime for campaign reuse, replayability, and operator visibility.
- [x] **Phase 5: Multiplayer usability, natural message intake, and starter adventure** - Make the bot runnable by a small group through natural channel input and a packaged one-shot.
- [x] **Phase 6: Structured Module Runtime** - Introduce reusable formal adventure packages with canonical state and reveal policy.
- [x] **Phase 7: 疯狂之馆 Formal Module** - Encode `疯狂之馆` as the first official structured module.
- [x] **Phase 8: Module UX, Session Continuity, and Operator Guidance** - Persist packaged-adventure sessions and improve operator visibility.
- [x] **Phase 9: Adventure Onboarding And Auto-Opening** - Make packaged-adventure startup feel like a real game session.
- [x] **Phase 10: Mature Dice Engine And Deterministic Roll Resolution** - Replace placeholder rolls with a mature dice engine.
- [x] **Phase 11: Streaming Responses And Message Reliability** - Make Discord play feel responsive with clearer processing feedback.
- [x] **Phase 12: True Streaming Discord Output** - Stream narrator output live into Discord through chunked edits with fallback.
- [x] **Phase 13: Structured Judgement And Roll Prompting** - Add keeper-style action judgement and explicit roll prompting.
- [x] **Phase 14: Hint Timing, Clue Flow, And Stall Recovery** - Add bounded guidance tiers and stall recovery.
- [x] **Phase 15: Keeper-Style Scene Framing And Consequence Presentation** - Strengthen room introductions, pressure, and return-to-choice rhythm.
- [x] **Phase 16: Room Graph Runtime Foundations** - Introduce location graphs, adjacency, and location-aware runtime state.
- [x] **Phase 17: AI Extraction For Room Graphs And Trigger Trees** - Add AI-first, reviewable extraction drafts for room graphs and trigger trees.
- [x] **Phase 18: 疯狂之馆 Room-Graph Migration** - Migrate `疯狂之馆` into room-graph-driven play behavior.

## Milestone v1.5 Planned Work

### Phase 19: Generic Trigger And Consequence Schema
**Goal**: Define a reusable, chain-capable trigger tree schema that can express declarative conditions and outcomes across many adventures while still allowing limited escape-hatch hooks.
**Depends on**: Phase 18
**Requirements**: TRIG-01, TRIG-02, TRIG-03, TRIG-04
**Success Criteria** (what must be TRUE):
  1. Trigger nodes can express chained evaluation rather than only one-shot prompts.
  2. Conditions can reference actions, roll outcomes, location context, state, clue state, and prior trigger history.
  3. Common mechanics stay declarative and reviewable in module data.
  4. Exceptional mechanics can plug into constrained code hooks without turning the engine into custom imperative sprawl.
**Plans**: 2 plans
Plans:
- [ ] 19-01-PLAN.md - Define generic trigger node, condition, effect, and chain structures for packaged adventures.
- [ ] 19-02-PLAN.md - Add minimal hook boundaries and validation rules so declarative triggers stay the default path.

### Phase 20: Runtime Trigger Engine
**Goal**: Execute trigger trees at runtime so actions and rolls produce persisted, auditable consequence chains rather than shallow prompt text.
**Depends on**: Phase 19
**Requirements**: CONS-01, CONS-02, CONS-03, CONS-04, EXE-01, EXE-02, EXE-03
**Success Criteria** (what must be TRUE):
  1. Trigger evaluation can mutate room state, module state, clue state, and future interaction availability.
  2. Roll outcomes can feed into consequence chains with deterministic, persisted results.
  3. The engine can emit table-facing consequence summaries plus structured internal state updates.
  4. AI extraction can draft trigger trees in the same schema runtime expects.
**Plans**: 2 plans
Plans:
- [ ] 20-01-PLAN.md - Implement trigger evaluation, consequence application, and audit-friendly event emission.
- [ ] 20-02-PLAN.md - Extend extraction outputs and roll handling so trigger trees become executable module data.

### Phase 21: 疯狂之馆 Trigger Migration
**Goal**: Migrate `疯狂之馆` key progress beats onto the generic trigger engine and verify the design still feels reusable beyond this one module.
**Depends on**: Phase 20
**Requirements**: MIG-01, MIG-02, MIG-03
**Success Criteria** (what must be TRUE):
  1. Major `疯狂之馆` interactions now produce structured consequence chains rather than isolated prompt text.
  2. Player actions and roll outcomes visibly change what becomes possible next inside the room graph.
  3. The resulting module remains faithful to the original while demonstrating reusable trigger patterns for future adventures.
**Plans**: 2 plans
Plans:
- [ ] 21-01-PLAN.md - Port `疯狂之馆` key beats onto generic trigger trees and consequence definitions.
- [ ] 21-02-PLAN.md - Tune live room-graph play so consequence chains feel natural and reusable rather than module-specific hacks.

## Progress

**Execution Order:**
Phases execute in numeric order: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Discord Runtime & Dual-Model Control | 3/3 | Completed | 2026-03-27 |
| 2. Character Import & Rules Authority | 3/3 | Completed | 2026-03-27 |
| 3. Gameplay Loop & Combat Play | 3/3 | Completed | 2026-03-27 |
| 4. Persistence, Recovery & Diagnostics | 2/2 | Completed | 2026-03-27 |
| 5. Multiplayer usability, natural message intake, and starter adventure | 2/2 | Completed | 2026-03-27 |
| 6. Structured Module Runtime | 1/1 | Completed | 2026-03-27 |
| 7. 疯狂之馆 Formal Module | 1/1 | Completed | 2026-03-27 |
| 8. Module UX, Session Continuity, and Operator Guidance | 1/1 | Completed | 2026-03-27 |
| 9. Adventure Onboarding And Auto-Opening | 2/2 | Completed | 2026-03-27 |
| 10. Mature Dice Engine And Deterministic Roll Resolution | 2/2 | Completed | 2026-03-27 |
| 11. Streaming Responses And Message Reliability | 2/2 | Completed | 2026-03-27 |
| 12. True Streaming Discord Output | 1/1 | Completed | 2026-03-27 |
| 13. Structured Judgement And Roll Prompting | 2/2 | Completed | 2026-03-27 |
| 14. Hint Timing, Clue Flow, And Stall Recovery | 2/2 | Completed | 2026-03-27 |
| 15. Keeper-Style Scene Framing And Consequence Presentation | 2/2 | Completed | 2026-03-27 |
| 16. Room Graph Runtime Foundations | 2/2 | Completed | 2026-03-28 |
| 17. AI Extraction For Room Graphs And Trigger Trees | 2/2 | Completed | 2026-03-28 |
| 18. 疯狂之馆 Room-Graph Migration | 2/2 | Completed | 2026-03-28 |
| 19. Generic Trigger And Consequence Schema | 0/2 | Planned | - |
| 20. Runtime Trigger Engine | 0/2 | Planned | - |
| 21. 疯狂之馆 Trigger Migration | 0/2 | Planned | - |
