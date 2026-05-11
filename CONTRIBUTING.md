# Contributing to AISS

The Ayliea AI Security Standard is developed in the open under CC-BY-4.0. Anyone may propose changes — practitioners, auditors, researchers, vendors, regulators, and curious readers. This document explains how.

## TL;DR

| You want to | Use this |
|---|---|
| Fix a typo, broken link, or citation error | [Errata issue](https://github.com/Ayliea/aiss/issues/new?template=errata.yml) |
| Disambiguate confusing wording (no semantic change) | [Clarification issue](https://github.com/Ayliea/aiss/issues/new?template=clarification.yml) |
| Propose a new control, modify an existing one, or restructure a domain | [RFC — Control change](https://github.com/Ayliea/aiss/issues/new?template=rfc-control-change.yml) |
| Add or update a framework crosswalk (NIST, ISO, EU AI Act, OWASP, ATLAS, etc.) | [RFC — Crosswalk](https://github.com/Ayliea/aiss/issues/new?template=rfc-crosswalk.yml) |
| Privately report a security issue in the standard itself | See [SECURITY.md](./SECURITY.md) |
| Ask an open-ended question or discuss interpretation | [GitHub Discussions](https://github.com/Ayliea/aiss/discussions) |

## What counts as what

- **Errata** are non-semantic — typos, broken citations, wrong dates, malformed JSON, wording that is unambiguously incorrect (not contested). Errata are fast-tracked and can be opened as direct PRs.
- **Clarifications** reword existing text for clarity without changing intent. They typically resolve as wording PRs.
- **RFCs** (Requests for Comment) cover anything that changes intent — new controls, sub-control splits, scope shifts, scoring methodology, crosswalk additions. RFCs are the contract between contributors and maintainers: nothing semantic ships without one.
- **Security issues in the standard itself** — controls that, if followed literally, would cause harm or create a vulnerability — go through private disclosure. See [SECURITY.md](./SECURITY.md).

## The RFC process

1. **File an RFC issue.** Use the appropriate template above. Provide proposed text, rationale with authoritative source citations, backwards-compatibility analysis, and alternatives considered.

2. **Triage.** The maintainer triages within 5 business days and applies one of:
   - `status/discussion` — open for community input
   - `status/accepted` — ready for a PR
   - `status/needs-revision` — feedback provided, revise and re-open
   - `status/declined` — not adopted, with reasoning

3. **Discussion period.** RFCs for control changes and methodology changes stay open for at least 14 days to gather practitioner feedback. Crosswalks and errata move faster.

4. **PR.** Once accepted, the submitter (or a maintainer) opens a PR that updates:
   - The relevant Markdown narrative (`domains/AC-N-*.md` or `crosswalks/*.md`)
   - The machine-readable spec (`spec/aiss-v*.json`)
   - The `CHANGELOG.md` under `## [Unreleased]`
   - Any deprecation notes if a control was renamed or removed

5. **Merge + version bump.** Accepted PRs merge into `main`. Releases follow [Semantic Versioning](#versioning) (see below). The submitter is credited in the changelog by GitHub handle and (optionally) full name.

6. **Downstream sync.** Ayliea's assessment platform consumes the published standard; merged changes propagate to the next platform release per the `question_published_versions` versioning system, so historical assessments remain valid against the AISS version they were taken under.

## Versioning

AISS follows [Semantic Versioning](https://semver.org/):

| Bump | Triggers |
|---|---|
| **Major (X.0)** | Breaking changes to control IDs, domain structure, or scoring methodology. Existing assessments may not be directly comparable across major versions. |
| **Minor (1.X)** | New controls, expanded guidance, new framework crosswalks, expanded methodology. Existing assessments remain valid; new content is additive. |
| **Patch (1.X.Y)** | Typo fixes, citation corrections, clarification rewordings without semantic change, governance updates. |

The current version is in `spec/aiss-v*.json` and on the latest GitHub release tag.

## Attribution and credit

Contributors are credited in `CHANGELOG.md` by GitHub handle. If you'd like your full name and affiliation in the credit (e.g., "Jane Doe, Acme Corp Security Team"), include it in your RFC issue or PR description. Anonymous and pseudonymous contributions are welcome — we credit by whatever handle you submit under.

## Licensing of contributions

By submitting an issue or PR, you agree that your contribution is licensed under [CC-BY-4.0](./LICENSE), the same license as AISS. This is inbound-equals-outbound: the standard remains permissively licensed end-to-end so any organization can fork, adapt, and redistribute. You retain copyright; you grant the world a CC-BY-4.0 license.

External content (quoted standards, regulatory text, etc.) must be attributed and used compatibly. Quoting normative clauses of standards bodies (NIST, ISO, OWASP, MITRE) for the purpose of cross-referencing falls under fair-use academic citation; reproducing copyrighted control text wholesale does not. When in doubt, paraphrase and cite.

## Code of Conduct

Participation in this project is governed by the [Contributor Covenant Code of Conduct](./CODE_OF_CONDUCT.md). Disrespectful, harassing, or bad-faith behavior is not tolerated. Report concerns to conduct@ayliea.com.

## Maintainer office hours

Ayliea's founder runs open office hours for AISS contributors. Cadence and channel are published on the repository home page. There is no gatekeeping — anyone interested in the methodology is welcome to attend.

## Questions

For open-ended questions about applying AISS to a specific environment, use [GitHub Discussions](https://github.com/Ayliea/aiss/discussions). For commercial use of Ayliea's assessment platform, see [ayliea.com](https://ayliea.com).
