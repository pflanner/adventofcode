from util import get_lines_for_day


def f(lines):
    reg = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

    i = 0
    while 0 <= i < len(lines):
        line = lines[i]
        line = line.split()
        op = line[0]

        if op == 'cpy':
            src = line[1]
            dest = line[2]

            try:
                reg[dest] = int(src)
            except:
                reg[dest] = reg[src]
        elif op == 'inc':
            reg[line[1]] += 1
        elif op == 'dec':
            reg[line[1]] -= 1
        elif op == 'jnz':
            test = line[1]
            jump = int(line[2])

            try:
                test = int(test)
            except:
                test = reg[test]

            if test != 0:
                i += jump
                continue
        i += 1

    return reg['a']


print(f(get_lines_for_day(2016, 12)))
