from util import get_lines_for_day
from collections import defaultdict, deque


def print_rooms(graph):
    minx = miny = maxx = maxy = 0

    for x, y in graph:
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)

    print((''.join(['#'] * ((maxx - minx + 1) * 2 + 1))))

    for y in range(maxy, miny - 1, -1):
        print('#', end='')
        for x in range(minx, maxx + 1):
            room_marker = 'X' if (x, y) == (0, 0) else '.'
            print(room_marker, end='')
            if (x + 1, y) in graph[(x, y)]:
                print('|', end='')
            else:
                print('#', end='')

        print()

        print('#', end='')
        for x in range(minx, maxx + 1):
            if (x, y - 1) in graph[(x, y)]:
                print('-', end='')
            else:
                print('#', end='')
            print('#', end='')

        print()


def populate_graph(line, i, graph, start_pos):
    pos = start_pos
    directions = {
        'N': lambda p: tuple(map(sum, zip(p, (0, 1)))),
        'S': lambda p: tuple(map(sum, zip(p, (0, -1)))),
        'E': lambda p: tuple(map(sum, zip(p, (1, 0)))),
        'W': lambda p: tuple(map(sum, zip(p, (-1, 0)))),
    }

    while i < len(line):
        c = line[i]
        if c in directions:
            new_pos = directions[c](pos)
            graph[pos].add(new_pos)
            graph[new_pos].add(pos)
            pos = new_pos
        elif c == '(':
            i = populate_graph(line, i + 1, graph, pos)
        elif c == '|':
            return populate_graph(line, i + 1, graph, start_pos)
        elif c == ')':
            return i
        i += 1

    return i


def f(lines):
    # using x, y coordinates where up (north) is positive

    start = (0, 0)
    graph = defaultdict(set)

    for line in lines:
        populate_graph(line, 0, graph, start)

    print_rooms(graph)

    # bfs for each destination
    longest_path = 0
    at_least_1000_count = 0
    for pos in graph:
        q = deque([(pos, 0)])
        visited = {pos}

        while q:
            cur, depth = q.pop()
            if cur == (0, 0):
                longest_path = max(longest_path, depth)
                if depth >= 1000:
                    at_least_1000_count += 1

            for neighbor in graph[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.appendleft((neighbor, depth + 1))

    return longest_path, at_least_1000_count


print(f(get_lines_for_day(2018, "20")))
