# AISS Scoring Methodology

## Maturity model

| Level | Name | Description |
|---|---|---|
| 0 | Non-Existent | No controls exist. The organization has not considered AI-specific security requirements for this area. |
| 1 | Ad Hoc | Informal, reactive, and person-dependent. Some awareness exists but no formal policy, consistent process, or documentation. |
| 2 | Developing | Processes are partially defined and inconsistently applied. Documentation exists but enforcement is incomplete. |
| 3 | Defined | Documented, communicated, and consistently applied across the organization. Controls cover all known AI systems. |
| 4 | Managed | Continuously monitored with metrics-driven improvement. Automated where feasible. Controls adapt to emerging AI risks. |

## Conformance thresholds

- **Baseline:** All applicable SHALL sub-controls assessed at Maturity Level 2 or higher
- **Full:** All applicable SHALL sub-controls at Level 3+, all applicable SHOULD sub-controls at Level 2+

## Applicability scoping

A sub-control MAY be declared Not Applicable (N/A) when the organization can document that the conditions for the control to apply are not present. N/A declarations MUST include written rationale and MUST be reviewed annually.

**Examples of legitimate N/A:**

- AC-10.3 (Model Versioning) and AC-10.4 (Model Integrity Verification) are N/A for organizations that consume only third-party AI APIs without fine-tuning or self-hosting.
- AC-3.6 (Cross-Border Data Transfer) is N/A for organizations that operate in a single legal jurisdiction with no cross-border AI service usage.
- AC-2.6 (AI Development Tool Governance) is N/A for organizations without internal software development teams.
- AC-3.7 (RAG and Vector Store Security) is N/A for organizations that do not operate retrieval-augmented generation (RAG) pipelines or vector stores.
- AC-10.6 (Agentic AI Action Authorization and Guardrails) is N/A for organizations that do not operate agentic AI systems (workflows that invoke tools, call APIs, or take autonomous actions on behalf of the organization or its users).

**Conformance impact:** N/A sub-controls are excluded from both the numerator and denominator of conformance ratios. An organization declaring all SHALL sub-controls in a domain as N/A cannot claim conformance to that domain.

**Scoring impact:** When using AISS for assessment scoring, N/A sub-controls do not affect the score. The Ayliea Assess platform implements this by allowing 'Not applicable' as an answer option that excludes the question from both points-earned and max-points calculations.

## Reproducing a score

Any AISS score should be reproducible by reading the assessment's recorded answers, mapping each to its point value using `spec/aiss-v1.3.json`, computing per-domain weighted averages, and computing the overall weighted average. If your reproduction does not match the platform's displayed score, that is a bug — report it via the RFC channel in [governance.md](./governance.md).
