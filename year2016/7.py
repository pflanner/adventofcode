from util import get_lines_for_day


def has_abba(line, i):
    a, b = line[i], line[i + 1]

    return a != b and line[i + 2] == b and line[i + 3] == a


def has_aba(line, i, ab=None):
    a, b = line[i], line[i + 1]
    if ab is not None:
        a, b = ab

    return a != b and a == line[i] and b == line[i + 1] and a == line[i + 2]


def get_hypernets_and_supernets(line):
    hypernets = []
    supernets = [[]]
    in_hypernet = False

    for c in line:
        if c == '[':
            in_hypernet = True
            hypernets.append([])
            continue

        if c == ']':
            in_hypernet = False
            supernets.append([])
            continue

        if in_hypernet:
            hypernets[-1].append(c)
        else:
            supernets[-1].append(c)

    return hypernets, supernets


def supports_tls(line):
    hypernets, supernets = get_hypernets_and_supernets(line)

    for hypernet in hypernets:
        for i in range(len(hypernet) - 3):
            if has_abba(hypernet, i):
                return False

    for supernet in supernets:
        for i in range(len(supernet) - 3):
            if has_abba(supernet, i):
                return True

    return False


def supports_ssl(line):
    hypernets, supernets = get_hypernets_and_supernets(line)

    for supernet in supernets:
        for i in range(len(supernet) - 2):
            if has_aba(supernet, i):
                for hypernet in hypernets:
                    for j in range(len(hypernet) - 2):
                        if has_aba(hypernet, j, supernet[i + 1] + supernet[i]):
                            return True

    return False


def f(lines):
    tls_count = ssl_count = 0

    for line in lines:
        if supports_tls(line):
            tls_count += 1

        if supports_ssl(line):
            ssl_count += 1

    return tls_count, ssl_count


print(f(get_lines_for_day(2016, 7)))

