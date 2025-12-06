#!/usr/bin/env python

from itertools import starmap
import math

P1_CARD_ORDER = '23456789TJQKA'
P2_CARD_ORDER = 'J23456789TQKA'

class Card:
    def __init__(self, value, mode=1) -> None:
        self.value = value
        self.mode = mode
    def __lt__(self, other) -> bool:
        if not isinstance(other, Card): return False
        card_order = [P1_CARD_ORDER, P2_CARD_ORDER][self.mode-1]
        return card_order.index(self.value) < card_order.index(other.value)
    def __eq__(self, other) -> bool:
        if not isinstance(other, Card): return False
        return self.value == other.value
    def __hash__(self) -> int:
        return hash(self.value)
    def __repr__(self) -> str:
        return self.value

def counts(cards):
    c = {}
    for card in cards:
        if card not in c: c[card] = 0
        c[card] += 1
    v = c.values()
    return list(sorted(v))

FIVE_OF_A_KIND = 7 
FOUR_OF_A_KIND = 6 
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1
PATTERNS = [
    [5], 
    [1, 4], 
    [2, 3], 
    [1, 1, 3], 
    [1, 2, 2], 
    [1, 1, 1, 2], 
    [1, 1, 1, 1, 1]
][::-1]

def p1_hand_type(hand):
    return PATTERNS.index(counts(hand.cards))+1

def p2_hand_type(hand):
    n_j = hand.cards.count(Card('J'))
    if n_j == 5: return FIVE_OF_A_KIND
    sans_j = list(card for card in hand.cards if card != Card('J'))
    c = counts(sans_j)
    c[-1] += n_j
    return PATTERNS.index(c)+1

class Hand:
    def __init__(self, cards, mode=1) -> None:
        if len(cards) != 5: raise IndexError
        self.cards = [Card(card, mode) for card in cards]
        self.mode = mode
    def __lt__(self, other) -> bool:
        hand_type = [p1_hand_type, p2_hand_type][self.mode-1]
        if not isinstance(other, Hand): return False
        if hand_type(self) < hand_type(other): return True
        if hand_type(self) > hand_type(other): return False
        for a, b in zip(self.cards, other.cards):
            if a < b: return True
            if a > b: return False
        return False
    def __eq__(self, other) -> bool:
        if not isinstance(other, Hand): return False
        return self.cards == other.cards
    def __repr__(self) -> str:
        return '<'+''.join(repr(card) for card in self.cards)+'>'
        
assert p1_hand_type(Hand('33332')) == p1_hand_type(Hand('2AAAA')) == FOUR_OF_A_KIND
assert Hand('33332') > Hand('2AAAA')
assert p1_hand_type(Hand('77888')) == p1_hand_type(Hand('77788')) == FULL_HOUSE
assert Hand('77888') > Hand('77788')

with open('inputs/2023/day7.txt') as f:
    data = [line.strip().split() for line in f.readlines()]

test_data = [
    line.split() for line in 
    [
        '32T3K 765',
        'T55J5 684',
        'KK677 28',
        'KTJJT 220',
        'QQQJA 483',
    ]
]

p1_test_hands = [
    (Hand(hand), int(bid)) for [hand, bid] in test_data
]
p1_test_hands.sort(key=lambda pair: pair[0])
assert p1_test_hands[0][0] == Hand('32T3K')
assert p1_test_hands[1][0] == Hand('KTJJT')
assert p1_test_hands[2][0] == Hand('KK677')
assert p1_test_hands[3][0] == Hand('T55J5')
assert p1_test_hands[4][0] == Hand('QQQJA')

prod = lambda *args: math.prod(args)
p1_test_bids = [bid for (_, bid) in p1_test_hands]
assert sum(starmap(prod, zip(p1_test_bids, range(1, 6)))) == 6440

p1_hands = [
    (Hand(hand), int(bid)) for [hand, bid] in data
]
p1_hands.sort(key=lambda pair: pair[0])
p1_bids = [bid for (_, bid) in p1_hands]
print('Part 1:', sum(starmap(prod, zip(p1_bids, range(1, len(data)+1)))))

assert p2_hand_type(Hand('32T3K', mode=2)) == ONE_PAIR
assert p2_hand_type(Hand('KK677', mode=2)) == TWO_PAIR
assert all(
    p2_hand_type(hand) == FOUR_OF_A_KIND
    for hand in [
        Hand('T55J5', mode=2),
        Hand('KTJJT', mode=2),
        Hand('QQQJA', mode=2),
    ]
)

p2_test_hands = [
    (Hand(hand, mode=2), int(bid)) for [hand, bid] in test_data
]
p2_test_hands.sort(key=lambda pair: pair[0])
assert [a for (a,_) in p2_test_hands] == [
    Hand('32T3K', mode=2),
    Hand('KK677', mode=2),
    Hand('T55J5', mode=2),
    Hand('QQQJA', mode=2),
    Hand('KTJJT', mode=2),
]
p2_test_bids = [bid for (_, bid) in p2_test_hands]
assert sum(starmap(prod, zip(p2_test_bids, range(1, 6)))) == 5905
p2_hands = [
    (Hand(hand, mode=2), int(bid)) for [hand, bid] in data
]
p2_hands.sort(key=lambda pair: pair[0])
p2_bids = [bid for (_, bid) in p2_hands]
print('Part 2:', sum(starmap(prod, zip(p2_bids, range(1, len(data)+1)))))
