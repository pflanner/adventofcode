from util import get_lines_for_day


def f(lines):
    line = list(map(int, lines[0]))
    result = 0

    for i, a in enumerate(line):
        b = line[(i + len(line) // 2) % len(line)]
        if a == b:
            result += a

    return result


print(f(get_lines_for_day(2017, 1)))
