from util import get_lines_for_day
from itertools import product


grid = {(r, c) for r in range(100) for c in range(100)}


def get_neighbors(r, c):
    neighbors = []
    for i, j in map(lambda t: (r + t[0], c + t[1]), product(*[[-1, 0, 1]]*2)):
        if (i != r or j != c) and (i, j) in grid:
            neighbors.append((i, j))

    return neighbors


def count_active(lights, active_lights):
    count = 0
    for r, c in lights:
        if (r, c) in active_lights:
            count += 1

    return count


def f(lines):
    active_lights = set()

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                active_lights.add((i, j))

    for _ in range(100):
        new_lights = set()
        visited = set()

        for r, c in active_lights:
            neighbors = get_neighbors(r, c)
            count = count_active(neighbors, active_lights)

            if count == 2 or count == 3:
                new_lights.add((r, c))

            for nr, nc in neighbors:
                if (nr, nc) not in active_lights and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    count = count_active(get_neighbors(nr, nc), active_lights)

                    if count == 3:
                        new_lights.add((nr, nc))

        active_lights = new_lights
        active_lights.update({(0, 0), (0, 99), (99, 0), (99, 99)})

    return len(active_lights)


print(f(get_lines_for_day(2015, 18)))

