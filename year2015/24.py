from util import get_lines_for_day
from functools import reduce
from operator import mul


def f(lines):
    weights = list(map(int, lines))

    total_weight = sum(weights)
    group_size = total_weight // 4
    all_groups = []

    def dfs(group, choices, i=0):
        size = sum(group)

        if size > group_size:
            return
        elif size == group_size:
            all_groups.append(group)
            return

        for index in range(i, len(choices)):
            c = choices[index]
            dfs(group + [c], choices[:index] + choices[index + 1:], index)

    dfs([], weights)

    all_groups.sort(key=len)

    min_qe = reduce(mul, all_groups[0])
    l = len(all_groups[0])
    i = 0

    while len(all_groups[i]) == l:
        min_qe = min(min_qe, reduce(mul, all_groups[i]))
        i += 1

    return min_qe


print(f(get_lines_for_day(2015, 24)))
# part 1
# 266172011551 is to high
