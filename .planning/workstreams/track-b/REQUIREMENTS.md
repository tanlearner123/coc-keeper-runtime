# Requirements: Discord AI Keeper - Track B

**Defined:** 2026-03-28
**Core Value:** Run a real multiplayer Call of Cthulhu session in Discord where a local AI Keeper can narrate, roleplay multiple characters, enforce investigation-heavy rules flow, and keep canonical module state without constant manual bookkeeping.

## vB.1.1 Requirements (Track B)

Milestone: Archive And Builder Normalization

### AI Summarization (核心修复)

- [x] **AI-01**: User completes builder interview, AI synthesizes cohesive character profile from raw answers instead of copying verbatim
- [x] **AI-02**: AI summarization respects COC 7e rules - no invented skills or occupations
- [x] **AI-03**: Summarization distinguishes derived fields (calculated by rules) from intent fields (user's explicit choices)
- [x] **AI-04**: Confirmation step before AI overwrites user's explicit character choices

### Archive Field Normalization

- [x] **FN-01**: Existing "life_goal" field maps to standard COC backstory section
- [x] **FN-02**: Existing "weakness" field maps to standard COC backstory section
- [x] **FN-03**: Existing "key past event" field maps to standard COC backstory section
- [x] **FN-04**: New fields follow COC 7e character sheet structure (Birthplace, Residence, Family, Education)
- [x] **FN-05**: Schema versioning - new fields are nullable with defaults for backward compatibility

### Builder-Archive Contracts

- [x] **BC-01**: Pydantic contracts define builder-to-archive communication schema
- [x] **BC-02**: AnswerNormalizer component cleans raw user input to canonical slot format
- [x] **BC-03**: CharacterSheetSynthesizer component transforms normalized answers into cohesive narrative
- [x] **BC-04**: SectionNormalizer maps synthesis output to COC 7e character sheet sections
- [x] **BC-05**: ArchiveProfileFactory creates profiles from synthesis output
- [x] **BC-06**: Fallback from synthesis to heuristic extraction for robustness

### Archive-Projection Sync

- [x] **PS-01**: Archive normalization updates automatically propagate to campaign projections
- [x] **PS-02**: Diagnostic command shows sync status between archive and projection
- [x] **PS-03**: Single active profile governance still works after normalization changes

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| AI-01 | Phase 41 | Completed |
| AI-02 | Phase 42 | Completed |
| AI-03 | Phase 42 | Completed |
| AI-04 | Phase 42 | Completed |
| FN-01 | Phase 42 | Completed |
| FN-02 | Phase 42 | Completed |
| FN-03 | Phase 42 | Completed |
| FN-04 | Phase 42 | Completed |
| FN-05 | Phase 40 | Completed |
| BC-01 | Phase 40 | Completed |
| BC-02 | Phase 40 | Completed |
| BC-03 | Phase 41 | Completed |
| BC-04 | Phase 41 | Completed |
| BC-05 | Phase 41 | Completed |
| BC-06 | Phase 42 | Completed |
| PS-01 | Phase 42 | Completed |
| PS-02 | Phase 42 | Completed |
| PS-03 | Phase 42 | Completed |

**Coverage:**
- vB.1.1 requirements: 18 total
- Mapped to phases: 18
- Unmapped: 0 ✓

---
*Requirements defined: 2026-03-28*
*Last updated: 2026-03-28 for vB.1.1*

---

## vB.1.2 Requirements (Track B)

Milestone: Investigator Archive Card Completion

### Archive Card Completeness

- [x] **AC-01**: Long-lived archive schema covers a broader set of COC-style investigator card sections inspired by `charSheetGenerator`
- [x] **AC-02**: New card sections remain backward compatible with old archive payloads
- [x] **AC-03**: New card sections are explicitly classified as long-lived archive truth, not campaign-local state

### Builder Writeback Quality

- [x] **BW-01**: Builder interview answers write back into richer card sections instead of only background summaries
- [x] **BW-02**: AI enrichment can extend card sections without silently overriding explicit player-provided answers
- [x] **BW-03**: Builder writeback still respects local COC rules and does not invent illegal rule-facing values

### Presentation

- [x] **PR-01**: `/profile_detail` presents richer card sections with clear grouping and readability
- [x] **PR-02**: Archive-channel `/sheet` shows the long-lived card in a fuller investigator-card layout
- [x] **PR-03**: Card presentation surfaces enough detail that collaborators can understand a character without reading raw builder transcripts

### Archive / Projection Boundary

- [x] **AP-01**: Richer archive cards do not cause module-local state to leak back into long-lived archives
- [x] **AP-02**: Projection sync still works after archive schema expansion
- [x] **AP-03**: Diagnostics or documentation clearly explain archive vs projection boundaries for new card fields

## vB.1.2 Traceability

| Requirement | Planned Phase |
|-------------|---------------|
| AC-01 | Phase 44 |
| AC-02 | Phase 44 |
| AC-03 | Phase 47 |
| BW-01 | Phase 45 |
| BW-02 | Phase 45 |
| BW-03 | Phase 45 |
| PR-01 | Phase 46 |
| PR-02 | Phase 46 |
| PR-03 | Phase 46 |
| AP-01 | Phase 47 |
| AP-02 | Phase 47 |
| AP-03 | Phase 47 |

**Coverage:**
- vB.1.2 requirements: 12 total
- Mapped to phases: 12
- Unmapped: 0 ✓

---

## vB.1.3 Requirements (Track B)

Milestone: Interview-To-Sheet Character Creation

### Interview Planner

- [x] **IP-01**: Builder starts from a short character concept and uses adaptive follow-up questions instead of large generic prompts
- [x] **IP-02**: Interview coverage maps to richer long-lived card/person sections without forcing every player through identical questions
- [x] **IP-03**: Builder stops once the person is sufficiently shaped rather than after exhausting a rigid questionnaire

### Character Portrait

- [x] **CP-01**: Interview answers synthesize into a structured person-level portrait before any numeric card finalization
- [x] **CP-02**: Portrait captures goal, weakness, beliefs, key past event, important ties, and other long-lived identity traits
- [x] **CP-03**: Portrait synthesis preserves explicit user intent and labels AI-derived interpretation separately when needed

### Rule Mapping And Finalization

- [x] **RF-01**: Interview output may influence rule-bounded finishing recommendations, but may not invent numeric rules or break local COC rulebook constraints
- [x] **RF-02**: Character creation flow explicitly separates:
  - person shaping
  - rule mapping
  - dice-based finalization
- [x] **RF-03**: Finalization stage explains which parts came from interview intent versus which parts came from COC rules and dice

### Integration

- [x] **IN-01**: Existing archive profiles and builder sessions remain backward compatible while the new two-stage flow is introduced
- [x] **IN-02**: Archive-channel builder UX clearly signals whether the player is still shaping the person or already finalizing the sheet
- [x] **IN-03**: The resulting contracts remain reusable for later projection, archive presentation, and future Track A/Track D work

## vB.1.3 Traceability

| Requirement | Planned Phase |
|-------------|---------------|
| IP-01 | Phase 48 |
| IP-02 | Phase 48 |
| IP-03 | Phase 48 |
| CP-01 | Phase 49 |
| CP-02 | Phase 49 |
| CP-03 | Phase 49 |
| RF-01 | Phase 50 |
| RF-02 | Phase 50 |
| RF-03 | Phase 50 |
| IN-01 | Phase 51 |
| IN-02 | Phase 51 |
| IN-03 | Phase 51 |

**Coverage:**
- vB.1.3 requirements: 12 total
- Mapped to phases: 12
- Unmapped: 0 ✓
