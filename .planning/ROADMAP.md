# Roadmap: Discord AI Keeper

## Overview

Milestone `v1.0` established the Discord-first local-DM runtime with deterministic rules, persistence, diagnostics, and a starter packaged adventure. Milestone `v1.1` introduced a formal module runtime and shipped `疯狂之馆` as the first structured full-length module. Milestone `v1.2` added ready-gated startup, mature dice integration, and true Discord streaming. Milestone `v1.3` polished live-play feel through structured judgement, bounded guidance, and keeper-style scene framing. Milestone `v1.4` introduced room graphs, AI-first extraction drafts, and location-driven play. Milestone `v1.5` completed the missing execution layer with a reusable trigger tree and consequence engine. Milestone `v1.6` pivots that foundation into a COC/Keeper-first runtime using local rulebooks, investigator assets, and COC module semantics. Milestone `v1.7` extends that base with persistent investigator panels, private knowledge flow, mixed room/scene/event graphs, and the first `覆辙`-class complex module sample. Milestone `v1.8` turns those systems into a clearer player product through channel-scoped command discipline, rules-grounded conversational character creation, and a clean split between archive profiles and campaign projections, and ships the first archive/builder flow. Milestone `v1.9` transformed that builder into a more game-like character-shaping experience driven by adaptive follow-up questions and richer archive identity. Milestone `v2.0` makes the archive itself feel like a real investigator-card system with richer schema, stronger normalization, better detail views, and explicit COC-bounded finishing logic. Milestone `v2.1` should harden operational delivery and player governance through a repeatable startup smoke check, a single-active-profile rule, and admin-facing character management.

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
- [x] **Phase 19: Generic Trigger And Consequence Schema** - Introduce a reusable trigger tree schema with declarative conditions, effects, and hook boundaries.
- [x] **Phase 20: Runtime Trigger Engine** - Execute trigger trees into persisted consequence chains and event logs.
- [x] **Phase 21: 疯狂之馆 Trigger Migration** - Migrate key `疯狂之馆` beats onto the generic trigger engine.
- [x] **Phase 22: COC Runtime Foundations** - Add COC 7th keeper-facing checks, SAN-aware resolution, and non-D&D runtime semantics on top of the existing engine.
- [x] **Phase 23: COC Asset And Character Intake** - Build reviewable knowledge and investigator intake paths from local rulebooks, pregens, templates, and curated COC references.
- [x] **Phase 24: COC Module And Keeper Experience Migration** - Reframe prompts, diagnostics, and module extraction around COC investigation flow and reusable keeper-style play.
- [x] **Phase 25: Investigator Panel Runtime** - Add persistent per-player investigator panels and panel-linked scenario state grounded in COC rules and explicit module metadata.
- [x] **Phase 26: Private Knowledge And Complex Module Graphs** - Extend runtime structure to support mixed room/scene/event graphs plus player- or group-scoped truths for complex investigations.
- [x] **Phase 27: 覆辙 Complex Module Migration** - Migrate `覆辙` as the first complex COC module sample and fold any needed primitives back into reusable runtime abstractions.
- [x] **Phase 28: Discord Channel Roles And Command Discipline** - Separate archive, game-hall, and keeper-trace responsibilities and enforce command boundaries across channels.
- [x] **Phase 29: COC Conversational Character Builder** - Add a Keeper-style conversational builder with canonical COC stat generation and private-first delivery.
- [x] **Phase 30: Profile Archive And Campaign Projection** - Split long-lived investigator archives from campaign-specific role instances and scenario overlays.
- [x] **Phase 31: Dynamic Builder Interview Engine** - Replace fixed builder prompts with structured, model-guided follow-up selection that adapts to the current character concept.
- [x] **Phase 32: Narrative Character Shaping And Fun Builder UX** - Make builder flow feel like a roleplay scene by collecting life goal, weakness, key past events, and other vivid anchors.
- [x] **Phase 33: COC-Legal Character Projection And Archive Writeback** - Map richer interview output back into legal COC sheets, archive summaries, and campaign-ready profile projections.
- [ ] **Phase 34: Rich Archive Schema And Normalization** - Expand archive fields and normalize interview answers into structured long-lived investigator-card data.
- [ ] **Phase 35: Archive Presentation And Detail Views** - Improve Discord-facing archive browsing and add richer profile detail presentation.
- [ ] **Phase 36: COC-Bounded Archive Finishing And Module Reuse** - Add rules-bounded finishing logic and ensure richer archive data projects cleanly into modules.
- [ ] **Phase 37: Local Delivery Smoke Check** - Add a repeatable local handoff gate that proves tests pass, the bot reaches `READY`, and the launched process stays alive.
- [ ] **Phase 38: Single Active Profile Lifecycle** - Enforce one active long-lived profile per account, with explicit archive/replace promotion flows.
- [ ] **Phase 39: Admin Character Governance** - Add admin-facing profile visibility and mutation commands plus preferred admin-channel guidance.

## Milestone v1.8 Delivery Plan

### Phase 28: Discord Channel Roles And Command Discipline
**Delivered**:
- Define Discord channel roles for `角色档案`, `游戏大厅`, and optional keeper/trace output.
- Enforce command discipline so profile/archive operations are redirected away from live-play halls.
- Keep hall channels focused on running sessions instead of mixing archive management into active play.

### Phase 29: COC Conversational Character Builder
**Delivered**:
- Add a Keeper-style conversational character builder that defaults to private flows but can also run in archive channels.
- Generate core stats through canonical COC methods or supported controlled variants, never freeform prompt invention.
- Let conversation shape occupation, background, skill leaning, and portrait/persona summaries within valid character-sheet constraints.

### Phase 30: Profile Archive And Campaign Projection
**Delivered**:
- Add long-lived investigator archives that can outlive any one module.
- Project archive profiles into campaign-specific character instances so SAN, injuries, and scenario secrets remain local to the campaign.
- Support explicit module overlays, such as special `覆辙` role states, without mutating the archive base record.

## Milestone v1.9 Delivery Plan

### Phase 31: Dynamic Builder Interview Engine
**Delivered**:
- Start from a short player concept and derive the next most valuable follow-up question through structured builder slots.
- Let a fast local model suggest the next question while code enforces slot coverage, stopping conditions, and anti-repetition rules.
- Keep builder answers reviewable and machine-readable so they can later feed archive summaries and campaign projections.

### Phase 32: Narrative Character Shaping And Fun Builder UX
**Delivered**:
- Make the builder feel like a Keeper-led character-shaping scene instead of a form.
- Explicitly collect life goal, weakness/flaw, and other humanizing anchors when they matter.
- Keep questions short, adaptive, and interesting rather than running every player through the same script.

### Phase 33: COC-Legal Character Projection And Archive Writeback
**Delivered**:
- Preserve canonical COC generation as the source of numeric truth while letting the richer interview influence occupation detail, finishing choices, and sheet flavor.
- Write richer identity data into the archive without letting campaign state overwrite it.
- Produce a campaign-ready projection that can reuse the new archive characterization in future modules.

## Milestone v2.0 Delivery Plan

### Phase 34: Rich Archive Schema And Normalization
**Planned**:
- Expand archive profiles into a fuller investigator-card schema, including specialty, career arc, core belief, desire/goal, weakness, and other structured identity anchors.
- Normalize richer builder answers into explicit archive fields instead of leaving them as loosely concatenated text.
- Keep rule-derived and narrative-derived data clearly separated inside the archive.

### Phase 35: Archive Presentation And Detail Views
**Planned**:
- Keep `/profiles` as a compact list, but add richer detail views that better match a real investigator card.
- Organize archive presentation into readable sections inside Discord, inspired by dedicated character-card tools.
- Keep archive presentation scoped to archive channels so live-play halls stay clean.

### Phase 36: COC-Bounded Archive Finishing And Module Reuse
**Planned**:
- Let interview signals influence finishing choices only through explicit legal COC paths and bounded supported modes.
- Preserve reviewable trace of any interview-driven finishing recommendations instead of hiding them in prompt behavior.
- Ensure richer archive data can be consumed by future modules, onboarding hooks, and role overlays without mutating the archive base.

## Milestone v2.1 Delivery Plan

### Phase 37: Local Delivery Smoke Check
**Planned**:
- Add a local smoke-check script or command that runs tests, starts the bot, waits for `READY`, and confirms the process remains alive.
- Eliminate false positives from stale logs or duplicate background bot instances.
- Treat smoke-check success as a release gate before claiming work is ready.

### Phase 38: Single Active Profile Lifecycle
**Planned**:
- Extend archive profiles with explicit lifecycle state such as active, archived, and replaced.
- Ensure each account has exactly one active long-lived investigator by default.
- Require explicit archive/replace actions when promoting a new main character.

### Phase 39: Admin Character Governance
**Planned**:
- Add admin commands to inspect, activate, archive, replace, and delete player profiles.
- Support these commands anywhere while steering operators toward a preferred admin channel.
- Keep governance actions auditable and distinct from ordinary player-facing archive flows.

## Progress

**Execution Order:**
Phases execute in numeric order: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27

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
| 19. Generic Trigger And Consequence Schema | 2/2 | Completed | 2026-03-28 |
| 20. Runtime Trigger Engine | 2/2 | Completed | 2026-03-28 |
| 21. 疯狂之馆 Trigger Migration | 2/2 | Completed | 2026-03-28 |
| 22. COC Runtime Foundations | 1/1 | Completed | 2026-03-28 |
| 23. COC Asset And Character Intake | 1/1 | Completed | 2026-03-28 |
| 24. COC Module And Keeper Experience Migration | 1/1 | Completed | 2026-03-28 |
| 25. Investigator Panel Runtime | 1/1 | Completed | 2026-03-28 |
| 26. Private Knowledge And Complex Module Graphs | 1/1 | Completed | 2026-03-28 |
| 27. 覆辙 Complex Module Migration | 1/1 | Completed | 2026-03-28 |
| 28. Discord Channel Roles And Command Discipline | 1/1 | Completed | 2026-03-28 |
| 29. COC Conversational Character Builder | 1/1 | Completed | 2026-03-28 |
| 30. Profile Archive And Campaign Projection | 1/1 | Completed | 2026-03-28 |
| 31. Dynamic Builder Interview Engine | 1/1 | Completed | 2026-03-28 |
| 32. Narrative Character Shaping And Fun Builder UX | 1/1 | Completed | 2026-03-28 |
| 33. COC-Legal Character Projection And Archive Writeback | 1/1 | Completed | 2026-03-28 |
