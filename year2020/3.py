from operator import mul
from functools import reduce

def part1():
    x = 0
    trees = 0
    with open('input/3.txt') as f:
        for line in f:
            line = line.strip()
            if line[x] == '#':
                trees += 1

            x = (x + 3) % len(line)

    return trees


# 278


def part2():
    input = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    treeses = []
    for x_delta, y_delta in input:
        x = y = trees = 0
        with open('input/3.txt') as f:
            for line in f:
                line = line.strip()
                if y % y_delta != 0:
                    print(line)
                    y += 1
                    continue

                if line[x] == '#':
                    trees += 1
                    line = line[:x] + 'X' + line[x+1:]
                else:
                    line = line[:x] + 'O' + line[x+1:]

                print(line)

                x = (x + x_delta) % len(line)
                y += 1

        treeses.append(trees)
        print()

    print(treeses, reduce(mul, treeses, 1))
