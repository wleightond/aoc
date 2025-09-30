#!/usr/bin/env python

from itertools import combinations

def transpose(it):
    "Swap the rows and columns of the input."
    # transpose([(1, 2, 3), (11, 22, 33)]) --> (1, 11) (2, 22) (3, 33)
    return zip(*it, strict=True)
test_data = '''
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''.strip().split()
with open('day11-input.txt') as f:
    data = [line.strip() for line in f.readlines()]

def expand_rows(lines):
    o = []
    for line in lines:
        if set(line) == {'.'}:
            o += [line, line]
        else:
            o += [line]
    return o

def expand_cols(lines):
    t = transpose(lines)
    x = expand_rows(t)
    o = transpose(x)
    return list(map(''.join, o))

def get_galaxies(lines):
    d = {}
    i = 0
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == '#':
                d[i] = (row, col)
                i += 1
    return d

test_expanded_data = expand_rows(expand_cols(test_data))
test_combinations = list(combinations(range(''.join(test_expanded_data).count('#')), 2))
assert len(test_combinations) == 36
expanded_data = expand_rows(expand_cols(data))
p1_combinations = list(combinations(range(''.join(expanded_data).count('#')), 2))

test_galaxies = get_galaxies(test_expanded_data)
galaxies = get_galaxies(expanded_data)
def shortest_path(galaxies, a, b):
    x1, y1 = galaxies[a]
    x2, y2 = galaxies[b]
    return abs(x1-x2) + abs(y1-y2)

assert shortest_path(test_galaxies, 4, 8) == 9
assert shortest_path(test_galaxies, 0, 6) == 15
assert shortest_path(test_galaxies, 2, 5) == 17
assert shortest_path(test_galaxies, 7, 8) == 5
assert sum(map(lambda combo: shortest_path(test_galaxies, *combo), test_combinations)) == 374
print('Part 1:', sum(map(lambda combo: shortest_path(galaxies, *combo), p1_combinations)))
