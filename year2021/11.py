from util import get_lines_for_day, get_input_for_day, get_groups

from collections import defaultdict, Counter, deque
from itertools import combinations, permutations, product
from functools import reduce
from operator import attrgetter, itemgetter
from math import factorial


def get_neighbors(x, y, lines):
    neighbors = []
    for dx, dy in product(*[[1, 0, -1]]*2):
        if dx != 0 or dy != 0:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(lines[0]) and 0 <= ny < len(lines):
                neighbors.append((nx, ny))
    return neighbors


def part1(lines, num_steps):
    flash_count = 0

    for step in range(num_steps):
        flashed = set()
        prev_lines = [line[:] for line in lines]

        for y, line in enumerate(lines):
            for x, val in enumerate(line):
                lines[y][x] = val + 1

        while lines != prev_lines:
            prev_lines = [line[:] for line in lines]
            for y, line in enumerate(lines):
                for x, val in enumerate(line):
                    if val > 9 and (x, y) not in flashed:
                        flashed.add((x, y))
                        flash_count += 1
                        neighbors = get_neighbors(x, y, lines)
                        for nx, ny in neighbors:
                            lines[ny][nx] += 1

        for y, line in enumerate(lines):
            for x, val in enumerate(line):
                if val > 9:
                    lines[y][x] = 0

    return flash_count


def part2(lines, test_dict):
    flash_count = 0
    i = 0

    while True:
        i += 1
        flashed = set()
        prev_lines = [line[:] for line in lines]

        # First, the energy level of each octopus increases by 1
        for y, line in enumerate(lines):
            for x, val in enumerate(line):
                lines[y][x] = val + 1

        while lines != prev_lines:
            prev_lines = [line[:] for line in lines]
            for y, line in enumerate(lines):
                for x, val in enumerate(line):
                    if val > 9 and (x, y) not in flashed:
                        flashed.add((x, y))
                        flash_count += 1
                        neighbors = get_neighbors(x, y, lines)
                        for nx, ny in neighbors:
                            lines[ny][nx] += 1

        for y, line in enumerate(lines):
            for x, val in enumerate(line):
                if val > 9:
                    lines[y][x] = 0
        # if i in [133, 134, 135]:
        #     for y, line in enumerate(lines):
        #         for x, val in enumerate(line):
        #             if val > 9:
        #                 print('*', end='')
        #             else:
        #                 print(val, end='')
        #         print()
        #     print()
        if i in test_dict:
            matches = 'matches' if test_dict[i] == lines else 'does not match'
            print(f'step {i} {matches}')
        if len(flashed) == 100:
            return i

if __name__ == '__main__':
    lines = [list(map(int, x)) for x in get_lines_for_day(2021, 11)]
    test_lines = [list(map(int, x)) for x in get_lines_for_day(2021, '11_test')]
    test_cases = get_lines_for_day(2021, '11_test_cases')
    # inp = get_input_for_day(2021, 11)
    groups = get_groups(test_cases)
    test_dict = {}
    for group in groups:
        test_step = int(group[0].split('After step ')[1][:-1])
        test_dict[test_step] = [list(map(int, x)) for x in group[1:]]

    print(part1(lines, 100))
    # 9821 is too high
    print(part2(test_lines, test_dict))
    # 135 is too low
