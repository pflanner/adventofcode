from util import get_input_for_day


def part1():
    todays_input = get_input_for_day(9)
    lines = todays_input.strip().split('\n')

    for i in range(25, len(lines)):
        preamble = lines[i-25:i]
        sums = set()
        for j in range(len(preamble) - 1):
            for k in range(j + 1, len(preamble)):
                sums.add(int(preamble[j]) + int(preamble[k]))

        if int(lines[i]) not in sums:
            print(lines[i])
            return


answer_from_part1 = 36845998


def part2():
    todays_input = get_input_for_day(9)
    lines = todays_input.strip().split('\n')

    for i in range(len(lines) - 1):
        for j in range(i, len(lines)):
            if sum(map(int, lines[i:j + 1])) == answer_from_part1:
                print(int(lines[i]) + int(lines[j]))
                return


part2()
