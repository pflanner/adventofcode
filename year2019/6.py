from util import get_lines_for_day, get_input_for_day, get_groups
from collections import defaultdict, deque


def part1(param):
    dag = defaultdict(set)
    for line in param:
        center, orbiter = line.split(')')
        dag[center].add(orbiter)

    orbits = 0

    def visit(planet, depth):
        nonlocal orbits
        orbits += depth
        if planet not in dag:
            return

        for other in dag[planet]:
            visit(other, depth + 1)

    visit('COM', 0)

    return orbits


def part2(param):
    dag = defaultdict(set)
    for line in param:
        center, orbiter = line.split(')')
        dag[center].add(orbiter)
        dag[orbiter].add(center)

    q = deque()
    q.appendleft(('YOU', 0))
    visited = {'YOU'}

    while q:
        cur, depth = q.pop()

        for neighbor in dag.get(cur, []):
            if neighbor == 'SAN':
                return depth - 1

            if neighbor not in visited:
                visited.add(neighbor)
                q.appendleft((neighbor, depth + 1))

    return -1


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 6)
    test_lines = get_lines_for_day(2021, '6_test')
    inp = get_input_for_day(2021, 6)
    groups = get_groups(lines)

    print(part1(lines))
    print(part2(lines))
    # 378 is too low
