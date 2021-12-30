from util import get_lines_for_day
from time import sleep


class Instruction:
    def __init__(self, line):
        line = line.split()

        self.op = line[0]
        self.a = int(line[1])
        self.b = int(line[2])
        self.c = int(line[3])

    def __repr__(self):
        return f'{self.op: <5}{self.a: >8}{self.b: >9}{self.c: >2}'


def print_state(instructions, registers, i, print_delay):
    print('\033c')

    print(registers)
    print()

    for idx, instruction in enumerate(instructions):
        s = repr(instruction)
        caret = '<' if i == idx else ''
        print(f'{s: <15}{caret: <2}{idx: >3}')

    if print_delay > 0:
        sleep(print_delay)


def f(lines, should_print=False, print_delay=0.1, stop_per_iteration=False):
    registers = [0] * 8
    registers[0] = 0
    instructions = []

    for line in lines:
        if line.startswith('#'):
            registers[6] = int(line.split()[1])
        else:
            instructions.append(Instruction(line))

    while 0 <= registers[7] < len(instructions):
        if should_print:
            print_state(instructions, registers, registers[7], print_delay)

        # shortcut for day 19
        # if registers[7] == 3:
        #     registers[4] = registers[2] + 1
        #     registers[5] = 1
        #     registers[0] += registers[1]
        #     registers[7] = 12
        #     continue

        # set the bound register to the value of the instruction pointer
        registers[registers[6]] = registers[7]

        instruction = instructions[registers[7]]

        if instruction.op == 'addr':
            registers[instruction.c] = registers[instruction.a] + registers[instruction.b]
        elif instruction.op == 'addi':
            registers[instruction.c] = registers[instruction.a] + instruction.b
        elif instruction.op == 'mulr':
            registers[instruction.c] = registers[instruction.a] * registers[instruction.b]
        elif instruction.op == 'muli':
            registers[instruction.c] = registers[instruction.a] * instruction.b
        elif instruction.op == 'banr':
            registers[instruction.c] = registers[instruction.a] & registers[instruction.b]
        elif instruction.op == 'bani':
            registers[instruction.c] = registers[instruction.a] & instruction.b
        elif instruction.op == 'borr':
            registers[instruction.c] = registers[instruction.a] | registers[instruction.b]
        elif instruction.op == 'bori':
            registers[instruction.c] = registers[instruction.a] | instruction.b
        elif instruction.op == 'setr':
            registers[instruction.c] = registers[instruction.a]
        elif instruction.op == 'seti':
            registers[instruction.c] = instruction.a
        elif instruction.op == 'gtir':
            registers[instruction.c] = 1 if instruction.a > registers[instruction.b] else 0
        elif instruction.op == 'gtri':
            registers[instruction.c] = 1 if registers[instruction.a] > instruction.b else 0
        elif instruction.op == 'gtrr':
            registers[instruction.c] = 1 if registers[instruction.a] > registers[instruction.b] else 0
        elif instruction.op == 'eqir':
            registers[instruction.c] = 1 if instruction.a == registers[instruction.b] else 0
        elif instruction.op == 'eqri':
            registers[instruction.c] = 1 if registers[instruction.a] == instruction.b else 0
        elif instruction.op == 'eqrr':
            registers[instruction.c] = 1 if registers[instruction.a] == registers[instruction.b] else 0

        # write the value of the bound register back to the instruction pointer
        registers[7] = registers[registers[6]]

        registers[7] += 1

        if stop_per_iteration:
            input('Enter to continue')

    return registers[0]


def g():
    count = 0

    # add up all of the factors of 10551305
    for i in range(1, 10551305 + 1):
        if 10551305 % i == 0:
            count += i

    return count


print(f(get_lines_for_day(2018, '19_test_21'), should_print=True, print_delay=0.3, stop_per_iteration=True))
# print(g())
# part 2
# 55665023877165 is too high
# 13406472 is the right answer
