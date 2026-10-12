"""Strict draft outcome evaluator. It does not inspect real evidence artifacts."""
import argparse
import hashlib
import json
import copy
from datetime import date
from pathlib import Path
from schema_validation import canonical_date, validate

ROOT = Path(__file__).resolve().parent
STATES = {'pass', 'fail', 'unknown', 'not-tested'}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def assessment_digest(data):
    """Pilot-specific canonical JSON binding; not a digital signature."""
    text=json.dumps(data,sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False)
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def obj(value, required, optional=()):
    if not isinstance(value, dict) or set(value) - set(required) - set(optional) or set(required) - set(value):
        raise ValueError('Missing, unknown or invalid object fields')


def string(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Expected nonempty string')


def unique(values):
    if not isinstance(values, list) or any(not isinstance(v, str) or not v.strip() for v in values) or len(values) != len(set(values)):
        raise ValueError('Expected unique string list')


def aggregate(states, unresolved=False):
    if not states:
        return 'not-applicable' if not unresolved else 'unknown'
    if 'fail' in states:
        return 'partial' if 'pass' in states else 'fail'
    if unresolved or 'unknown' in states:
        return 'unknown'
    if 'not-tested' in states:
        return 'not-tested'
    return 'pass'


def load_release(root=ROOT):
    manifest = json.loads((root / 'manifest.json').read_text())
    if manifest['schema_version'] != '2' or manifest['status'] != 'draft' or manifest['evaluator_version'] != 'pilot.2':
        raise ValueError('Unsupported release')
    for name, expected in manifest['files'].items():
        if Path(name).name != name or digest(root / name) != expected:
            raise ValueError(f'Release component missing or changed: {name}')
    catalog = json.loads((root / 'catalog.json').read_text())
    if catalog['methodology_version'] != manifest['methodology_version']:
        raise ValueError('Release version mismatch')
    return catalog, digest(root / 'manifest.json')


def evaluate(data, root=ROOT):
    catalog, manifest_hash = load_release(root)
    validate(data,json.loads((root/'assessment.schema.json').read_text()))
    data=copy.deepcopy(data)
    input_hash=assessment_digest(data)
    obj(data, ['assessment_id', 'manifest_sha256', 'as_of', 'profile', 'evidence', 'observations'], ['mappings', 'maturity_narratives'])
    string(data['assessment_id'])
    if data['manifest_sha256'] != manifest_hash:
        raise ValueError('Assessment not pinned to this release')
    today = canonical_date(data['as_of'])
    profile = data['profile']
    obj(profile, ['id', 'control_ids', 'scope_kind'])
    string(profile['id']); unique(profile['control_ids'])
    controls = {c['id']: c for c in catalog['controls']}
    selected = profile['control_ids']
    if not set(selected) <= controls.keys():
        raise ValueError('Unknown profile controls')
    if profile['scope_kind'] not in ['full-draft-baseline', 'synthetic-subset']:
        raise ValueError('Unsupported profile type')
    if profile['scope_kind'] == 'full-draft-baseline' and set(selected) != controls.keys():
        raise ValueError('Full baseline profile omits controls')
    if not isinstance(data['evidence'], list) or not isinstance(data['observations'], list):
        raise ValueError('Expected evidence/observation lists')
    evidence = {}
    for e in data['evidence']:
        obj(e, ['id', 'origin', 'source', 'provenance', 'collected_at', 'valid_until', 'confidence', 'coverage', 'sufficient', 'available'], ['inheritance'])
        for k in ['id', 'source', 'provenance']: string(e[k])
        unique(e['coverage'])
        if e['id'] in evidence or e['confidence'] not in ['high', 'medium', 'low'] or e['origin'] not in ['direct', 'inherited', 'mixed']:
            raise ValueError('Invalid/duplicate evidence')
        if type(e['sufficient']) is not bool or type(e['available']) is not bool:
            raise ValueError('Evidence flags must be boolean')
        collected, expires = date.fromisoformat(e['collected_at']), date.fromisoformat(e['valid_until'])
        if collected > today or expires < collected:
            raise ValueError('Invalid evidence dates')
        if e['origin'] != 'direct' or 'inheritance' in e:
            inherited = e.get('inheritance')
            obj(inherited, ['scope_verified', 'period_verified', 'responsibility_verified'])
            if any(type(v) is not bool for v in inherited.values()): raise ValueError('Invalid inheritance checks')
        evidence[e['id']] = e
    expected = {r['id']: c['id'] for k in selected for c in [controls[k]] for r in c['criteria']}
    observations = {}
    for o in data['observations']:
        obj(o, ['criterion_id', 'applicability', 'state', 'evidence_ids', 'test_activity'], ['na', 'reason', 'execution'])
        key = o['criterion_id']
        if key not in expected or key in observations:
            raise ValueError('Unknown or duplicate observation')
        if o['applicability'] not in ['applicable', 'not-applicable', 'unresolved'] or o['state'] not in STATES:
            raise ValueError('Invalid applicability/state; partial is parent-only')
        if o['test_activity']=='not-performed' and ('execution' in o or o['state']!='not-tested'):
            raise ValueError('Unperformed procedure cannot claim execution or a tested state')
        if o['state']=='not-tested' and o['test_activity']!='not-performed':
            raise ValueError('Not-tested requires confirmed nonperformance')
        unique(o['evidence_ids'])
        if not set(o['evidence_ids']) <= evidence.keys():
            raise ValueError('Dangling evidence reference')
        if o['applicability'] == 'not-applicable':
            obj(o.get('na'), ['rationale', 'owner_approval', 'assessor_approval'])
            for v in o['na'].values(): string(v)
        elif 'na' in o: raise ValueError('N/A approval attached to applicable criterion')
        if 'execution' in o:
            x=o['execution']
            obj(x, ['procedure_id', 'scope', 'system_version', 'population_size', 'sample_ids', 'selection_method', 'period_start', 'period_end', 'performed_at', 'assessor', 'observations', 'limitations'])
            for k in ['scope','system_version','selection_method','assessor','observations']: string(x[k])
            if not isinstance(x['limitations'], str): raise ValueError('Limitations must be explicit text')
            if x['procedure_id'] != f'VP-{expected[key]}': raise ValueError('Wrong procedure binding')
            unique(x['sample_ids'])
            if type(x['population_size']) is not int or x['population_size'] < 1 or not x['sample_ids'] or len(x['sample_ids']) > x['population_size']:
                raise ValueError('Invalid execution population/sample')
            start,end,performed=[date.fromisoformat(x[k]) for k in ['period_start','period_end','performed_at']]
            if not start <= end <= performed <= today: raise ValueError('Invalid procedure dates')
        observations[key] = o
    evaluated = {}
    counts = {'mandatory': {}, 'advisory': {}}
    parent_results = {}
    mandatory_fail, uncertainty, mandatory_applicable = False, False, 0
    for key, parent in expected.items():
        o = observations.get(key, {'applicability': 'unresolved', 'state': 'unknown', 'evidence_ids': [], 'test_activity': 'undetermined'})
        app, state = o['applicability'], o['state']
        reasons = []
        if app == 'not-applicable':
            state = 'not-applicable'
        elif app == 'unresolved':
            # A violation cannot conclusively fail a requirement whose scope is unresolved.
            state = 'unknown'; reasons.append('Applicability unresolved')
        elif o['test_activity']=='not-performed':
            state='not-tested'; reasons.append('Procedure confirmed unperformed')
        elif o['test_activity']!='performed':
            state='unknown'; reasons.append('Procedure attempted/incomplete or activity undetermined')
        elif state == 'pass':
            good = [evidence[k] for k in o['evidence_ids'] if evidence[k]['available'] and evidence[k]['sufficient'] and key in evidence[k]['coverage'] and date.fromisoformat(evidence[k]['valid_until']) >= today and (evidence[k]['origin'] == 'direct' or all(evidence[k]['inheritance'].values()))]
            high = any(e['confidence'] == 'high' for e in good)
            # Distinct source labels are only a claimed corroboration signal, not proof of independence.
            medium = len({e['source'] for e in good if e['confidence'] == 'medium'}) >= 2
            if not (high or medium) or 'execution' not in o:
                state = 'unknown'; reasons.append('Pass lacks sufficient current, scoped evidence or corroboration')
        elif state == 'fail':
            violation = [evidence[k] for k in o['evidence_ids'] if evidence[k]['available'] and evidence[k]['sufficient'] and key in evidence[k]['coverage'] and date.fromisoformat(evidence[k]['valid_until']) >= today and evidence[k]['confidence'] in ['high', 'medium'] and (evidence[k]['origin'] == 'direct' or all(evidence[k]['inheritance'].values()))]
            if not violation or 'execution' not in o:
                state = 'unknown'; reasons.append('Failure lacks supported violation evidence')
        evaluated[key] = {'applicability': app, 'state': state, 'reasons': reasons}
        required = controls[parent]['normative_level'] == 'SHALL'
        bucket = counts['mandatory' if required else 'advisory']
        bucket[state] = bucket.get(state, 0) + 1
        if required:
            mandatory_fail |= state == 'fail'
            uncertainty |= state in ['unknown', 'not-tested']
            mandatory_applicable += app == 'applicable'
    for parent in selected:
        children = [evaluated[r['id']] for r in controls[parent]['criteria']]
        states = [x['state'] for x in children if x['applicability'] != 'not-applicable']
        parent_results[parent] = aggregate(states, any(x['applicability'] == 'unresolved' for x in children))
    overall = 'not-conformant' if mandatory_fail else 'indeterminate' if uncertainty else 'no-applicable-mandatory-requirements' if not mandatory_applicable else 'conformant-to-declared-draft-profile'
    mapping_results = {}
    for mapping in data.get('mappings', []):
        obj(mapping, ['target_id', 'alternatives', 'evidence_delta_ids'])
        target = mapping['target_id']
        if not isinstance(target, str) or not target.startswith('synthetic:') or not target[len('synthetic:'):].strip() or target in mapping_results:
            raise ValueError('Only unique synthetic mappings are supported')
        if not isinstance(mapping['alternatives'], list) or not mapping['alternatives']:
            raise ValueError('Mapping needs OR alternatives')
        paths = []
        for path in mapping['alternatives']:
            unique(path)
            if not path or not set(path) <= evaluated.keys(): raise ValueError('Invalid AND path')
            values = [evaluated[k]['state'] for k in path]
            paths.append('supported' if all(v == 'pass' for v in values) else 'not-supported' if 'fail' in values else 'insufficient-evidence')
        unique(mapping['evidence_delta_ids'])
        if not set(mapping['evidence_delta_ids']) <= evidence.keys(): raise ValueError('Unknown mapping evidence delta')
        deltas = [evidence[k] for k in mapping['evidence_delta_ids']]
        delta_good = all(e['available'] and e['sufficient'] and e['confidence'] == 'high' and target in e['coverage'] and date.fromisoformat(e['valid_until']) >= today and (e['origin'] == 'direct' or all(e['inheritance'].values())) for e in deltas)
        mapping_results[target] = 'insufficient-evidence' if not delta_good else 'supported' if 'supported' in paths else 'insufficient-evidence' if 'insufficient-evidence' in paths else 'not-supported'
    narratives = data.get('maturity_narratives', {})
    if not isinstance(narratives, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k,v in narratives.items()):
        raise ValueError('Maturity must be narrative text')
    if not set(narratives) <= {controls[k]['domain_id'] for k in selected}:
        raise ValueError('Narrative for unassessed/unknown domain')
    reconciliation = sorted({controls[k]['domain_id'] for k,v in parent_results.items() if v in ['fail','partial']})
    decision_records={}
    for key in evaluated:
        o=observations.get(key)
        decision_records[key]={'submitted_state':o['state'] if o else None,
                              'test_activity':o['test_activity'] if o else 'undetermined',
                              'evidence_ids':o['evidence_ids'] if o else [],
                              'na':o.get('na') if o else None,
                              'reason':o.get('reason','') if o else 'Observation missing',
                              'execution':{k:v for k,v in o.get('execution',{}).items() if k!='observations'} if o else {}}
    evidence_index={key:{k:e[k] for k in ['id','origin','collected_at','valid_until','confidence','coverage','sufficient','available']} for key,e in evidence.items()}
    return {'assessment_id': data['assessment_id'], 'manifest_sha256': manifest_hash,
            'assessment_input_sha256':input_hash, 'input_binding_format':'pilot-json-sortkeys-ascii-v1',
            'as_of':data['as_of'], 'decision_records':decision_records, 'evidence_index':evidence_index,
            'status': 'draft-pilot-result', 'profile': profile, 'overall': overall,
            'criteria': evaluated, 'parents': parent_results, 'counts': counts,
            'mapping_outcomes': mapping_results, 'maturity_narratives': narratives,
            'maturity_reconciliation_required_for_domains': reconciliation,
            'limitations': ['Synthetic subset results are not full baseline conformance.', 'Evidence sufficiency/provenance are assessor assertions, not artifact validation.', 'No real framework conformance, production approval enforcement or numeric maturity score.']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('assessment', type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(evaluate(json.loads(args.assessment.read_text())), indent=2, sort_keys=True))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(2, f'Invalid assessment/release: {exc}\n')
