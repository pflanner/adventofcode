from util import get_lines_for_day
from itertools import permutations
from math import ceil


def add(a, b):
    if not a:
        return b

    pair = ['['] + a + [','] + b + [']']
    was_exploded = was_split = True

    while was_exploded or was_split:
        was_exploded = was_split = False
        i = 0
        level = 0
        while i < len(pair):
            c = pair[i]
            if c == '[':
                level += 1
                if level == 5:
                    pair = explode(pair, i + 1)
                    was_exploded = True
                    break
            elif c == ']':
                level -= 1
            i += 1

        if was_exploded:
            continue

        i = 0
        while i < len(pair):
            c = pair[i]
            if isinstance(c, int) and c >= 10:
                pair = split(pair, i)
                was_split = True
                break
            i += 1

    return pair

def explode(pair, i):
    new_pair = []
    left_num = pair[i]
    right_num = pair[i+2]

    # mark current pair for zeroing
    for j in range(i-1, i+4):
        pair[j] = '-'
    pair[i] = 0

    # add left_num to next num to the left
    j = i - 1
    while j >= 0:
        if isinstance(pair[j], int):
            pair[j] += left_num
            break
        j -= 1

    # add right_num to the next num to the right
    j = i + 4
    while j < len(pair):
        if isinstance(pair[j], int):
            pair[j] += right_num
            break
        j += 1

    # create the new pair
    for c in pair:
        if c != '-':
            new_pair.append(c)

    return new_pair

def split(pair, i):
    num_to_split = pair[i]
    left_num = num_to_split // 2
    right_num = ceil(num_to_split / 2)

    to_insert = ['[', left_num, ',', right_num, ']']

    new_pair = []

    for j, c in enumerate(pair):
        if j == i:
            new_pair.extend(to_insert)
        else:
            new_pair.append(c)

    return new_pair


def calc_magnitude(n):
    if isinstance(n, int):
        return n
    return 3*calc_magnitude(n[0]) + 2*calc_magnitude(n[1])


def parse_pair(pair):
    new_pair = []
    i = 0
    while i < len(pair):
        c = pair[i]
        if c.isnumeric():
            j = i
            while pair[j].isnumeric():
                j += 1
            new_pair.append(int(''.join(pair[i:j])))
            i = j - 1
        else:
            new_pair.append(c)
        i += 1
    return new_pair


def part1(lines):
    l1 = []

    for l2 in lines:
        l1 = add(l1, parse_pair(list(l2)))

    l1 = eval(''.join(str(c) for c in l1))

    return calc_magnitude(l1)


def part2(lines):
    pairs = [parse_pair(list(line)) for line in lines]
    largest = 0

    for pair1, pair2 in permutations(pairs, 2):
        result = eval(''.join(str(c) for c in add(pair1, pair2)))
        largest = max(largest, calc_magnitude(result))

    return largest


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 18)

    print(part1(lines))
    print(part2(lines))