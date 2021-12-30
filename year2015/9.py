from util import get_lines_for_day
from typing import List, Set


def f(lines):
    places = set()
    distances = {}

    for line in lines:
        p, d = line.split(' = ')
        p1, p2 = p.split(' to ')
        places.update(p.split(' to '))
        distances[p] = int(d)
        distances[p2 + ' to ' + p1] = int(d)

    # places = list(places)
    permutations = []

    def permutation(per: List, choices: Set):
        if not choices:
            if len(per) == len(places):
                permutations.append(per)
            return

        for choice in choices:
            if len(per) == 0 or per[-1] + ' to ' + choice in distances:
                permutation(per + [choice], choices - {choice})

    permutation([], places)

    least = float('inf')
    most = -1
    for p in permutations:
        d = 0
        for a, b in zip(p, p[1:]):
            d += distances[a + ' to ' + b]
        least = min(least, d)
        most = max(most, d)

    return least, most


print(f(get_lines_for_day(2015, 9)))
