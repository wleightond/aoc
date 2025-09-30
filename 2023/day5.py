#!/usr/bin/env python
from functools import reduce
from more_itertools import batched

with open('day5-input.txt') as f:
    data = f.read().split('\n\n')

test_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".split('\n\n')

p1_get_seeds = lambda s: list(map(int, s.split(': ')[1].split()))
test_seeds = p1_get_seeds(test_data[0])
assert test_seeds == [79, 14, 55, 13]
test_map_strs = test_data[1:]

def range_overlap(a_start, a_end, b_start, b_end):
    overlap_start = max(a_start, b_start)
    overlap_end = min(a_end, b_end)
    if overlap_end <= overlap_start:
        overlap = []
    else:
        overlap = [(overlap_start, overlap_end)]

    a_outside_start = a_start if a_start < overlap_start else overlap_end
    a_outside_end = a_end if a_end > overlap_end else overlap_start
    if overlap:
        if a_outside_start < overlap_start and a_outside_end > overlap_end:
            a_outside = [(a_outside_start, overlap_start), (overlap_end, a_outside_end)]
        elif a_outside_start >= a_outside_end:
            a_outside = []
        else:
            a_outside = [(a_outside_start, a_outside_end)]
    else:
        a_outside = [(a_start, a_end)]

    b_outside_start = b_start if b_start < overlap_start else overlap_end
    b_outside_end = b_end if b_end > overlap_end else overlap_start
    if overlap:
        if b_outside_start < overlap_start and b_outside_end > overlap_end:
            b_outside = [(b_outside_start, overlap_start), (overlap_end, b_outside_end)]
        elif b_outside_start >= b_outside_end:
            b_outside = []
        else:
            b_outside = [(b_outside_start, b_outside_end)]
    else:
        b_outside = [(b_start, b_end)]

    return {
        'intersection': list(set(overlap)),
        'a_outside': list(set(a_outside)),
        'b_outside': list(set(b_outside)),
    }


class Map:
    def __init__(self, ranges) -> None:
        self.ranges = [((src, src+run), (dest, dest+run)) for (dest, src, run) in ranges]
        self.ranges.sort()
    def __getitem__(self, val):
        for ((s_start, s_end), (d_start, d_end)) in self.ranges:
            if val >= s_start and val < s_end:
                return d_start + val - s_start
        return val
    get = __getitem__
    def rev_get(self, val):
        for ((s_start, s_end), (d_start, d_end)) in self.ranges:
            if val >= d_start and val < d_end:
                return s_start + val - d_start
        return val

    def s_overlap(self, start, end):
        o_ranges = []
        for ((s_start, s_end), (d_start, d_end)) in self.ranges:
            ov = range_overlap(s_start, s_end, start, end)
            breakpoint()
            o_ranges += ov['intersection']
            o_ranges += ov['b_outside']
        o_ranges.sort()
        return o_ranges

    def d_overlap(self, start, end):
        o_ranges = []
        for ((s_start, s_end), (d_start, d_end)) in self.ranges:
            ov = range_overlap(d_start, d_end, start, end)
            for ls in ov.values():
                o_ranges += ls
        o_ranges.sort()
        return o_ranges


def get_name(map_str):
    name, _ = map_str.split(' map:\n')
    return name

def get_map(map_str):
    _, rest = map_str.split(' map:\n')
    ranges = [tuple(map(int, i.split())) for i in rest.split('\n')]
    return Map(ranges)

test_maps = {get_name(s): get_map(s) for s in test_map_strs}
assert test_maps['seed-to-soil'][98] == 50
assert test_maps['seed-to-soil'][99] == 51
assert test_maps['seed-to-soil'][53] == 55
assert test_maps['seed-to-soil'][10] == 10
assert test_maps['seed-to-soil'][79] == 81
assert test_maps['seed-to-soil'][14] == 14
assert test_maps['seed-to-soil'][55] == 57
assert test_maps['seed-to-soil'][13] == 13
LEVELS = [
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
]
get_val = lambda maps, val: reduce(
    lambda src, level: maps[level][src], 
    LEVELS,
    val
)
assert get_val(test_maps, 79) == 82
assert get_val(test_maps, 14) == 43
assert get_val(test_maps, 55) == 86
assert get_val(test_maps, 13) == 35
assert min(map(lambda s: get_val(test_maps, s), test_seeds)) == 35

seeds = p1_get_seeds(data[0])
map_strs = data[1:]
maps = {get_name(s): get_map(s) for s in map_strs}
print('Part 1:', min(map(lambda s: get_val(maps, s), seeds)))

def p2_get_seeds(s):
    return [
        (src, src+run)
        for src, run 
        in batched(map(int, s.split(': ')[1].split()), 2)
    ]

def map_range(maps: dict[str, Map], level: str, rng):
    m = maps[level]
    s_ranges = m.s_overlap(*rng)
    d_ranges = [(m[start], m[end]) for (start, end) in s_ranges]
    return d_ranges

def map_ranges(maps: dict[str, Map], level: str, ranges):
    breakpoint()
    d_ranges = []
    for rng in ranges:
        d_ranges += map_range(maps, level, rng)
    return d_ranges

test_init_ranges = p2_get_seeds(test_data[0])
assert test_init_ranges[0] == (79, 93)
assert test_init_ranges[1] == (55, 68)
print(test_init_ranges)

traverse = lambda maps, init_ranges: reduce(
    lambda ranges, level: map_ranges(maps, level, ranges), 
    LEVELS,
    init_ranges
)

print(traverse(test_maps, test_init_ranges))
