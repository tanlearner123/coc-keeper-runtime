# Requirements: Discord AI Keeper

**Defined:** 2026-03-28
**Core Value:** Run a real multiplayer Call of Cthulhu session in Discord where a local AI Keeper can narrate, roleplay multiple characters, and enforce investigation-heavy rules flow without constant manual bookkeeping.

## v2.0 Requirements

### Rich Archive Schema

- [ ] **ARCHX-01**: Long-lived archive profiles should store a fuller set of investigator-card fields, including specialty, career arc, core belief, desire/goal, weakness, key past event, and other structured identity anchors.
- [ ] **ARCHX-02**: Builder answers should be normalized into explicit archive fields wherever possible instead of remaining buried in freeform background text.
- [ ] **ARCHX-03**: Archive data should distinguish clearly between rule-derived mechanical fields and narrative identity fields.

### Archive Presentation

- [ ] **PRES-01**: `/profiles` should remain a compact listing, but the system should add a richer detail view for a selected archive profile.
- [ ] **PRES-02**: Archive presentation in Discord should be organized into readable sections, closer to an investigator card than a debug dump.
- [ ] **PRES-03**: Players should be able to inspect the richer archive details in the archive channel without polluting live-play game halls.

### COC-Bounded Finishing Logic

- [ ] **FIN-01**: Interview-driven signals may influence finishing choices or recommended allocation only through explicit COC-compatible rules or bounded supported modes.
- [ ] **FIN-02**: The system should never invent arbitrary stat bonuses from prompt output; any adjustment path must be reviewable and rules-scoped.
- [ ] **FIN-03**: The archive should preserve both the raw investigator card and the normalized reasoning behind any interview-driven finishing recommendations.

### Module Reuse

- [ ] **MODARCH-01**: Future modules should be able to consume richer archive identity fields for onboarding hooks, private prompts, and role overlays.
- [ ] **MODARCH-02**: Campaign projection should continue to protect the archive base record from scenario-specific mutations.
- [ ] **MODARCH-03**: The richer archive format should remain compatible with the existing projection and panel flows.

## v1.9 Requirements

### Immersive Character-Shaping Flow

- [x] **CHAR-01**: Character creation should begin from a short concept or premise and evolve through adaptive Keeper-style follow-up questions instead of a fixed questionnaire.
- [x] **CHAR-02**: The builder should explicitly shape a character's life goal, weakness/flaw, key past event, and other roleplay anchors so the finished investigator feels like a person rather than just a sheet.
- [x] **CHAR-03**: Follow-up questions should vary by the concept already given, rather than asking the same generic prompts to every player.

### Model-Guided Builder Control

- [x] **ASK-01**: A fast local model may select the next best follow-up question, but only within structured slots and strict interview constraints.
- [x] **ASK-02**: The builder must stop asking questions once the required narrative and mechanical information is sufficient, instead of dragging through unnecessary rounds.
- [x] **ASK-03**: The system should be able to summarize collected answers into structured narrative fields for downstream archive storage and campaign projection.

### COC-Legal Generation Discipline

- [x] **COCGEN-01**: Core attributes and other canonical sheet fields must still come from supported COC generation rules or explicit allowed modes, never from freeform model invention.
- [x] **COCGEN-02**: Narrative answers should influence occupation detail, background, finishing choices, and skill leanings without breaking COC legality.
- [x] **COCGEN-03**: The finished archive profile should clearly distinguish rules-derived values from narrative characterization fields.

### Archive Value And Future Module Reuse

- [x] **ARCH-01**: Archive profiles should store richer long-term identity fields, including life goal and weakness, for reuse across future modules.
- [x] **ARCH-02**: Campaign projections should continue to derive from archive profiles without mutating the archive base.
- [x] **ARCH-03**: Complex modules should be able to read the richer archive characterization to improve onboarding, private hooks, and role overlays.

## v1.8 Requirements

### Discord Channel Discipline

- [x] **CHAN-01**: The system should support distinct Discord channel roles for character archives, live-play game halls, and optional keeper/trace output.
- [x] **CHAN-02**: Character/archive commands should be discouraged or blocked in live-play halls, with clear redirect messaging instead of silent failure.
- [x] **CHAN-03**: Live-play channels should stay focused on campaign actions, narration, and rules resolution rather than profile management noise.

### Conversational Character Builder

- [x] **BUILD-01**: The bot should support conversational investigator creation that feels like a Keeper-guided interview rather than a raw form.
- [x] **BUILD-02**: Core attributes must be generated through canonical COC rules or explicit supported generation modes, not freeform prompt invention.
- [x] **BUILD-03**: The conversational layer should shape occupation, background, skill leaning, portrait/persona summary, and recommended finishing choices without breaking rules validity.
- [x] **BUILD-04**: Character creation should support private-first operation through ephemeral replies or DM, while still allowing an archive-channel mode.

### Long-Lived Profiles And Campaign Projection

- [x] **PROF-01**: Players should own long-lived investigator archives that remain independent of any single module.
- [x] **PROF-02**: Campaigns should project an archive character into a module-specific instance whose SAN, injuries, secrets, and role state do not overwrite the archive base.
- [x] **PROF-03**: Complex modules should be able to add explicit role overlays, such as `覆辙`'s magical-girl track, on top of a projected archive character.

### COC Rule Discipline

- [x] **RULE-01**: Character generation and projection must stay grounded in the supplied local COC 7th rulebooks wherever the base system covers them.
- [x] **RULE-02**: Any scenario-specific modifications to a projected character must be recorded as explicit module metadata or runtime state, not as hidden prompt behavior.
- [x] **RULE-03**: Operator and player surfaces should be able to distinguish base investigator data from campaign-instance state.

## v2 Requirements

### Adventure Authoring And GM Controls

- **AUTHR-01**: Operators can author or edit adventures through a higher-level authoring tool instead of hand-editing JSON.
- **AUTHR-02**: The runtime supports per-player secret handouts or whisper reveals as a first-class mechanic.
- **AUTHR-03**: Operators can override or patch packaged adventure state live during a session without editing stored files manually.
- **AUTHR-04**: The module schema supports richer puzzle scripting and reusable logic macros beyond the first formal adventure set.

## Out Of Scope

| Feature | Reason |
|---------|--------|
| Inventing unsupported rules because a module feels dramatic | New logic must map to canonical COC rules or explicit module-specific rules. |
| Treating `覆辙` as a one-off special case with bespoke runtime hacks | This milestone is explicitly about reusable support for more complex COC modules. |
| Replacing the current room-graph/trigger foundations wholesale | The milestone should extend the runtime, not discard the foundation that already works. |
| Full visual parity with the public character generator in one round | The first goal is persistent player panels and runtime linkage, not a pixel-perfect website clone. |
| Replacing canonical COC generation with pure personality questionnaires | Questioning may shape the character, but stats and card validity must remain rules-grounded. |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| CHAN-01 | Phase 28 | Completed |
| CHAN-02 | Phase 28 | Completed |
| CHAN-03 | Phase 28 | Completed |
| BUILD-01 | Phase 29 | Completed |
| BUILD-02 | Phase 29 | Completed |
| BUILD-03 | Phase 29 | Completed |
| BUILD-04 | Phase 29 | Completed |
| PROF-01 | Phase 30 | Completed |
| PROF-02 | Phase 30 | Completed |
| PROF-03 | Phase 30 | Completed |
| RULE-01 | Phase 29 | Completed |
| RULE-02 | Phase 30 | Completed |
| RULE-03 | Phase 30 | Completed |
| CHAR-01 | Phase 31 | Completed |
| CHAR-02 | Phase 32 | Completed |
| CHAR-03 | Phase 32 | Completed |
| ASK-01 | Phase 31 | Completed |
| ASK-02 | Phase 31 | Completed |
| ASK-03 | Phase 33 | Completed |
| COCGEN-01 | Phase 33 | Completed |
| COCGEN-02 | Phase 33 | Completed |
| COCGEN-03 | Phase 33 | Completed |
| ARCH-01 | Phase 32 | Completed |
| ARCH-02 | Phase 33 | Completed |
| ARCH-03 | Phase 33 | Completed |
| ARCHX-01 | Phase 34 | Planned |
| ARCHX-02 | Phase 34 | Planned |
| ARCHX-03 | Phase 34 | Planned |
| PRES-01 | Phase 35 | Planned |
| PRES-02 | Phase 35 | Planned |
| PRES-03 | Phase 35 | Planned |
| FIN-01 | Phase 36 | Planned |
| FIN-02 | Phase 36 | Planned |
| FIN-03 | Phase 36 | Planned |
| MODARCH-01 | Phase 36 | Planned |
| MODARCH-02 | Phase 36 | Planned |
| MODARCH-03 | Phase 36 | Planned |

**Coverage:**
- v1.8 requirements: 13 total
- v1.9 requirements: 12 total
- v2.0 requirements: 12 total
- Completed: 25
- Planned: 12
- Unmapped: 0

---
*Requirements defined: 2026-03-28*
*Last updated: 2026-03-28 after milestone v1.8 execution*
