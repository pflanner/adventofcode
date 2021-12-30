from util import get_lines_for_day, get_input_for_day, get_groups


def part1(param):
    pos = depth = 0
    for line in param:
        command, n = line.split()
        n = int(n)
        if command == 'forward':
            pos += n
        if command == 'down':
            depth += n
        if command == 'up':
            depth -= n

    return pos * depth


def part2(param):
    pos = depth = aim = 0
    for line in param:
        command, n = line.split()
        n = int(n)
        if command == 'forward':
            pos += n
            depth += n * aim
        if command == 'down':
            aim += n
        if command == 'up':
            aim -= n

    return pos * depth


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 2)
    # inp = get_input_for_day(2021, 2)
    # groups = get_groups(lines)

    print(part1(lines))
    print(part2(lines))
