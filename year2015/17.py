from util import get_lines_for_day


def f(lines):
    containers = []
    num_combinations = 0

    for line in lines:
        containers.append(int(line))

    def dfs(choices, total, start_index):
        nonlocal num_combinations
        num_containers = len(containers) - len(choices)

        if total == 150 and num_containers == 4:
            num_combinations += 1
            return

        if not choices or total > 150:
            return

        for i, choice in enumerate(choices[start_index:], start_index):
            dfs(choices[:i] + choices[i + 1:], total + choice, i)

    dfs(containers, 0, 0)

    return num_combinations


print(f(get_lines_for_day(2015, 17)))
