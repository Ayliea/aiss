# AISS Changelog

All notable changes to the Ayliea AI Security Standard are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning follows semantic versioning as described in [governance.md](./governance.md).

## [1.2.2] — 2026-05-11

**Status:** Released

First vertical industry crosswalk: cyber-insurance underwriting for healthcare. No changes to the normative spec (sub-controls and scoring unchanged from v1.2.1).

### Added

- `crosswalks/healthcare-cyber-insurance.md` — AISS sub-controls mapped to typical cyber-insurance underwriting questions for healthcare organizations adopting AI. Carrier-neutral (Coalition, At-Bay, Travelers, Beazley, Chubb, Hiscox baseline). Sourced from public broker materials + NAIC bulletins. Submitable evidence package for AI section of healthcare cyber applications.

### Changed

- `README.md` — directory layout now distinguishes framework crosswalks (peer-standard reverse mappings) from industry-profile crosswalks (vertical-specific application contexts).

## [1.2.1] — 2026-05-11

**Status:** Released

Governance scaffolding addition. No changes to the standard's normative content (spec, controls, methodology, crosswalks unchanged from v1.2).

### Added

- `CONTRIBUTING.md` — full RFC workflow, versioning rules, contribution licensing, attribution policy.
- `CODE_OF_CONDUCT.md` — adopts Contributor Covenant 2.1.
- `SECURITY.md` — private disclosure process for security issues in the standard itself, with explicit scope and SLAs.
- `rfcs/` directory with `README.md`, RFC template (`0000-template.md`), and the first retroactive RFC ([`0001-aiss-v1.2-ratification.md`](./rfcs/0001-aiss-v1.2-ratification.md)).
- `.github/ISSUE_TEMPLATE/` — four issue forms covering RFC control changes, RFC crosswalks, errata, and clarifications, plus a `config.yml` routing security reports to the private channel.
- `.github/PULL_REQUEST_TEMPLATE.md` for direct PRs.

### Changed

- `README.md` — added "How to contribute" table, updated directory layout, removed Release-Candidate status (now Released).
- `governance.md` — security-disclosure subsection now references `SECURITY.md` for the full policy.

## [1.2] — 2026-05

**Status:** Released

Substantive content additions addressing OWASP LLM06 (Excessive Agency), LLM08 (Vector and Embedding Weaknesses), and EU AI Act Article 50 obligations. NIST AI 600-1 (Generative AI Profile) mappings added to all sub-controls. Authoritative ATLAS technique catalog refreshed to v5.6. Editorial and citation hygiene improvements.

### Added

- AC-3.7 — RAG and Vector Store Security (SHALL). Addresses OWASP LLM08, MITRE ATLAS T0070/T0071/T0082/T0085.000. Covers source classification at ingest, vector store access control, retrieved-content trust boundary, source citations, refresh cadence, and tenant isolation.
- AC-6.6 — Synthetic Content Provenance and Marking (SHALL). Addresses EU AI Act Article 50(2)/(4) machine-readable AI-content marking and deepfake disclosure (effective 2 August 2026). References C2PA Content Credentials and SynthID.
- AC-10.6 — Agentic AI Action Authorization and Guardrails (SHALL). Addresses OWASP LLM06 (Excessive Agency) and MITRE ATLAS agentic-AI techniques (T0080, T0081, T0083, T0086, T0098, T0099, T0100, T0101, T0102, T0103, T0104, T0105, T0108, T0110, T0112).
- NIST AI 600-1 (Generative AI Profile, July 2024) per-control mappings on all 56 sub-controls — verified against the published action catalog (211 action IDs).
- owasp_llm_top_10 field in framework_mappings — added on new v1.2 controls; coverage on v1.1 controls to be added incrementally.

### Changed

- MITRE ATLAS reference bumped from v5.4 to v5.6 in normative_references (verified against authoritative atlas-data/data/techniques.yaml).
- OWASP LLM Top 10 2025 publication date corrected to 2025-03 (was 2024-11).
- ENISA Multilayer Framework reference clarified with citation_key.
- AC-3 control_count: 6 → 7 (added AC-3.7). AC-6 control_count: 5 → 6 (added AC-6.6). AC-10 control_count: 5 → 6 (added AC-10.6). Framework total_controls: 53 → 56.
- Applicability scoping examples extended for AC-3.7 (RAG) and AC-10.6 (agentic AI).

### Fixed

- Citation padding removed: §6-1-1703(3)(a) (Colorado AI Act) trimmed from 32 controls where it did not materially apply.

## [1.1] — 2026-03

**Status:** Published

Added 5 new sub-controls strengthening governance, data protection, and model security. Expanded MITRE ATLAS coverage. Updated EU AI Act and Colorado AI Act references.

### Added

- AC-1.3 — Risk Appetite documentation
- AC-3.3 — Encryption in transit and at rest for AI data flows
- AC-3.4 — Data minimization for AI interactions
- AC-10.2 — Adversarial testing on annual cadence
- AC-10.3 — Model versioning and rollback

### Changed

- Expanded ATLAS technique mappings on AC-2 through AC-10
- Clarified normative levels (SHALL vs SHOULD) across all 53 sub-controls
- Added concrete cadences and timelines (90-day key rotation, 72-hour breach notification, etc.)

## [1.0] — 2025-12

**Status:** Superseded by v1.1

Initial public draft. 48 sub-controls across 10 domains.
