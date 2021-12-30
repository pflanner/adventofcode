from util import get_lines_for_day, get_input_for_day, get_groups

from collections import defaultdict, Counter
from itertools import combinations, permutations
from functools import reduce
from operator import attrgetter, itemgetter
from math import factorial


def part1(positions):
    min_fuel = float('inf')
    for i in range(min(positions), max(positions) + 1):
        fuel = 0
        for p in positions:
            fuel += abs(p - i)
        min_fuel = min(fuel, min_fuel)

    return min_fuel


def part2(positions):
    min_fuel = float('inf')
    for i in range(min(positions), max(positions) + 1):
        fuel = 0
        for p in positions:
            diff = abs(p - i)
            for j in range(diff + 1):
                fuel += j
        min_fuel = min(fuel, min_fuel)

    return min_fuel


def part2_2(positions):
    min_fuel = float('inf')
    for i in range(min(positions), max(positions) + 1):
        fuel = 0
        for p in positions:
            diff = abs(p - i)
            fuel += (diff**2 + diff) // 2

        min_fuel = min(fuel, min_fuel)

    return min_fuel


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 7)
    # inp = get_input_for_day(2021, 7)
    # groups = get_groups(lines)
    # test_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    # print(sorted(test_input))

    # print(part1([int(n) for n in lines[0].split(',')]))
    # print(part2([int(n) for n in lines[0].split(',')]))
    # print(part2(test_input))
    # print(part2_2(test_input))
    print(part2_2([int(n) for n in lines[0].split(',')]))
    # 157968979 not right
    # 200030022
