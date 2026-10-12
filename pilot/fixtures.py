"""Declared synthetic calibration inputs and expectations, not client evidence."""
import copy
import json
from pathlib import Path
from evaluator import ROOT, digest


def baseline():
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    control = next(c for c in catalog['controls'] if c['id'] == 'AC-4.1')
    ids = [r['id'] for r in control['criteria']]
    data = {'assessment_id': 'synthetic-pass', 'manifest_sha256': digest(ROOT / 'manifest.json'), 'as_of': '2026-10-06',
            'profile': {'id': 'fixture-access-only', 'control_ids': ['AC-4.1'], 'scope_kind': 'synthetic-subset'},
            'evidence': [{'id': 'ev1', 'origin': 'direct', 'source': 'synthetic-execution-boundary', 'provenance': 'canary test receipt, fictional',
                          'collected_at': '2026-10-06', 'valid_until': '2026-10-07', 'confidence': 'high',
                          'coverage': ids, 'sufficient': True, 'available': True}],
            'observations': [{'criterion_id': key, 'applicability': 'applicable', 'state': 'pass', 'evidence_ids': ['ev1'], 'test_activity':'performed'} for key in ids]}
    for o in data['observations']:
        o['execution'] = dict(procedure_id='VP-AC-4.1', scope='Synthetic fixture resource only', system_version='fixture-v1',
                              population_size=1, sample_ids=['fixture-resource'], selection_method='Full synthetic population',
                              period_start='2026-10-06', period_end='2026-10-06', performed_at='2026-10-06', assessor='fixture-assessor',
                              observations='Declared synthetic observation; not a real system execution', limitations='Synthetic data; no production coverage')
    return data


def cases():
    rows = []
    def case(name, mutate, overall, parent=None):
        data = baseline(); data['assessment_id'] = 'synthetic-' + name
        mutate(data)
        rows.append({'name': name, 'assessment': data, 'expected': {'overall': overall, **({'parent': parent} if parent else {})}})
    conformant = 'conformant-to-declared-draft-profile'
    case('pass', lambda d: None, conformant, 'pass')
    case('mandatory-failure', lambda d: d['observations'][0].update(state='fail'), 'not-conformant', 'partial')
    case('missing-evidence', lambda d: d['observations'][0].update(evidence_ids=[]), 'indeterminate', 'unknown')
    case('low-confidence', lambda d: d['evidence'][0].update(confidence='low'), 'indeterminate', 'unknown')
    case('stale-evidence', lambda d: d['evidence'][0].update(valid_until='2026-10-05', collected_at='2026-10-01'), 'indeterminate', 'unknown')
    case('deleted-evidence', lambda d: d['evidence'][0].update(available=False), 'indeterminate', 'unknown')
    def unperformed(d):
        o=d['observations'][0];o.pop('execution');o.update(state='not-tested', evidence_ids=[],test_activity='not-performed')
    case('unperformed', unperformed, 'indeterminate', 'not-tested')
    case('attempted-without-execution-record', lambda d: (d['observations'][0].pop('execution'),d['observations'][0].update(test_activity='attempted',state='unknown',evidence_ids=[])), 'indeterminate', 'unknown')
    case('undetermined-test-activity', lambda d: d['observations'][0].update(test_activity='undetermined'), 'indeterminate', 'unknown')
    case('unresolved-scope', lambda d: d['observations'][0].update(applicability='unresolved'), 'indeterminate', 'unknown')
    case('missing-observation', lambda d: d['observations'].pop(), 'indeterminate', 'unknown')
    case('missing-execution', lambda d: d['observations'][0].pop('execution'), 'indeterminate', 'unknown')
    def na(d):
        for o in d['observations']:
            o.pop('execution');o.update(applicability='not-applicable', state='not-tested', test_activity='not-performed',evidence_ids=[], na={'rationale': 'Synthetic unused capability, explicit fixture', 'owner_approval': 'fixture-owner', 'assessor_approval': 'fixture-assessor'})
    case('approved-na', na, 'no-applicable-mandatory-requirements', 'not-applicable')
    def inherited(d, valid):
        d['evidence'][0].update(origin='inherited', inheritance={'scope_verified': valid, 'period_verified': True, 'responsibility_verified': True})
    case('inherited-valid', lambda d: inherited(d, True), conformant, 'pass')
    case('inherited-unverified', lambda d: inherited(d, False), 'indeterminate', 'unknown')
    def fail_unknown(d):
        d['observations'][0]['state'] = 'fail'
        d['observations'][1].update(state='unknown', evidence_ids=[])
    case('failure-with-uncertainty', fail_unknown, 'not-conformant', 'partial')
    def medium(d):
        d['evidence'][0]['confidence'] = 'medium'
        second = copy.deepcopy(d['evidence'][0]); second.update(id='ev2', source='independent-synthetic-config')
        d['evidence'].append(second)
        for o in d['observations']: o['evidence_ids'].append('ev2')
    case('corroborated-medium', medium, conformant, 'pass')
    def mapping(d, mode):
        ids = [o['criterion_id'] for o in d['observations']]
        d['observations'][1].update(state='unknown', evidence_ids=[])
        d['mappings'] = [{'target_id': 'synthetic:outcome', 'alternatives': [ids[:2]] if mode == 'and' else [ids[:2], [ids[2]]], 'evidence_delta_ids': []}]
    case('mapping-and', lambda d: mapping(d, 'and'), 'indeterminate', 'unknown')
    rows[-1]['expected']['mapping'] = 'insufficient-evidence'
    case('mapping-or', lambda d: mapping(d, 'or'), 'indeterminate', 'unknown')
    rows[-1]['expected']['mapping'] = 'supported'
    def delta(d):
        d['mappings'] = [{'target_id': 'synthetic:outcome', 'alternatives': [[o['criterion_id'] for o in d['observations']]], 'evidence_delta_ids': ['ev1']}]
        # Existing evidence covers controls, not the additional target-specific duty.
    case('mapping-delta', delta, conformant, 'pass')
    rows[-1]['expected']['mapping'] = 'insufficient-evidence'
    def full(d):
        catalog = json.loads((ROOT / 'catalog.json').read_text())
        d['profile'] = {'id': 'full-synthetic-draft', 'control_ids': [c['id'] for c in catalog['controls']], 'scope_kind': 'full-draft-baseline'}
    case('full-baseline-incomplete', full, 'indeterminate')
    def provenance(d, legal_state):
        catalog=json.loads((ROOT/'catalog.json').read_text())
        c=next(c for c in catalog['controls'] if c['id']=='AC-6.6')
        d['profile']['control_ids']=['AC-6.6'];d['profile']['id']='fixture-provenance-only'
        d['evidence'][0]['coverage']=[r['id'] for r in c['criteria']]
        template=copy.deepcopy(d['observations'][0]);template['execution']['procedure_id']='VP-AC-6.6'
        template['execution']['observations']='Synthetic unsupported machine marking, capability recorded and human-readable fallback present; legal requirement evaluated separately'
        d['observations']=[]
        for r in c['criteria']:
            o=copy.deepcopy(template);o['criterion_id']=r['id']
            if r['id']=='AC-6.6/R06':o['state']=legal_state
            d['observations'].append(o)
    case('provenance-capability-fallback',lambda d:provenance(d,'pass'),conformant)
    case('provenance-unmet-legal-marking',lambda d:provenance(d,'fail'),'not-conformant')
    return rows


def write_fixtures():
    directory = ROOT / 'fixtures'; directory.mkdir(exist_ok=True)
    rows = cases()
    for row in rows:
        (directory / (row['name'] + '.json')).write_text(json.dumps(row['assessment'], indent=2) + '\n')
    (directory / 'expectations.json').write_text(json.dumps({r['name']: r['expected'] for r in rows}, indent=2) + '\n')
    return rows


if __name__ == '__main__':
    print(f'Wrote {len(write_fixtures())} synthetic assessment fixtures')
