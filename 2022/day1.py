#!/usr/bin/env python
from sys import stdin
with open('inputs/2022/day1.txt') as f:
    instr = f.read().strip()

data = [[int(i) for i in elf.split('\n')] for elf in instr.split('\n\n')]
print(max(map(sum, data)))
print(sum(list(map(sum, sorted(data, key=sum)[-3:]))))
