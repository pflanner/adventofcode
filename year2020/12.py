from util import get_input_for_day


def part1(i):
    i = i.strip().split('\n')
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir = 1
    ew = 0
    ns = 0

    print((-90 % 360) // 90)
    print(-1 % 4)
    for line in i:
        op, n = line[:1], int(line[1:])

        if op == 'F':
            ns += dirs[dir][0] * n
            ew += dirs[dir][1] * n
        elif op == 'N':
            ns += n
        elif op == 'S':
            ns -= n
        elif op == 'E':
            ew += n
        elif op == 'W':
            ew -= n
        elif op == 'L':
            dir += (n%360) // 90
            dir %= 4
        elif op == 'R':
            dir -= (n%360) // 90
            dir %= 4

        print(ns, ew)

    print(ns, ew)


def part2(i):
    i = i.strip().split('\n')
    dirs = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
    ns = 0
    ew = 0
    wns = 1
    wew = 10

    print((-90 % 360) // 90)
    print(-1 % 4)
    for line in i:
        op, n = line[:1], int(line[1:])

        if op == 'F':
            ns += n * wns
            ew += n * wew
        elif op == 'N':
            wns += n
        elif op == 'S':
            wns -= n
        elif op == 'E':
            wew += n
        elif op == 'W':
            wew -= n
        elif op == 'L':
            dir = -1 *(n%360) // 90
            dir %= 4
            if dir % 2 != 0:
                wns, wew = wew, wns
            wns *= dirs[dir][0]
            wew *= dirs[dir][1]
        elif op == 'R':
            dir = (n%360) // 90
            dir %= 4
            if dir % 2 != 0:
                wns, wew = wew, wns
            wns *= dirs[dir][0]
            wew *= dirs[dir][1]

        # print(ns, ew)

    print(ns, ew)
    print(abs(ns) + abs(ew))


def part2_2(i):
    i = i.strip().split('\n')
    pos, waypoint = [0, 0], [10, 1]
    ops = {'N': (1, 1), 'S': (-1, 1), 'E': (1, 0), 'W': (-1, 0), 'L': (-1, 1), 'R': (1, -1)}

    for line in i:
        op, n = line[:1], int(line[1:])

        if op == 'F':
            pos = list(map(sum, zip(pos, [coord*n for coord in waypoint])))
        elif op in 'NSEW':
            waypoint[ops[op][1]] += ops[op][0] * n
        elif op in 'LR':
            number_of_90s = (n % 360) // 90
            for i in range(number_of_90s):
                waypoint[0], waypoint[1] = ops[op][0] * waypoint[1], ops[op][1] * waypoint[0]

    return abs(pos[0]) + abs(pos[1])


# 35400 is not right
# 41130 is not right
# 45766 is not right
# 53128 is not right
# 101860 is the answer

print(part2_2(get_input_for_day(12)))
