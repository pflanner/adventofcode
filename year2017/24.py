from util import get_lines_for_day


class Connector:
    def __init__(self, a, b, id):
        self.a = a
        self.b = b
        self.id = id

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return isinstance(other, Connector) and self.id == other.id


def f(lines):
    connectors = set()

    for i, line in enumerate(lines):
        a, b = line.split('/')
        connectors.add(Connector(a, b, i))

    strongest = 0
    longest = 0
    short_circuit_count = 0
    mem = set()

    def dfs(bridge, strength, remaining):
        nonlocal strongest, longest, short_circuit_count

        h = '-'.join(bridge)
        if h in mem:
            short_circuit_count += 1
            return

        mem.add(h)

        if len(bridge) > longest:
            strongest = strength
            longest = len(bridge)
        elif len(bridge) == longest and strength > strongest:
            strongest = strength

        for connector in remaining:
            a, b = connector.a, connector.b
            new_strength = strength + int(a) + int(b)
            new_remaining = remaining.difference({connector})

            if a == bridge[-1]:
                bridge.extend([a, b])
                dfs(bridge, new_strength, new_remaining)
                bridge.pop()
                bridge.pop()

            if b == bridge[-1]:
                bridge.extend([b, a])
                dfs(bridge, new_strength, new_remaining)
                bridge.pop()
                bridge.pop()

    dfs(['0'], 0, connectors)

    return strongest


print(f(get_lines_for_day(2017, 24)))
# part 1
# 1367 is too low
