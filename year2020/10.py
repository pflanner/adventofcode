from util import get_input_for_day
from collections import defaultdict


def part1():
    i = get_input_for_day(10)

    i = list(map(int, i.strip().split('\n')))

    i.sort()
    print(i)
    prev = ones = twos = threes = 0
    m = defaultdict(int)

    for n in i:
        diff = n - prev
        m[diff] += 1
        prev = n

    print(m)
    print(m[1] * (m[3] + 1))


def part2():
    s = set(map(int, get_input_for_day(10).strip().split('\n')))
    last_adapter = max(s)
    mem = {}

    def dfs(prev=0):
        if prev in mem:
            return mem[prev]
        elif prev == last_adapter:
            return 1

        c = 0

        for n in range(prev + 1, prev + 4):
            if n in s:
                s.remove(n)
                c += dfs(n)
                s.add(n)

        mem[prev] = c
        return c

    return dfs()
    # 42313823813632


print(part2())
