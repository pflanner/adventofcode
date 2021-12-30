from util import get_lines_for_day


def f(lines):
    instructions = list(map(int, lines))

    i = count = 0

    while 0 <= i < len(instructions):
        jump = instructions[i]

        if jump >= 3:
            instructions[i] -= 1
        else:
            instructions[i] += 1

        i += jump
        count += 1

    return count


print(f(get_lines_for_day(2017, 5)))

