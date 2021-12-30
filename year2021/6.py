from util import get_lines_for_day, get_input_for_day, get_groups

from collections import defaultdict, Counter
from itertools import combinations, permutations
from functools import reduce
from operator import attrgetter, itemgetter


def part1(param):
    fish = list(param)
    days = [0] * 80
    days[0] = len(fish)

    for d in range(80):
        new_fish = []
        for i, f in enumerate(fish):
            if f == 0:
                new_fish.append(8)
                fish[i] = 6
            else:
                fish[i] -= 1
        fish += new_fish
        if d > 0:
            days[d] = len(new_fish)

    print(days)
    return len(fish)


def part2(fish, num_days):
    days = [0] * num_days
    days[0] = len(fish)

    for i, f in enumerate(fish):
        while f < num_days:
            days[f] += 1
            f += 7

    for i in range(1, num_days):
        d = days[i]
        j = i + 9
        while j < num_days:
            days[j] += d
            j += 7

    return sum(days)


def part2_2(start_fish, num_days):
    days = [0] * num_days
    days[0] = len(start_fish)

    for f in start_fish:
        for day in range(f, num_days, 7):
            days[day] += 1

    for i in range(1, num_days):
        for day in range(i + 9, num_days, 7):
            days[day] += days[i]

    return sum(days)


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 6)
    # inp = get_input_for_day(2021, 6)
    groups = get_groups(lines)

    # print(part1(map(int, lines[0].split(','))))
    print(part2([int(n) for n in lines[0].split(',')], 80))
    print(part2([int(n) for n in lines[0].split(',')], 256))
    print(part2_2([int(n) for n in lines[0].split(',')], 80))
    print(part2_2([int(n) for n in lines[0].split(',')], 256))

    """
    [300, 155, 33, 45, 41, 26, 0, 0, 155, 33, 200, 74, 71, 41, 26, 155, 33, 355, 107, 271, 115, 97, 196, 59, 510, 140, 626, 222, 368, 311, 156, 706, 199, 1136, 362, 994, 533, 524, 1017, 355, 1842, 561, 2130, 895, 1518, 1550, 879, 2859, 916, 3972, 1456, 3648, 2445, 2397, 4409, 1795, 6831, 2372, 7620, 3901, 6045, 6854, 4192, 11240, 4167, 14451, 6273, 13665, 10755, 10237, 18094, 8359, 25691, 10440, 28116, 17028, 23902, 28849, 18596, 43785]
    375482
    [300, 155, 33, 45, 41, 26, 0, 0, 155, 33, 200, 74, 71, 41, 26, 155, 33, 355, 107, 116, 82, 52, 155, 33, 510, 140, 161, 123, 78, 155, 33, 665, 173, 206, 164, 104, 155, 33, 820, 206, 251, 205, 130, 155, 33, 975, 239, 296, 246, 156, 155, 33, 1130, 272, 341, 287, 182, 155, 33, 1285, 305, 386, 328, 208, 155, 33, 1440, 338, 431, 369, 234, 155, 33, 1595, 371, 476, 410, 260, 155, 33]
    20288
    """
