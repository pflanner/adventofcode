from util import get_lines_for_day

display_width = 50
display_height = 6


def print_display(display, filler='.'):
    for r in range(display_height):
        for c in range(display_width):
            if (r, c) in display:
                print('#', end='')
            else:
                print(filler, end='')
        print()
    print()


def f(lines):
    display = set()

    for line in lines:
        line = line.split()
        if line[0].startswith('rect'):
            w, h = map(int, line[1].split('x'))
            for r in range(h):
                for c in range(w):
                    display.add((r, c))
        elif line[1] == 'row':
            new_display = set()
            row = int(line[2].split('=')[1])
            num = int(line[4])

            for r, c in display:
                if r == row:
                    c = (c + num) % display_width
                new_display.add((r, c))
            display = new_display
        elif line[1] == 'column':
            new_display = set()
            col = int(line[2].split('=')[1])
            num = int(line[4])

            for r, c in display:
                if c == col:
                    r = (r + num) % display_height
                new_display.add((r, c))
            display = new_display

        print_display(display)

    print_display(display, filler=' ')

    return len(display)


print(f(get_lines_for_day(2016, 8)))
