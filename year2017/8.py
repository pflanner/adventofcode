from util import get_lines_for_day


def f(lines):
    registers = {}
    highest = 0

    for line in lines:
        line = line.split()
        r = line[0]
        op = line[1]
        val = int(line[2])
        cmp_reg = line[4]
        cmp_op = line[5]
        cmp_val = int(line[6])

        rval = registers.get(r, 0)
        cmpreg_val = registers.get(cmp_reg, 0)

        if cmp_op == '==' and cmpreg_val != cmp_val:
            continue
        if cmp_op == '!=' and cmpreg_val == cmp_val:
            continue
        if cmp_op == '<' and cmpreg_val >= cmp_val:
            continue
        if cmp_op == '>' and cmpreg_val <= cmp_val:
            continue
        if cmp_op == '<=' and cmpreg_val > cmp_val:
            continue
        if cmp_op == '>=' and cmpreg_val < cmp_val:
            continue

        new_val = rval + val if op == 'inc' else rval - val
        registers[r] = new_val
        highest = max(highest, new_val)

    return max(registers.values()), highest


print(f(get_lines_for_day(2017, 8)))

