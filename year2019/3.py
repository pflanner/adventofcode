from util import get_lines_for_day


def get_wire(line):
    dirs = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0),
    }

    cur = (0, 0)
    points = {}
    steps = 1

    for move in line.split(','):
        direction, magnitude = move[0], int(move[1:])

        for _ in range(magnitude):
            cur = tuple(map(sum, zip(cur, dirs[direction])))
            points[cur] = steps
            steps += 1

    return points


def distance_from_origin(point):
    return abs(point[0]) + abs(point[1])


def part1(lines):
    wires = []

    for line in lines:
        wires.append(get_wire(line))

    distance = float('inf')

    for point in wires[0]:
        if point in wires[1]:
            distance = min(distance, distance_from_origin(point))

    return distance


def part2(lines):
    wires = []

    for line in lines:
        wires.append(get_wire(line))

    min_steps = float('inf')

    for point, steps in wires[0].items():
        if point in wires[1]:
            min_steps = min(min_steps, steps + wires[1][point])

    return min_steps


if __name__ == '__main__':
    print(part1(get_lines_for_day(2019, 3)))
    print(part2(get_lines_for_day(2019, 3)))
    # 63524 is too low
