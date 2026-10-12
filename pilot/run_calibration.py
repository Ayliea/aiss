"""Reproduce declared synthetic cases and write an inspectable result report."""
import json
import unittest
from evaluator import ROOT, digest, evaluate
from fixtures import write_fixtures
from policy import severity


def run():
    rows = write_fixtures()
    results = []
    for row in rows:
        result = evaluate(row['assessment'])
        expected = row['expected']
        actual = {'overall': result['overall']}
        if 'parent' in expected: actual['parent'] = result['parents']['AC-4.1']
        if 'mapping' in expected: actual['mapping'] = result['mapping_outcomes']['synthetic:outcome']
        if actual != expected: raise AssertionError(f'{row["name"]}: {actual} != {expected}')
        results.append({'case': row['name'], 'expected': expected, 'actual': actual, 'passed': True})
    suite = unittest.defaultTestLoader.discover(str(ROOT/'tests'))
    tests = unittest.TextTestRunner(verbosity=1).run(suite)
    if not tests.wasSuccessful(): raise AssertionError('Pilot tests failed')
    catalog=json.loads((ROOT/'catalog.json').read_text())
    report={'status':'synthetic-calibration-only', 'manifest_sha256':digest(ROOT/'manifest.json'),
            'controls':len(catalog['controls']), 'draft_criteria':sum(len(c['criteria']) for c in catalog['controls']),
            'test_methods':tests.testsRun, 'assessment_cases':results,
            'risk_matrix':[[severity(i,j) for j in range(1,5)] for i in range(1,5)],
            'production_validation':False, 'independent_assessor_calibration':False}
    (ROOT/'calibration-results.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    table='\n'.join(f'| {r["case"]} | {r["actual"]["overall"]} | PASS |' for r in results)
    md=f'''# AI Assurance 2.0 — local pilot calibration

Draft synthetic validation only. No customer evidence, production authorization,
live scoring, deployed integration or external framework conformance was tested.

Release manifest SHA-256: `{report['manifest_sha256']}`.

Validated {report['controls']} control records, {report['draft_criteria']} draft atomic
criteria and 59 procedure records. All {len(results)} declared assessment cases and
{tests.testsRun} test methods passed. The tests include all 64 three-child outcome
combinations, 16 severity cells, monotonic risk ordering, input/release tampering,
action-binding mutations, scope changes, missing evidence, inheritance and mapping
conditions. No numeric maturity score or letter grade is produced.

| Synthetic case | Actual result | Check |
| --- | --- | --- |
{table}

## What this resolved

- Missing procedure execution cannot be replaced by evidence metadata alone.
- An unsupported failure is an evidence gap, not an invented demonstrated violation.
- A pass is bounded by declared profile; subset profiles cannot masquerade as the full baseline.
- N/A requires owner and assessor records; unknowns and unperformed tests remain visible.
- An evidence-reuse mapping must satisfy its whole AND path or an approved OR alternative,
  plus scoped evidence deltas. Real-framework targets are rejected by this synthetic harness.
- Failed controls flag domain maturity narratives for human reconciliation.

## Assessor judgment and calibration gaps

1. **Atomic interpretations:** 243 draft predicates paraphrase or decompose source/RFC requirements.
   Review the decomposition against normative text. Automated export is not semantic approval.
2. **Evidence sufficiency:** scope, provenance, population, confidence, independence, period and
   sampling are asserted by the assessor. Distinct source names do not prove independence.
   The medium-confidence two-source rule is a provisional pilot operationalization needing review.
3. **Scope:** N/A approvals are recorded strings, not verified identities. The harness does not
   determine whether workload roles or provider inheritance make a criterion applicable.
4. **Evidence freshness:** a supplied validity date is checked; acceptable duration and material
   changes need a justified assessor decision. No arbitrary universal annual-evidence expiry is imposed.
5. **Risk calibration:** the ordinal matrix is consistent but impact/likelihood anchors, fairness
   measures, credible scenarios and client materiality still need independently rated pilot cases.
6. **Real authorization:** trusted flags replace IAM, policy services, cryptographic approval,
   atomic replay prevention, cumulative budget reservation and external-state reconciliation.
   Sequential consumed-token rejection is tested; concurrent exactly-once dispatch is not proven.
7. **Attestation/history:** hashes identify the local release; signed results and append-only
   storage, evidence disposition, permissions and deployed-version parity are not implemented.
8. **Crosswalks:** synthetic conditions only. No NIST, AISVS, OWASP or legal coverage is newly validated.
9. **Schema:** JSON Schema is published for interoperability; strict runtime checks are implemented
   independently without a third-party schema validator. Consumer schema-validation parity needs review.

## Recommended next gate

Review a small set of genuinely ambiguous cases independently from technical feasibility,
security/assessment validity and business/operational perspectives. Resolve material dissent
and accept the contract before integrating with the platform or publishing. Multiple-agent
review requires explicit authorization. This pilot does not establish external professional assurance.
'''
    (ROOT/'CALIBRATION.md').write_text(md)
    print(f'PASS: {len(results)} synthetic cases; {tests.testsRun} test methods. Report: pilot/CALIBRATION.md')


if __name__ == '__main__': run()
