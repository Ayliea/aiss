"""Review-derived regression cases and independently declared contract cases."""
import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from evaluator import ROOT, assessment_digest, evaluate
from fixtures import baseline
from policy import authorize
from schema_validation import validate
from test_pilot import action,approval,context,grant


class InputContractTests(unittest.TestCase):
    def test_review_schema_invalid_examples_are_rejected(self):
        schema=json.loads((ROOT/'assessment.schema.json').read_text())
        invalid=[
            lambda d:d.update(mappings={}),
            lambda d:d['observations'][0].update(reason={}),
            lambda d:d['evidence'][0].update(inheritance={}),
            lambda d:d['evidence'][0]['coverage'].append(' '),
            lambda d:d.update(as_of='20261006'),
            lambda d:d['evidence'][0].update(collected_at='20261006'),
            lambda d:d['observations'][0]['execution'].update(performed_at='20261006'),
            lambda d:d['observations'][0].update(test_activity=' '),
            lambda d:d['observations'][0].pop('test_activity'),
            lambda d:d.update(mappings=[{'target_id':'synthetic:','alternatives':[[d['observations'][0]['criterion_id']]],'evidence_delta_ids':[]}]),
        ]
        for mutation in invalid:
            d=baseline();mutation(d)
            with self.subTest(mutation=mutation):
                with self.assertRaises(ValueError):validate(d,schema)
                with self.assertRaises(ValueError):evaluate(d)

    def test_valid_optional_fields_and_inheritance(self):
        d=baseline();d['observations'][0]['reason']='Synthetic verified observation'
        d['evidence'][0]['inheritance']={'scope_verified':False,'period_verified':False,'responsibility_verified':False}
        validate(d,json.loads((ROOT/'assessment.schema.json').read_text()))
        self.assertEqual(evaluate(d)['overall'],'conformant-to-declared-draft-profile')

    def test_schema_rejects_unknown_keyword_and_external_ref(self):
        with self.assertRaises(ValueError):validate({}, {'externalMagic':True})
        with self.assertRaises(ValueError):validate({}, {'$ref':'https://example.invalid/schema'})

    def test_canonical_date_and_enum_boundaries(self):
        for value in ['2026-02-30','2026-1-01','2026-W41-2',123,None]:
            d=baseline();d['as_of']=value
            with self.subTest(date=value),self.assertRaises(ValueError):evaluate(d)
        d=baseline();d['mappings']=[{'target_id':'synthetic: ','alternatives':[[d['observations'][0]['criterion_id']]],'evidence_delta_ids':[]}]
        with self.assertRaises(ValueError):evaluate(d)

    def test_old_release_input_is_not_silently_upgraded(self):
        import hashlib,subprocess
        d=baseline();raw=subprocess.check_output(['git','show','e48090b:pilot/manifest.json'],cwd=ROOT.parent)
        old=json.loads(raw)
        self.assertEqual(old['evaluator_version'],'pilot.1')
        d['manifest_sha256']=hashlib.sha256(raw).hexdigest()
        with self.assertRaises(ValueError):evaluate(d)


class ExportLinkageTests(unittest.TestCase):
    def test_material_scope_and_evidence_changes_alter_binding(self):
        base=baseline();original=evaluate(base)
        mutations=[lambda d:d['observations'][0]['execution'].update(scope='Other scope'),
                   lambda d:d['observations'][0]['execution'].update(system_version='Other version'),
                   lambda d:d['observations'][0]['execution'].update(assessor='Other assessor'),
                   lambda d:d['observations'][0]['execution'].update(limitations='A material sampling limitation'),
                   lambda d:d['evidence'][0].update(source='Other source',provenance='Other provenance')]
        for mutate in mutations:
            d=copy.deepcopy(base);mutate(d);new=evaluate(d)
            with self.subTest(mutation=mutate):
                self.assertNotEqual(original,new)
                self.assertNotEqual(original['assessment_input_sha256'],new['assessment_input_sha256'])
        self.assertEqual(original['as_of'],base['as_of'])
        key=base['observations'][0]['criterion_id']
        self.assertEqual(original['decision_records'][key]['execution']['sample_ids'],['fixture-resource'])
        self.assertEqual(original['decision_records'][key]['evidence_ids'],['ev1'])

    def test_binding_stable_for_object_key_order_and_result_has_no_input_alias(self):
        d=baseline();result=evaluate(d);snapshot=copy.deepcopy(result)
        self.assertEqual(assessment_digest(d),assessment_digest(dict(reversed(list(d.items())))))
        self.assertEqual(result['assessment_input_sha256'],assessment_digest(d))
        d['profile']['control_ids'].clear();d['observations'][0]['execution']['scope']='Changed after export'
        self.assertEqual(result,snapshot)

    def test_raw_evidence_and_observation_body_not_exported(self):
        d=baseline();d['evidence'][0]['provenance']='PRIVATE_RAW_BODY';d['observations'][0]['execution']['observations']='PRIVATE_OBSERVATION_BODY'
        output=json.dumps(evaluate(d))
        self.assertNotIn('PRIVATE_RAW_BODY',output);self.assertNotIn('PRIVATE_OBSERVATION_BODY',output)


class ActivityTests(unittest.TestCase):
    def test_confirmed_unperformed_vs_attempted_vs_missing_documentation(self):
        key=baseline()['observations'][0]['criterion_id']
        for activity,submitted,expected in [('not-performed','not-tested','not-tested'),('attempted','unknown','unknown'),('performed','pass','unknown'),('undetermined','pass','unknown')]:
            d=baseline();o=d['observations'][0];o.pop('execution');o.update(test_activity=activity,state=submitted)
            with self.subTest(activity=activity):
                result=evaluate(d)
                self.assertEqual(result['criteria'][key]['state'],expected)
                self.assertEqual(result['overall'],'indeterminate')
        d=baseline();d['observations'][0].update(test_activity='not-performed',state='not-tested')
        with self.assertRaises(ValueError):evaluate(d)  # Contradictory execution record retained.


class ParameterEnvelopeTests(unittest.TestCase):
    def test_changed_selector_and_invalid_values_are_denied(self):
        for value in ['secret',None,True,1,[],{'field':'title'}]:
            a=action();g=grant(a);a['parameters']['field']=value
            with self.subTest(value=value):self.assertEqual(authorize(a,context(),grant=g)['decision'],'deny')
        a=action();g=grant(a);a['parameters'].clear()
        self.assertEqual(authorize(a,context(),grant=g)['decision'],'deny')

    def test_integer_bounds_boolean_confusion_and_currency(self):
        for value,expected in [(1,'permit'),(5,'permit'),(0,'deny'),(6,'deny'),(True,'deny'),(1.0,'deny')]:
            a=action();a['parameters']={'limit':value};g=grant(a)
            g['parameter_rules']={'limit':{'type':'integer','minimum':1,'maximum':5}}
            with self.subTest(value=value):self.assertEqual(authorize(a,context(),grant=g)['decision'],expected)
        a=action();g=grant(a);a['currency']='EUR'
        self.assertEqual(authorize(a,context(),grant=g)['decision'],'deny')

    def test_missing_or_unbounded_rule_is_denied(self):
        for rule in [None,{}, {'field':{'type':'string'}},{'field':{'type':'string','enum':[]}},{'field':{'type':'string','enum':['title'],'unknown':1}}]:
            a=action();g=grant(a);g['parameter_rules']=rule
            with self.subTest(rule=rule):self.assertEqual(authorize(a,context(),grant=g)['decision'],'deny')
        a=action();a['parameters']['field']=float('nan')
        with self.assertRaises(ValueError):authorize(a,context(),grant=grant(a))


class ProcedureSemanticsTests(unittest.TestCase):
    def test_provenance_and_documented_review_qualifier(self):
        catalog=json.loads((ROOT/'catalog.json').read_text());procedures=json.loads((ROOT/'procedures.json').read_text())
        control=next(c for c in catalog['controls'] if c['id']=='AC-6.1')
        self.assertIn('Documented human review',control['criteria'][0]['text'])
        proc=next(p for p in procedures['procedures'] if p['control_id']=='AC-6.6')
        self.assertIn('satisfies that technical fallback criterion',proc['acceptance'])
        self.assertIn('unmet obligation fails',proc['acceptance'])
        self.assertNotIn('Unsupported text/provenance capability is unknown/failed',proc['acceptance'])


if __name__=='__main__':unittest.main()
