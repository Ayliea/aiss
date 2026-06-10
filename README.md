# Ayliea AI Security Standard (AISS)

**Version:** 1.3
**Status:** Release Candidate
**Publication Date:** 2026-06
**License:** [CC-BY-4.0](./LICENSE)
**Canonical URL:** https://github.com/Ayliea/aiss

## What is AISS?

A comprehensive control framework for organizational AI security governance, covering 10 domains with 59 sub-controls mapped to normative reference frameworks. Targets mid-market organizations (50-500 employees) deploying generative, predictive, and agentic AI.

AISS is a controls framework purpose-built for organizations deploying generative, predictive, and agentic AI. It complements general-purpose security frameworks (NIST CSF, ISO 27001) with AI-specific controls covering governance, asset management, data protection, access, supply chain, output validation, incident response, monitoring, training, and model security.

## Why open-source the standard?

Most compliance scoring is opaque. Vendors keep their methodology proprietary because that's where their pricing leverage lives. AISS takes the opposite position: **the standard is public, the scoring math is published, and the framework citations are auditable**. Customers and their auditors can reproduce any AISS score using only this document and the answers an organization provides.

This transparency is structural — VC-funded competitors structurally cannot publish their scoring because their entire business model depends on opacity.

## How it's structured

- **10 control domains** (AC-1 through AC-10)
- **59 sub-controls** mapped to 11 normative reference frameworks
- **5-level maturity model** (0 Non-Existent → 4 Managed) with explicit conformance thresholds
- **Each sub-control has:** requirement, assessment question, implementation guidance, 5-7 step testing procedure, evidence requirements, framework mappings

## Directory layout

```
aiss/
├── README.md            ← this file
├── LICENSE              ← CC-BY-4.0
├── CHANGELOG.md         ← version history
├── methodology.md       ← scoring math and maturity model
├── governance.md        ← who maintains, how to propose changes, RFC process
├── spec/
│   └── aiss-v1.3.json   ← machine-readable canonical specification
├── domains/
│   └── AC-N-<slug>.md   ← per-domain pages (10 files)
├── crosswalks/
│   └── <framework>.md   ← reverse mappings to peer frameworks
└── appendices/
    └── ai-service-domains.md  ← curated AI service domain reference
```

The JSON spec at `spec/aiss-v1.3.json` is the canonical source of truth. The markdown files are deterministically regenerated from it by `scripts/export-aiss-spec.ts`.

## Governance

See [governance.md](./governance.md) for maintainers, license, change-proposal process, and security contact.

## Versioning

- **Current:** v1.3 (released 2026-06)
- **Status:** Release Candidate

See [CHANGELOG.md](./CHANGELOG.md) for full version history.

## Using AISS

1. **Self-assessment** — Walk through the 59 sub-controls, score each at a maturity level (0-4), document evidence. Conformance baseline = all applicable SHALL sub-controls at ML2+.
2. **Audit / compliance crosswalk** — Use the per-control framework_mappings to map AISS findings to NIST CSF, ISO 27001, EU AI Act, NIST AI 600-1, or other frameworks an auditor cares about.
3. **Vendor risk assessment** — Send AISS as a self-assessment questionnaire to AI vendors. The standard's specificity makes it easier to compare vendor responses.

The [Ayliea Assess platform](https://ayliea.com) implements AISS as an in-app assessment with automated scoring, recommendations, and evidence collection — but the standard itself is fully usable on its own.

## Contributing

Pull requests, issues, and RFCs welcome. See [governance.md](./governance.md). Security issues should be reported privately to security@ayliea.com.
