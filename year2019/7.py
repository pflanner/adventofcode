from util import get_lines_for_day
from itertools import permutations


intcomputer_id = 0


class Intcomputer:
    def __init__(self, opcodes, phase):
        global intcomputer_id
        self.id = intcomputer_id
        intcomputer_id += 1
        self.opcodes = opcodes
        self.phase = phase
        self.is_phase_set = False
        self.i = 0

    def run(self, inp):
        while self.i < len(self.opcodes):
            code = self.opcodes[self.i]
            if code == '99':
                return None

            arg1 = self.opcodes[self.i + 1]
            # opcodes with 2 args
            if code[-1] in ['1', '2', '5', '6', '7', '8']:
                if len(code) <= 2 or (len(code) > 2 and code[-3] == '0'):
                    arg1 = self.opcodes[int(arg1)]
                arg2 = self.opcodes[self.i + 2]
                if len(code) <= 3 or (len(code) > 3 and code[-4] == '0'):
                    arg2 = self.opcodes[int(arg2)]
                arg2 = int(arg2)

                # opcodes with 3 args
                if code[-1] in ['1', '2', '7', '8']:
                    arg3 = int(self.opcodes[self.i + 3])

            arg1 = int(arg1)

            if code.endswith('1'):
                self.opcodes[arg3] = str(arg1 + arg2)
                self.i += 4
            elif code.endswith('2'):
                self.opcodes[arg3] = str(arg1 * arg2)
                self.i += 4
            elif code.endswith('3'):
                if not self.is_phase_set:
                    self.opcodes[arg1] = self.phase
                    self.is_phase_set = True
                else:
                    self.opcodes[arg1] = inp
                self.i += 2
            elif code.endswith('4'):
                if len(code) <= 2 or (len(code) > 2 and code[-3] == '0'):
                    arg1 = self.opcodes[int(arg1)]
                self.i += 2
                return arg1
            elif code.endswith('5'):
                if arg1 != 0:
                    self.i = arg2
                else:
                    self.i += 3
            elif code.endswith('6'):
                if arg1 == 0:
                    self.i = arg2
                else:
                    self.i += 3
            elif code.endswith('7'):
                if arg1 < arg2:
                    self.opcodes[arg3] = '1'
                else:
                    self.opcodes[arg3] = '0'
                self.i += 4
            elif code.endswith('8'):
                if arg1 == arg2:
                    self.opcodes[arg3] = '1'
                else:
                    self.opcodes[arg3] = '0'
                self.i += 4
            else:
                print('Something went wrong')
                return None


def calc_signal(phases, lines):
    inp = '0'
    for phase in phases:
        ic = Intcomputer(lines[:], str(phase))
        inp = ic.run(inp)
    return inp


def calc_feedback_loop(phases, lines):
    inp = '0'
    halt = False
    intcomputers = {}
    to_thrusters = 0
    while not halt:
        for i, phase in enumerate(phases):
            intcomputer = intcomputers.get(i, Intcomputer(lines[:], phase))
            intcomputers[i] = intcomputer
            inp = intcomputer.run(inp)
            if i == len(phases) - 1:
                to_thrusters = inp
            if inp is None:
                halt = True
                break

    return to_thrusters


def part1(lines):
    largest = 0
    inp = '0'
    for p in permutations(range(5), 5):
        for phase in p:
            ic = Intcomputer(lines[:], str(phase))
            inp = ic.run(inp)
        largest = max(largest, int(inp))
        inp = '0'

    return largest


def part2(lines):
    largest = 0
    inp = '0'
    for p in permutations(range(5, 10), 5):
        halt = False
        intcomputers = {}
        to_thrusters = 0
        while not halt:
            for i, phase in enumerate(p):
                intcomputer = intcomputers.get(i, Intcomputer(lines[:], phase))
                intcomputers[i] = intcomputer
                inp = intcomputer.run(inp)
                if i == len(p) - 1:
                    to_thrusters = inp
                if inp is None:
                    halt = True
                    break

            largest = max(largest, int(to_thrusters))
        inp = '0'

    return largest


if __name__ == '__main__':
    # print(part1(get_lines_for_day(2019, 7)[0].split(",")))
    print(part2(get_lines_for_day(2019, 7)[0].split(",")))
    # print(calc_feedback_loop('97856', get_lines_for_day(2019, '7_test')[0].split(',')))
