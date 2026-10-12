"""Pure decision fixtures, not a production authorization/approval service."""
import hashlib
import json
from datetime import datetime, timezone

MATRIX = (
    ('Low', 'Low', 'Medium', 'High'),
    ('Low', 'Medium', 'High', 'High'),
    ('Medium', 'Medium', 'High', 'Critical'),
    ('Medium', 'High', 'Critical', 'Critical'),
)


def severity(likelihood, impact):
    for value in [likelihood, impact]:
        if value is not None and (type(value) is not int or value not in range(1, 5)):
            raise ValueError('Ratings must be 1–4 or unresolved (null)')
    return 'unrated' if likelihood is None or impact is None else MATRIX[likelihood - 1][impact - 1]


def classify(action):
    if action['effect'] not in {'prepare', 'read', 'write'}:
        return 'AX'
    keys = ['prohibited', 'rights_sensitive', 'external_disclosure', 'privileged', 'financial', 'destructive', 'production', 'external_persistence', 'downstream_trigger', 'reversible']
    if any(type(action.get(k)) is not bool for k in keys):
        raise ValueError('Classification flags must be explicit booleans')
    if action['prohibited']: return 'AX'
    if action['rights_sensitive']: return 'A4'
    if any(action[k] for k in ['external_disclosure', 'privileged', 'financial', 'destructive', 'production', 'external_persistence', 'downstream_trigger']): return 'A3'
    if action['effect'] == 'prepare': return 'A0'
    if action['effect'] == 'read': return 'A1'
    return 'A2' if action['reversible'] else 'A3'


def action_binding(action):
    # Bind the entire validated decision record, including actor, scope, tool,
    # resource/version, destination, currency, amount, policy and side effects.
    encoded = json.dumps(action, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False)
    return hashlib.sha256(encoded.encode()).hexdigest()


def instant(value):
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None: raise ValueError('Timezone required')
    return result.astimezone(timezone.utc)


def bounded_parameters(parameters, rules):
    """Closed scalar envelope. Composite tool schemas need a separate adapter."""
    if not isinstance(rules,dict) or set(parameters)!=set(rules): return False
    types={'string':lambda v:isinstance(v,str), 'integer':lambda v:type(v) is int,
           'boolean':lambda v:type(v) is bool}
    for key,value in parameters.items():
        rule=rules[key]
        if not isinstance(key,str) or not isinstance(rule,dict) or set(rule)-{'type','enum','minimum','maximum'}:
            return False
        kind=rule.get('type')
        if kind not in types or not types[kind](value): return False
        if 'enum' in rule:
            allowed=rule['enum']
            if not isinstance(allowed,list) or not allowed or any(not types[kind](x) for x in allowed) or value not in allowed:
                return False
        elif kind!='integer' or not {'minimum','maximum'}<=rule.keys():
            return False  # No implicitly unbounded selectors or values.
        if 'minimum' in rule or 'maximum' in rule:
            if kind!='integer' or type(rule.get('minimum')) is not int or type(rule.get('maximum')) is not int:
                return False
            if not rule['minimum']<=value<=rule['maximum']: return False
    return True


def authorize(action, context, approval=None, grant=None):
    """Trusted context assertions stand in for real services, crypto and locking."""
    required = ['principal', 'tenant', 'agent', 'tool_version', 'operation', 'resource', 'resource_version', 'policy_version', 'purpose', 'destination', 'currency']
    for key in required:
        if not isinstance(action.get(key), str) or not action[key]: raise ValueError('Incomplete action binding')
    if type(action.get('cost_minor')) is not int or action['cost_minor'] < 0 or type(action.get('resource_count')) is not int or action['resource_count'] < 1:
        raise ValueError('Invalid amount/count')
    if not isinstance(action.get('currency'), str) or not action['currency']:
        raise ValueError('Currency must be explicit (NONE for nonfinancial action)')
    if not isinstance(action.get('parameters'), dict): raise ValueError('Typed parameters required')
    action_binding(action)  # Reject non-JSON/nonfinite values in all classes.
    cls = classify(action)
    def deny(reason): return {'decision': 'deny', 'class': cls, 'reason': reason}
    if cls in ['AX', 'A4']: return deny('Prohibited/unknown or no accepted sector profile')
    for flag in ['actor_authorized', 'policy_available', 'limits_available']:
        if type(context.get(flag)) is not bool: raise ValueError('Invalid authorization context')
        if not context[flag]: return deny(flag)
    now = instant(context['now'])
    if action['policy_version'] != context['policy_version']:
        return deny('Policy changed')
    if cls == 'A0': return {'decision': 'permit', 'class': cls, 'reason': 'Isolated preparation within asserted authority'}
    if cls in ['A1', 'A2']:
        if not grant: return deny('Bounded preauthorization missing')
        expected = {k: action[k] for k in required}
        if grant.get('binding') != expected or cls not in grant.get('classes', []): return deny('Grant scope mismatch')
        if not bounded_parameters(action['parameters'],grant.get('parameter_rules')):
            return deny('Parameter types/values exceed bounded grant')
        if grant.get('revoked') is not False or instant(grant['expires']) <= now: return deny('Grant expired/revoked')
        for key in ['max_cost_minor', 'max_count', 'used_cost_minor', 'used_count']:
            if type(grant.get(key)) is not int or grant[key] < 0: raise ValueError('Concrete nonnegative grant limits required')
        if grant['used_cost_minor'] + action['cost_minor'] > grant['max_cost_minor'] or grant['used_count'] + action['resource_count'] > grant['max_count']:
            return deny('Cumulative limits exceeded')
        return {'decision': 'permit', 'class': cls, 'reason': 'Scoped bounded grant (reservation not implemented)'}
    if not approval: return deny('Exact-action approval missing')
    if approval.get('binding') != action_binding(action): return deny('Approval binding mismatch')
    if approval.get('revoked') is not False or approval.get('consumed') is not False: return deny('Approval revoked/consumed')
    if context.get('approver_authorized') is not True or context.get('approval_service_available') is not True: return deny('Approver authority/service unavailable')
    if not isinstance(approval.get('id'), str) or not approval['id'] or not isinstance(approval.get('approver'), str) or not approval['approver'] or approval['approver'] == action['agent']:
        return deny('Invalid/self approval')
    if instant(approval['expires']) <= now: return deny('Approval expired')
    return {'decision': 'permit', 'class': cls, 'reason': 'Exact action approved (atomic consumption/dispatch not implemented)'}
