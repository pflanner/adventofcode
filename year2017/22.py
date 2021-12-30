from util import get_lines_for_day
from operator import itemgetter


def turn_left(dir):
    x, y = dir
    return -y, x


def turn_right(dir):
    x, y = dir
    return y, -x


def reverse(dir):
    x, y = dir
    return -x, -y


def print_grid(grid, pos):
    minx = min(pos[0], min(map(itemgetter(0), grid.keys())))
    maxx = max(pos[0], max(map(itemgetter(0), grid.keys())))
    miny = min(pos[1], min(map(itemgetter(1), grid.keys())))
    maxy = max(pos[1], max(map(itemgetter(1), grid.keys())))

    for y in range(maxy, miny - 1, -1):
        for x in range(minx, maxx + 1):
            start = end = ' '
            val = grid[(x, y)] if (x, y) in grid else '.'
            if (x, y) == pos:
                start = '['
                end = ']'

            print(f'{start}{val}{end}', end='')
        print()


def f(lines, iterations=10000):
    w, h = len(lines[0]), len(lines)
    x = y = 0
    infected = {}
    infect_count = 0

    for line in lines:
        for c in line:
            if c == '#':
                infected[(x, y)] = '#'
            x += 1
        y -= 1
        x = 0

    dir = (0, 1)
    pos = (w//2, -(h//2))

    for i in range(iterations):
        # print_grid(infected, pos)
        # print()
        val = infected.get(pos)
        if val == '#':
            dir = turn_right(dir)
            infected[pos] = 'F'
        elif val == 'F':
            dir = reverse(dir)
            del infected[pos]
        elif val == 'W':
            infected[pos] = '#'
            infect_count += 1
        else:
            dir = turn_left(dir)
            infected[pos] = 'W'

        pos = tuple(map(sum, zip(pos, dir)))

    return infect_count


print(f(get_lines_for_day(2017, '22'), 10000000))
# part 1
# 5242 is too high
