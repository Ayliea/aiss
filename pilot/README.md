# AI Assurance Methodology — local 2.0 pilot

Draft implementation for RFC 0002. This is a local calibration harness, not a
published standard, certification engine, production integration or deployed
agent authorization service. Existing v1.3 specifications and scoring stay intact.

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

The evaluator validates a closed set of inputs, checks release/catalog/procedure
identity, evaluates evidence sufficiency and aggregates requirement outcomes.
It evaluates the declared profile only. Synthetic subset profiles must never be
presented as full baseline conformance. No aggregate maturity score is emitted.
Evidence sufficiency supplied to the harness is an assessor assertion, not an
automated determination that artifacts are truthful or complete.

Risk ratings use the proposed ordinal matrix with uncertainty preserved. The
action-policy helper demonstrates classification and approval decision fixtures;
it cannot prevent real dispatch, make approvals unforgeable, guarantee atomic
consumption or reconcile external actions. Those require a real execution service
and integration tests. Reports explicitly identify these limits.

Files:

- `sources/rfc-0002.md`: private local review snapshot, publication pending.
- `criteria.py`: draft criterion interpretation per existing control.
- `catalog.json`, `procedures.json`, `manifest.json`: generated contracts.
- `assessment.schema.json`: structural interoperability contract.
- `evaluator.py`, `policy.py`: reference pure functions and CLI.
- `fixtures/`: synthetic assessments, declared expected results.
- `CALIBRATION.md`: reproducible results and unresolved assessor judgments.

The manifest pins the catalog, procedures, criterion interpretation, evaluator,
policy helper and input schema. Fixtures and calibration scripts are review/test
assets, not methodology release components. The manifest itself is not signed;
the assessment's expected digest is the trust anchor for this local harness.

No external framework satisfaction is claimed: the crosswalk evaluator accepts
synthetic AND/OR evidence conditions only. Real mappings need source and semantic
validation. Reports cannot authorize risk acceptance, legal conclusions or client
system actions.
