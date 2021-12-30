from util import get_lines_for_day, get_input_for_day, get_groups

from collections import defaultdict, Counter, deque
from itertools import combinations, permutations
from functools import reduce
from operator import attrgetter, itemgetter
from math import factorial


def part1(graph):
    count = 0
    visited = {'start'}
    def bfs(cur='start'):
        nonlocal count
        if cur == 'end':
            count += 1
            return
        for neighbor in graph.get(cur, []):
            if neighbor not in visited:
                if neighbor.islower():
                    visited.add(neighbor)
                bfs(neighbor)
                if neighbor is not 'start':
                    visited.discard(neighbor)
    bfs()
    return count


def part2(graph):
    count = 0
    visited = defaultdict(int)
    visited['start'] += 1
    path_set = set()

    # start,A,c,A,b,b,A,c,end
    def bfs(double_visit, cur='start'):
        nonlocal count
        if cur == 'end':
            count += 1
            paths.append(path[:])
            return
        for neighbor in graph.get(cur, []):
            if visited.get(neighbor, 0) < 1 or (neighbor == double_visit and visited[neighbor] < 2):
                if neighbor.islower():
                    visited[neighbor] += 1
                path.append(neighbor)
                bfs(double_visit, neighbor)
                path.pop()
                if neighbor.islower():
                    visited[neighbor] -= 1

    caves = graph.keys() - {'start', 'end'}
    caves = {c for c in caves if c.islower()}
    for cave in caves:
        path = ['start']
        paths = []
        bfs(cave)
        for p in paths:
            path_set.add(','.join(p))

    return path_set


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 12)
    test_lines = get_lines_for_day(2021, '12_test')
    # inp = get_input_for_day(2021, 12)
    groups = get_groups(lines)
    test_case = get_lines_for_day(2021, '12_test_case')
    test_case = set(test_case)

    g = defaultdict(list)
    for line in lines:
        a, b = line.split('-')
        g[a].append(b)
        g[b].append(a)

    print(part1(g))
    # print(part2(g))
    p2 = part2(g)
    print(len(p2))
    # print(test_case - p2)
    # print(p2 - test_case)
    # print(p2.intersection(test_case))
