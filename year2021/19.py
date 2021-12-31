from operator import itemgetter


rotations = [
    (0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3),
    (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 1, 3),
    (0, 2, 0), (0, 2, 1), (0, 2, 2), (0, 2, 3),
    (0, 3, 0), (0, 3, 1), (0, 3, 2), (0, 3, 3),
    (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 0, 3),
    (3, 0, 0), (3, 0, 1), (3, 0, 2), (3, 0, 3),
]


def rotate(scanner, x, y, z):
    """
    :param scanner: the scanner to rotate
    :param x: how many 90 degree rotations about the x axis?
    :param y: how many 90 degree rotations about the y axis?
    :param z: how many 90 degree rotations about the z axis?
    :return: the scanner after all rotation is complete
    """
    # first, rotate about the x axis
    for _ in range(x):
        new_scanner = set()
        for sx, sy, sz in scanner:
            new_scanner.add((sx, sz, -sy))
        scanner = new_scanner

    # next, about the y axis
    for _ in range(y):
        new_scanner = set()
        for sx, sy, sz in scanner:
            new_scanner.add((-sz, sy, sx))
        scanner = new_scanner

    # about the z axis
    for _ in range(z):
        new_scanner = set()
        for sx, sy, sz in scanner:
            new_scanner.add((-sy, sx, sz))
        scanner = new_scanner

    return scanner


def flip_axis(scanner, axis):
    if axis is None:
        return scanner

    index = 0 if axis == 'x' else 1 if axis == 'y' else 2
    new_scanner = set()

    for p in scanner:
        newp = list(p)
        newp[index] *= -1
        new_scanner.add(tuple(newp))

    return new_scanner


def translate(scanner, tx, ty, tz):
    new_scanner = set()

    for x, y, z in scanner:
        new_scanner.add((x+tx, y+ty, z+tz))

    return new_scanner


# what translations do we have to apply to s2 to get all possible overlaps of s1?
def get_translations(s1, s2):
    translations = []

    for x1, y1, z1 in s1:
        for x2, y2, z2 in s2:
            translations.append((x1-x2, y1-y2, z1-z2))

    return translations


def combine(s1, s2):
    max_points_matched = 0
    operation_count = 0
    for rotation in rotations:
        s2_rotated = rotate(s2, *rotation)
        for axis in ['x', 'y', 'z', None]:
            s2_flipped = flip_axis(s2_rotated, axis)
            for translation in get_translations(s1, s2):
                operation_count += 1
                s2_translated = translate(s2_flipped, *translation)
                max_points_matched = max(max_points_matched, len(s1.intersection(s2_translated)))
                l1 = s1
                if len(s1.intersection(s2_translated)) >= 3:
                    s1.update(s2_translated)
                    return True
    return False


def part1(scanners):
    """
    compare everything against the orientation of scanner 0
    quadratic iteration, compare 2 scanners at a time
    try all 24 orientations
    :param scanners:
    :return:
    """
    megascanner, scanners = scanners[0], scanners[1:]
    did_combine = True
    while did_combine:
        did_combine = False
        new_scanners = []
        for i, s in enumerate(scanners):
            if combine(megascanner, s):
                did_combine = True
            else:
                new_scanners.append(s)
        scanners = new_scanners

    return len(megascanner)


if __name__ == '__main__':
    scanners = []
    with open("input/19_test.txt") as f:
        lines = f.read()
        groups = lines.split('\n\n')
        for group in groups:
            scanners.append(set())
            for coords in group.strip().split('\n')[1:]:
                x, y, z = map(int, coords.split(','))
                scanners[-1].add((x, y, z))

    print(part1(scanners))
