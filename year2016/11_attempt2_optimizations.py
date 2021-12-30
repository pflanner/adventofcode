from collections import deque


def f():
    count = 0

    # array value is the floor each item is on
    # the array is arranged such that each microchip is to the right of its generator
    # so all microchips are at odd indices and all generators are at even indices
    # the elevator is in the last position
    # floors = [1, 1, 2, 3, 2, 3, 2, 3, 2, 3, 1]              # Part 1
    floors = [1, 1, 2, 3, 2, 3, 2, 3, 2, 3, 1, 1, 1, 1, 1]  # Part 2
    # floors = [2, 1, 3, 1, 1]                              # Advent of Code Test
    # floors = [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1]            # Redditor Test

    def is_valid(floors):
        if not all(1 <= floor <= 4 for floor in floors):
            return False

        generators = floors[:-1:2]
        microchips = floors[1:-1:2]

        for g, m in zip(generators, microchips):
            if g != m and any(m == otherg for otherg in generators):
                return False

        return True

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
    visited = {h(floors)}

    while q:
        # if count % 10000 == 0:
        #     print(count)
        cur, depth = q.pop()

        for i in range(len(cur) - 1):
            if cur[i] != cur[-1]:
                continue

            up = cur[:]
            up[i] += 1
            up[-1] += 1

            if all(floor == 4 for floor in up):
                return depth + 1, count

            if is_valid(up):
                t = h(up)
                if t not in visited:
                    visited.add(t)
                    q.appendleft((up, depth + 1))

            down = cur[:]
            down[i] -= 1
            down[-1] -= 1

            if all(floor == 4 for floor in down):
                return depth + 1, count

            if is_valid(down):
                t = h(down)
                if t not in visited:
                    visited.add(t)
                    q.appendleft((down, depth + 1))

            count += 2

            for j in range(i + 1, len(cur) - 1):
                if cur[j] != cur[-1]:
                    continue

                up = cur[:]
                up[i] += 1
                up[j] += 1
                up[-1] += 1

                if all(floor == 4 for floor in up):
                    return depth + 1, count

                if is_valid(up):
                    t = h(up)
                    if t not in visited:
                        visited.add(t)
                        q.appendleft((up, depth + 1))

                down = cur[:]
                down[i] -= 1
                down[j] -= 1
                down[-1] -= 1

                if all(floor == 4 for floor in down):
                    return depth + 1, count

                if is_valid(down):
                    t = h(down)
                    if t not in visited:
                        visited.add(t)
                        q.appendleft((down, depth + 1))

                count += 2
    else:
        return "unsolved", count


print(f())
# part 1
# 27 is not the right answer
