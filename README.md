# Ayliea AI Security Standard (AISS)

**Version:** 1.2
**Status:** Released
**Publication Date:** 2026-05
**License:** [CC-BY-4.0](./LICENSE)
**Canonical URL:** https://github.com/Ayliea/aiss

## What is AISS?

A comprehensive control framework for organizational AI security governance, covering 10 domains with 56 sub-controls mapped to 11 normative reference frameworks. Targets mid-market organizations (50-500 employees) deploying generative, predictive, and agentic AI.

AISS is a controls framework purpose-built for organizations deploying generative, predictive, and agentic AI. It complements general-purpose security frameworks (NIST CSF, ISO 27001) with AI-specific controls covering governance, asset management, data protection, access, supply chain, output validation, incident response, monitoring, training, and model security.

## Why open-source the standard?

Most compliance scoring is opaque. Vendors keep their methodology proprietary because that is where their pricing leverage lives. AISS takes the opposite position: **the standard is public, the scoring math is published, and the framework citations are auditable**. Customers and their auditors can reproduce any AISS score using only this document and the answers an organization provides.

This transparency is structural — VC-funded competitors structurally cannot publish their scoring because their entire business model depends on opacity.

## How it is structured

- **10 control domains** (AC-1 through AC-10)
- **56 sub-controls** mapped to 11 normative reference frameworks
- **5-level maturity model** with explicit conformance thresholds
- **Each sub-control has:** requirement, assessment question, implementation guidance, 5-7 step testing procedure, evidence requirements, framework mappings

## Directory layout

```
aiss/
├── README.md                ← this file
├── LICENSE                  ← CC-BY-4.0
├── CHANGELOG.md             ← version history
├── CONTRIBUTING.md          ← how to propose changes
├── CODE_OF_CONDUCT.md       ← community standards
├── SECURITY.md              ← private disclosure for issues in the standard
├── methodology.md           ← scoring math and maturity model
├── governance.md            ← maintainers, license, cadence, versioning
├── spec/
│   └── aiss-v1.2.json       ← machine-readable canonical specification
├── domains/
│   └── AC-N-<slug>.md       ← per-domain pages (10 files)
├── crosswalks/
│   ├── <framework>.md       ← reverse mappings to peer frameworks (9 files)
│   ├── healthcare-cyber-insurance.md      ← industry-profile crosswalk (cyber-insurance, healthcare)
│   └── financial-services-cyber-insurance.md  ← industry-profile crosswalk (cyber-insurance, FinServ)
├── appendices/
│   └── ai-service-domains.md
├── rfcs/
│   └── NNNN-<slug>.md       ← Request-for-Comment record
└── .github/
    ├── ISSUE_TEMPLATE/      ← RFC, errata, clarification forms
    └── PULL_REQUEST_TEMPLATE.md
```

The JSON spec at `spec/aiss-v1.2.json` is the canonical source of truth. The markdown narrative files are deterministically regenerated from it.

## Using AISS

1. **Self-assessment** — Walk through the 56 sub-controls, score each at a maturity level, document evidence. Conformance baseline = all applicable SHALL sub-controls at ML2+.
2. **Audit / compliance crosswalk** — Use the per-control framework_mappings to map AISS findings to NIST CSF, ISO 27001, EU AI Act, NIST AI 600-1, or other frameworks an auditor cares about.
3. **Vendor risk assessment** — Send AISS as a self-assessment questionnaire to AI vendors. The standard's specificity makes it easier to compare vendor responses.

The [Ayliea Assess platform](https://ayliea.com) implements AISS as an in-app assessment with automated scoring, recommendations, and evidence collection — but the standard itself is fully usable on its own.

## How to contribute

AISS is developed in the open. Anyone may propose changes — practitioners, auditors, researchers, vendors, regulators.

| You want to | Use this |
|---|---|
| Fix a typo, broken link, or citation error | [Errata issue](https://github.com/Ayliea/aiss/issues/new?template=errata.yml) |
| Disambiguate confusing wording (no semantic change) | [Clarification issue](https://github.com/Ayliea/aiss/issues/new?template=clarification.yml) |
| Propose a new control or modify an existing one | [RFC — Control change](https://github.com/Ayliea/aiss/issues/new?template=rfc-control-change.yml) |
| Add or update a framework crosswalk | [RFC — Crosswalk](https://github.com/Ayliea/aiss/issues/new?template=rfc-crosswalk.yml) |
| Privately report a security issue in the standard | [SECURITY.md](./SECURITY.md) |
| Open-ended question or discuss interpretation | [GitHub Discussions](https://github.com/Ayliea/aiss/discussions) |

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full RFC workflow, versioning rules, attribution policy, and license acceptance.

## Governance

See [governance.md](./governance.md) for maintainers, license, cadence, and versioning. Past design decisions are recorded as RFCs in [`rfcs/`](./rfcs/) — start with [RFC 0001](./rfcs/0001-aiss-v1.2-ratification.md) for the v1.2 ratification record.

## Versioning

- **Current:** v1.2 (released 2026-05)
- **Status:** Released

See [CHANGELOG.md](./CHANGELOG.md) for full version history.
