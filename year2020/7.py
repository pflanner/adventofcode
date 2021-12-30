from util import get_input_for_day, get_groups
from collections import defaultdict, deque
from functools import reduce
from operator import add


def f():
    todays_input = get_input_for_day(7)
    contained_graph = defaultdict(set)
    contains_graph = defaultdict(list)

    for line in todays_input.strip().split('\n'):
        container, rule = line.split(' bags contain ')
        container = container.strip()
        contained = rule.split(', ')

        for c in contained:
            c = c.split()
            if c[0] == 'no':
                continue
            bag_type = ' '.join(c[1:-1]).strip()
            n = int(c[0])

            if len(container) == 1:
                print(container)

            contained_graph[bag_type].add(container)
            contains_graph[container].extend([bag_type] * n)

    q = deque(['shiny gold'])
    visited = {'shiny gold'}

    while q:
        cur = q.pop()

        for neighbor in contained_graph.get(cur, []):
            if neighbor not in visited:
                visited.add(neighbor)
                q.appendleft(neighbor)

    print(len(visited) - 1)

    # part 2
    result = 0

    def dfs(node='shiny gold'):
        nonlocal result

        for b in contains_graph.get(node, []):
            result += 1
            dfs(b)

    dfs()
    print(result)


f()
