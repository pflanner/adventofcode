from util import get_lines_for_day


def func(lines, times=5000000):
    divisor = 2147483647
    factora, factorb = 16807, 48271
    a, b = (int(line.split()[-1]) for line in lines)
    matches = 0

    for _ in range(times):
        while a % 4 != 0:
            a = (a * factora) % divisor

        while b % 8 != 0:
            b = (b * factorb) % divisor

        if a & (2**16 - 1) == b & (2**16 - 1):
            matches += 1

        a = (a * factora) % divisor
        b = (b * factorb) % divisor

    return matches


print(func(get_lines_for_day(2017, 15)))
