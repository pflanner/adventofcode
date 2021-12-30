from util import get_lines_for_day


def part1(opcodes):
    i = 0
    while i < len(opcodes):
        code = opcodes[i]
        if code == '99':
            return opcodes[0]

        arg1 = opcodes[i + 1]
        if code.endswith('1') or code.endswith('2'):
            if len(code) <= 2 or (len(code) > 2 and code[-3] == '0'):
                arg1 = opcodes[int(arg1)]
            arg2, arg3 = opcodes[i + 2], opcodes[i + 3]
            if len(code) <= 3 or (len(code) > 3 and code[-4] == '0'):
                arg2 = opcodes[int(arg2)]
            arg2,arg3 = int(arg2), int(arg3)

        arg1 = int(arg1)

        if code.endswith('1'):
            opcodes[arg3] = str(arg1 + arg2)
            i += 4
        elif code.endswith('2'):
            opcodes[arg3] = str(arg1 * arg2)
            i += 4
        elif code.endswith('3'):
            inp = input('enter your input:')
            opcodes[arg1] = inp
            i += 2
        elif code.endswith('4'):
            if len(code) <= 2 or (len(code) > 2 and code[-3] == '0'):
                arg1 = opcodes[int(arg1)]
            print(arg1)
            i += 2
        else:
            print('Something went wrong')
            return None


def part2(opcodes):
    i = 0
    while i < len(opcodes):
        code = opcodes[i]
        if code == '99':
            return opcodes[0]

        arg1 = opcodes[i + 1]
        # opcodes with 2 args
        if code[-1] in ['1', '2', '5', '6', '7', '8']:
            if len(code) <= 2 or (len(code) > 2 and code[-3] == '0'):
                arg1 = opcodes[int(arg1)]
            arg2 = opcodes[i + 2]
            if len(code) <= 3 or (len(code) > 3 and code[-4] == '0'):
                arg2 = opcodes[int(arg2)]
            arg2 = int(arg2)

            # opcodes with 3 args
            if code[-1] in ['1', '2', '7', '8']:
                arg3 = int(opcodes[i + 3])

        arg1 = int(arg1)

        if code.endswith('1'):
            opcodes[arg3] = str(arg1 + arg2)
            i += 4
        elif code.endswith('2'):
            opcodes[arg3] = str(arg1 * arg2)
            i += 4
        elif code.endswith('3'):
            inp = input('enter your input:')
            opcodes[arg1] = inp
            i += 2
        elif code.endswith('4'):
            if len(code) <= 2 or (len(code) > 2 and code[-3] == '0'):
                arg1 = opcodes[int(arg1)]
            print(arg1)
            i += 2
        elif code.endswith('5'):
            if arg1 != 0:
                i = arg2
            else:
                i += 3
        elif code.endswith('6'):
            if arg1 == 0:
                i = arg2
            else:
                i += 3
        elif code.endswith('7'):
            if arg1 < arg2:
                opcodes[arg3] = '1'
            else:
                opcodes[arg3] = '0'
            i += 4
        elif code.endswith('8'):
            if arg1 == arg2:
                opcodes[arg3] = '1'
            else:
                opcodes[arg3] = '0'
            i += 4
        else:
            print('Something went wrong')
            return None



if __name__ == '__main__':
    ops = list(get_lines_for_day(2019, 5)[0].split(','))
    # print(part1(list(map(str, [1002,4,3,4,33]))))
    # print(part1(ops[:]))
    print(part2(ops[:]))
