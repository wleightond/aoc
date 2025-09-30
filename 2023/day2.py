#!/usr/bin/env python

from functools import reduce
from math import prod


with open('day2-input.txt') as f:
    data = [line.strip() for line in f.readlines()]
game_id = lambda game: int(game[5:game.index(':')])
c2d = lambda s: {k: int(v) for v, k in map(str.split, s.split(', '))}
subsets = lambda line: list(map(
    c2d,
    line[line.index(':')+1:].split('; ')
))

test_data = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

test_g1_sets = subsets(test_data[0])
assert len(test_g1_sets) == 3
assert test_g1_sets[0]['blue'] == 3
assert test_g1_sets[0]['red'] == 4
assert test_g1_sets[1]['red'] == 1
assert test_g1_sets[1]['green'] == 2
assert test_g1_sets[1]['blue'] == 6
assert test_g1_sets[2]['green'] == 2

MAX_R=12
MAX_G=13
MAX_B=14
test_sets = list(map(subsets, test_data))
exceeds = lambda setls, color, value: (
    any(s.get(color, 0) > value for s in setls)
)
assert not exceeds(test_sets[0], 'blue', 6)
assert exceeds(test_sets[2], 'red', 19)
check_game = lambda game, max_r, max_g, max_b: (
        not exceeds(subsets(game), 'red', max_r)
    and not exceeds(subsets(game), 'green', max_g)
    and not exceeds(subsets(game), 'blue', max_b)
)

test_possible_games = list(map(
    game_id,
    filter(
        lambda game: check_game(
            game,
            max_b=MAX_B,
            max_g=MAX_G,
            max_r=MAX_R), 
        test_data)
)) 
assert test_possible_games == [1, 2, 5]
assert sum(test_possible_games) == 8

print('Part 1:',
    sum(map(
        game_id,
        filter(
            lambda game: check_game(
                game,
                max_b=MAX_B,
                max_g=MAX_G,
                max_r=MAX_R), 
            data)
    ))
)
zero = {
    'red': 0, 
    'green': 0, 
    'blue': 0
}
add = lambda a, b: {
    color: max(a.get(color, 0), b.get(color, 0)) for color in ['red', 'green', 'blue']
}
min_rgb = lambda game: reduce(add, subsets(game), zero)
assert min_rgb(test_data[0]) == {'red': 4, 'green': 2, 'blue': 6}
assert min_rgb(test_data[1]) == {'red': 1, 'green': 3, 'blue': 4}
assert min_rgb(test_data[2]) == {'red': 20, 'green': 13, 'blue': 6}
assert min_rgb(test_data[3]) == {'red': 14, 'green': 3, 'blue': 15}
assert min_rgb(test_data[4]) == {'red': 6, 'green': 3, 'blue': 2}

power = lambda game: prod(min_rgb(game).values())
assert power(test_data[0]) == 48
assert [power(game) for game in test_data[1:]] == [12, 1560, 630, 36]
assert sum(power(game) for game in test_data) == 2286
print('Part 2:', sum(map(power, data)))
