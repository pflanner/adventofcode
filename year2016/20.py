from util import get_lines_for_day


def f(lines):
    lowest = None
    num_allowed = 0
    ranges = []
    merged = []

    for line in lines:
        line = line.split('-')
        start, end = int(line[0]), int(line[1])

        ranges.append([start, end])

    ranges.sort()
    merged.append(ranges[0])
    if merged[-1][0] != 0:
        lowest = 0
        num_allowed += merged[-1][0]

    for start, end in ranges[1:]:
        if start <= merged[-1][1] + 1:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            if lowest is None:
                lowest = merged[-1][1] + 1
            num_allowed += start - merged[-1][1] - 1
            merged.append([start, end])

    return lowest, num_allowed


print(f(get_lines_for_day(2016, 20)))
