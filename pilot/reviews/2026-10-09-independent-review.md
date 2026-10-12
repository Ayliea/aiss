# AI Assurance 2.0 pilot — three-perspective review

Review date: October 8, 2026, America/Chicago (October 9 UTC).

**Recommendation: hold acceptance of the reference pilot pending targeted fixes.**
Continue isolated experimentation only. Do not adopt for client decisions, publish,
integrate with live scoring, or deploy the approval helper.

## Scope and independence

Reviewed commit: `e48090b2a09ed6c5a98dd198dde521eb2586a963`.
Baseline: `055f55cceb0c92372178c8d73988c223f806be21`.
All changed files are within `pilot/`; v1.3 specification and methodology are unchanged.
The worktree was clean at review start. No fixes were applied during review.

The user explicitly authorized three GPT-6.1 Sol reviewers at medium reasoning.
Each received a distinct perspective and evaluated independently before conclusions
were reconciled. Same-model reviews can share blind spots; this is neither external
professional assurance nor an independent human-assessor calibration exercise.
No actual token or dollar measurements were available; no cost estimate is asserted.

The security-diff skill's required preflight resource was inaccessible. Security
review used a scoped manual fallback, not a completed formal Codex Security scan.
No external standards, laws, framework mappings or deployment were revalidated.

## Reviewer conclusions

| Perspective | Local reference-pilot recommendation | Client/production use | Confidence and reasoning |
| --- | --- | --- | --- |
| Technical feasibility | **Hold for fixes** | Not ready | High confidence in reproduced schema/runtime defects and export reproducibility; moderate confidence in overall correctness given narrow synthetic assessment coverage. Invalid input can receive successful outcomes despite a published closed-input contract. |
| Security / assessment validity | **Hold for fixes** | Not approved | High confidence in reproduced result-linkage and grant-boundary behavior; medium confidence in completeness of criterion interpretation. Useful reversible design, but exported results and scoped grants do not yet fulfill their stated contract. |
| Business / operational impact | **Approve continued isolated synthetic experimentation only** | Hold adoption/publication/client use | High confidence in local-only boundary; medium confidence in engagement feasibility. No reason to reject the experiment, but provenance instructions conflict and real assessor effort, evidence access and professional calibration are unmeasured. |

**Majority: 2 of 3 recommend holding acceptance of the local reference pilot.**
**Unanimous: 3 of 3 reject client/production readiness at this stage.**

Meaningful minority position: operational review would allow the existing commit
to continue as explicitly provisional local experimentation. Technical review also
considers missing standalone input/result linkage tolerable for a transient harness
retaining its input separately; security review considers linkage a necessary local
contract correction. Both agree it is required before auditable client reporting.
The vote is advice, not permission to execute changes or adopt policy.

## Validated objections and proposed correction scope

### R1 — Runtime/schema input mismatch

Evidence: `pilot/evaluator.py` lines 26–28, 88–96 and 159–162 versus
`pilot/assessment.schema.json`.

Technical review reproduced acceptance of `mappings={}`, object-valued `reason`,
malformed direct-evidence `inheritance`, whitespace-only list identifiers, an empty
`synthetic:` target and compact date strings. Main review separately reproduced:

- `baseline()['mappings'] = {}` still returns `conformant-to-declared-draft-profile`.
- A mapping target `synthetic:` receives `supported`.

Proposed correction: validate every present optional field and container; reject
empty/whitespace identifiers and noncanonical contractual dates; add schema/runtime
negative cases and compatibility tests. Additional semantic/date-order checks can
remain stricter than JSON Schema. This is a local input-contract defect, not proof
of deployed authorization bypass.

### R2 — Bounded grants constrain parameter names but not allowed selector values

Evidence: `pilot/policy.py` lines 57 and 70–80; fixture helpers in
`pilot/tests/test_pilot.py` lines 17–36.

Main review reproduced the security reviewer finding: construct the existing read
action/grant, change `parameters.field` from `title` to `secret`, then authorize with
the same grant. Result is `permit`, class A1. The helper has no grant field capable
of expressing the intended allowed selector value. The caller's actual IAM authority
is a separate trusted assertion; this is not evidence of real data exfiltration.

Proposed correction: explicit typed parameter/value constraints for approved tool
schemas, with deny on missing consequential bounds; negative tests for changed field
selectors, invalid values/types and parameter combinations. Do not add a real dispatch
service, cryptographic approval system or production IAM integration to fix this pilot.

### R3 — Exported results omit assessment-input identity and scope limitations

Evidence: `pilot/evaluator.py` lines 183–188.

Main review independently changed every execution's scope, system version, assessor
and limitations, plus evidence source and provenance, in a copied baseline assessment.
Both calls to `evaluate()` returned identical objects. The result includes the release
digest, but no exact assessment-input digest, assessment date or retained execution/
evidence linkage. It cannot distinguish those inputs when detached from them.

Proposed correction: canonical assessment-input digest, assessment date, criterion-level
evidence/execution references, and material scope/version/period/sample/limitations.
Keep redacted evidence references rather than exporting raw sensitive artifacts. Add a
regression proving materially changed assessment scope/input changes the exported binding.
Signed result storage is a separate deployment gate, not necessary for this local fix.

### R4 — Provenance procedure contradicts the proposed AC-6.6 replacement

Evidence: `pilot/catalog.json` lines 1039–1066 and `pilot/procedures.json` lines 939–940.

The replacement allows documented unsupported technical capability with clear human-
readable fallback, while preserving independently applicable legal marking obligations.
The generated procedure calls unsupported provenance capability unknown/failed and not
waived. Main review confirmed both strings in the generated contracts.

Proposed correction: align RFC procedure, generated procedure and criterion interpretation
with the accepted capability/fallback design; test both legitimate technical limitation
with disclosure and unmet mandatory legal-overlay marking. Do not relax legal duties or
claim all modalities support equivalent durable marking.

### R5 — Attempted versus unperformed procedure state needs explicit input

Evidence: `pilot/evaluator.py` lines 126–144; RFC verification-state definitions.

Security review observed that deleting an execution record from a submitted pass converts
the result to unknown. This is conservative for overall conformance but does not establish
whether the procedure was unperformed or attempted with missing documentation. Main review
treats this as an input/semantic ambiguity, not evidence that a missing record necessarily
proves an unperformed test.

Proposed correction: record attempted/performed status explicitly; derive not-tested for
confirmed unperformed procedures and unknown for attempted-but-insufficient evidence. Do
not infer either actual execution or nonexecution from missing documentation alone. Preserve
indeterminate conformance and add both branches to fixtures.

## Semantic and operational acceptance gates

- Reconcile criterion interpretation with authoritative parent text. Example: the AC-6.1
  draft predicate omits the explicit documented review/approval qualifier; compound RAG
  predicates also need atomic or clearly grouped treatment. Full catalog semantic validation
  was not completed by the reviewers.
- Evidence sufficiency, source independence, applicability, sampling and provider inheritance
  remain accountable assessor judgments. The provisional two-medium-source rule does not prove
  independence and requires deliberate acceptance or revision.
- No live workload profile is accepted. Synthetic subset profiles must not be repurposed into
  commercial claims without a reviewed applicability/claim contract.
- Measure effort and access on one bounded workload: evidence request rounds, collection,
  technical tests, unsupported provider visibility, analysis and reporting. No hours or pricing
  inference follows from fast deterministic tests.
- Define a minimal human report-review checklist covering scope, verified/self-reported claims,
  failed/unknown/not-tested criteria, sampling limits, severity rationale and remediation/retest.
- Independently rate ambiguous risk/evidence cases. These three agent reviewers do not fulfill
  the RFC's two-professional-assessor operational calibration gate. Choose a feasible arrangement
  or explicitly amend/defer that gate; do not silently mark it complete.
- Prioritize one useful real crosswalk and defer optional overlay breadth until validated and
  economically justified. Existing source references are not new evidence of framework coverage.

## Validation performed and limitations

Main reran all 16 existing test methods successfully. Technical reviewer ran 15, skipping
the temporary-file tamper test under its stricter read-only assignment, and independently
reproduced exports in memory. Security review reproduced all 19 checked-in fixture overall
expectations. Operational review performed static inspection only. Passing tests did not
detect the contract gaps above; new adversarial/negative cases are necessary.

Explicit nonimplemented pilot features remain limits, not invented vulnerabilities:
verified identity, cryptographic approvals, atomic consumption/budget reservation, real
dispatch/reconciliation, signed results/history, platform parity, artifact truth verification
and actual framework/legal fulfillment. No production/customer incident was observed.

## Consequences, rollback and next approval

If adopted unchanged, different assessors or schema consumers can obtain inconsistent
outcomes; reports can obscure scope; grant demonstrations can overstate boundedness.
The immediate exposure is misleading local assurance behavior, not a deployed compromise.

Rollback now is to leave the pilot isolated and retain the pinned snapshot and its results.
v1.3 needs no rollback. A corrective pass should produce a new pilot version/manifest and
regenerated fixtures, keeping this reviewed commit recoverable. No history rewrite or live
assessment rescore is proposed.

**Recommended next action:** obtain owner acceptance of this recommendation and authorization
for a local corrective pass addressing R1–R5 and the clear AC-6.1 decomposition omission, then
rerun positive, negative and reproducibility checks. Remaining semantic/operational gates must
stay open. Publishing, client adoption, platform integration and deployment remain separately
authorized decisions. No corrections were applied as part of this review.
