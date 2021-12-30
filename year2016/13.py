from collections import deque
from itertools import product


num_to_bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]


def count_bits(n):
    if 0 == n:
        return num_to_bits[0]

    nibble = n & 0xf

    return num_to_bits[nibble] + count_bits(n >> 4)


def is_wall(x, y):
    magic_number = x*x + 3*x + 2*x*y + y + y*y
    favorite_number = 1352
    s = magic_number + favorite_number

    bits = count_bits(s)

    return bits & 1 != 0


def get_neighbors(x, y):
    neighbors = []

    for i, j in product(*[[-1, 0, 1]] * 2):
        if (i == 0 or j == 0) and i != j:
            xx = i + x
            yy = j + y
            if xx >= 0 and yy >= 0 and not is_wall(xx, yy):
                neighbors.append((xx, yy))

    return neighbors


def f():
    visited = {(1, 1): 0}
    q = deque([(1, 1, 0)])

    while q:
        x, y, depth = q.pop()

        if depth == 51:
            break

        for nx, ny in get_neighbors(x, y):
            if (nx, ny) not in visited:
                visited[(nx, ny)] = depth
                q.appendleft((nx, ny, depth + 1))

    return len([None for depth in visited.values() if depth < 50])


print(f())
# part 2
# 141 is too high