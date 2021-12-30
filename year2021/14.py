from util import get_lines_for_day, get_groups
from collections import Counter


def polymerize(pair_counter, rules, element_counter, num_steps):
    for _ in range(num_steps):
        new_pair_counter = pair_counter.copy()
        for pair, count in pair_counter.items():
            m, n = pair
            element = rules[pair]
            element_counter[element] += count
            new_pair_counter[pair] -= count
            new_pair_counter[m+element] += count
            new_pair_counter[element+n] += count
        pair_counter = new_pair_counter
    return max(element_counter.values()) - min(element_counter.values())


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 14)

    # gets a List[List[str]] representing groups of lines separated by blank lines from the input
    groups = get_groups(lines)

    template = groups[0][0]
    element_counter = Counter(template)
    rules = {}
    pair_counter = {}
    for line in groups[1]:
        pair, element = line.split(' -> ')
        rules[pair] = element
        pair_counter[pair] = 0
    for m, n in zip(template, template[1:]):
        pair_counter[m+n] += 1

    element_counter2 = element_counter.copy()
    pair_counter2 = pair_counter.copy()

    print(polymerize(pair_counter, rules, element_counter, 10))
    print(polymerize(pair_counter2, rules, element_counter2, 40))