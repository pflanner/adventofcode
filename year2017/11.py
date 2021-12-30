from util import get_lines_for_day
from collections import deque
from itertools import product


def get_neighbors(pos):
    neighbors = []

    for i, j in product(*[[-1, 1]]*2):
        neighbors.append((pos[0] + i, pos[1] + j))

    neighbors.append((pos[0], pos[1] + 2))
    neighbors.append((pos[0], pos[1] - 2))

    return neighbors


def f(lines):
    steps = lines[0].split(',')
    x = y = 0
    max_dist = 0

    for step in steps:
        if step == 'n':
            y += 2
        elif step == 'ne':
            x += 1
            y += 1
        elif step == 'se':
            x += 1
            y -= 1
        elif step == 's':
            y -= 2
        elif step == 'sw':
            x -= 1
            y -= 1
        elif step == 'nw':
            x -= 1
            y += 1

        i, j = abs(x), abs(y)
        distance = i
        if j > i:
            distance += (j - i) // 2
        max_dist = max(max_dist, distance)

    # q = deque([((0, 0), 0)])
    # visited = {(0, 0)}
    #
    # while q:
    #     pos, depth = q.pop()
    #
    #     for neighbor in get_neighbors(pos):
    #         if neighbor == (x, y):
    #             return depth + 1
    #         if neighbor not in visited:
    #             visited.add(neighbor)
    #             q.appendleft((neighbor, depth + 1))

    return max_dist


print(f(get_lines_for_day(2017, '11')))
# part 1
# 542 is too low
