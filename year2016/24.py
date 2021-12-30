from util import get_lines_for_day
from collections import deque
from itertools import product


NUM_CONTROLS = 8


def get_neighbors(pos, grid):
    r, c = pos
    neighbors = []

    for i, j in product(*[[-1, 0, 1]]*2):
        if (i == 0 or j == 0) and i != j:
            neighbor = (r + i, c + j)
            if neighbor in grid:
                neighbors.append(neighbor)

    return neighbors


def shortest_distance(source, dest, grid):
    q = deque([(source, 0)])
    visited = {source}

    while q:
        cur, depth = q.pop()

        for neighbor in get_neighbors(cur, grid):
            if neighbor == dest:
                return depth + 1
            if neighbor not in visited:
                visited.add(neighbor)
                q.appendleft((neighbor, depth + 1))

    return float('inf')


def new_dist_array():
    return [float('inf')] * NUM_CONTROLS


def f(lines):
    grid = set()
    controls = [None] * NUM_CONTROLS
    distances = [[float('inf')] * NUM_CONTROLS for _ in range(NUM_CONTROLS)]

    for r, line in enumerate(lines):
        for c, token in enumerate(line):
            if token == '.':
                grid.add((r, c))
            elif token == '#':
                continue
            else:
                grid.add((r, c))
                control = int(token)
                controls[control] = (r, c)

    # calculate shortest distances between every pair of controls

    for i in range(len(controls) - 1):
        for j in range(i + 1, len(controls)):
            c1, c2 = controls[i], controls[j]
            distance = shortest_distance(c1, c2, grid)
            distances[i][j] = distance
            distances[j][i] = distance

    def dfs(path, target, total_dist=0, shortest=float('inf'), shortest_path=None):
        if total_dist >= shortest:
            return shortest, shortest_path
        if len(path) == len(controls) and path[-1] == target:
            if total_dist < shortest:
                return total_dist, path
            else:
                return shortest, shortest_path

        last = path[-1]

        for i, dist in enumerate(distances[last]):
            if i != last and i not in path:
                pdist, p = dfs(path + [i], target, total_dist + dist, shortest)
                if pdist < shortest and p[-1] == target:
                    shortest = pdist
                    shortest_path = p

        return shortest, shortest_path

    shortest = float('inf')
    shortest_path = None

    for i in range(1, NUM_CONTROLS):
        pdist, p = dfs([0], i)
        if p is not None:
            pdist += distances[p[-1]][0]
            if pdist < shortest:
                shortest = pdist
                shortest_path = p + [0]

    return shortest, shortest_path


print(f(get_lines_for_day(2016, '24')))
