from util import get_lines_for_day, get_input_for_day, get_groups
from collections import deque
from functools import reduce
from operator import mul
from itertools import product


def get_neighbors(x, y):
    dirs = [(dx, dy) for dx, dy in product(*[[1, 0, -1]]*2) if abs(dx) != abs(dy)]
    return [(x + dx, y + dy) for dx, dy in dirs]


def make_grid(lines):
    return {(x, y): int(val) for y, line in enumerate(lines) for x, val in enumerate(line)}


def is_basin(x, y, grid):
    for nx, ny in get_neighbors(x, y):
        if grid.get((nx, ny), 10) <= grid[(x, y)]:
            return False
    return True


def part1(lines):
    total = 0
    grid = make_grid(lines)

    for y, line in enumerate(lines):
        for x in range(len(line)):
            if is_basin(x, y, grid):
                total += grid[(x, y)] + 1

    return total


def bfs(x, y, visited, grid):
    q = deque()
    q.appendleft((x, y))
    visited.add((x, y))
    size = 1

    while q:
        curx, cury = q.pop()
        for neighbor in get_neighbors(curx, cury):
            if neighbor not in visited and grid.get(neighbor, 9) != 9:
                visited.add(neighbor)
                q.appendleft(neighbor)
                size += 1

    return size


def part2(lines):
    grid = make_grid(lines)
    all_basins = []
    visited = set()

    for y, line in enumerate(lines):
        for x in range(len(line)):
            if is_basin(x, y, grid):
                size = bfs(x, y, visited, grid)
                all_basins.append(size)

    return reduce(mul, (sorted(all_basins)[-3:]))


def dfs(x, y, visited, grid):
    visited.add((x, y))
    return sum([1 + dfs(nx, ny, visited, grid) for nx, ny in get_neighbors(x, y) if (nx, ny) not in visited and grid.get((nx, ny), 9) != 9])


def part2_dfs(lines):
    grid = make_grid(lines)
    all_basins = []
    visited = set()

    for y, line in enumerate(lines):
        for x in range(len(line)):
            if is_basin(x, y, grid):
                all_basins.append(1 + dfs(x, y, visited, grid))

    return reduce(mul, (sorted(all_basins)[-3:]))


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 9)
    test_lines = get_lines_for_day(2021, '9_test')
    # inp = get_input_for_day(2021, 9)
    groups = get_groups(lines)

    # print(part1(test_lines))
    # 276 is not right
    # 318 is not right
    print(part2(test_lines))
    print(part2_dfs(test_lines))
    # 78260 is not right

    get_neighbors(1, 2)
