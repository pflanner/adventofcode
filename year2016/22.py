from util import get_lines_for_day
from collections import deque
from itertools import combinations, product
from operator import itemgetter

class DiskUsage:
    def __init__(self, used, avail):
        self.used = int(used)
        self.avail = int(avail)


class Grid:
    def __init__(self, grid, w, h, goal=None):
        self.grid = grid
        self.w = w
        self.h = h
        self.goal = (w - 1, 0) if goal is None else goal
        self.hash = 0
        self.rehash()

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return type(other) == Grid and self.hash == other.hash

    def copy(self):
        return Grid(self.grid.copy(), self.w, self.h, self.goal)

    def rehash(self):
        self.hash = 0
        for y in range(self.h):
            for x in range(self.w):
                u, a = self.grid[(x, y)]
                self.hash *= 1000
                self.hash += u
                self.hash *= 1000
                self.hash += a
        for coord in self.goal:
            self.hash *= 100
            self.hash += coord

    def update(self, x, y, avail, used):
        self.grid[(x, y)] = (avail, used)
        self.rehash()

    def update_goal(self, x, y):
        self.goal = (x, y)
        self.rehash()


def is_viable(pair):
    a, b = pair
    return 0 < a.used, b.avail


def f(lines):
    disk_usage = [DiskUsage(line[2][:-1], line[3][:-1]) for line in map(lambda x: x.split(), lines[2:])]
    num_viable_pairs = 0

    for a, b in combinations(disk_usage, 2):
        if 0 < a.used <= b.avail:
            num_viable_pairs += 1
        if 0 < b.used <= a.avail:
            num_viable_pairs += 1

    return num_viable_pairs


def grid_hash(grid, goal, w):
    h = 0
    for k, v in grid.items():
        x, y = k
        u, a = v
        h += u << ((y * w + x) * 7)
    for coord in goal:
        h <<= 6
        h += coord

    return h


def grid_hash2(grid, goal):
    return ''.join(map(str, (n[0] for n in grid.values()))) + ''.join(map(str, goal))



def num_digits(n):
    num = 0

    while n > 0:
        num += 1
        n //= 10

    return num


def get_grid(lines):
    grid = {}

    for line in lines[2:]:
        line = line.split()
        du = (int(line[2][:-1]), int(line[3][:-1]))
        path = line[0].split('-')
        x, y = path[1], path[2]
        x, y = int(x.replace('x', '')), int(y.replace('y', ''))
        grid[(x, y)] = du

    min_used = min(map(itemgetter(0), grid.values()))
    max_avail = max(map(itemgetter(1), grid.values()))

    keys_to_delete = []
    for k, v in grid.items():
        if v[1] < min_used or v[0] > max_avail:
            keys_to_delete.append(k)

    for k in keys_to_delete:
        del grid[k]

    return grid


def h(lines):
    grid = {}
    empty = None
    maxx = maxy = 0
    min_used = float('inf')
    max_avail = 0
    count = 0

    for line in lines[2:]:
        line = line.split()
        du = (int(line[2][:-1]), int(line[3][:-1]))
        path = line[0].split('-')
        x, y = path[1], path[2]
        x, y = int(x.replace('x', '')), int(y.replace('y', ''))
        grid[(x, y)] = du
        maxx = max(maxx, x)
        maxy = max(maxy, y)
        min_used = min(min_used, du[0])
        max_avail = max(max_avail, du[1])
        if du[0] == 0:
            empty = (x, y)

    keys_to_delete = []
    for k, v in grid.items():
        if v[1] < min_used or v[0] > max_avail:
            keys_to_delete.append(k)

    for k in keys_to_delete:
        del grid[k]

    # min_used = min(map(itemgetter(0), grid.values()))
    # max_avail = max(map(itemgetter(1), grid.values()))
    # max_size = max(map(lambda n: n[0] + n[1], grid.values()))

    goal = (maxx, 0)
    q = deque([(grid, goal, empty, 0)])
    visited = {(empty, goal)}

    while q:
        cur, goal, empty, depth = q.pop()
        if count % 10000 == 0:
            print(depth, count)

        x, y = empty
        avail = cur[empty][1]
        for i, j in product(*[[-1, 0, 1]] * 2):
            xx, yy = x + i, y + j
            if (i == 0 or j == 0) and i != j and (xx, yy) in cur:
                count += 1
                # print(count)
                candidate = cur.copy()
                new_goal = (goal[0], goal[1])
                used = cur[(xx, yy)][0]
                if used <= avail:
                    candidate[(x, y)] = (used, avail - used)
                    candidate[(xx, yy)] = (0, used + cur[(xx, yy)][1])
                    empty = (xx, yy)
                    if goal == (xx, yy):
                        new_goal = (x, y)
                    if new_goal == (0, 0):
                        return depth + 1
                    if (empty, new_goal) not in visited:
                        visited.add((empty, new_goal))
                        q.appendleft((candidate, new_goal, empty, depth + 1))


def g(lines):
    grid = {}
    maxx = maxy = 0
    count = 0

    for line in lines[2:]:
        line = line.split()
        du = (int(line[2][:-1]), int(line[3][:-1]))
        path = line[0].split('-')
        x, y = path[1], path[2]
        x, y = int(x.replace('x', '')), int(y.replace('y', ''))
        grid[(x, y)] = du
        maxx = max(maxx, x)
        maxy = max(maxy, y)

    g = Grid(grid, maxx + 1, maxy + 1)
    q = deque([(g, 0)])
    visited = {g}

    while q:
        cur, depth = q.pop()
        print(depth, count)

        for y in range(cur.h):
            for x in range(cur.w):
                for i, j in product(*[[-1, 0, 1]]*2):
                    xx, yy = x + i, y + j
                    if (i == 0 or j == 0) and i != j and (xx, yy) in cur.grid:
                        count += 1
                        candidate = cur.copy()
                        old_used, old_avail = cur.grid[(x, y)][0], cur.grid[(x, y)][1]
                        new_used, new_avail = cur.grid[(xx, yy)][0] + old_used, cur.grid[(xx, yy)][1] - old_used
                        if new_avail >= 0:
                            candidate.update(x, y, 0, old_avail + old_used)
                            candidate.update(xx, yy, new_used, new_avail)
                            if candidate.goal == (x, y):
                                candidate.update_goal(xx, yy)
                            if candidate.goal == (0, 0):
                                return depth + 1
                            if candidate not in visited:
                                visited.add(candidate)
                                q.appendleft((candidate, depth + 1))
    print(count)


print(h(get_lines_for_day(2016, '22')))

# import timeit
#
# grid = get_grid(get_lines_for_day(2016, '22'))
#
# start = timeit.default_timer()
# for _ in range(1000):
#     grid_hash(grid, (35, 0), 35)
# print(timeit.default_timer() - start)
#
# start = timeit.default_timer()
# for _ in range(1000):
#     grid_hash2(grid, (35, 0))
# print(timeit.default_timer() - start)

