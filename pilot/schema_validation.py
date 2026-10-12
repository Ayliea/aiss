"""Validate the JSON Schema keywords used by this closed pilot contract.

This is not a general-purpose JSON Schema implementation. Unsupported keywords
fail closed; no remote references are fetched. Dates are canonical YYYY-MM-DD.
"""
import re
from datetime import date


def canonical_date(value):
    if not isinstance(value, str) or not re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', value):
        raise ValueError('Expected canonical YYYY-MM-DD date')
    return date.fromisoformat(value)


def validate(value, schema, root=None, path='$'):
    root = schema if root is None else root
    supported = {'$schema','$id','$defs','$ref','title','type','additionalProperties','required','properties','items','uniqueItems','minItems','minLength','minimum','pattern','format','enum','const','allOf','if','then','else','not'}
    if set(schema) - supported:
        raise ValueError(f'{path}: unsupported schema keyword')
    if '$ref' in schema:
        ref=schema['$ref']
        if not ref.startswith('#/'):
            raise ValueError('Only local schema references supported')
        target=root
        for segment in ref[2:].split('/'):
            target=target[segment.replace('~1','/').replace('~0','~')]
        validate(value,target,root,path)
    if 'type' in schema:
        kind=schema['type']
        matches={'object':lambda x:isinstance(x,dict) and all(isinstance(k,str) for k in x),
                 'array':lambda x:isinstance(x,list), 'string':lambda x:isinstance(x,str),
                 'integer':lambda x:type(x) is int, 'boolean':lambda x:type(x) is bool}
        if kind not in matches or not matches[kind](value):
            raise ValueError(f'{path}: expected {kind}')
    if 'enum' in schema and value not in schema['enum']: raise ValueError(f'{path}: invalid enum')
    if 'const' in schema and value != schema['const']: raise ValueError(f'{path}: invalid constant')
    if isinstance(value,dict):
        missing=set(schema.get('required',[]))-set(value)
        if missing: raise ValueError(f'{path}: missing {sorted(missing)}')
        props=schema.get('properties',{})
        extra=schema.get('additionalProperties',True)
        for key,child in value.items():
            if key in props: validate(child,props[key],root,f'{path}.{key}')
            elif extra is False: raise ValueError(f'{path}: unknown field {key}')
            elif isinstance(extra,dict): validate(child,extra,root,f'{path}.{key}')
    if isinstance(value,list):
        if len(value)<schema.get('minItems',0): raise ValueError(f'{path}: too few items')
        if schema.get('uniqueItems') and any(x in value[:i] for i,x in enumerate(value)):
            raise ValueError(f'{path}: duplicate item')
        if 'items' in schema:
            for i,child in enumerate(value): validate(child,schema['items'],root,f'{path}[{i}]')
    if isinstance(value,str):
        if len(value)<schema.get('minLength',0): raise ValueError(f'{path}: too short')
        if 'pattern' in schema and not re.search(schema['pattern'],value): raise ValueError(f'{path}: pattern mismatch')
        if 'format' in schema:
            if schema['format']!='date': raise ValueError(f'{path}: unsupported format')
            canonical_date(value)
    if 'minimum' in schema and value<schema['minimum']: raise ValueError(f'{path}: below minimum')
    for child in schema.get('allOf',[]): validate(value,child,root,path)
    if 'not' in schema:
        try: validate(value,schema['not'],root,path)
        except ValueError: pass
        else: raise ValueError(f'{path}: forbidden shape')
    if 'if' in schema:
        try: validate(value,schema['if'],root,path)
        except ValueError: branch=schema.get('else',{})
        else: branch=schema.get('then',{})
        validate(value,branch,root,path)
