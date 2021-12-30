from util import get_input_for_day
from collections import Counter
from functools import reduce
from operator import add


def f():
    todays_input = get_input_for_day(6)
    n = 0
    group = set()

    for line in todays_input.split('\n'):
        if not line:
            n += len(group)
            group.clear()
            continue

        group.update(set(line))

    print(n)


def get_groups(lines):
    groups = []
    group = []

    for line in lines:
        if line:
            group.append(line)
        else:
            groups.append(group)
            group = []

    return groups


def both_parts():
    i = get_input_for_day(6)
    n = 0
    m = 0

    for group in get_groups(i.split('\n')):
        s = set(group[0])
        t = set(group[0])

        for line in group:
            s |= set(line)
            t &= set(line)

        n += len(s)
        m += len(t)

    print(n, m)


def groups(input_text):
    return [[set(answers) for answers in group.split('\n')] for group in input_text.split('\n\n')]


def functional():
    i = get_input_for_day(6)
    print(reduce(add, map(len, (reduce(lambda s, t: s | t, map(set, group)) for group in groups(i.strip())))))
    print(reduce(add, map(len, (reduce(lambda s, t: s & t, map(set, group)) for group in groups(i.strip())))))


def functional2():
    i = get_input_for_day(6)
    print(sum(len(set.union(*group)) for group in groups(i.strip())))
    print(sum(len(set.intersection(*group)) for group in groups(i.strip())))


def g():
    todays_input = get_input_for_day(6)
    n = 0
    group = Counter()
    lines = 0

    for line in todays_input.split('\n'):
        if not line:
            n += len([True for q, count in group.items() if count == lines])
            group.clear()
            lines = 0
            continue

        group.update(line)
        lines += 1

    print(n)


functional()
functional2()
