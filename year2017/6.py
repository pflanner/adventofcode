from util import get_lines_for_day


def count_cycles(blocks):
    cycles = 0
    seen = set()

    while tuple(blocks) not in seen:
        seen.add(tuple(blocks))
        cycles += 1
        highest = blocks[0]
        index = 0

        for i, block in enumerate(blocks):
            if block > highest:
                highest = block
                index = i

        blocks[index] = 0

        i = (index + 1) % len(blocks)
        for _ in range(highest):
            blocks[i] += 1
            i = (i + 1) % len(blocks)

    return cycles, blocks


def f(lines):
    blocks = list(map(int, lines[0].split()))

    _, blocks = count_cycles(blocks)
    cycles, _ = count_cycles(blocks)

    return cycles


print(f(get_lines_for_day(2017, 6)))
