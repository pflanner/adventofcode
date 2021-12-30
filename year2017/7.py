from util import get_lines_for_day
from collections import defaultdict, Counter


def f(lines):
    programs = defaultdict(list)
    children = set()
    weights = {}
    root = None

    for line in lines:
        line = line.split()
        weight = line[1].replace('(', '')
        weight = int(weight.replace(')', ''))
        c = list(map(lambda x: x.replace(',', ''), line[3:]))
        program = line[0]
        programs[program].extend(c)
        weights[program] = weight
        children.update(c)

    for program in programs:
        if program not in children:
            root = program
            break

    def dfs(root):
        w = weights[root]

        if len(programs[root]) == 0:
            return w

        to_compare = []

        for child in programs[root]:
            to_compare.append(dfs(child))

        counts = Counter(to_compare)
        for n, c in counts.items():
            if c == 1:
                i = to_compare.index(n)
                diff = to_compare[(i + 1) % len(to_compare)] - n
                w = weights[programs[root][i]]
                adjusted_weight = w + diff
                print(adjusted_weight)

        return sum(to_compare) + w

    return dfs(root)


print(f(get_lines_for_day(2017, 7)))
