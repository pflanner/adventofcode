from util import get_lines_for_day
from itertools import product
from heapq import heappush, heappop


def get_neighbors(x, y):
    return [(x + dx, y + dy) for dx, dy in product(*[[1, 0, -1]]*2) if abs(dx) != abs(dy)]


def min_distance(cur, distances, visited, cave_map, q, h):
    for neighbor in get_neighbors(*cur):
        if neighbor in cave_map and neighbor not in visited:
            distances[neighbor] = min(distances[neighbor], distances[cur] + cave_map[neighbor])
            if neighbor not in q:
                q.add(neighbor)
                heappush(h, (distances[neighbor], neighbor))
    visited.add(cur)


def least_dangerous_path(cave_map, start, end):
    q = {start}
    h = [(0, start)]
    distances = {k: float('inf') for k in cave_map}
    distances[start] = 0
    visited = set()

    while q:
        dist, cur = heappop(h)
        q.remove(cur)
        if cur == end:
            return dist
        min_distance(cur, distances, visited, cave_map, q, h)


def multiply_cave(cave_map, w, h, multiple):
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_cave_map = {}
    for y in range(multiple):
        for x in range(multiple):
            for pos, val in cave_map.items():
                cx, cy = pos
                new_pos = (cx + (x*w), cy + (y*h))
                new_val = vals[(val + x + y - 1) % len(vals)]
                new_cave_map[(new_pos)] = new_val
    return new_cave_map

if __name__ == '__main__':
    lines = get_lines_for_day(2021, 15)
    cave_map = {(x, y): int(val) for y, line in enumerate(lines) for x, val in enumerate(line)}
    width, height = len(lines[0]), len(lines)
    print(least_dangerous_path(cave_map, (0, 0), (width - 1, height - 1)))  # part 1
    multiple = 5
    expanded_cave_map = multiply_cave(cave_map, width, height, multiple)
    print(least_dangerous_path(expanded_cave_map, (0, 0), (multiple * width - 1, multiple * height - 1)))  # part 2