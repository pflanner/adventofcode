from util import get_lines_for_day


def print_grid(grid, i):
    for r in range(i + 1):
        for c in range(i + 1):
            if (r, c) in grid:
                num = str(grid[(r, c)])
                spaces = [' '] * (10 - len(num))
                print(''.join(spaces) + num, end='')
        print()


def f(lines, row_override=None, col_override=None):
    line = lines[0].split()
    row = int(line[15].replace(',', '')) if row_override is None else row_override
    col = int(line[17].replace('.', '')) if col_override is None else col_override

    grid = {}
    i = 0
    prev = 20151125
    count = 0
    percent = 0

    while (row - 1, col - 1) not in grid:
        for r in range(i, -1, -1):
            count += 1
            new_percent = int(count / 17853300 * 100)
            if new_percent >= percent + 1:
                print(str(new_percent) + '%')
                percent = new_percent

            c = i - r
            code = (prev * 252533) % 33554393 if (r, c) != (0, 0) else prev
            prev = code
            grid[(r, c)] = code

        i += 1

    print(count)
    return grid[(row - 1, col - 1)]


print(f(get_lines_for_day(2015, 25)))
# part 1
# 19749359 is too low
