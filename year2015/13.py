from util import get_lines_for_day


def f(lines):
    h = {}
    all_people = set()
    max_happiness = 0
    best_arrangement = None

    for line in lines:
        line = line.split()
        p1, p2 = line[0], line[-1][:-1]
        all_people.update({p1, p2})
        amt = int(line[3])
        if line[2] == 'lose':
            amt *= -1

        h[(p1, p2)] = amt

    all_people.add('Tito')

    def dfs(p, choices):
        nonlocal max_happiness, best_arrangement
        if len(p) == len(all_people):
            happiness = 0
            for p1, p2 in zip(p, p[1:]):
                happiness += h.get((p1, p2), 0)
                happiness += h.get((p2, p1), 0)
            happiness += h.get((p[0], p[-1]), 0)
            happiness += h.get((p[-1], p[0]), 0)
            if happiness > max_happiness:
                max_happiness = happiness
                best_arrangement = p
            return

        for c in choices:
            dfs(p + [c], choices - {c})

    dfs([], all_people)

    return max_happiness, best_arrangement


print(f(get_lines_for_day(2015, 13)))
