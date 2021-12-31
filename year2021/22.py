def in_range(n):
    return -50 <= n <= 50

def part1(actions):
    on_cubes = set()
    for action in actions:
        command, x, y, z = action
        xstart, xend = x
        ystart, yend = y
        zstart, zend = z

        for x in range(max(xstart, -50), min(xend + 1, 50)):
            for y in range(max(ystart, -50), min(yend + 1, 50)):
                for z in range(max(zstart, -50), min(zend + 1, 50)):
                    if in_range(x) and in_range(y) and in_range(z):
                        if command == 'on':
                            on_cubes.add((x, y, z))
                        else:
                            on_cubes.discard((x, y, z))
    return len(on_cubes)


def find_overlap(a1, a2):
    _, onx, ony, onz = a1
    onxstart, onxend = onx
    onystart, onyend = ony
    onzstart, onzend = onz
    _, offx, offy, offz = a2
    offxstart, offxend = offx
    offystart, offyend = offy
    offzstart, offzend = offz

    xoverlap = min(onxend, offxend) - max(onxstart, offxstart)
    if xoverlap <= 0:
        return 0

    yoverlap = min(onyend, offyend) - max(onystart, offystart)
    if yoverlap <= 0:
        return 0

    zoverlap = min(onzend, offzend) - max(onzstart, offzstart)
    if zoverlap <= 0:
        return 0

    return xoverlap*yoverlap*zoverlap


def part2(actions):
    num_on_cubes = 0
    on_actions = []
    off_actions = []
    for i, action in enumerate(actions):
        command, x, y, z = action
        if command == 'on':
            on_actions.append((i, action))
        else:
            off_actions.append((i, action))

    for i, action in enumerate(actions):
        command, x, y, z = action
        xstart, xend = x
        ystart, yend = y
        zstart, zend = z
        volume = (xend - xstart + 1)*(yend - ystart + 1)*(zend - zstart + 1)

        if command == 'on':
            num_on_cubes += volume
            for p in actions[:i]:
                if p[0] == 'on':
                    num_on_cubes -= find_overlap(action, p)
        else:
            # command == 'off'


    for index_and_off_action in off_actions:
        i, off_action = index_and_off_action
        for index_and_on_action in on_actions:
            j, on_action = index_and_on_action
            if i > j:
                overlapping_volume = find_overlap(on_action, off_action)
                num_on_cubes -= overlapping_volume
            else:
                break
    return num_on_cubes



if __name__ == '__main__':
    with open("input/22_test.txt") as f:
        lines = f.readlines()
        actions = []
        for line in lines:
            command, ranges = line.split()
            x, y, z = ranges.split(',')
            xstart, xend = map(int, x.split('=')[1].split('..'))
            ystart, yend = map(int, y.split('=')[1].split('..'))
            zstart, zend = map(int, z.split('=')[1].split('..'))
            actions.append((command, (xstart, xend), (ystart, yend), (zstart, zend)))

        # print(part1(actions))
        print(part2(actions))
        # 11560839384435931
