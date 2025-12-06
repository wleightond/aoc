#!/usr/bin/env python
with open('inputs/2023/day9.txt') as f:
    data = [[int(i) for i in line.strip().split()] for line in f.readlines()]

def rank(line):
    c = list(line)
    depth = 0
    while sum(c) > 0:
        c = get_parent(c)
        depth +=1
    return depth

def get_parent(line):
    return [line[i+1]-line[i] for i in range(len(line)-1)]

def next_val(line):
    parent = get_parent(line)
    if all(x==0 for x in parent):
        return line[-1]
    return line[-1] + next_val(parent)

assert next_val([10,  13,  16,  21,  30,  45]) == 68
print('Part 1:', sum(map(next_val, data)))
