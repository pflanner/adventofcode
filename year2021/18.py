from util import get_lines_for_day
from itertools import permutations
from math import ceil


class Adder:
    def __init__(self):
        self.level = 0

    def add(self, a, b):
        if not a:
            return b

        pair = ['['] + a + [','] + b + [']']
        exploded = split = True
        while exploded or split:
            exploded = split = False
            i = 0
            while i < len(pair):
                c = pair[i]
                if c == '[':
                    self.level += 1
                    if self.level == 5:
                        pair = self.explode(pair, i + 1)
                        i = 0
                        self.level = 0
                        exploded = True
                        break
                elif c == ']':
                    self.level -= 1
                i += 1

            if exploded:
                continue

            i = 0
            while i < len(pair):
                c = pair[i]
                if isinstance(c, int) and c >= 10:
                    pair = self.split(pair, i)
                    i = 0
                    self.level = 0
                    split = True
                    break
                i += 1

        return pair

    def explode(self, pair, i):
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

    def split(self, pair, i):
        num_to_split = pair[i]
        left_num = num_to_split // 2
        right_num = ceil(num_to_split / 2)

        to_insert = ['['] + [left_num] + [','] + [right_num] + [']']

        new_pair = []

        for j, c in enumerate(pair):
            if j == i:
                new_pair.extend(to_insert)
            else:
                new_pair.append(c)

        return new_pair


def calc_magnitude(n):
    left, right = n

    if isinstance(left, int) and isinstance(right, int):
        return 3*left + 2*right
    elif isinstance(left, int):
        return 3*left + 2*calc_magnitude(right)
    elif isinstance(right, int):
        return 3*calc_magnitude(left) + 2*right
    else:
        return 3*calc_magnitude(left) + 2*calc_magnitude(right)


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
        adder = Adder()
        l1 = adder.add(l1, parse_pair(list(l2)))

    l1 = eval(''.join(str(c) for c in l1))


    return calc_magnitude(l1)


def part2(lines):
    pairs = [parse_pair(list(line)) for line in lines]
    largest = 0

    for pair1, pair2 in permutations(pairs, 2):
        adder = Adder()
        result = adder.add(pair1, pair2)
        n = eval(''.join(str(c) for c in result))
        largest = max(largest, calc_magnitude(n))

    return largest


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 18)

    print(part1(lines))
    print(part2(lines))