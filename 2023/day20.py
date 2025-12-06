#!/usr/bin/env python

OFF = 0
ON  = 1
KIND = 'kind'
NAME = 'name'
TARGETS = 'targets'
SWITCH = 'switch'

FLIPFLOP = '%'
CONJUNCTION = '&'
BROADCAST = 'broadcaster'

def gen_pulses(node: dict[str, str]):
    match node[KIND]:
        case str(FLIPFLOP):
            print(f'found FLIPFLOP: {node}')
        case str(CONJUNCTION):
            print(f'found CONJUNCTION: {node}')
        case str(BROADCAST):
            print(f'found BROADCAST: {node}')

with open('inputs/2023/day20.txt') as f:
    data = f.read().strip().split('\n')
test_data_a = r'''
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
'''.strip().split('\n')

def parse_line(line):
    lft, rgt = line.split('->')
    kind, name = (lft[0], lft[1:]) if lft != BROADCAST else (BROADCAST, BROADCAST)
    targets = rgt.split(', ')
    return {
        KIND: kind,
        NAME: name,
        TARGETS: targets,
        SWITCH: OFF,
    }

gen_pulses(parse_line(test_data_a[0]))


test_data_b = r'''
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
'''.strip().split('\n')
