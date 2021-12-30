from util import get_input_for_day
from operator import add, mul


ops = {
    '+': add,
    '*': mul,
}


def parse_input_line(line):
    result = []
    for c in line:
        if c in '()+*':
            result.append(c)
        elif c.isspace():
            continue
        else:
            result.append(int(c))

    return result

# '(5 * 6 * 5 * 7) + (6 + (8 * 3 * 9 + 2 + 7) + 7 + (4 * 2 + 5)) + 8'
def evaluate(expr, i=0):
    result = 1
    add_result = []
    op = '+'

    while i < len(expr):
        c = expr[i]

        if c == ')':
            result *= sum(add_result) if add_result else 1
            return result, i + 1
        elif c == '(':
            intermediate, i = evaluate(expr, i + 1)
            if op == '+':
                add_result.append(intermediate)
            else:
                result *= sum(add_result) if add_result else 1
                add_result.clear()
                add_result.append(intermediate)
            continue
        elif c in ['+', '*']:
            op = c
        elif op == '+':
            add_result.append(c)
        else:
            result *= sum(add_result) if add_result else 1
            add_result.clear()
            add_result.append(c)

        i += 1

    result *= sum(add_result) if add_result else 1

    return result, i


def f(i):
    i = i.strip().split('\n')

    result = 0

    for line in i:
        r, i = evaluate(parse_input_line(line))
        result += r

    return result


print(f(get_input_for_day(18)))

#1050 238
# 1050 + 6 + 432 + 7 + 28 + 8
# first line = 1531