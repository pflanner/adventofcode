from util import get_lines_for_day


def maybe_to_int(s):
    try:
        return int(s)
    except:
        return s


def get_value(arg, reg):
    try:
        return int(arg)
    except:
        return reg[arg]


def multiply(r1, r2, r3, reg):
    x, y = reg[r1], reg[r2]
    reg[r1] = reg[r2] = 0

    reg[r3] += x * y


class Instruction:
    def __init__(self, line):
        self.op = line[0]
        self.arg1 = maybe_to_int(line[1])
        self.arg2 = maybe_to_int(line[2]) if len(line) >= 3 else None

    def __repr__(self):
        return ' '.join([str(item) for item in [self.op, self.arg1, self.arg2] if item is not None])


toggle_map = {
    'jnz': 'cpy',
    'cpy': 'jnz',
    'inc': 'dec',
    'dec': 'inc',
    'tgl': 'inc',
}


def f(lines, start, optimized=False):
    output = []
    reg = {'a': start, 'b': 0, 'c': 0, 'd': 0}

    instructions = [Instruction(line.split()) for line in lines]

    i = 0
    while 0 <= i < len(instructions):
        inst = instructions[i]
        # print(reg)
        # print(i, inst)

        if inst.op == 'cpy':

            src = get_value(inst.arg1, reg)
            dest = inst.arg2

            try:
                int(dest)
                i += 1
                continue
            except:
                pass

            reg[dest] = src

            # check if this is really a multiply
            if i + 5 < len(instructions):
                three_ahead = instructions[i + 3]
                five_ahead = instructions[i + 5]
                if three_ahead.op == 'jnz' and three_ahead.arg2 == -2 and five_ahead.op == 'jnz' and five_ahead.arg2 == -5:
                    multiply(instructions[i + 2].arg1, instructions[i + 4].arg1, instructions[i + 1].arg1, reg)
                    i += 6
                    continue
        elif inst.op == 'inc':
            reg[inst.arg1] += 1
        elif inst.op == 'dec':
            reg[inst.arg1] -= 1
        elif inst.op == 'jnz':
            test = get_value(inst.arg1, reg)
            jump = get_value(inst.arg2, reg)

            if test != 0:
                if i == 13 and optimized:  # a += b // 2
                    reg['a'] += reg['b'] // 2
                    reg['c'] = 2 if reg['b'] % 2 == 0 else 1
                    reg['b'] = 0
                    i += 7
                else:
                    i += jump
                continue

        elif inst.op == 'out':
            output.append(get_value(inst.arg1, reg))
            if len(output) == 30:
                return output

        i += 1

    return reg['a']


test_val1 = [1 if i % 2 == 0 else 0 for i in range(30)]
test_val2 = [0 if i % 2 == 0 else 1 for i in range(30)]


for i in range(1000000):
    print(i)
    o = f(get_lines_for_day(2016, '25'), i, optimized=True)
    if o == test_val1 or o == test_val2:
        print(i)
        break

# highest index tried 2773
