from util import get_lines_for_day
from functools import reduce


def part1(depths):
    return reduce(lambda a, t: a + 1 if t[1] > t[0] else a, zip(depths, depths[1:]), 0)


def part2(depths):
    tuples = [(a, b, c) for a, b, c in zip(depths, depths[1:], depths[2:])]
    pairs = zip(tuples, tuples[1:])
    return reduce(lambda a, t: a + 1 if sum(t[1]) > sum(t[0]) else a, pairs, 0)


if __name__ == '__main__':
    d = list(map(int, get_lines_for_day(2021, 1)))
    print(part1(d))
    print(part2(d))
