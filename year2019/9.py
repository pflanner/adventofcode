from util import get_lines_for_day
from enum import Enum, auto


intcomputer_id = 0


class AutoexpandingList(list):
    def __setitem__(self, key, value):
        if key >= len(self):
            self.extend([0] * (key - len(self) + 1))
        super().__setitem__(key, value)

    def __getitem__(self, key):
        if key >= len(self):
            return 0
        return super().__getitem__(key)


class Mode(Enum):
    POSITION = '0'
    IMMEDIATE = '1'
    RELATIVE = '2'

class Intcomputer:
    def __init__(self, opcodes):
        global intcomputer_id
        self.id = intcomputer_id
        intcomputer_id += 1
        self.opcodes = AutoexpandingList(opcodes)
        self.i = 0
        self.relative_base = 0

    @staticmethod
    def _get_modes(code):
        mode1 = mode2 = mode3 = Mode.POSITION

        if len(code) > 2:
            mode1 = Mode(code[-3])
        if len(code) > 3:
            mode2 = Mode(code[-4])
        if len(code) > 4:
            mode3 = Mode(code[-5])

        return mode1, mode2, mode3

    def run(self, inp):
        while True:
            code = self.opcodes[self.i]
            mode1, mode2, mode3 = self._get_modes(code)

            if code == '99':
                print('Halted')
                return None

            arg1 = write_arg1 = int(self.opcodes[self.i + 1])
            if mode1 == Mode.POSITION:
                arg1 = int(self.opcodes[arg1])
            elif mode1 == Mode.RELATIVE:
                arg1 = int(self.opcodes[arg1 + self.relative_base])

            # opcodes with 2 args
            if code[-1] in ['1', '2', '5', '6', '7', '8']:
                arg2 = self.opcodes[self.i + 2]
                if mode2 == Mode.POSITION:
                    arg2 = self.opcodes[int(arg2)]
                elif mode2 == Mode.RELATIVE:
                    arg2 = self.opcodes[int(arg2) + self.relative_base]
                arg2 = int(arg2)

                # opcodes with 3 args
                if code[-1] in ['1', '2', '7', '8']:
                    arg3 = int(self.opcodes[self.i + 3])
                    if mode3 == Mode.RELATIVE:
                        arg3 = arg3 + self.relative_base

            arg1 = int(arg1)

            if code.endswith('1'):
                self.opcodes[arg3] = str(arg1 + arg2)
                self.i += 4
            elif code.endswith('2'):
                self.opcodes[arg3] = str(arg1 * arg2)
                self.i += 4
            elif code.endswith('3'):
                if mode1 == Mode.RELATIVE:
                    self.opcodes[write_arg1 + self.relative_base] = inp
                else:
                    self.opcodes[write_arg1] = inp
                self.i += 2
            elif code.endswith('4'):
                self.i += 2
                print(arg1)
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
            elif code.endswith('9'):
                self.relative_base += arg1
                self.i += 2
            else:
                print('Something went wrong')
                return None


def part1(opcodes):
    intcomputer = Intcomputer(opcodes)
    intcomputer.run('1')


def part2(opcodes):
    intcomputer = Intcomputer(opcodes)
    intcomputer.run('2')


if __name__ == '__main__':
    opcodes = get_lines_for_day(2019, 9)[0].split(',')
    test = [
        '109',
        '1',
        '204',
        '-1',
        '1001',
        '100',
        '1',
        '100',
        '1008',
        '100',
        '16',
        '101',
        '1006',
        '101',
        '0',
        '99'
    ]

    part1(opcodes)
    part2(opcodes)