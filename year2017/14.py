from adventofcode.year2017.day10 import h
from collections import deque
from itertools import product


def f(key):
    used = set()

    for i in range(128):
        hexhash = h([key + '-' + str(i)])
        binhash = bin(int(hexhash, 16))[2:].zfill(128)
        for j, bit in enumerate(binhash):
            if bit == '1':
                used.add((i, j))

    regions = 0
    visited = set()
    for u in used:
        if u in visited:
            continue

        regions += 1
        visited.add(u)
        q = deque([u])

        while q:
            x, y = q.pop()

            for i, j in product(*[[-1, 0, 1]]*2):
                if (i == 0 or j == 0) and i != j:
                    neighbor = (x + i, y + j)
                    if neighbor in used and neighbor not in visited:
                        visited.add(neighbor)
                        q.appendleft(neighbor)
        
    return regions


print(f('vbqugkhl'))
