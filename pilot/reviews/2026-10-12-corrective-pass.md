# Accepted pilot corrective pass — October 12, 2026

The owner accepted the October 8 three-perspective hold recommendation and authorized
a local corrective pass with regression tests. This record reports implementation
verification, not a new independent review vote or acceptance for client use.

Current draft: **2.0.0-pilot.2**, evaluator pilot.2, input schema 2. The reviewed pilot.1
remains recoverable at `e48090b2a09ed6c5a98dd198dde521eb2586a963`; its review record is
unchanged. Old release digests/input contracts are rejected rather than silently migrated.

| Review item | Correction | Verification |
| --- | --- | --- |
| R1 — Runtime/schema mismatch | Validate present optional fields, containers, nonempty identifiers and canonical dates through the published closed schema; keep additional semantic checks. | Negative examples reject malformed mappings/reason/inheritance, whitespace IDs, compact dates and empty synthetic targets. Valid optional-field examples pass. |
| R2 — Grant parameter bounds | Complete scalar parameter rules constrain allowed values or integer ranges; missing/unbounded/unknown envelopes deny. Currency joins the bound grant context. | Changed title→secret selector, wrong scalar/composite types, boolean-as-integer, omitted selectors, invalid limits and currency changes denied. |
| R3 — Result/input linkage | Canonical exact-input SHA-256 plus date, criterion decision records, evidence references/index and procedure scope/version/period/sample/assessor/limitations. | Material scope/evidence changes alter binding/output; object key reordering is stable; exported result does not alias mutable input. Raw provenance and observation bodies excluded. |
| R4 — AC-6.6 contradiction | Align the procedure with supported machine-readable marking or documented unsupported capability plus clear disclosure; separately mandatory legal duties remain required. | Technical fallback fixture passes its declared profile; unmet legal-marking fixture is nonconformant. Generated wording is checked. |
| R5 — Test activity ambiguity | Explicit performed/attempted/not-performed/undetermined record. Confirmed nonperformance yields not-tested; attempted/incomplete or missing documentation yields unknown. | Both activity branches and contradictory execution claims covered; missing documentation alone does not imply nonperformance. |
| AC-6.1 qualifier | Restore explicit documented human review/approval in the draft criterion. | Generated criterion retains the documented-review qualifier. |

Validation: **23 synthetic assessment cases and 29 test methods passed**. Catalog,
procedure and manifest regeneration is byte-identical. Repeated CLI fixture evaluation
is stable. Generated coverage remains 59 controls, 243 provisional criteria and 59
procedures. Changes are confined to `pilot/`; v1.3 specifications/scoring remain intact.

The schema helper is deliberately limited to the declared contract keywords and local
references, with canonical date/strict integer checks. It is not a general-purpose JSON
Schema implementation. Tests establish the reviewed compatibility cases, not equivalence
to every external validator or proof of all future schema extensions.

The policy helper remains a pure fixture evaluator. Actual identity, classification,
resource counts, prices and authority must be derived/verified by a real execution adapter;
no real atomic consume, budget reservation, provider reconciliation or dispatch is added.
The exported digest is an input binding, not a signature. Retain the restricted original
input for independent reproduction; the report is not a standalone authenticated attestation.

Open gates remain: broader semantic criterion reconciliation, real workload applicability,
evidence sufficiency/independence and assessor calibration, measured delivery effort, actual
framework mappings, real-platform parity and accepted deployment controls. The prior hold
recommendation is not retroactively changed by this implementation pass. No new agents or
reviewers were invoked, and no publication/client adoption/deployment was performed.

## Separate public README correction

Branch `docs/aiss-transparency-readme`, commit `b0fde73`, changes only the root README
against current public main `055f55c`. It removes unsupported vendor/venture-funding
claims and the blanket numerical reproducibility promise. It describes the actual public
controls, methodology and mappings, and states the missing numerical rubrics/weights.
This edit is isolated from the pilot and ready for publication approval. It has not been
pushed or merged into public main as part of this pass.
