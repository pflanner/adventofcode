from util import get_lines_for_day
from itertools import product
import string


def get_neighbors(r, c, nodes, visited):
    neighbors = []
    for i, j in product(*[[-1, 0, 1]]*2):
        neighbor = (r + i, c + j)
        if abs(i + j) == 1 and neighbor in nodes and neighbor not in visited:
            neighbors.append(neighbor)
    return neighbors


def f(lines):
    start = cur = (0, lines[0].find('|'))
    direction = (1, 0)
    nodes = {start: '|'}
    visited = {start}
    path = []
    steps = 0

    for i, line in enumerate(lines[1:], 1):
        for j, c in enumerate(line):
            if c != ' ':
                nodes[(i, j)] = c

    while True:
        steps += 1
        r, c = cur
        i, j = direction
        cur = (r + i, c + j)

        if cur not in nodes:
            neighbors = get_neighbors(r, c, nodes, visited)

            for neighbor in neighbors:
                direction = (neighbor[0] - r, neighbor[1] - c)
                cur = neighbor
                break

        if cur not in nodes:
            break

        visited.add(cur)
        if nodes[cur] in string.ascii_letters:
            path.append(nodes[cur])

    return ''.join(path), steps


print(f(get_lines_for_day(2017, 19)))
# part 2
# 16333 is too high
