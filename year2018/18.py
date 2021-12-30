from util import get_lines_for_day
from itertools import product

EMPTY_TO_EMPTY = 0
EMPTY_TO_LUMBERYARD = 1
EMPTY_TO_TREE = 2
LUMBERYARD_TO_EMPTY = 3
LUMBERYARD_TO_LUMBERYARD = 4
LUMBERYARD_TO_TREE = 5
TREE_TO_EMPTY = 6
TREE_TO_LUMBERYARD = 7
TREE_TO_TREE = 8

EMPTY = {EMPTY_TO_EMPTY, EMPTY_TO_LUMBERYARD, EMPTY_TO_TREE}
LUMBERYARD = {LUMBERYARD_TO_EMPTY, LUMBERYARD_TO_LUMBERYARD, LUMBERYARD_TO_TREE}
TREE = {TREE_TO_EMPTY, TREE_TO_LUMBERYARD, TREE_TO_TREE}

TO_EMPTY = {EMPTY_TO_EMPTY, LUMBERYARD_TO_EMPTY, TREE_TO_EMPTY}
TO_LUMBERYARD = {EMPTY_TO_LUMBERYARD, LUMBERYARD_TO_LUMBERYARD, TREE_TO_LUMBERYARD}
TO_TREE = {EMPTY_TO_TREE, LUMBERYARD_TO_TREE, TREE_TO_TREE}


def get_neighbors(grid, r, c):
    lumberyard_neighbors = 0
    tree_neighbors = 0

    for i, j in product(*[[-1, 0, 1]]*2):
        if i != 0 or j != 0:
            rr = r + i
            cc = c + j

            if 0 <= rr < len(grid) and 0 <= cc < len(grid[rr]):
                neighbor = grid[r + i][c + j]

                if neighbor in LUMBERYARD:
                    lumberyard_neighbors += 1
                elif neighbor in TREE:
                    tree_neighbors += 1

    return lumberyard_neighbors, tree_neighbors


def compute_change(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            acre = grid[r][c]
            lumberyard_neighbors, tree_neighbors = get_neighbors(grid, r, c)

            if acre in LUMBERYARD:
                if lumberyard_neighbors >= 1 and tree_neighbors >= 1:
                    grid[r][c] = LUMBERYARD_TO_LUMBERYARD
                else:
                    grid[r][c] = LUMBERYARD_TO_EMPTY
            elif acre in TREE:
                if lumberyard_neighbors >= 3:
                    grid[r][c] = TREE_TO_LUMBERYARD
                else:
                    grid[r][c] = TREE_TO_TREE
            else:
                if tree_neighbors >= 3:
                    grid[r][c] = EMPTY_TO_TREE
                else:
                    grid[r][c] = EMPTY_TO_EMPTY

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            acre = grid[r][c]

            if acre in TO_EMPTY:
                grid[r][c] = EMPTY_TO_EMPTY
            elif acre in TO_LUMBERYARD:
                grid[r][c] = LUMBERYARD_TO_LUMBERYARD
            elif acre in TO_TREE:
                grid[r][c] = TREE_TO_TREE


def get_hash(grid):
    h = 0

    for row in grid:
        for acre in row:
            h += acre
            h *= 9

    return h


def print_grid(grid):
    for row in grid:
        for acre in row:
            if acre in EMPTY:
                print('.', end='')
            elif acre in LUMBERYARD:
                print('#', end='')
            else:
                print('|', end='')
        print()
    print()


def f(lines):
    grid = []
    iterations = 1000000000

    for line in lines:
        grid.append([])

        for c in line:
            if c == '#':
                grid[-1].append(LUMBERYARD_TO_LUMBERYARD)
            elif c == '|':
                grid[-1].append(TREE_TO_TREE)
            else:
                grid[-1].append(EMPTY_TO_EMPTY)

    original_grid = [[acre for acre in row] for row in grid]

    seen = {}
    for i in range(iterations):
        if i % 100 == 0:
            print(i)

        h = get_hash(grid)
        if h not in seen:
            seen[get_hash(grid)] = i
            compute_change(grid)
        else:
            print(f'loop from {seen[h]} to {i}')
            break

    new_range = (iterations - seen[h]) % (i - seen[h])

    for i in range(new_range):
        compute_change(grid)

    lumberyards = 0
    trees = 0

    for row in grid:
        for acre in row:
            if acre in LUMBERYARD:
                lumberyards += 1
            elif acre in TREE:
                trees += 1

    return lumberyards * trees


print(f(get_lines_for_day(2018, '18')))
# part 2
# 17427 is too low
# 199593 is too low
