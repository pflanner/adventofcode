from itertools import product


def get_neighbors(pos, values):
    neighbors = []
    x, y = pos

    for i, j in product(*[[-1, 0, 1]]*2):
        xx, yy = x + i, y + j
        if (xx, yy) in values:
            neighbors.append(values[(xx, yy)])

    return neighbors


def f(n):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    pos = (0, 0)
    values = {pos: 1}
    i = 0
    count = countdown = 1

    while True:
        pos = tuple(map(sum, zip(pos, dirs[i])))
        value = sum(get_neighbors(pos, values))

        if value > n:
            return value

        values[pos] = value

        countdown -= 1

        if countdown == 0:
            i = (i + 1) % len(dirs)

            if i % 2 == 0:
                count += 1

            countdown = count


print(f(368078))
