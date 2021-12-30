from util import get_lines_for_day
import string


def f(lines, dancers=list(string.ascii_lowercase[:16])):
    for move in lines[0].split(','):
        if move.startswith('s'):
            x = int(move[1:])
            dancers = dancers[-x:] + dancers[:-x]
        elif move.startswith('x'):
            a, b = map(int, move[1:].split('/'))
            dancers[a], dancers[b] = dancers[b], dancers[a]
        elif move.startswith('p'):
            a, b = move[1:].split('/')
            i, j = dancers.index(a), dancers.index(b)
            dancers[i], dancers[j] = dancers[j], dancers[i]

    return dancers


def g(lines, dancers=list(string.ascii_lowercase[:16])):
    order = f(lines, dancers.copy())
    new_dancers = [None]*len(dancers)
    count = 0

    for _ in range(1000000000):
        if count % 100000 == 0:
            print(count)
        count += 1
        for i in range(len(dancers)):
            new_i = ord(order[i]) - ord('a')
            new_dancers[i] = dancers[new_i]
        dancers = new_dancers.copy()

    return ''.join(dancers)


def h(lines, dancers=list(string.ascii_lowercase[:16])):
    seen = {tuple(dancers)}
    loop = 1

    for i in range(1000000000):
        dancers = f(lines, dancers.copy())
        t = tuple(dancers)
        if t in seen:
            loop = i + 1
            break

    for _ in range(1000000000 % loop):
        dancers = f(lines, dancers.copy())

    return ''.join(dancers)


print(h(get_lines_for_day(2017, 16)))
# print(h(['s1,x3/4,pe/b'], list(string.ascii_lowercase[:5])))
# part 2
# abpdegkhijflmcon is not the right answer
