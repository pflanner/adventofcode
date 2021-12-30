from collections import deque


def f():
    count = 0

    # array value is the floor each item is on
    # the array is arranged such that each microchip is to the right of its generator
    # so all microchips are at odd indices and all generators are at even indices
    # the elevator is in the last position
    # floors = [1, 1, 2, 3, 2, 3, 2, 3, 2, 3, 1]
    floors = [1, 1, 2, 3, 2, 3, 2, 3, 2, 3, 1, 1, 1, 1, 1]
    # floors = [2, 1, 3, 1, 1]
    # floors = [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1]

    def is_valid(floors):
        if not all(1 <= floor <= 4 for floor in floors):
            return False

        generators = floors[:-1:2]
        microchips = floors[1:-1:2]

        for g, m in zip(generators, microchips):
            if g != m and any(m == otherg for otherg in generators):
                return False

        return True

    # This counts the number of generators and microchips on each floor and makes a string out of the combo
    # Why does this work? Why don't we need the exact state for marking things visited?
    def generalize(floors):
        g = [sum(1 for floor in floors[:-1:2] if floor == fn) for fn in range(1, 5)]
        m = [sum(1 for floor in floors[1:-1:2] if floor == fn) for fn in range(1, 5)]
        return ''.join(map(str, g + m)) + str(floors[-1])

    def h(floors):
        pairs = 0
        singles = 0
        for g, m in zip(floors[:-1:2], floors[1:-1:2]):
            if g == m:
                pairs += 1 << (3 * (g - 1))
            else:
                singles += 1 << (4 * (g - 1))
                singles += 1 << (4 * (m - 1))

        return pairs + (singles << 10) + (floors[-1] << 22)

    q = deque([(floors, 0)])
    visited = set(tuple(floors))

    while q:
        # if count % 10000 == 0:
        #     print(count)
        count += 1
        cur, depth = q.pop()

        if not is_valid(cur):
            continue

        t = h(cur)

        if t in visited:
            continue

        visited.add(t)

        if all(floor == 4 for floor in cur):
            return depth, count

        for i in range(len(cur) - 1):
            if cur[i] != cur[-1]:
                continue

            up = cur[:]
            up[i] += 1
            up[-1] += 1
            q.appendleft((up, depth + 1))

            down = cur[:]
            down[i] -= 1
            down[-1] -= 1
            q.appendleft((down, depth + 1))

            for j in range(i + 1, len(cur) - 1):
                if cur[j] != cur[-1]:
                    continue

                up = cur[:]
                up[i] += 1
                up[j] += 1
                up[-1] += 1
                q.appendleft((up, depth + 1))

                down = cur[:]
                down[i] -= 1
                down[j] -= 1
                down[-1] -= 1
                q.appendleft((down, depth + 1))
    else:
        return "unsolved", count


print(f())
# part 1
# 27 is not the right answer
