from itertools import product
from util import get_lines_for_day, get_groups


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
    if x > 0:
        for _ in range(x):
            new_scanner = set()
            for sx, sy, sz in scanner:
                new_scanner.add((sx, sz, -sy))
            scanner = new_scanner

    # next, about the y axis
    if y > 0:
        for _ in range(y):
            new_scanner = set()
            for sx, sy, sz in scanner:
                new_scanner.add((-sz, sy, sx))
            scanner = new_scanner

    # about the z axis
    if z > 0:
        for _ in range(z):
            new_scanner = set()
            for sx, sy, sz in scanner:
                new_scanner.add((-sy, sx, sz))
            scanner = new_scanner

    return scanner


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


def combine(s1, s2, locations):
    for rotation in rotations:
        s2_rotated = rotate(s2, *rotation)
        for translation in get_translations(s1, s2_rotated):
            s2_translated = translate(s2_rotated, *translation)
            if len(s1.intersection(s2_translated)) >= 12:
                locations.append((translation[0], translation[1], translation[2]))
                s1.update(s2_translated)
                return True
    return False


def arrange_scanners(scanners, locations):
    """
    keep trying to combine into a large scanner with the orientation of scanner 0 until we can't anymore
    :param scanners: all scanners to combine
    :param locations: the locations where scanners end up after we move them to fit
    :return: how many total points all scanners can see
    """
    megascanner, scanners = scanners[0], scanners[1:]
    did_combine = True
    while did_combine:
        did_combine = False
        new_scanners = []
        for i, s in enumerate(scanners):
            if combine(megascanner, s, locations):
                did_combine = True
            else:
                new_scanners.append(s)
        scanners = new_scanners

    return len(megascanner)


if __name__ == '__main__':
    scanners = []
    lines = get_lines_for_day(2021, 19)
    groups = get_groups(lines)
    for group in groups:
        scanners.append(set())
        for coords in group[1:]:
            x, y, z = map(int, coords.split(','))
            scanners[-1].add((x, y, z))

    locations = [(0, 0, 0)]
    print(arrange_scanners(scanners, locations))  # part 1

    farthest = 0
    for l1, l2 in product(locations, locations):
        x1, y1, z1 = l1
        x2, y2, z2 = l2
        distance = abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)
        farthest = max(farthest, distance)
    print(farthest)  # part2
