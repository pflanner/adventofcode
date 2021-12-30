from util import get_lines_for_day


def f(lines):
    registers = {'a': 1, 'b': 0}
    i = 0

    while i < len(lines):
        line = lines[i].split()
        op = line[0]
        r = line[1].replace(',', '')
        if op in ['jio', 'jie']:
            j = int(line[2])
        elif op == 'jmp':
            j = int(line[1])

        if op == 'hlf':
            registers[r] //= 2
        elif op == 'tpl':
            registers[r] *= 3
        elif op == 'inc':
            registers[r] += 1
        elif op == 'jmp':
            i += j
            continue
        elif op == 'jie':
            if registers[r] % 2 == 0:
                i += j
                continue
        elif op == 'jio':
            if registers[r] == 1:
                i += j
                continue

        i += 1

    return registers['b']


print(f(get_lines_for_day(2015, 23)))
