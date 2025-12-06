#!/usr/bin/env python
from itertools import count, cycle, takewhile

with open('inputs/2023/day8.txt') as f:
    data = [line.strip() for line in f.readlines()]


test_data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".split('\n')
START = 'AAA'
END = 'ZZZ'

def extract(data):
    step_seq, _, *graph_lines = data
    graph = dict(map(
        lambda s: (s[0:3], (s[7:10], s[12:15])), 
        graph_lines))
    nodes = list(graph.keys())
    for node in nodes:
        if graph[node] == (node, node) and not node.endswith('Z'):
            graph.pop(node)
    steps = zip(cycle(step_seq), count(1))
    return steps, graph

test_steps, test_graph = extract(test_data)

take_step = lambda graph, node, dir: graph[node][0 if dir == 'L' else 1]

cur_node = START
while cur_node != END:
    cur_step = next(test_steps)
    cur_node = take_step(test_graph, cur_node, cur_step[0])
nsteps = cur_step[1]
assert nsteps == 2

steps, graph = extract(data)
cur_node = START
while cur_node != END:
    cur_step = next(steps)
    cur_node = take_step(graph, cur_node, cur_step[0])
nsteps = cur_step[1]
print('Part 1:', nsteps)

test_data = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".split('\n')
test_steps, test_graph = extract(test_data)
def p2_take_step(graph, nodes, dir): 
    # print(nodes, dir, set(graph[node][dir == 'R'] for node in nodes if node in graph), sep=' -> ')
    return set(graph[node][dir == 'R'] for node in nodes if node in graph)

cur_nodes = set(filter(
    lambda node: node.endswith('A'),
    test_graph.keys()
))
while not all(node.endswith('Z') for node in cur_nodes):
    cur_step = next(test_steps)
    cur_nodes = p2_take_step(test_graph, cur_nodes, cur_step[0])
nsteps = cur_step[1]
assert nsteps == 6

cur_nodes = set(filter(
    lambda node: node.endswith('A'),
    graph.keys()
))
while not all(node.endswith('Z') for node in cur_nodes):
    cur_step = next(steps)
    cur_nodes = p2_take_step(graph, cur_nodes, cur_step[0])
nsteps = cur_step[1]
print('Part 2:', nsteps)
