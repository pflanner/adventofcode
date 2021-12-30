from util import get_lines_for_day


def f(lines):
    line = lines[0]

    pos = (0, 0)
    visited = {pos}

    north = (0, 1)
    south = (0, -1)
    east = (1, 0)
    west = (-1, 0)
    dirs = [north, east, south, west]
    d = 0

    for instruction in line.split():
        instruction = instruction.replace(',', '')
        turn = instruction[0]
        dist = int(instruction[1:])

        if turn == 'R':
            d = (d + 1) % len(dirs)
        elif turn == 'L':
            d -= 1
            d = len(dirs) - 1 if d == -1 else d

        for _ in range(dist):
            pos = tuple(map(sum, zip(pos, dirs[d])))
            if pos in visited:
                return abs(pos[0]) + abs(pos[1])
            visited.add(pos)

    return abs(pos[0]) + abs(pos[1])


print(f(get_lines_for_day(2016, 1)))
# part 2
# 307 is too high
