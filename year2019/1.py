from util import get_lines_for_day


def part1(lines):
    total = 0
    for line in lines:
        total += int(line) // 3 - 2

    return total


def part2(lines):
    total = 0
    for line in lines:
        total += calc_fuel(int(line))

    return total


def calc_fuel(weight):
    if weight <= 0:
        return 0

    fuel = max(weight // 3 - 2, 0)

    cf = calc_fuel(fuel)

    return fuel + cf


if __name__ == '__main__':
    print(part1(get_lines_for_day(2019, 1)))
    print(part2(get_lines_for_day(2019, 1)))
