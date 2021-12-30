from util import get_lines_for_day

dirs = {
    'nw': (-1, 1),
    'se': (1, -1),
    'ne': (1, 1),
    'sw': (-1, -1),
    'e': (2, 0),
    'w': (-2, 0),
}


def f(lines):
    flipped = set()

    for line in lines:
        pos = (0, 0)

        while line:
            for dir in dirs:
                if line.startswith(dir):
                    pos = tuple(map(sum, zip(pos, dirs[dir])))
                    line = line[len(dir):]
                    break

        if pos in flipped:
            flipped.remove(pos)
        else:
            flipped.add(pos)

    # print(len(flipped))
    return flipped
    # 293 is not the right answer


def get_neighbors(pos):
    x, y = pos
    return [(x + dirx, y + diry) for dirx, diry in dirs.values()]


def g(flipped):
    for _ in range(100):
        new_flipped = flipped.copy()
        visited = set()

        for f in flipped:
            if f in visited:
                continue
            visited.add(f)
            count = 0
            for n in get_neighbors(f):
                if n in flipped:
                    count += 1
                else:
                    if n in visited:
                        continue
                    visited.add(n)
                    ncount = 0
                    for nn in get_neighbors(n):
                        if nn in flipped:
                            ncount += 1
                    if ncount == 2:
                        new_flipped.add(n)
            if count == 0 or count > 2:
                new_flipped.remove(f)

        flipped = new_flipped

    print(len(flipped))


g(f(get_lines_for_day(24)))
