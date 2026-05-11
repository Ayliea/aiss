---
rfc: 0000
title: <descriptive title>
author: <GitHub handle> (<optional full name + affiliation>)
status: Draft
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
discussion: <link to originating issue>
target_version: <e.g., 1.3 or 2.0>
---

# RFC 0000 — <title>

## Summary

One paragraph. Plain language. If a reader stops after this section, they should know what is being proposed and why it matters.

## Motivation

Why does AISS need this change? Reference authoritative sources where applicable — published standards, regulatory text, peer-reviewed research, documented production incidents, or community-confirmed coverage gaps. This is the strongest section of any RFC; weak motivation is the most common reason an RFC is declined.

## Detailed design

The concrete proposal, in enough detail that a future maintainer could implement it from this document alone. For control changes, include:

- Proposed control text (verbatim, as it will appear in the spec)
- Assigned control ID(s)
- Updates required in `spec/aiss-v*.json`
- Updates required in `domains/AC-N-*.md`
- Crosswalk updates required in `crosswalks/*.md`
- MITRE ATLAS / OWASP / NIST mappings (with citations)

For methodology changes, include the algorithm change in formal terms (math, pseudocode, or both) plus a worked example showing the old and new outputs.

## Drawbacks and trade-offs

What does this proposal cost? Be honest. Common costs:

- Backwards-incompatibility risk (existing assessments become harder to interpret)
- Scope creep (AISS becomes harder to learn)
- Implementation burden on the Ayliea platform and other downstream consumers
- Disagreement with peer frameworks (NIST AI RMF says X, this proposal says Y)

## Alternatives considered

What else was on the table? Why is this proposal preferred? "We didn't consider any" is rarely a credible answer — explore the design space and explain the trade-offs.

## Adoption and migration

If this RFC is adopted, what does the rollout look like?

- Is it additive (no migration needed) or breaking?
- Do existing assessments scored against the previous version need to be re-scored, annotated, or simply preserved via the version snapshot system?
- Will downstream consumers (the Ayliea platform, third-party forks) need to update?

## Unresolved questions

What is intentionally left open by this RFC? List them so future RFCs can pick them up.

## References

- Authoritative source URLs cited above (full URLs, not summaries)
- Related RFCs (link by number)
- Related issues and PRs
