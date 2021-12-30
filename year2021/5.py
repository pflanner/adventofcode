from util import get_lines_for_day, get_input_for_day, get_groups
from collections import defaultdict, Counter
from itertools import combinations, permutations
from functools import reduce
from operator import attrgetter, itemgetter


def part1(param):
    points = set()
    overlap = set()
    for line in param:
        one, two = line.split(' -> ')
        x1, y1 = map(int, one.split(','))
        x2, y2 = map(int, two.split(','))

        if x1 == x2:
            ystart = min(y1, y2)
            yend = max(y1, y2)

            for i in range(ystart, yend + 1):
                point = (x1, i)
                if point in points:
                    overlap.add(point)
                points.add(point)
        elif y1 == y2:
            xstart = min(x1, x2)
            xend = max(x1, x2)

            for i in range(xstart, xend + 1):
                point = (i, y1)
                if point in points:
                    overlap.add(point)
                points.add((i, y1))
        else:
            xstart = min(x1, x2)
            xend = max(x1, x2)
            ystart = y1 if xstart == x1 else y2

            for i, j in enumerate(range(xstart, xend + 1)):
                point = (j, ystart + i) if ystart < y2 or ystart < y1 else (j, ystart - i)
                if point in points:
                    overlap.add(point)
                points.add(point)
    return len(overlap)



def part2(param):

    return None


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 5)
    # inp = get_input_for_day(2021, 5)
    groups = get_groups(lines)

    print(part1(lines))
    #7334 is not right
    #5992 is not right
    print(part2(lines))
    #19092 is not right
