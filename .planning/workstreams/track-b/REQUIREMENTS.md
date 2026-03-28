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
