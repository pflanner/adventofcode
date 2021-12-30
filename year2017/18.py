from util import get_lines_for_day
from collections import deque


def get_value(arg, reg):
    try:
        return int(arg)
    except:
        return reg[arg]


def f(lines):
    sound = 0
    registers = {'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 0}
    i = 0

    while 0 <= i < len(lines):
        line = lines[i].split()
        op = line[0]
        arg1 = line[1]

        if op not in ('rcv', 'snd'):
            arg2 = get_value(line[2], registers)

        if op == 'snd':
            sound = get_value(arg1, registers)
        elif op == 'set':
            registers[arg1] = arg2
        elif op == 'add':
            registers[arg1] += arg2
        elif op == 'mul':
            registers[arg1] *= arg2
        elif op == 'mod':
            registers[arg1] %= arg2
        elif op == 'rcv':
            if get_value(arg1, registers) != 0:
                return sound
        elif op == 'jgz':
            if get_value(arg1, registers) > 0:
                i += arg2
                continue

        i += 1

    return "not found"


def terminated(indices, deadlocks, num_ops):
    return not any(0 <= i < num_ops for i in indices) or all(deadlocks)


def g(lines):
    result = 0
    regs = [
        {'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 0},
        {'a': 0, 'b': 0, 'f': 0, 'i': 0, 'p': 1},
    ]
    indices = [0, 0]
    deadlocks = [False, False]
    queues = [deque(), deque()]

    while not terminated(indices, deadlocks, len(lines)):
        for i in range(len(indices)):
            line = lines[indices[i]].split()
            reg = regs[i]
            op = line[0]
            arg1 = line[1]

            if op not in ('rcv', 'snd'):
                arg2 = get_value(line[2], reg)

            if op == 'snd':
                if i == 1:
                    result += 1
                q = queues[(i + 1) % len(queues)]
                q.appendleft(get_value(arg1, reg))
            elif op == 'set':
                reg[arg1] = arg2
            elif op == 'add':
                reg[arg1] += arg2
            elif op == 'mul':
                reg[arg1] *= arg2
            elif op == 'mod':
                reg[arg1] %= arg2
            elif op == 'rcv':
                q = queues[i]
                if len(q) == 0:
                    deadlocks[i] = True
                    continue

                deadlocks[i] = False
                reg[arg1] = get_value(q.pop(), reg)
            elif op == 'jgz':
                if get_value(arg1, reg) > 0:
                    indices[i] += arg2
                    continue

            indices[i] += 1

    return result


print(g(get_lines_for_day(2017, 18)))


