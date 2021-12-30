from util import get_lines_for_day, get_input_for_day, get_groups
from collections import deque, defaultdict, Counter
from functools import reduce
from operator import attrgetter, itemgetter


def helper(param):
    mcbs0 = [0] * len(param[0])
    mcbs1 = [0] * len(param[0])
    mcbs = []
    inv = []
    for line in param:
        for i, c in enumerate(line):
            if c == '0':
                mcbs0[i] += 1
            else:
                mcbs1[i] += 1

    for i in range(len(mcbs0)):
        if mcbs0[i] > mcbs1[i]:
            mcbs.append('0')
            inv.append('1')
        else:
            mcbs.append('1')
            inv.append('0')

    return mcbs, inv


def part1(param):
    mcbs, inv = helper(param)
    gamma = int(''.join(mcbs), 2)
    epsilon = int(''.join(inv), 2)

    return gamma * epsilon


def part2(param):
    mcbs, inv = helper(param)

    # oxygen
    ox = param[:]
    nextox = []
    i = 0

    while len(ox) > 1:
        for line in ox:
            if line[i] == mcbs[i]:
                nextox.append(line)
        ox = nextox
        nextox = []
        mcbs, inv = helper(ox)
        i += 1

    # co2
    co2 = param[:]
    nextco2 = []
    i = 0

    while len(co2) > 1:
        for line in co2:
            if line[i] == inv[i]:
                nextco2.append(line)
        co2 = nextco2
        nextco2 = []
        mcbs, inv = helper(co2)
        i += 1

    o = int(ox[0], 2)
    c = int(co2[0], 2)

    return o * c


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 3)
    # inp = get_input_for_day(2021, 3)
    # groups = get_groups(lines)

    print(part1(lines))
    print(part2(lines))
    # 5517801 isn't right
