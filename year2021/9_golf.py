from util import get_lines_for_day
from functools import reduce
from operator import mul
from itertools import product

def get_neighbors(x, y):
    return [(x + dx, y + dy) for dx, dy in product(*[[1, 0, -1]]*2) if abs(dx) != abs(dy)]

def is_basin(grid, x, y):
    return all(grid.get((nx, ny), 10) > grid[(x, y)] for nx, ny in get_neighbors(x, y))

def dfs(visited, grid, x, y):
    visited.add((x, y))
    return sum([1 + dfs(visited, grid, nx, ny) for nx, ny in get_neighbors(x, y) if (nx, ny) not in visited and grid.get((nx, ny), 9) != 9])

if __name__ == '__main__':
    lines = get_lines_for_day(2021, 9)
    grid = {(x, y): int(val) for y, line in enumerate(lines) for x, val in enumerate(line)}
    low_points = [loc for loc in grid if is_basin(grid, *loc)]
    print(sum(1 + grid[(x, y)] for x, y in low_points)) # part 1
    visited = set()
    print(reduce(mul, sorted([1 + dfs(visited, grid, *loc) for loc in low_points])[-3:])) # part 2
