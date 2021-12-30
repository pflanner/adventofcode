from util import get_lines_for_day
from itertools import combinations


def f(lines):
    checksum = 0

    for line in lines:
        nums = list(map(int, line.split()))
        checksum += max(nums) - min(nums)

    return checksum


def g(lines):
    checksum = 0

    for line in lines:
        nums = list(map(int, line.split()))
        for a, b in combinations(nums, 2):
            m = min(a, b)
            n = max(a, b)
            if n % m == 0:
                checksum += n // m

    return checksum


print(g(get_lines_for_day(2017, 2)))
