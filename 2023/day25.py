#!/usr/bin/env python

from functools import partial
from random import choice

with open('inputs/2023/day25.txt') as f:
    data = f.read().strip().split('\n')

test_data = '''
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
'''.strip().split('\n')

def data_to_dict(data):
    d = {
        k: set(v.split())
        for k, v in map(partial(str.split, sep=': '), data)
    }
    for k, v in d:
        for item in v:
            if item not in d:
                d[item] = set()
            d[item].add(k)

def get_edges(data):
    edges = set()
    for this, v in map(partial(str.split, sep=': '), data):
        for that in v.split():
            edges.add(tuple(sorted((this, that))))
    return edges

print(f'{len(get_edges(data))=}')

def get_nodes(data):
    return  set(' '.join(data).replace(':', '').split())

print(get_nodes(test_data))
print(get_nodes(data))

def is_cross_edge(this, that, edge):
    n1, n2 = edge
    return (n1 in this and n2 in that) or (n2 in this and n1 in that)

tg1 = {'cmg', 'frs', 'lhk', 'lsr', 'nvd', 'pzl', 'qnr', 'rsh', 'rzs'}
tg2 = {'bvb', 'hfx', 'jqt', 'ntq', 'rhn', 'xhk'}

def get_cross_edges(this, that, edges):
    return set(
        filter(partial(is_cross_edge, this, that), edges)
    )

print(get_cross_edges(tg1, tg2, get_edges(test_data)))

from hashlib import md5
from random import choice

class Graph:
    def __init__(self, e, v=None) -> None:
        self.e = set(
            (md5(repr(edge).encode()).hexdigest()[-8:], edge) for edge in e
        )
        self.backup_e = set(self.e)
        if v: 
            self.v = set(v)
        else:
            self.v = set()
            for _, b in self.e:
                e1, e2 = b
                self.v.add(e1)
                self.v.add(e2)
    def remove(self, tg_edge):
        print(f'remove: {tg_edge=}')
        # left node is tgt
        _, (tgt, rm_tgt) = tg_edge
        # rm the right node from the node set
        print(f'v.remove: {rm_tgt=}')
        self.v.remove(rm_tgt)
        for edge in list(self.e):
            hash, (lft, rgt) = edge
            
            if lft == rgt: 
                pass
            # rename edges which mention it lft to tgt
            elif lft == rm_tgt:
                print(f'{edge=}; {rm_tgt=}')
                try:
                    self.e.remove(edge)
                    print(f'e.remove {edge=}')
                except:
                    pass
                self.e.add((hash, tuple(sorted((tgt, rgt)))))
                print(f'e.add {(hash, tuple(sorted((tgt, rgt))))=}')
            # rename edges which mention it rgt to tgt
            elif rgt == rm_tgt and lft != tgt:
                print(f'{edge=}; {rm_tgt=}')
                try:
                    self.e.remove(edge)
                    print(f'e.remove {edge=}')
                except:
                    pass
                self.e.add((hash, tuple(sorted((lft, tgt)))))
                print(f'e.add {(hash, tuple(sorted((lft, tgt))))=}')
        try:
            self.e.remove(tg_edge)
            print(f'e.remove {tg_edge=}')
        except:
            pass

def contract(graph, t):
    while len(graph.v) > t:
        c = choice(graph.e)
        graph = graph.remove(c)


g = Graph(get_edges(test_data))

for e in sorted(g.e): print(e)
g.remove(('d90f2bcd', ('nvd', 'qnr')))
for e in sorted(g.e): print(e)

breakpoint()