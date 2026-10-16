# Evaluation record

**Draft restricted working paper template.** One record per defined case/configuration. This is a companion record, not a pilot.2 schema extension. Never treat template defaults as execution evidence.

## Plan fixed before execution

- Test ID / linked failure-path case / record revision: [values]
- Claim and applicable control/criterion, or out-of-core observation: [reference and rationale]
- Threat/failure mode and boundary under test: [values]
- Written authorization / approved environment, targets and synthetic resources: [references]
- Test status: **planned** [change only with evidence: executed / attempted / not performed / undetermined]
- Model, version, platform, access tier, safeguards, tools and settings: [values or unknowns]
- Data/corpus version / sample IDs / selection rationale / population / repetitions: [values]
- Normal-task baseline and negative variants: [values]
- Expected allowed/denied actions, resulting state and acceptance thresholds: [predeclared values]
- Isolation/reset, non-delivering sink, stop conditions and incident owner: [values]

## Execution and observations

- Assessor / timestamps with time zone / procedure revision: [values]
- Actual configuration, deviations and approvals: [values]
- Requested action and exact arguments / effective destination: [redacted values or restricted references]
- Provider safeguard result / application enforcement result: [separate observations; unknown if unavailable]
- Independent action, denial, egress and resulting-state evidence IDs: [references, including gaps]
- Monitor detection / stop / in-flight cancellation / reconciliation: [separate results and latency where measured]
- Agent narrative vs independently observed behavior: [distinguish assertion and evidence]
- Counterevidence, missing coverage and evidence-access constraints: [values]

## Decision

- Claim: [supported / partially supported / insufficient evidence / contradicted, with rationale]
- Pilot criterion outcome, only if applicable: [use existing outcome and test_activity rules; do not infer from this document alone]
- Attack successes / attempted attacks; legitimate completions / legitimate trials; false blocks / legitimate trials: [counts, denominators, exclusions and uncertainty]
- Repeatability and generalization limits: [corpus/configuration-specific; no blanket security claim]
- Finding and validation status: [open / change supplied, not validated / validated within stated test scope / client-accepted risk]
- Evidence cutoff, material changes and retest trigger: [values]
- Assessor/reviewer decision and date: [actual review; no invented independent reviewer]
