from collections import defaultdict
from io import StringIO
import re
from typing import IO

example_data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

FOLD_RE = re.compile(r"(?P<axis>[xy])=(?P<value>\d+)$")


def fold_data(data: IO, limit_folds=False) -> int:
    grid = defaultdict(lambda: ' ')
    x_max = 0
    y_max = 0
    folds = []
    for line in data:
        line = line.rstrip()
        if not line:
            continue
        if (match := re.search(FOLD_RE, line)):
            axis, value = match.groups()
            value = int(value)
            folds.append((axis, value))
            continue
        x, y = map(int, line.split(','))
        grid[x, y] = '#'
        x_max = max(x_max, x)
        y_max = max(y_max, y)

    for axis, value in folds:
        if axis == "x":
            for y in range(y_max + 1):
                grid[value, y] = '|'
        elif axis == "y":
            for x in range(x_max + 1):
                grid[x, value] = '-'

    for axis, value in folds[0:1 if limit_folds else len(folds)]:
        for (x, y), v in list(grid.items()):
            if v != '#':
                continue
            if axis == "x":
                if x > value:
                    grid[(2 * value) - x, y] = v
                    x_max = value - 1
            elif axis == "y":
                if y > value:
                    grid[x, (2 * value) - y] = v
                    y_max = value - 1

    visible_dots = 0
    for y in range(y_max + 1):
        for x in range(x_max + 1):
            if not limit_folds:
                print(grid[x, y], end='')
            if grid[x, y] == '#':
                visible_dots += 1
        if not limit_folds:
            print()
    return visible_dots


# print("Part 1 Example:", fold_data(StringIO(example_data), True))
with open(r'C:\Users\rosem\adventofcode\advent\day13\day13.txt') as f:
    print("Part 1:", fold_data(f, True))
# print("Part 2 Example:", fold_data(StringIO(example_data)))
with open(r'C:\Users\rosem\adventofcode\advent\day13\day13.txt') as f:
    print("Part 2:", fold_data(f))
