from util import get_lines_for_day


def get_new_molecules(molecule, replacements):
    new_molecules = set()

    for to_find, to_replace in replacements:
        i = molecule.find(to_find)
        while i != -1:
            new_molecules.add(molecule[:i] + to_replace + molecule[i + len(to_find):])
            i = molecule.find(to_find, i + 1)

    return new_molecules


def reverse_get_new_molecules(molecule, replacements, visited):
    new_molecules = []

    for to_replace, to_find in replacements:
        i = molecule.find(to_find)
        while i != -1:
            new_molecule = molecule[:i] + to_replace + molecule[i + len(to_find):]
            if new_molecule not in visited:
                visited.add(new_molecule)
                new_molecules.append(new_molecule)
                i = molecule.find(to_find, i + 1)

    return new_molecules


def f(lines):
    replacements = []
    min_steps = float('inf')
    visited = set()

    for i, line in enumerate(lines):
        if line == '':
            break

        line = line.split(' => ')
        replacements.append((line[0], line[1]))

    molecule = lines[i + 1]
    count = 1

    def dfs(new_molecules, steps, prev_len=float('inf')):
        nonlocal min_steps, molecule, count

        if steps >= min_steps:
            return

        if len(new_molecules) == 0:
            return

        min_len = min(map(len, new_molecules))

        if min_len <= 1 and 'e' not in new_molecules:
            return

        if min_len > prev_len:
            return

        if 'e' in new_molecules:
            min_steps = steps
            return

        for m in new_molecules:
            if count % 1000 == 0:
                print(count, min_steps, min(map(len, new_molecules)))
            #     exit(1)

            count += 1
            if m not in visited:
                visited.add(m)
                dfs(reverse_get_new_molecules(m, replacements, visited), steps + 1, min_len)

    dfs({molecule}, 0)

    return min_steps


print(f(get_lines_for_day(2015, '19')))
# part 1
# 192 is too low
# part 2
# 200 is the right answer, but my program doesn't halt. why?
