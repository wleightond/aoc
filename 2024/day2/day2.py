from pathlib import Path

data = [
    [*map(int, line.split())]
    for line in Path('input.txt').read_text().strip().split('\n')
]

# data = [
#   [7, 6, 4, 2, 1],
#   [1, 2, 7, 8, 9],
#   [9, 7, 6, 2, 1],
#   [1, 3, 2, 4, 5],
#   [8, 6, 4, 4, 1],
#   [1, 3, 6, 7, 9]
# ]

def is_safe(line):
    # diffs
    diffs = [line[i]-line[i-1] for i in range(1,len(line))]
    # monotonic
    if (
        not all(x>0 for x in diffs) and
        not all(x<0 for x in diffs)
    ):
        return False
    # diffs are less than
    if any(abs(x)>3 for x in diffs):
        return False
    return True

print(*(int(is_safe(line))for line in data))