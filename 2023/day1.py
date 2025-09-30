#!/usr/bin/env python

digits = lambda s: ''.join(filter(str.isdigit, s))
calibr_val = lambda s: int(digits(s)[0] + digits(s)[-1])
part1_sample_data = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]
part1_sample_vals = list(map(calibr_val, part1_sample_data))
assert part1_sample_vals == [12, 38, 15, 77]
assert sum(part1_sample_vals) == 142
with open('day1-input.txt') as f:
    data = f.readlines()
part1_vals = list(map(calibr_val, data))
print(f'Part 1: {sum(part1_vals)}')

dig_pairs = [
    ("nine",   "9"),
    ("eight",  "8"),
    ("seven",  "7"),
    ("six",    "6"),
    ("five",   "5"),
    ("four",   "4"),
    ("three",  "3"),
    ("two",    "2"),
    ("one",    "1"),
]
def rep_digs(line: str) -> str:
    buf = line
    spelled_present = lambda s: any(
        idx != -1 for (idx, _) in [
            (buf.find(word), (word, dig)) for (word, dig) in dig_pairs
        ]
    )
    while spelled_present(buf):
        for idx, dig in sorted(filter(
            lambda pair: pair[0] != -1,
            [(buf.find(word), dig) for (word, dig) in dig_pairs]
        ), key=lambda pair: pair[0]):
            buf = buf[:idx] + dig + buf[idx+1:]
    return buf

def digify(line: str) -> str:
    buf = line
    found1 = False
    for i in range(len(buf)):
        if found1: break
        for (word, dig) in dig_pairs:
            if buf[i:].startswith(word):
                buf = buf[:i] + dig + buf[i+len(word)-1:]
                found1 = True
                break
    found2 = False
    for i in range(len(buf), 0, -1):
        if found2: break
        for (word, dig) in dig_pairs:
            if buf[:i].endswith(word):
                buf = buf[:i-len(word)+1] + dig + buf[i:]
                found2 = True
                break
    return buf
data = [
    digify(line)
    for line in data
]
part1_sample_pairs = [
    ("two1nine",        29),
    ("eightwothree",    83),
    ("abcone2threexyz", 13),
    ("xtwone3four",     24),
    ("4nineeightseven2", 42),
    ("zoneight234",     14),
    ("7pqrstsixteen",   76),
    ("nineight",        98),
    ("1two1",           11),
    ("one21",           11),
    ("onetwo1",         11),
    ("one2one",         11),
    ("1",               11),
    ("onetwone",        11),
    ("121",             11),
    ("1twoone",         11),
    ("12one",           11),
    ("nine",            99),
    ("eight",           88),
    ("seven",           77),
    ("six",             66),
    ("five",            55),
    ("four",            44),
    ("three",           33),
    ("two",             22),
    ("one",             11),
    ("twone",           21),
    ("eightwo",         82),
    ("nineight",        98),
    ("eighthree",       83),
    ("nineeight",       98),
    ("eeeight",         88),
    ("oooneeone",       11),
]
part2_sample_data = [
    digify(line) 
    for line, _ in part1_sample_pairs
]
part2_sample_expected = [
    expected for _, expected in part1_sample_pairs
]
part2_sample_vals = list(map(calibr_val, part2_sample_data))
for line, expected in part1_sample_pairs:
    if calibr_val(digify(line)) != expected:
        print(f'failed on {line=}; {expected=}; {calibr_val(digify(line))}')
assert part2_sample_vals == part2_sample_expected
part2_vals = list(map(calibr_val, data))
print(f'Part 2: {sum(part2_vals)}')
