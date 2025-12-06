#!/usr/bin/env python

from more_itertools import flatten
from day3 import box

DEBUGGING = False

with open('inputs/2023/day10.txt') as f:
    data = [
        list(line)
        for line in f.read().strip().split('\n')
    ]


N = 'n'
E = 'e'
S = 's'
W = 'w'

UP = '↑'
RT = '→'
DN = '↓'
LT = '←'

INSIDE = 'I'
OUTSIDE = ' '
AMBIGUOUS = '?'

ANTICLOCKWISE = True
CLOCKWISE = False

kind2dir = {
    '|': {
        N: S,
        S: N,
    },
    '-': {
        E: W,
        W: E,
    },
    'L': {
        N: E,
        E: N,
    },
    'J': {
        N: W,
        W: N,
    },
    '7': {
        S: W,
        W: S,
    },
    'F': {
        S: E,
        E: S,
    },
}

dir2delta = {
    N: (-1,  0),
    S: ( 1,  0),
    E: ( 0,  1),
    W: ( 0, -1),
}


flipdir = {N: S, S: N, E: W, W: E}
altrep  = {N: UP, S: DN, E: RT, W: LT}

def find_start(mat):
    s_indices = enumerate([''.join(l).find('S') for l in mat])
    for row, col in s_indices:
        if col >= 0:
            start = (row, col)
            return start
    if not start:
        raise ValueError('Start not found')

def start_dir(mat, row, col):
    e, s, w, n = mat[row][col+1], mat[row+1][col], mat[row][col-1], mat[row-1][col]
    for dir, cell in [
        (E, e),
        (S, s),
        (W, w),
        (N, n),
    ]:
        allowed = list(filter(lambda x: flipdir[dir] in kind2dir[x],kind2dir.keys()))
        if cell in allowed:
            return dir
    raise ValueError('No valid path found from start')

def step(mat, indir, row, col):
    kind = mat[row][col]
    if kind == 'S':
        outdir = start_dir(mat, row, col)
    else:
        outdir = kind2dir[kind][indir]
    drow, dcol = dir2delta[outdir]
    return outdir, row+drow, col+dcol

test_data_a = [
    list(line)
    for line in '''
.....
.S-7.
.|.|.
.L-J.
.....
'''.strip().split('\n')
]

def loop_len(mat):
    lmat = list(mat)
    cdir, crow, ccol = None, *find_start(lmat)
    steps = 0
    kind = 'init'
    while kind != 'S':
        cdir = flipdir.get(cdir)
        ndir, nrow, ncol = step(lmat, cdir, crow, ccol)
        if kind != 'init': lmat[crow][ccol] = altrep[ndir]
        cdir, crow, ccol = ndir, nrow, ncol
        steps += 1
        kind = lmat[crow][ccol]
    return lmat, steps

def walk(mat):
    lmat = list(mat)
    cdir, crow, ccol = None, *find_start(lmat)
    kind = 'init'
    while kind != 'S':
        cdir = flipdir.get(cdir)
        ndir, nrow, ncol = step(lmat, cdir, crow, ccol)
        if kind != 'init': lmat[crow][ccol] = altrep[ndir]
        cdir, crow, ccol = ndir, nrow, ncol
        kind = lmat[crow][ccol]
    return lmat

max_dist = lambda mat: (loop_len(mat)[1]+1)//2

assert max_dist(test_data_a) == 4

test_data_b = [
    list(line)
    for line in '''
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
'''.strip().split('\n')
]
print('Part 1:', max_dist(data))
clockwise = {
    N: RT,
    S: LT,
    E: DN,
    W: UP,
}

anticlockwise = {
    N: LT,
    S: RT,
    E: UP,
    W: DN,
}

def strip_outside(line):
    if not any(arr in line for arr in '→↓↑←'): return OUTSIDE*len(line)
    lin = min(line.index(arr) for arr in '→↓↑←' if arr in line)
    rin = max(line.rindex(arr)+1 for arr in '→↓↑←' if arr in line)
    return OUTSIDE*lin + line[lin:rin] + OUTSIDE*(len(line)-rin)

def check_extended(mat, row, col):
    if DEBUGGING: print('\n\n    ',row, col, 'ambiguous:')
    if DEBUGGING: print(*map(''.join, box(mat, row, col, 1)), sep='\n')
    BEG, MID, END = 0, 1, 2
    b = box(mat, row, col, 1)
    if b[BEG][MID] == UP:
        if b[BEG][BEG] == RT: return ANTICLOCKWISE
        if b[BEG][END] == LT: return CLOCKWISE
    if b[MID][END] == RT:
        if b[BEG][END] == DN: return ANTICLOCKWISE
        if b[END][END] == UP: return CLOCKWISE
    if b[END][MID] == DN:
        if b[END][END] == LT: return ANTICLOCKWISE
        if b[END][BEG] == RT: return CLOCKWISE
    if b[MID][BEG] == LT:
        if b[END][BEG] == UP: return ANTICLOCKWISE
        if b[BEG][BEG] == DN: return CLOCKWISE
    if DEBUGGING: print('===')
    if DEBUGGING: print(*map(''.join, b), sep='\n')
    return None

def mark(mat, wise, side):
    lmat = list(mat)
    for row in range(len(lmat)):
        for col in range(len(lmat[0])):
            if lmat[row][col] in '.F7LJ-|':
                if any(
                    lmat[row+dx][col+dy] in [clockwise, anticlockwise][wise][dir]
                    for dir, (dx, dy) in dir2delta.items()
                ):
                    lmat[row][col] = side
                elif not any(
                    lmat[row+dx][col+dy] in [clockwise, anticlockwise][not wise][dir]
                    for dir, (dx, dy) in dir2delta.items()
                ):
                    ext = check_extended(lmat, row, col)
                    if ext is not None and wise != ext:
                        lmat[row][col] = side
                        if DEBUGGING: print('---')
                        if DEBUGGING: print(*map(''.join, box(lmat, row, col, 1)), sep='\n')
    return lmat

def extend(mat, side):
    lmat = list(mat)
    for row in range(len(lmat)):
        for col in range(len(lmat[0])):
            if lmat[row][col] == side and any(
                symb in flatten(box(lmat, row, col, 1))
                for symb in '.F7LJ-|'
            ):
                for _, (dx, dy) in dir2delta.items():
                    if lmat[row+dx][col+dy] in '.F7LJ-|':
                        lmat[row+dx][col+dy] = side
    return lmat


test_data_c = [
    list(line)
    for line in '''
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
'''.strip().split('\n')
]


if DEBUGGING: print('-'*len(test_data_c[0]), *map(''.join, test_data_c), sep='\n')

test_x1 = list(map(strip_outside, map(''.join, walk(test_data_c))))
test_tx1 = list(map(''.join,zip(*test_x1, strict=True)))
test_tx2 = list(map(strip_outside, test_tx1))
test_x2 = list(map(list,zip(*test_tx2, strict=True)))

test_x2 = mark(test_x2, ANTICLOCKWISE, OUTSIDE)
test_x2 = mark(test_x2, CLOCKWISE, INSIDE)
test_x2 = extend(test_x2, OUTSIDE)
test_x2 = extend(test_x2, INSIDE)
if DEBUGGING: print('-'*len(test_x2[0]), *map(''.join, test_x2), sep='\n')

assert list(flatten(test_x2)).count(INSIDE) == 10

x1 = list(map(strip_outside, map(''.join, data)))
tx1 = list(map(''.join,zip(*x1, strict=True)))
tx2 = list(map(strip_outside, tx1))
x2 = list(map(list,zip(*tx2, strict=True)))

x2 = mark(x2, CLOCKWISE, OUTSIDE)
x2 = mark(x2, ANTICLOCKWISE, INSIDE)

x2 = extend(x2, OUTSIDE)
x2 = extend(x2, INSIDE)
for l in x2: 
    if DEBUGGING: print(''.join(l))
print('Part 2:', list(flatten(x2)).count(INSIDE))
