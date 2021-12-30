from util import get_input_for_day


def f():
    i = get_input_for_day(2015, 1).strip()
    floor = 0

    for index, c in enumerate(i):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor < 0:
            return index + 1

    return floor


print(f())