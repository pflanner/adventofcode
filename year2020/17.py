from util import get_input_for_day


def count_active_neighbors(active_cells, x, y, z, w):
    count = 0
    delta = [-1, 0, 1]

    for i in delta:
        for j in delta:
            for k in delta:
                for l in delta:
                    if any((i, j, k, l)):
                        if (x+i, y+j, z+k, w+l) in active_cells:
                            count += 1

    return count


def f(i):
    i = i.strip().split('\n')
    active_cells = {(x, y, 0, 0) for x, line in enumerate(i) for y, c in enumerate(line) if c == '#'}

    for _ in range(6):
        xmin = xmax = ymin = ymax = zmin = zmax = wmin = wmax = 0
        for x, y, z, w in active_cells:
            xmin = min(xmin, x)
            xmax = max(xmax, x)
            ymin = min(ymin, y)
            ymax = max(ymax, y)
            zmin = min(zmin, z)
            zmax = max(zmax, z)
            wmin = min(wmin, w)
            wmax = max(wmax, w)

        new_board = active_cells.copy()

        for x in range(xmin - 1, xmax + 2):
            for y in range(ymin - 1, ymax + 2):
                for z in range(zmin - 1, zmax + 2):
                    for w in range(wmin - 1, wmax + 2):
                        num_active_neighbors = count_active_neighbors(active_cells, x, y, z, w)
                        if (x, y, z, w) in active_cells:
                            if num_active_neighbors not in (2, 3):
                                new_board.remove((x, y, z, w))
                        else:
                            if num_active_neighbors == 3:
                                new_board.add((x, y, z, w))

        active_cells = new_board

    return len(active_cells)


print(f(get_input_for_day(17)))
