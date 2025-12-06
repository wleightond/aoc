#!/usr/bin/env python

from functools import partial
from operator import gt, lt

from flask import app

def parse_workflow(wfs):
    name, body = wfs[:-1].split('{')
    stages = map(tuple, map(partial(str.split, sep=':'), body.split(',')))
    return (name, list(stages))

ex = "ex{x>10:one,m<20:two,a>30:R,A}"
t_wf = parse_workflow(ex)
assert len(t_wf[1]) == 4

def eval_rule(rule, pt):
    var, mode, val = rule[0], rule[1], int(rule[2:])
    op = {
        '>': gt,
        '<': lt,
    }[mode]
    return op(pt[var], val)

def apply_workflow(wf, pt):
    for *rule, target in wf:
        if rule:
            if eval_rule(rule[0], pt):
                return target
        else:
            return target
    raise IndexError

REJECT = 'R'
ACCEPT = 'A'

def parse_part(pt):
    return {
        k: int(v) 
        for k, v in map(partial(str.split, sep='='), pt[1:-1].split(','))
    }

with open('inputs/2023/day19.txt') as f:
    workflow_data, part_data = f.read().split('\n\n')
test_workflow_data, test_part_data = '''
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
'''.split('\n\n')
test_workflows = dict(map(parse_workflow, test_workflow_data.strip().split('\n')))
workflows = dict(map(parse_workflow, workflow_data.strip().split('\n')))

test_parts = list(map(parse_part, test_part_data.strip().split('\n')))
parts = list(map(parse_part, part_data.strip().split('\n')))

INIT = 'in'

def is_accepted(part, workflows):
    status = INIT
    while status != ACCEPT and status != REJECT:
        workflow = workflows[status]
        status = apply_workflow(workflow, part)
    return status == ACCEPT

test_outputs = list(map(partial(is_accepted, workflows=test_workflows), test_parts))
assert test_outputs[0]
assert not test_outputs[1]
assert test_outputs[2]
assert not test_outputs[3]
assert test_outputs[4]

def score(part):
    return sum(part.values())

assert sum(map(score, filter(partial(is_accepted, workflows=test_workflows), test_parts))) == 19114

print('Part 1:', sum(map(score, filter(partial(is_accepted, workflows=workflows), parts))))
