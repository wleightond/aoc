#!/usr/bin/env python

with open('inputs/2023/day4.txt') as f:
    data = [line.strip() for line in f.readlines()]

get_card = lambda line: int(line.split(': ')[0].split()[-1]) - 1
get_sets = lambda line: [
    set(map(int, side.split()))
    for side in line.split(': ')[1].split(' | ')
]

n_matches = lambda a, b: len(a.intersection(b))

def points(line):
    mine, winning = get_sets(line) 
    return int(2**(n_matches(mine, winning)-1))

test_data = '''
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''.strip().split('\n')

assert points(test_data[0]) == 8
assert points(test_data[1]) == 2
assert points(test_data[2]) == 2
assert points(test_data[3]) == 1
assert points(test_data[4]) == 0
assert points(test_data[5]) == 0
assert sum(map(points, test_data)) == 13

print('Part 1:', sum(map(points, data)))

test_multipliers = {i: 1 for i in range(len(test_data))}

def do_round(line, mult, max_n):
    card = get_card(line)+1
    score = n_matches(*get_sets(line))
    for i in range(card, card+score):
        if i <= max_n:
            mult[i] += mult[card-1]

do_round(test_data[0], test_multipliers, len(test_data))
assert test_multipliers == {
    0: 1,
    1: 2,
    2: 2,
    3: 2,
    4: 2,
    5: 1,
}
do_round(test_data[1], test_multipliers, len(test_data))
assert test_multipliers == {
    0: 1,
    1: 2,
    2: 4,
    3: 4,
    4: 2,
    5: 1,
}
do_round(test_data[2], test_multipliers, len(test_data))
assert test_multipliers == {
    0: 1,
    1: 2,
    2: 4,
    3: 8,
    4: 6,
    5: 1,
}
do_round(test_data[3], test_multipliers, len(test_data))
assert test_multipliers == {
    0: 1,
    1: 2,
    2: 4,
    3: 8,
    4: 14,
    5: 1,
}
assert sum(test_multipliers.values()) == 30

multipliers = {i: 1 for i in range(len(data))}
ld = len(data)
for i in range(ld):
    do_round(data[i], multipliers, ld)

print('Part 2:', sum(multipliers.values()))
