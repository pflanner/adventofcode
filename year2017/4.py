from util import get_lines_for_day
from itertools import permutations


def f(lines):
    count = 0

    for line in lines:
        s = set()

        for word in line.split():
            if tuple(word) in s:
                break
            s.update(permutations(word))
        else:
            count += 1

    return count


print(f(get_lines_for_day(2017, 4)))
