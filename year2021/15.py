from util import get_lines_for_day, get_input_for_day, get_groups

from collections import defaultdict, Counter, deque
from itertools import combinations, permutations, product
from functools import reduce
from operator import attrgetter, itemgetter
from math import factorial
from heapq import heappush, heappop, heapify, heappushpop, heapreplace


def min_distance(cur, distances, visited, cave_map, q):
    for neighbor in get_neighbors(*cur):
        if neighbor in cave_map and neighbor not in visited:
            distances[neighbor] = min(distances[neighbor], distances[cur] + cave_map[neighbor])
            q.add(neighbor)
    visited.add(cur)


def min_distance2(cur, distances, visited, cave_map, q, h):
    for neighbor in get_neighbors(*cur):
        if neighbor in cave_map and neighbor not in visited:
            distances[neighbor] = min(distances[neighbor], distances[cur] + cave_map[neighbor])
            if neighbor not in q:
                q.add(neighbor)
                heappush(h, (distances[neighbor], neighbor))
    visited.add(cur)


def get_neighbors(x, y):
    return [(x + dx, y + dy) for dx, dy in product(*[[1, 0, -1]]*2) if abs(dx) != abs(dy)]


def least_dangerous_path(cave_map, start, end):
    q = set()
    q.add(start)
    distances = {k: float('inf') for k in cave_map}
    distances[start] = 0
    visited = set()

    while q:
        cur = end
        for position in q:
            if distances[position] < distances[cur]:
                cur = position
        q.remove(cur)
        if cur == end:
            return distances[cur]
        min_distance(cur, distances, visited, cave_map, q)


def least_dangerous_path2(cave_map, start, end):
    q = set()
    h = [(0, start)]
    q.add(start)
    distances = {k: float('inf') for k in cave_map}
    distances[start] = 0
    visited = set()

    while q:
        dist, cur = heappop(h)
        q.remove(cur)
        if cur == end:
            return dist
        min_distance2(cur, distances, visited, cave_map, q, h)


def part2(cave_map, start, end):
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    w, h = end[0] + 1, end[1] + 1
    additional_cave_map = {}
    for y in range(5):
        for x in range(5):
            if x == 0 and y == 0:
                continue
            for pos, val in cave_map.items():
                cx, cy = pos
                new_pos = (cx + (x*w), cy + (y*h))
                new_val = vals[(val + x + y - 1) % len(vals)]
                additional_cave_map[(new_pos)] = new_val
    cave_map.update(additional_cave_map)
    return least_dangerous_path2(cave_map, start, (5 * w - 1, 5 * h - 1))




if __name__ == '__main__':
    lines = get_lines_for_day(2021, 15)
    test_lines = get_lines_for_day(2021, '15_test')
    # inp = get_input_for_day(2021, 15)
    groups = get_groups(lines)

    # lines = test_lines

    cave_map = {(x, y): int(val) for y, line in enumerate(lines) for x, val in enumerate(line)}

    print(least_dangerous_path(cave_map, (0, 0), (len(lines[0]) - 1, len(lines) - 1)))
    print(part2(cave_map, (0, 0), (len(lines[0]) - 1, len(lines) - 1)))