# Security Policy

This policy covers security concerns about the **AISS standard itself** — that is, controls that are wrong, dangerous, or misleading in a way that could create risk if followed literally. It does not cover security incidents in your own systems; those follow your organization's incident-response procedures (see control AC-7).

## Reporting a security concern about AISS

Please disclose privately before public discussion.

- **Email:** security@ayliea.com
- **Subject prefix:** `[AISS Security]`
- **Encrypted reports welcome.** Request a PGP key in your initial message if needed.

## What to include

- Which control or section is implicated (e.g., `AC-6.3`, `spec/aiss-v1.2.json`)
- The current language
- The concrete harm a literal reading would enable, with a worked example if possible
- Suggested mitigation (rewording, deletion, scope-narrowing)
- Your preferred attribution in the eventual fix

## What we commit to

| Step | SLA |
|---|---|
| Acknowledge receipt | 5 business days |
| Initial assessment (in-scope / out-of-scope / declined) | 14 days |
| Remediation plan or coordinated disclosure timeline | 30 days |
| Public disclosure (after fix or coordinated date) | 90 days from initial report |

## Scope

**In scope:**

- Control wording that, if followed literally, would create a vulnerability or compliance gap
- Cross-framework mapping that misrepresents an external standard's actual requirement
- Methodology guidance (scoring, weighting, maturity model) with a logical flaw

**Out of scope:**

- Disagreements about whether a control is the *best* practice — those are RFCs
- Subjective rewording preferences — those are clarifications
- Security issues in your own AI systems or environment — those follow AC-7
- Security issues in Ayliea's commercial assessment platform — report to security@ayliea.com with subject `[Platform Security]`

## Coordinated disclosure

When a reporter requests coordinated disclosure, we will agree on a public-disclosure date and not disclose before it. If we cannot agree, the default is 90 days from initial report. Reporters who follow this policy will be credited (unless they request anonymity) in the corresponding `CHANGELOG.md` entry.

## Acknowledgements

A list of credited reporters is maintained in `CHANGELOG.md` against the corresponding patch release.
