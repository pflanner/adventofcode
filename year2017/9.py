from util import get_lines_for_day


def f(lines):
    score = 0
    garbage_count = 0
    open_groups = 0
    is_garbage = False
    i = 0

    while i < len(lines[0]):
        c = lines[0][i]

        if is_garbage:
            if c == '!':
                i += 2
                continue
            if c == '>':
                is_garbage = False
            else:
                garbage_count += 1
        elif c == '{':
            open_groups += 1
            score += open_groups
        elif c == '}':
            open_groups -= 1
        elif c == '<':
            is_garbage = True

        i += 1

    return score, garbage_count


print(f(get_lines_for_day(2017, 9)))
