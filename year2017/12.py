from util import get_lines_for_day
from collections import defaultdict, deque


def f(lines):
    graph = defaultdict(set)
    num_groups = 0

    for line in lines:
        left, right = line.split(' <-> ')
        graph[left].update(right.split(', '))

    while graph:
        num_groups += 1
        root = next(iter(graph))
        q = deque([root])
        visited = {root}

        while q:
            cur = q.pop()

            for n in graph[cur]:
                if n not in visited:
                    visited.add(n)
                    q.appendleft(n)

        for n in visited:
            del graph[n]

    return num_groups


print(f(get_lines_for_day(2017, 12)))
