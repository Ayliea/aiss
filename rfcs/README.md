# RFCs — Requests for Comment

This directory holds the formal record of design decisions for AISS. Every non-trivial change to the standard — new controls, scope changes, scoring methodology, structural refactors, crosswalk introductions — is documented as an RFC.

## Why RFCs?

Open standards live or die on legibility. A practitioner forking AISS in three years should be able to read `rfcs/` and understand *why* the standard looks the way it does — not just *what* it says. That context lives here, in writing, with the authors named and the alternatives weighed.

## Workflow

1. **Propose** — file a [Control change RFC](../.github/ISSUE_TEMPLATE/rfc-control-change.yml) or [Crosswalk RFC](../.github/ISSUE_TEMPLATE/rfc-crosswalk.yml) on the issue tracker. The issue is where discussion happens.
2. **Discuss** — at least 14 days for control / methodology changes; faster for crosswalks and errata.
3. **Decide** — the maintainer marks the issue `status/accepted`, `status/needs-revision`, or `status/declined`.
4. **Write** — accepted RFCs get a file in this directory: `rfcs/NNNN-slug.md`, copied from [`0000-template.md`](./0000-template.md).
5. **Merge** — the RFC document and the corresponding spec/markdown changes ship in the same PR.
6. **Tag** — released in the next minor or patch version per [Semantic Versioning](../CONTRIBUTING.md#versioning).

## Numbering

RFCs are numbered sequentially in the order they are accepted: `0001`, `0002`, `0003`. Numbers are never reused. Rejected or withdrawn RFCs get a number too, with their final status recorded in their frontmatter.

## States

| State | Meaning |
|---|---|
| `Draft` | Proposed; under discussion in the originating issue |
| `Accepted` | Approved by maintainer; PR pending or merged |
| `Declined` | Not adopted; reasoning recorded |
| `Withdrawn` | Author retracted before decision |
| `Superseded` | Replaced by a later RFC (linked in frontmatter) |

## Index

| # | Title | Status | Released in |
|---|---|---|---|
| [0001](./0001-aiss-v1.2-ratification.md) | AISS v1.2 Initial Public Ratification | Accepted (retroactive) | v1.2 |

## Template

Copy [`0000-template.md`](./0000-template.md) when starting a new RFC after acceptance.
