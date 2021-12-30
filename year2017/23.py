from util import get_lines_for_day
import string


def get_value(arg, reg):
    try:
        return int(arg)
    except:
        return reg[arg]


def print_state(instructions, pos, registers):
    # clear
    print('\033c')

    print(registers)

    col_width = 15

    for i, instruction in enumerate(instructions):
        marker = '<' if pos == i else ''
        line = f'{str(i).rjust(2)} {instruction.ljust(col_width)}{marker}'
        print(line)


def f(lines, debug_mode=True):
    registers = {c: 0 for c in string.ascii_lowercase[:8]}
    if not debug_mode:
        registers['a'] = 1
    mul_count = 0
    i = 0

    while 0 <= i < len(lines):
        # print_state(lines, i, registers)
        # time.sleep(0.2)

        # optimizations
        if i == 10:
            registers['e'] = registers['b']
            i = 20
            if registers['g'] == 0:
                registers['f'] = 0
            continue

        if i == 20:
            registers['d'] = registers['b']
            i = 24
            continue

        line = lines[i].split()
        op = line[0]
        arg1 = line[1]
        arg2 = get_value(line[2], registers)

        if op == 'set':
            registers[arg1] = arg2
        elif op == 'sub':
            registers[arg1] -= arg2
        elif op == 'mul':
            registers[arg1] *= arg2
            mul_count += 1
        elif op == 'jnz':
            if get_value(arg1, registers) != 0:
                i += arg2
                continue

        i += 1

    return registers['h']


def g(debug_mode=False):
    registers = {c: 0 for c in string.ascii_lowercase[:8]}

    registers['b'] = 65
    registers['c'] = 65

    if not debug_mode:
        registers['b'] = 106500
        registers['c'] = 123500

    while True:
        registers['f'] = 1
        registers['d'] = 2

        while True:
            registers['e'] = 2

            while True:
                registers['g'] = registers['d']
                registers['g'] *= registers['e']
                registers['g'] -= registers['b']

                # if d * e == b
                if registers['g'] == 0:
                    registers['f'] = 0

                registers['e'] += 1
                registers['g'] = registers['e']
                registers['g'] -= registers['b']

                # if e == b
                if registers['g'] == 0:
                    break

            registers['d'] += 1
            registers['g'] = registers['d']
            registers['g'] -= registers['b']

            # if d == b
            if registers['g'] == 0:
                break

        if registers['f'] == 0:
            registers['h'] += 1

        registers['g'] = registers['b']
        registers['g'] -= registers['c']

        if registers['g'] == 0:
            return registers['h']

        registers['b'] += 17


# print(f(get_lines_for_day(2017, 23), debug_mode=False))
print(g(debug_mode=True))
# part 2
# 0 is not the right answer
# 1001 is too high
# 1000 is not the right answer

# state at i == 20
# {a: 1, b: 106500, c: 123500, d: 2, e: 106500, f: 0, g: 0, h: 0

# state at i == 24
# {a: 1, b: 106500, c: 123500, d: 106500, e: 106500, f: 0, g: 0, h: 0
