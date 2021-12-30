from util import get_lines_for_day


def part1(opcodes, noun=12, verb=2):
    opcodes[1] = noun
    opcodes[2] = verb

    for i in range(0, len(opcodes), 4):
        code, arg1, arg2, out = opcodes[i], opcodes[i + 1], opcodes[i + 2], opcodes[i + 3]

        if code == 99:
            return opcodes[0]
        elif code == 1:
            opcodes[out] = opcodes[arg1] + opcodes[arg2]
        elif code == 2:
            opcodes[out] = opcodes[arg1] * opcodes[arg2]
        else:
            print('Something went wrong')
            return None


def part2(opcodes):
    for noun in range(100):
        for verb in range(100):
            new_ops = opcodes[:]
            new_ops[1] = noun
            new_ops[2] = verb

            if part1(new_ops, noun, verb) == 19690720:
                return 100*noun + verb

    return -1


if __name__ == '__main__':
    ops = list(map(int, get_lines_for_day(2019, 2)[0].split(',')))
    print(part1(ops[:]))
    print(part2(ops[:]))
