from util import get_lines_for_day


def f(lines):
    discs = []

    for line in lines:
        line = line.split()
        discs.append((int(line[3]), int(line[11][:-1])))
    discs.append((11, 0))

    i = 0
    while True:
        j = i
        for num_pos, start_pos in discs:
            if (start_pos + j) % num_pos != 0:
                break
            j += 1
        else:
            break

        i += 1

    return i - 1


print(f(get_lines_for_day(2016, 15)))

# part 1
# 122319 is too high
