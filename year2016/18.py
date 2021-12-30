from util import get_input_for_day


def f(row):
    row = row.strip()
    safe_count = len([c for c in row if c == '.'])

    for _ in range(399999):
        row = '.' + row + '.'
        new_row = []

        for i in range(1, len(row) - 1):
            left, center, right = row[i - 1], row[i], row[i + 1]

            if left == '^' and right == '.' or right == '^' and left == '.':
                new_row.append('^')
            else:
                new_row.append('.')

        safe_count += len([c for c in new_row if c == '.'])
        row = ''.join(new_row)

    return safe_count


print(f(get_input_for_day(2016, 18)))
# part 1
# 2041 is too high
