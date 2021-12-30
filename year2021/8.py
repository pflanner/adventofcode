from util import get_lines_for_day, get_input_for_day, get_groups

from collections import defaultdict, Counter
from itertools import combinations, permutations
from functools import reduce
from operator import attrgetter, itemgetter
from math import factorial

def part1(entries):
    nums = 0
    for entry in entries:
        signal, output = entry.split(' | ')
        output = output.split()
        for o in output:
            if len(o) in [2, 3, 4, 7]:
                nums += 1
    return nums


def part2(entries):
    total = 0

    for entry in entries:
        code_to_int = {}
        int_to_code = {}
        signal, output = entry.split(' | ')
        signal = [''.join(sorted(s)) for s in signal.split()]
        output = [''.join(sorted(o)) for o in output.split()]
        segments = [None] * 7

        for o in output + signal:
            if len(o) == 2:
                code_to_int[o] = 1
                int_to_code[1] = o
            elif len(o) == 3:
                code_to_int[o] = 7
                int_to_code[7] = o
            elif len(o) == 4:
                code_to_int[o] = 4
                int_to_code[4] = o
            elif len(o) == 7:
                code_to_int[o] = 8
                int_to_code[8] = o

        for o in output + signal:
            if len(o) == 5 and set(int_to_code[1]).issubset(set(o)):
                code_to_int[o] = 3
                int_to_code[3] = o
            elif len(o) == 6 and set(int_to_code[4]).issubset(o):
                code_to_int[o] = 9
                int_to_code[9] = o

        for o in output + signal:
            if len(o) == 6 and set(int_to_code[1]).issubset(o) and o != int_to_code[9]:
                code_to_int[o] = 0
                int_to_code[0] = o

        for o in output + signal:
            if len(o) == 6 and o != int_to_code[0] and o != int_to_code[9]:
                code_to_int[o] = 6
                int_to_code[6] = o

        # at this point we have 1, 3, 4, 7, 8, 9

        # 5 segments left = 2, 5
        # 6 segments left = 6, 0

        segments[0] = next(iter(set(int_to_code[9]) - set(int_to_code[4]) - set(int_to_code[7])))
        segments[1] = next(iter(set(int_to_code[4]) - set(int_to_code[3])))
        segments[4] = next(iter(set(int_to_code[8]) - set(int_to_code[9])))
        segments[6] = next(iter(set(int_to_code[9]) - set(int_to_code[4]) - {segments[0]}))

        for o in output + signal:
            if len(o) == 5 and segments[1] in o:
                code_to_int[o] = 5
                int_to_code[5] = o

        for o in output + signal:
            if len(o) == 5 and segments[1] not in o and o != int_to_code[3]:
                code_to_int[o] = 2
                int_to_code[2] = o

        answer = 0
        for o in output:
            answer *= 10
            answer += code_to_int[o]

        print(answer)
        total += answer

    return total


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 8)
    test_lines = get_lines_for_day(2021, '8_test')
    # inp = get_input_for_day(2021, 8)
    groups = get_groups(lines)

    print(part1(lines))
    print(part2(lines))
    # 822053 is too low
