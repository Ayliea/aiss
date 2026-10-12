# AI Assurance 2.0 — local pilot calibration

Draft synthetic validation only. No customer evidence, production authorization,
live scoring, deployed integration or external framework conformance was tested.

Release manifest SHA-256: `dd93d060577532d219abc650993c88ce5f2f1e1c0486e80f7da1904c122a4904`.

Validated 59 control records, 243 draft atomic
criteria and 59 procedure records. All 23 declared assessment cases and
29 test methods passed. The tests include all 64 three-child outcome
combinations, 16 severity cells, monotonic risk ordering, input/release tampering,
action-binding mutations, scope changes, missing evidence, inheritance and mapping
conditions. No numeric maturity score or letter grade is produced.

| Synthetic case | Actual result | Check |
| --- | --- | --- |
| pass | conformant-to-declared-draft-profile | PASS |
| mandatory-failure | not-conformant | PASS |
| missing-evidence | indeterminate | PASS |
| low-confidence | indeterminate | PASS |
| stale-evidence | indeterminate | PASS |
| deleted-evidence | indeterminate | PASS |
| unperformed | indeterminate | PASS |
| attempted-without-execution-record | indeterminate | PASS |
| undetermined-test-activity | indeterminate | PASS |
| unresolved-scope | indeterminate | PASS |
| missing-observation | indeterminate | PASS |
| missing-execution | indeterminate | PASS |
| approved-na | no-applicable-mandatory-requirements | PASS |
| inherited-valid | conformant-to-declared-draft-profile | PASS |
| inherited-unverified | indeterminate | PASS |
| failure-with-uncertainty | not-conformant | PASS |
| corroborated-medium | conformant-to-declared-draft-profile | PASS |
| mapping-and | indeterminate | PASS |
| mapping-or | indeterminate | PASS |
| mapping-delta | conformant-to-declared-draft-profile | PASS |
| full-baseline-incomplete | indeterminate | PASS |
| provenance-capability-fallback | conformant-to-declared-draft-profile | PASS |
| provenance-unmet-legal-marking | not-conformant | PASS |

## What this resolved

- Missing procedure execution cannot be replaced by evidence metadata alone.
- An unsupported failure is an evidence gap, not an invented demonstrated violation.
- A pass is bounded by declared profile; subset profiles cannot masquerade as the full baseline.
- N/A requires owner and assessor records; unknowns and unperformed tests remain visible.
- An evidence-reuse mapping must satisfy its whole AND path or an approved OR alternative,
  plus scoped evidence deltas. Real-framework targets are rejected by this synthetic harness.
- Failed controls flag domain maturity narratives for human reconciliation.
- Review-derived corrections reject malformed optional fields, mapping containers/IDs,
  whitespace identifiers and noncanonical dates under the published input contract.
- Exact-input binding and decision metadata distinguish scope, period, version, sample,
  assessor and limitation changes without copying raw artifact bodies into the report.
- Explicit test activity distinguishes confirmed nonperformance from incomplete attempts
  and missing procedure documentation.
- Grant parameter rules bound selector values and scalar types, not only parameter names.
- AC-6.6 capability fallback and separately mandatory legal marking are distinct; the
  documented-review qualifier is retained in AC-6.1.

## Assessor judgment and calibration gaps

1. **Atomic interpretations:** 243 draft predicates paraphrase or decompose source/RFC requirements.
   Review the decomposition against normative text. Automated export is not semantic approval.
2. **Evidence sufficiency:** scope, provenance, population, confidence, independence, period and
   sampling are asserted by the assessor. Distinct source names do not prove independence.
   The medium-confidence two-source rule is a provisional pilot operationalization needing review.
3. **Scope:** N/A approvals are recorded strings, not verified identities. The harness does not
   determine whether workload roles or provider inheritance make a criterion applicable.
4. **Evidence freshness:** a supplied validity date is checked; acceptable duration and material
   changes need a justified assessor decision. No arbitrary universal annual-evidence expiry is imposed.
5. **Risk calibration:** the ordinal matrix is consistent but impact/likelihood anchors, fairness
   measures, credible scenarios and client materiality still need independently rated pilot cases.
6. **Real authorization:** trusted flags replace IAM, policy services, cryptographic approval,
   atomic replay prevention, cumulative budget reservation and external-state reconciliation.
   Sequential consumed-token rejection is tested; concurrent exactly-once dispatch is not proven.
7. **Attestation/history:** hashes identify the local release; signed results and append-only
   storage, evidence disposition, permissions and deployed-version parity are not implemented.
8. **Crosswalks:** synthetic conditions only. No NIST, AISVS, OWASP or legal coverage is newly validated.
9. **Schema:** runtime validates the published closed JSON Schema through a standard-library helper
   limited to its declared keywords, with canonical dates and additional semantic checks. Review-derived
   valid/invalid cases exercise compatibility. It is not a general-purpose third-party validator;
   other consumers still need compatibility testing, including strict integer handling.

## Corrective pass status

The owner accepted the prior hold recommendation and authorized this local corrective pass.
R1 (input shape), R2 (parameter envelope), R3 (result linkage), R4 (provenance contradiction)
and R5 (test activity) have targeted regression cases in `tests/test_corrections.py`.
The clear AC-6.1 qualifier omission was also corrected. This does not mark the broader
semantic or operational gates complete, or revise the original independent review votes.
Current draft version is 2.0.0-pilot.2; the prior snapshot remains in git at e48090b.

## Recommended next gate

Review a small set of genuinely ambiguous cases independently from technical feasibility,
security/assessment validity and business/operational perspectives. Resolve material dissent
and accept the contract before integrating with the platform or publishing. Multiple-agent
review requires explicit authorization. This pilot does not establish external professional assurance.
