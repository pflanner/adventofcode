from util import get_lines_for_day, get_input_for_day, get_groups

from collections import defaultdict, Counter, deque
from itertools import combinations, permutations
from functools import reduce
from operator import attrgetter, itemgetter
from math import factorial

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

scores2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

match = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

rev = {v: k for k, v in match.items()}


def part1(lines):
    points = 0
    for line in lines:
        stack = []
        for c in line:
            if c in match:
                if stack[-1] != match[c]:
                    points += scores[c]
                    break
                else:
                    stack.pop()
            else:
                stack.append(c)
    return points

def part2(lines):
    all_points = []
    for line in lines:
        points = 0
        stack = []
        corrupt = False
        for c in line:
            if c in match:
                if stack[-1] != match[c]:
                    corrupt = True
                    break
                else:
                    stack.pop()
            else:
                stack.append(c)
        if not corrupt:
            for cc in reversed(stack):
                points *= 5
                points += scores2[rev[cc]]
            all_points.append(points)
    return sorted(all_points)[len(all_points) // 2]


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 10)
    test_lines = get_lines_for_day(2021, '10_test')
    # inp = get_input_for_day(2021, 10)
    groups = get_groups(lines)

    print(part1(lines))
    # 976359 is not right
    print(part2(lines))
    # 1638 is not right
    # 3040537471 is not right
