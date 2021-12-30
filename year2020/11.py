from util import get_input_for_day


def occupied_neighbor_count(r, c, grid):
    count = 0

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            rr = r + i
            cc = c + j

            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and (i != 0 or j != 0) and grid[rr][cc] == '#':
                count += 1

    return count


def occupied_neighbor_count2(r, c, grid):
    count = 0

    # left
    for col in range(c-1, -1, -1):
        if grid[r][col] == 'L':
            break
        if grid[r][col] == '#':
            count += 1
            break

    # right
    for col in range(c+1, len(grid[0])):
        if grid[r][col] == 'L':
            break
        if grid[r][col] == '#':
            count += 1
            break

    # up
    for row in range(r-1, -1, -1):
        if grid[row][c] == 'L':
            break
        if grid[row][c] == '#':
            count += 1
            break

    # down
    for row in range(r+1, len(grid)):
        if grid[row][c] == 'L':
            break
        if grid[row][c] == '#':
            count += 1
            break

    # up/left
    for n in range(1, max(len(grid), len(grid[0]))):
        rr = r - n
        cc = c - n

        if rr < 0 or cc < 0:
            break

        if grid[rr][cc] == 'L':
            break

        if grid[rr][cc] == '#':
            count += 1
            break

    # up/right
    for n in range(1, max(len(grid), len(grid[0]))):
        rr = r - n
        cc = c + n

        if rr < 0 or cc >= len(grid[0]):
            break

        if grid[rr][cc] == 'L':
            break

        if grid[rr][cc] == '#':
            count += 1
            break

    # down/left
    for n in range(1, max(len(grid), len(grid[0]))):
        rr = r + n
        cc = c - n

        if rr >= len(grid) or cc < 0:
            break

        if grid[rr][cc] == 'L':
            break

        if grid[rr][cc] == '#':
            count += 1
            break

    # down/right
    for n in range(1, max(len(grid), len(grid[0]))):
        rr = r + n
        cc = c + n

        if rr >= len(grid) or cc >= len(grid[0]):
            break

        if grid[rr][cc] == 'L':
            break

        if grid[rr][cc] == '#':
            count += 1
            break

    return count


def occupied_neighbor_count3(r, c, grid, n):
    count = 0
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    for y, x in dirs:
        for i in range(1, n):
            seat = grid.get((r + y*i, c + x*i))
            if seat is None or seat == 'L' or seat == '#':
                if seat == '#':
                    count += 1
                break

    return count


def count_occupied_seats(grid):
    count = 0

    for row in grid:
        for seat in row:
            if seat == '#':
                count += 1

    return count


def part2(i):
    i = i.strip().split('\n')

    old_grid = []
    new_grid = []

    occupied_seats = 0
    new_occupied_seats = -1

    for r, line in enumerate(i):
        old_grid.append([])
        new_grid.append([])
        for c, char in enumerate(line):
            old_grid[r].append(char)
            new_grid[r].append(char)
            if char == '#':
                occupied_seats += 1

    while occupied_seats != new_occupied_seats:
        for r in range(len(old_grid)):
            for c in range(len(old_grid[0])):
                seat = old_grid[r][c]

                if seat == 'L':
                    if occupied_neighbor_count2(r, c, old_grid) == 0:
                        new_grid[r][c] = '#'
                elif seat == '#':
                    if occupied_neighbor_count2(r, c, old_grid) >= 5:
                        new_grid[r][c] = 'L'

        occupied_seats = count_occupied_seats(old_grid)
        new_occupied_seats = count_occupied_seats(new_grid)
        print(new_occupied_seats)
        old_grid = [line[:] for line in new_grid]
    print(new_occupied_seats)


def part2_2(i):
    i = i.strip().split('\n')
    m, n = len(i), len(i[0])
    old_grid = {(r, c): seat for r, line in enumerate(i) for c, seat in enumerate(line)}
    new_grid = old_grid.copy()
    occupied_seats = -1
    new_occupied_seats = list(new_grid.values()).count('#')

    while occupied_seats != new_occupied_seats:
        for r in range(m):
            for c in range(n):
                seat = old_grid[(r, c)]

                if seat == 'L':
                    if occupied_neighbor_count3(r, c, old_grid, max(m, n)) == 0:
                        new_grid[(r, c)] = '#'
                elif seat == '#':
                    if occupied_neighbor_count3(r, c, old_grid, max(m, n)) >= 5:
                        new_grid[(r, c)] = 'L'

        occupied_seats = new_occupied_seats
        new_occupied_seats = list(new_grid.values()).count('#')
        print(new_occupied_seats)
        old_grid = new_grid.copy()
    print(new_occupied_seats)

# 95 is not right
# 2117 for part 2


part2_2(get_input_for_day(11))
