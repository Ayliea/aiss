"""Deterministic export of the pinned draft; no network or live integrations."""
import hashlib
import json
import re
from pathlib import Path
from criteria import CRITERIA

ROOT = Path(__file__).resolve().parent
PINNED = {
    'spec/aiss-v1.3.json': '2601bde5e89d53df8f0c22962b471c369185a3d203506d65f10b121bad91162f',
    'pilot/sources/rfc-0002.md': 'd37f0a2893ed0e40fedffb4c32d5bc150ad8f09a96ca984e371c27b81461461e',
}


def write(name, value):
    (ROOT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def build():
    for relative, digest in PINNED.items():
        if hashlib.sha256((ROOT.parent / relative).read_bytes()).hexdigest() != digest:
            raise ValueError(f'Pinned source drift: {relative}')
    source = json.loads((ROOT.parent / 'spec/aiss-v1.3.json').read_text())
    rfc = (ROOT / 'sources/rfc-0002.md').read_text()
    if set(CRITERIA) != {c['id'] for c in source['controls']}:
        raise ValueError('Criterion catalog must cover exactly the source controls')
    table = rfc.split('### C2. Control-specific checks and decision criteria')[1].split('### C3.')[0]
    rows = {}
    for line in table.splitlines():
        if re.match(r'\| AC-\d+\.\d+ \|', line):
            key, actions, criteria = [c.strip() for c in line.split('|')[1:-1]]
            if key in rows:
                raise ValueError('Duplicate procedure')
            rows[key] = (actions, criteria)
    overrides = {}
    for control in ['AC-4.6', 'AC-6.5', 'AC-10.6']:
        overrides[control] = re.search(re.escape(f'**{control} — proposed replacement requirement:** “') + r'(.*?)”', rfc).group(1)
    for line in rfc.split('### C4. Proposed semantic conflict resolutions')[1].splitlines():
        if re.match(r'\| AC-', line) and '“' in line:
            key = line.split('|')[1].strip()
            proposed = re.search('“(.*?)”', line).group(1)
            overrides[key] = proposed if key in ['AC-8.5', 'AC-6.6'] else next(c['requirement'] for c in source['controls'] if c['id'] == key) + ' ' + proposed
    facets = {}
    for line in rfc.splitlines():
        if re.match(r'\| AC-10\.6/R\d\d \|', line):
            key, normative, procedure = [c.strip() for c in line.split('|')[1:-1]]
            # Earlier candidate table has the normative text; C3 has its test.
            if key not in facets:
                facets[key] = {'id': key, 'text': normative, 'procedure': procedure}
            elif 'SHALL' not in normative:
                facets[key]['procedure'] = normative + ' Pass: ' + procedure
    if len(facets) != 11:
        raise ValueError('Expected eleven proposed agent facets')
    controls, procedures = [], []
    for c in source['controls']:
        key = c['id']
        criteria = [{'id': f'{key}/R{i:02}', 'text': text} for i, text in enumerate(CRITERIA[key], 1)]
        if key == 'AC-10.6':
            criteria = [{'id': 'AC-10.6/INV', 'text': 'Maintain per-agent tool inventory tied to a justified least-privilege use case'}] + [dict(id=f['id'], text=f['text']) for f in facets.values()]
        controls.append({
            'id': key, 'domain_id': c['domain_id'], 'title': c['title'],
            'normative_level': 'SHALL' if key in ['AC-4.6', 'AC-6.5'] else c['normative_level'],
            'requirement': overrides.get(key, c['requirement']),
            'source_requirement': c['requirement'],
            'semantic_change': key in overrides or key == 'AC-10.6',
            'criteria_status': 'draft interpretation — semantic review required',
            'criteria': criteria,
        })
        actions, acceptance = rows[key]
        procedures.append({'id': f'VP-{key}', 'control_id': key,
                           'criterion_ids': [x['id'] for x in criteria],
                           'actions': actions, 'acceptance': acceptance,
                           'shared_contract': 'RFC0002/C1',
                           'execution_fields': ['scope', 'version', 'population', 'sample', 'period', 'provenance', 'observations', 'limitations', 'assessor'],
                           'facets': list(facets.values()) if key == 'AC-10.6' else []})
    catalog = {'schema_version': '2', 'methodology_version': '2.0.0-pilot.2',
               'status': 'draft', 'controls': controls}
    write('catalog.json', catalog)
    write('procedures.json', {'schema_version': '2', 'status': 'draft', 'procedures': procedures})
    manifest = {'schema_version': '2', 'methodology_version': catalog['methodology_version'],
                'status': 'draft', 'evaluator_version': 'pilot.2', 'source_commit': '055f55cceb0c92372178c8d73988c223f806be21',
                'supersedes_pilot_commit': 'e48090b2a09ed6c5a98dd198dde521eb2586a963',
                'source_hashes': PINNED, 'files': {}}
    for name in ['catalog.json', 'procedures.json', 'criteria.py', 'evaluator.py', 'policy.py', 'assessment.schema.json', 'schema_validation.py']:
        manifest['files'][name] = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    write('manifest.json', manifest)
    print(f'Exported {len(controls)} controls, {sum(len(c["criteria"]) for c in controls)} draft criteria and {len(procedures)} procedures')


if __name__ == '__main__':
    build()
