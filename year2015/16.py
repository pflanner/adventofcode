from util import get_lines_for_day


def f(lines):
    m = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

    for line in lines:
        line = line.split()
        id = int(line[1][:-1])
        for i in range(2, len(line), 2):
            item = line[i][:-1]
            value = int(line[i + 1].replace(',', ''))
            expected_value = m.get(item, '')
            if item in ('cats', 'trees'):
                if value <= expected_value:
                    break
            elif item in ('pomeranians', 'goldfish'):
                if value >= expected_value:
                    break
            elif expected_value != value:
                break
        else:
            return id


print(f(get_lines_for_day(2015, 16)))
# part2
# 213 is too low
