# AI Assurance Methodology — local 2.0 pilot

Draft implementation for RFC 0002. This is an experimental calibration harness, not an
adopted standard, certification engine, production integration or deployed
agent authorization service. Existing v1.3 specifications and scoring stay intact.

Current draft: `2.0.0-pilot.2`, evaluator `pilot.2`, assessment schema `2`.
The reviewed pilot.1 remains recoverable at commit `e48090b`. This version intentionally
rejects its old release digest/input contract; no automatic migration or historical
rescore is provided. Reproduce pilot.1 in a separate checkout of that commit.

Run from the repository root with Python 3.11+ (standard library only):

```bash
python3 pilot/build_catalog.py
python3 pilot/fixtures.py
python3 -m unittest discover -s pilot/tests -v
python3 pilot/run_calibration.py
python3 pilot/evaluator.py pilot/fixtures/pass.json
```

`build_catalog.py` reads the pinned v1.3 source and the reviewed local RFC snapshot.
It emits a draft catalog, procedures and release manifest with SHA-256 hashes.
The catalog includes explicitly curated criterion interpretations. They are
provisional atomic IDs and need semantic review before adoption. Generated files
must be reproducible; source hashes block unnoticed input drift.

The evaluator validates the published closed input schema using a standard-library
validator limited to its declared keywords and canonical dates, checks release/catalog/procedure
identity, evaluates evidence sufficiency and aggregates requirement outcomes.
It evaluates the declared profile only. Synthetic subset profiles must never be
presented as full baseline conformance. No aggregate maturity score is emitted.
Evidence sufficiency supplied to the harness is an assessor assertion, not an
automated determination that artifacts are truthful or complete.

Observations explicitly declare `test_activity`: performed, attempted, not-performed
or undetermined. Confirmed nonperformance yields not-tested; attempted/incomplete
review or performed review with missing evidence yields unknown. Missing documentation
alone never establishes nonperformance. Reports carry date, procedure decision metadata,
sampling/period/limitations, evidence references and a canonical exact-input SHA-256.
Retain the original restricted input for reproduction; the digest is not a signature.
Raw evidence/provenance and free-form observation bodies are not copied into reports.

Bounded A1/A2 grants require a complete scalar `parameter_rules` envelope. Strings
and booleans need explicit permitted values; integers need permitted values or minimum/
maximum bounds. Unknown/omitted parameters and unsupported composite schemas are denied.
Currency is bound alongside the resource/operation/purpose. These fixture rules do not
replace a real typed-tool adapter or establish the truth of caller-supplied IAM context.

Risk ratings use the proposed ordinal matrix with uncertainty preserved. The
action-policy helper demonstrates classification and approval decision fixtures;
it cannot prevent real dispatch, make approvals unforgeable, guarantee atomic
consumption or reconcile external actions. Those require a real execution service
and integration tests. Reports explicitly identify these limits.

Files:

- `sources/rfc-0002.md`: published draft proposal snapshot; methodology adoption pending.
- `criteria.py`: draft criterion interpretation per existing control.
- `catalog.json`, `procedures.json`, `manifest.json`: generated contracts.
- `assessment.schema.json`: structural interoperability contract.
- `schema_validation.py`: local supported-keyword validation, with remote references disabled.
- `evaluator.py`, `policy.py`: reference pure functions and CLI.
- `fixtures/`: synthetic assessments, declared expected results.
- `CALIBRATION.md`: reproducible results and unresolved assessor judgments.

The manifest pins the catalog, procedures, criterion interpretation, evaluator,
policy helper, input schema and schema-validation helper. Fixtures and calibration scripts are review/test
assets, not methodology release components. The manifest itself is not signed;
the assessment's expected digest is the trust anchor for this local harness.

No external framework satisfaction is claimed: the crosswalk evaluator accepts
synthetic AND/OR evidence conditions only. Real mappings need source and semantic
validation. Reports cannot authorize risk acceptance, legal conclusions or client
system actions.

Repository publication was authorized on October 12, 2026. Publishing this draft
does not close semantic, evidence, professional-assessor or deployment acceptance
gates. The repository's existing v1.3 specification remains unchanged.
