#!/usr/bin/env python
R = 'rock'
P = 'paper'
S = 'scissors'

outcome = lambda theirs, yours: \
    'D' if theirs == yours \
    else ['W', 'L'][(theirs, yours) in [(R, S),(S, P),(P, R)]]
their_move = lambda letter: {
    'A': R,
    'B': P,
    'C': S,
}[letter]
your_move_pt1 = lambda letter: {
    'X': R,
    'Y': P,
    'Z': S,
}[letter]
move_score = lambda move: {
    R: 1, 
    P: 2, 
    S: 3
}[move]

outcome_score = lambda outcome: {
    'L': 0,
    'D': 3,
    'W': 6,
}[outcome]

round_score = lambda theirs_yours: \
    move_score(theirs_yours[1]) \
    + outcome_score(outcome(theirs_yours[0], theirs_yours[1]))
test_guide = '''
A Y
B X
C Z
'''.strip().split('\n')

test_moves_pt1 = [
    (their_move(move_pair.split()[0]), your_move_pt1(move_pair.split()[1])) 
    for move_pair in test_guide 
]
assert sum(map(round_score, test_moves_pt1)) == 15

with open('inputs/2022/day2.txt') as f:
    strategy_guide = f.read().strip().split('\n')

moves_pt1 = [
    (their_move(move_pair.split()[0]), your_move_pt1(move_pair.split()[1])) 
    for move_pair in strategy_guide 
]

print('part 1:', sum(map(round_score, moves_pt1)))



outcome_pt2 = lambda letter: {
    'X': 'L',
    'Y': 'D',
    'Z': 'W',
}[letter]
your_move_pt2 = lambda theirs, outcome: {
    R: {
        'W': P,
        'L': S,
        'D': R,
    },
    P: {
        'W': S,
        'L': R,
        'D': P,
    },
    S: {
        'W': R,
        'L': P,
        'D': S,
    },
}[theirs][outcome]
test_moves_pt2 = [
    (
        their_move(move_pair.split()[0]), 
        your_move_pt2(
            their_move(move_pair.split()[0]),
            outcome_pt2(move_pair.split()[1])
        )
    ) 
    for move_pair in test_guide 
]
assert sum(map(round_score, test_moves_pt2)) == 12
moves_pt2 = [
    (
        their_move(move_pair.split()[0]), 
        your_move_pt2(
            their_move(move_pair.split()[0]),
            outcome_pt2(move_pair.split()[1])
        )
    ) 
    for move_pair in strategy_guide 
]

print('part 2:', sum(map(round_score, moves_pt2)))