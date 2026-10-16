# Ayliea AI Assurance Methodology

**Open methodology for AI security and governance assessments.**

AISS is the historical name and control identifier. The repository currently contains the historical **v1.3 Release Candidate** and a **draft 2.0 pilot**; the name change does not adopt the draft or change historical assessment results.

## Start here

- [Draft methodology pilot](./pilot/README.md): outcome evaluator, assessment contracts, synthetic cases and limitations.
- [Draft assessment working papers](./pilot/assessment-supplement.md): scope, failure-path evaluation and report templates; adoption pending.
- [Calibration results](./pilot/CALIBRATION.md): reproducible checks and remaining acceptance gates.
- [Historical v1.3 catalog](./spec/aiss-v1.3.json): 59 controls across 10 domains.
- [Historical assessment methodology](./methodology.md) and [domain pages](./domains/AC-1-governance-and-policy.md).

## Transparency and limitations

Ayliea publishes its controls, documented assessment approach, proposed mappings and pilot review findings so readers can inspect the assessment basis and propose improvements.

The historical framework mappings are **unvalidated** and must not substantiate framework fulfillment or compliance. Reproducing a numerical v1.3 score requires versioned rubrics, point values, weights and calculation rules that are not fully specified in the public catalog.

The draft pilot is experimental. Synthetic tests establish implementation consistency, not evidence authenticity, assessor calibration, framework conformance, certification, authorization to operate or government readiness. Publication is not methodology adoption.

Evidence may be reused across applicable frameworks, but each target requires its own scope, applicability, verification and acceptance decision. A source-control result does not automatically fulfill another framework's requirement.

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md), [governance.md](./governance.md) and [CHANGELOG.md](./CHANGELOG.md). Existing control IDs remain traceable. The original project material uses [CC-BY-4.0](./LICENSE); external publications retain their own terms.

Report security issues privately to security@ayliea.com.
