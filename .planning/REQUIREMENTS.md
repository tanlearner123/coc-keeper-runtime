# Requirements: Discord AI DM

**Defined:** 2026-03-28
**Core Value:** Run a real multiplayer D&D session in Discord where a local AI DM can narrate, roleplay multiple characters, and enforce heavy rules flow without constant manual bookkeeping.

## v1.5 Requirements

### Generic Trigger Schema

- [ ] **TRIG-01**: The runtime should support a reusable trigger tree schema that can express chained conditions and outcomes rather than one-shot prompts.
- [ ] **TRIG-02**: Trigger definitions should be mostly declarative so future adventures can reuse them without bespoke code for common cases.
- [ ] **TRIG-03**: The schema should support actions, roll outcomes, state comparisons, location context, clue state, and trigger history as conditions.
- [ ] **TRIG-04**: The engine should still allow a limited code-hook escape hatch for exceptional mechanics that are too awkward or brittle to express declaratively.

### Consequence Engine

- [ ] **CONS-01**: Trigger resolution should be able to update module state, room state, clue state, reachable paths, interactable availability, and ending progress.
- [ ] **CONS-02**: Roll results should feed into the consequence engine so success, failure, partial success, and threshold outcomes cause structured downstream changes.
- [ ] **CONS-03**: Chained outcomes should be deterministic, auditable, and persistable so the same action never depends on narrator improvisation alone.
- [ ] **CONS-04**: The engine should emit table-facing consequence summaries that narration can build on, rather than only mutating hidden state.

### Reusable Extraction Contract

- [ ] **EXE-01**: AI-first module extraction should be able to draft trigger trees in the same reusable schema used by runtime execution.
- [ ] **EXE-02**: Extracted trigger drafts should clearly separate declarative nodes from places that require human review or code hooks.
- [ ] **EXE-03**: Trigger extraction should remain portable across future scripts instead of learning only `疯狂之馆`.

### 疯狂之馆 Trigger Migration

- [ ] **MIG-01**: `疯狂之馆` should migrate its key progress beats into the new trigger engine rather than handling them as shallow prompt text or ad hoc checks.
- [ ] **MIG-02**: Key actions such as inspecting landmarks, entering halls, major investigations, and blood-exit logic should produce structured consequence chains.
- [ ] **MIG-03**: The migrated module should feel more like a tabletop session because roll outcomes and decisions visibly change what becomes possible next.

## v2 Requirements

### Adventure Authoring And GM Controls

- **AUTHR-01**: Operators can author or edit adventures through a higher-level authoring tool instead of hand-editing JSON.
- **AUTHR-02**: The runtime supports per-player secret handouts or whisper reveals as a first-class mechanic.
- **AUTHR-03**: Operators can override or patch packaged adventure state live during a session without editing stored files manually.
- **AUTHR-04**: The module schema supports richer puzzle scripting and reusable logic macros beyond the first formal adventure set.

## Out Of Scope

| Feature | Reason |
|---------|--------|
| Rewriting the entire module runtime around imperative Python logic | This milestone is explicitly about a mostly declarative trigger engine. |
| Making every trigger purely declarative with no escape hatch | Some mechanics need limited hook support to stay sane and maintainable. |
| Limiting the trigger system to `疯狂之馆` only | The whole point of this milestone is reuse across future adventures. |
| Replacing room graphs with trigger trees as the primary spatial model | Trigger trees should build on room graphs, not displace them. |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| TRIG-01 | Phase 19 | Planned |
| TRIG-02 | Phase 19 | Planned |
| TRIG-03 | Phase 19 | Planned |
| TRIG-04 | Phase 19 | Planned |
| CONS-01 | Phase 20 | Planned |
| CONS-02 | Phase 20 | Planned |
| CONS-03 | Phase 20 | Planned |
| CONS-04 | Phase 20 | Planned |
| EXE-01 | Phase 20 | Planned |
| EXE-02 | Phase 20 | Planned |
| EXE-03 | Phase 20 | Planned |
| MIG-01 | Phase 21 | Planned |
| MIG-02 | Phase 21 | Planned |
| MIG-03 | Phase 21 | Planned |

**Coverage:**
- v1.5 requirements: 14 total
- Mapped to phases: 14
- Unmapped: 0

---
*Requirements defined: 2026-03-28*
*Last updated: 2026-03-28 for milestone v1.5 planning*
