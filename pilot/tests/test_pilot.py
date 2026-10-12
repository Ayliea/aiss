import copy
import itertools
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from evaluator import ROOT, aggregate, digest, evaluate, load_release
from fixtures import baseline, cases
from policy import MATRIX, action_binding, authorize, classify, severity


def action():
    return dict(principal='u1', tenant='t1', agent='agent1', tool_version='tool-v1', operation='read',
                resource='record1', resource_version='rev1', policy_version='policy1', purpose='scoped-task',
                destination='internal', parameters={'field': 'title'}, cost_minor=0, currency='NONE', resource_count=1,
                effect='read', prohibited=False, rights_sensitive=False, external_disclosure=False, privileged=False,
                financial=False, destructive=False, production=False, external_persistence=False, downstream_trigger=False, reversible=True)


def context():
    return dict(actor_authorized=True, policy_available=True, limits_available=True, approver_authorized=True,
                approval_service_available=True, now='2026-10-06T16:00:00Z', policy_version='policy1')


def approval(a):
    return dict(id='ap1', approver='reviewer', binding=action_binding(a), expires='2026-10-06T17:00:00Z', revoked=False, consumed=False)


def grant(a):
    keys = ['principal', 'tenant', 'agent', 'tool_version', 'operation', 'resource', 'resource_version', 'policy_version', 'purpose', 'destination', 'currency']
    return dict(binding={k: a[k] for k in keys}, parameter_rules={'field':{'type':'string','enum':['title']}}, classes=['A1', 'A2'], expires='2026-10-06T17:00:00Z', revoked=False,
                max_cost_minor=0, max_count=3, used_cost_minor=0, used_count=0)


class OutcomeTests(unittest.TestCase):
    def test_declared_synthetic_assessments(self):
        for case in cases():
            with self.subTest(case=case['name']):
                result = evaluate(case['assessment'])
                self.assertEqual(result['overall'], case['expected']['overall'])
                if 'parent' in case['expected']: self.assertEqual(result['parents']['AC-4.1'], case['expected']['parent'])
                if 'mapping' in case['expected']: self.assertEqual(result['mapping_outcomes']['synthetic:outcome'], case['expected']['mapping'])
                self.assertNotIn('score', result); self.assertNotIn('grade', result)

    def test_all_parent_state_combinations(self):
        # Failure cannot disappear; uncertainty cannot turn into pass. Permutations invariant.
        for states in itertools.product(['pass','fail','unknown','not-tested'], repeat=3):
            actual = aggregate(states)
            self.assertEqual(actual, aggregate(list(reversed(states))))
            if 'fail' in states: self.assertIn(actual, ['fail','partial'])
            elif 'unknown' in states: self.assertEqual(actual, 'unknown')
            elif 'not-tested' in states: self.assertEqual(actual, 'not-tested')
            else: self.assertEqual(actual, 'pass')
        self.assertEqual(aggregate([]), 'not-applicable')
        self.assertEqual(aggregate(['pass'], True), 'unknown')

    def test_invalid_inputs_do_not_silently_pass(self):
        mutations = [lambda d: d.update(score=100), lambda d: d.update(manifest_sha256='0'*64),
                     lambda d: d['observations'].append(copy.deepcopy(d['observations'][0])),
                     lambda d: d['observations'][0].update(state='partial'),
                     lambda d: d['observations'][0].update(evidence_ids=['missing']),
                     lambda d: d['profile'].update(scope_kind='full-draft-baseline'),
                     lambda d: d['evidence'][0].update(collected_at='2026-10-08'),
                     lambda d: d['evidence'][0].update(sufficient=1),
                     lambda d: d['observations'][0].update(applicability='not-applicable'),
                     lambda d: d['evidence'].append(copy.deepcopy(d['evidence'][0]))]
        for mutate in mutations:
            d=baseline(); mutate(d)
            with self.subTest(data=d), self.assertRaises(ValueError): evaluate(d)

    def test_unsupported_failure_becomes_unknown(self):
        d=baseline(); d['observations'][0].update(state='fail', evidence_ids=[])
        self.assertEqual(evaluate(d)['overall'], 'indeterminate')

    def test_empty_scope_not_conformant(self):
        d=baseline(); d['profile']['control_ids']=[]; d['observations']=[]
        self.assertEqual(evaluate(d)['overall'], 'no-applicable-mandatory-requirements')

    def test_advisory_failure_does_not_fail_mandatory_conformance(self):
        d=baseline(); catalog,_=load_release(); c=next(c for c in catalog['controls'] if c['id']=='AC-5.6')
        d['profile']['control_ids'].append(c['id'])
        for r in c['criteria']:
            d['evidence'][0]['coverage'].append(r['id'])
            x=copy.deepcopy(d['observations'][0]['execution']); x['procedure_id']='VP-AC-5.6'
            d['observations'].append(dict(criterion_id=r['id'], applicability='applicable', state='fail', evidence_ids=['ev1'], test_activity='performed', execution=x))
        result=evaluate(d)
        self.assertEqual(result['overall'], 'conformant-to-declared-draft-profile')
        self.assertEqual(result['parents']['AC-5.6'], 'fail')

    def test_tampered_release_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            for file in ROOT.glob('*'):
                if file.is_file(): shutil.copy(file, root/file.name)
            (root/'catalog.json').write_text('{}')
            with self.assertRaises(ValueError): load_release(root)

    def test_execution_binding_and_maturity_reconciliation(self):
        d=baseline(); d['observations'][0]['execution']['procedure_id']='VP-AC-1.1'
        with self.assertRaises(ValueError): evaluate(d)
        d=baseline(); d['observations'][0]['state']='fail'
        result=evaluate(d)
        self.assertEqual(result['maturity_reconciliation_required_for_domains'],['AC-4'])
        d['maturity_narratives']={'AC-99':'Strong'}
        with self.assertRaises(ValueError): evaluate(d)

    def test_reproducibility_and_criterion_coverage(self):
        data=baseline()
        first=json.dumps(evaluate(data),sort_keys=True)
        second=json.dumps(evaluate(copy.deepcopy(data)),sort_keys=True)
        self.assertEqual(first,second)
        cat,_=load_release(); ids=[r['id'] for c in cat['controls'] for r in c['criteria']]
        self.assertEqual(len(ids),len(set(ids))); self.assertEqual(len(cat['controls']),59)
        procedures=json.loads((ROOT/'procedures.json').read_text())['procedures']
        self.assertEqual(set(ids),{r for p in procedures for r in p['criterion_ids']})


class RiskTests(unittest.TestCase):
    def test_matrix_and_monotonicity(self):
        ranks={'Low':1,'Medium':2,'High':3,'Critical':4}
        for i,j in itertools.product(range(1,5),repeat=2):
            self.assertEqual(severity(i,j),MATRIX[i-1][j-1])
            if i<4: self.assertLessEqual(ranks[severity(i,j)],ranks[severity(i+1,j)])
            if j<4: self.assertLessEqual(ranks[severity(i,j)],ranks[severity(i,j+1)])
        self.assertEqual(severity(None,4),'unrated')
        for invalid in [0,5,True,'3',float('nan')]:
            with self.assertRaises(ValueError): severity(invalid,2)


class ApprovalTests(unittest.TestCase):
    def test_scoped_read_and_write(self):
        a=action(); self.assertEqual(authorize(a,context(),grant=grant(a))['decision'],'permit')
        a['effect']='write'; self.assertEqual(authorize(a,context(),grant=grant(a))['class'],'A2')

    def test_external_read_reclassified(self):
        a=action(); a['external_disclosure']=True
        self.assertEqual(authorize(a,context(),grant=grant(a))['decision'],'deny')
        self.assertEqual(classify(a),'A3')

    def test_exact_action_mutation(self):
        a=action(); a.update(financial=True,effect='write',cost_minor=10000,currency='USD')
        ap=approval(a); self.assertEqual(authorize(a,context(),ap)['decision'],'permit')
        for key,value in [('cost_minor',10100),('currency','EUR'),('destination','other'),('resource_version','rev2'),('tool_version','v2'),('principal','u2'),('operation','delete'),('parameters',{'field':'secret'})]:
            changed=copy.deepcopy(a); changed[key]=value
            with self.subTest(key=key): self.assertEqual(authorize(changed,context(),ap)['decision'],'deny')
        self.assertEqual(action_binding(a),action_binding(dict(reversed(list(a.items())))))

    def test_revocation_replay_and_outages(self):
        a=action(); a['production']=True; ap=approval(a)
        for change in [{'consumed':True},{'revoked':True},{'expires':'2026-10-06T15:00:00Z'},{'approver':'agent1'}]:
            self.assertEqual(authorize(a,context(),dict(ap,**change))['decision'],'deny')
        for key in ['actor_authorized','policy_available','limits_available','approver_authorized','approval_service_available']:
            ctx=context(); ctx[key]=False
            self.assertEqual(authorize(a,ctx,ap)['decision'],'deny')

    def test_composed_effects_and_cumulative_limits(self):
        a=action(); g=grant(a); g['used_count']=3
        self.assertEqual(authorize(a,context(),grant=g)['decision'],'deny')
        for key in ['downstream_trigger','privileged','external_persistence','destructive']:
            changed=copy.deepcopy(a); changed[key]=True
            self.assertEqual(classify(changed),'A3')
        a['rights_sensitive']=True
        self.assertEqual(authorize(a,context(),approval(a))['decision'],'deny')

    def test_scope_field_and_invalid_value_rejection(self):
        a=action(); g=grant(a); a['parameters']['admin']=True
        self.assertEqual(authorize(a,context(),grant=g)['decision'],'deny')
        a=action(); a['resource_count']=True
        with self.assertRaises(ValueError): authorize(a,context(),grant=grant(a))
        a=action(); a['reversible']='yes'
        with self.assertRaises(ValueError): classify(a)


if __name__ == '__main__': unittest.main()
