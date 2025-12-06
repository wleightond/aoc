#!/usr/bin/env python

test_rucksacks = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw',
]
halves = lambda s: (s[:len(s)//2], s[len(s)//2:])
inters = lambda a, b: set(a).intersection(set(b)).pop()

def check_index_half(idx: int, half: int, expected_value: str) -> None: 
    assert(halves(test_rucksacks[idx])[half] == expected_value)

def check_index_common_element(idx: int, expected_value: str) -> None:
    assert inters(*halves(test_rucksacks[idx])) == expected_value

assert test_rucksacks[0] == 'vJrwpWtwJgWrhcsFMMfFFhFp'
check_index_half(0, half=0, expected_value='vJrwpWtwJgWr')
check_index_half(0, half=1, expected_value='hcsFMMfFFhFp')
check_index_common_element(0, expected_value='p')
check_index_half(1, half=0, expected_value='jqHRNqRjqzjGDLGL')
check_index_half(1, half=1, expected_value='rsFMfFZSrLrFZsSL')
check_index_common_element(1, expected_value='L')
check_index_half(2, half=0, expected_value='PmmdzqPrV')
check_index_half(2, half=1, expected_value='vPwwTWBwg')
check_index_common_element(2, expected_value='P')
check_index_common_element(3, expected_value='v')
check_index_common_element(4, expected_value='t')
check_index_common_element(5, expected_value='s')
az = 'abcdefghijklmnopqrstuvwxyz'

def priority(l: str) -> int:
    return az.index(l.lower()) + 1 + 26*l.isupper()

test_priorities = list(map(
    priority,
    map(
        lambda x: inters(*halves(x)),
        test_rucksacks
    )
))
assert test_priorities == [16, 38, 42, 22, 20, 19]
assert sum(test_priorities) == 157


with open('inputs/2022/day3.txt') as f:
    rucksacks = f.readlines()
    
print(
    'part 1:', 
    sum(
        map(
            priority,
            map(lambda x: inters(*halves(x)), rucksacks)
        )
    )
)
