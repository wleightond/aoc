#!/usr/bin/env python

from math import prod

if __name__ == "__main__":
    with open('inputs/2023/day3.txt') as f:
        data = [line.strip() for line in f.readlines()]

base = lambda idx: max(idx-1, 0)

def box(schematic, row, col, run):
    maxline, maxrun = len(schematic), len(schematic[0])
    top = max(row-1, 0)
    bot = min(row+1, maxline)
    lft = max(col-1, 0)
    rgt = min(col+1+run, maxrun)
    lines = schematic[top:bot+1]
    return [line[lft:rgt] for line in lines]

def is_symbol(x: str):
    return not x.isdigit() and x != '.'

def symbol_in(window):
    return any(is_symbol(x) for x in ''.join(window))

def numbers(schematic: list[str]):
    found = []
    for row in range(len(schematic)):
        for col in range(len(schematic[0])):
            if not schematic[row][col-1].isdigit() and schematic[row][col].isdigit():
                run = 1
                while schematic[row][col+run].isdigit(): 
                    run += 1
                    if col+run == len(schematic[0]):
                        break
                n = int(schematic[row][col:col+run])
                found.append((n, row, col, run))
    return found

if __name__ == "__main__":
    test_data = [
    '467..114..',
    '...*......',
    '..35...633',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
    ]

    assert not symbol_in(box(test_data, 0, 5, 3))
    assert not symbol_in(box(test_data, 5, 7, 2))
    assert sum(
        n for n, row, col, run in numbers(test_data)
        if symbol_in(box(test_data, row, col, run))
    ) == 4361

    print('Part 1:', sum(
        n for n, row, col, run in numbers(data)
        if symbol_in(box(data, row, col, run))
    ))

def nearby_stars(window, base_row, base_col):
    candidates = []
    for row in range(len(window)):
        for col in range(len(window[0])):
            if window[row][col] == '*':
                candidates.append((base_row+row, base_col+col))
    return candidates

def find_gears(schematic):
    stars = {}
    for n, row, col, run in numbers(schematic):
        for x, y in nearby_stars(box(schematic, row, col, run), base(row), base(col)):
            if (x, y) not in stars: stars[(x, y)] = []
            stars[(x, y)].append((n, row, col))
    return [
        (n1, n2) 
        for [(n1, _, _), (n2, _, _)] in filter(
            lambda val: len(val) == 2,
            stars.values()
        )
    ]

if __name__ == "__main__":
    ratio = prod
    test_gears = find_gears(test_data)
    assert len(test_gears) == 2
    assert test_gears[0] == (467, 35)
    assert ratio(test_gears[0]) == 16345
    assert ratio(test_gears[1]) == 451490
    sum(map(ratio, test_gears)) == 467835
    print('Part 2:', sum(map(ratio, find_gears(data))))
    