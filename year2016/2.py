from util import get_lines_for_day


def get_part1_buttons():
    buttons = {}
    b = 1
    for r in range(3):
        for c in range(3):
            buttons[(r, c)] = str(b)
            b += 1


def get_part2_buttons():
    return {
                                 (-1, 3): '1',
                     (0, 2): '2', (0, 3): '3', (0, 4): '4',
        (1, 1): '5', (1, 2): '6', (1, 3): '7', (1, 4): '8', (1, 5): '9',
                     (2, 2): 'A', (2, 3): 'B', (2, 4): 'C',
                                  (3, 3): 'D',
    }


def f(lines):
    code = []
    pos = (1, 1)
    dirs = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }

    buttons = get_part2_buttons()

    for line in lines:
        for c in line:
            new_pos = tuple(map(sum, zip(dirs[c], pos)))
            if new_pos in buttons:
                pos = new_pos
        code.append(buttons[pos])

    return ''.join(code)


print(f(get_lines_for_day(2016, 2)))
