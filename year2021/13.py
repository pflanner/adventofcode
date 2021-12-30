from util import get_lines_for_day, get_input_for_day, get_groups

from collections import defaultdict, Counter, deque
from itertools import combinations, permutations
from functools import reduce
from operator import attrgetter, itemgetter
from math import factorial


def part1(points, fx, fy):
    new_points = set()
    for px, py in points:
        if 0 < fx < px:
            nx = fx - (px - fx)
            new_points.add((nx, py))
        elif 0 < fy < py:
            ny = fy - (py - fy)
            new_points.add((px, ny))
        else:
            new_points.add((px, py))

    return len(new_points)


def part2(points, folds, w, h):

    for fx, fy in folds:
        if fx > 0:
            w = w // 2 - 1
        else:
            h = h // 2 - 1
        new_points = set()
        for px, py in points:
            if 0 < fx < px:
                nx = fx - (px - fx)
                new_points.add((nx, py))
            elif 0 < fy < py:
                ny = fy - (py - fy)
                new_points.add((px, ny))
            else:
                new_points.add((px, py))
        points = new_points

    return points, w, h


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 13)
    test_lines = get_lines_for_day(2021, '13_test')
    # inp = get_input_for_day(2021, 13)
    groups = get_groups(lines)
    width = height = 0
    point_set = set()

    for line in groups[0]:
        x, y = map(int, line.split(','))
        point_set.add((x, y))
        width = max(width, x + 1)
        height = max(height, y + 1)

    fold_list = []
    for line in groups[1]:
        f = line.split('fold along ')[1]
        axis, val = f.split('=')
        if axis == 'x':
            fold_list.append((int(val), 0))
        else:
            fold_list.append((0, int(val)))

    print(part1(point_set, *fold_list[0]))
    print()
    result_points, new_width, new_height = part2(point_set, fold_list, width, height)
    for y in range(new_height + 1):
        for x in range(new_width + 1):
            if (x, y) in result_points:
                print('#', end='')
            else:
                print(' ', end='')
        print()
