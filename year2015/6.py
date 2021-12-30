from util import get_lines_for_day
from collections import defaultdict


def f(i):
    active_lights = defaultdict(int)

    for line in i:
        if line.startswith('toggle'):
            op = 'toggle'
        elif line.startswith('turn off'):
            op = 'turn off'
        elif line.startswith('turn on'):
            op = 'turn on'

        line = line[len(op) + 1:]
        corner1, _, corner2 = line.split()
        corner1 = list(map(int, corner1.split(',')))
        corner2 = list(map(int, corner2.split(',')))
        xs = [corner1[0], corner2[0]]
        ys = [corner1[1], corner2[1]]
        x_range = range(min(xs), max(xs) + 1)
        y_range = range(min(ys), max(ys) + 1)

        for x in x_range:
            for y in y_range:
                loc = (x, y)
                if op == 'toggle':
                    active_lights[loc] += 2
                elif op == 'turn off' and active_lights.get(loc, 0) > 0:
                    active_lights[loc] -= 1
                elif op == 'turn on':
                    active_lights[loc] += 1

    return sum(active_lights.values())


print(f(get_lines_for_day(2015, 6)))
# part 2
# 10903132 is not the right answer
# 13064032 is not the right answer
