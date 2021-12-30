from util import get_lines_for_day


reverse_rotate_indices = {
    1: -1,
    3: -2,
    5: -3,
    7: -4,
    2: 2,
    4: 1,
    6: 0,
    0: 7,
}


def rotate(password, n):
    if n == 0:
        return
    if n < 0:
        password.reverse()

    for _ in range(abs(n)):
        tmp = password[-1]
        for i in range(len(password)):
            tmp, password[i] = password[i], tmp
    if n < 0:
        password.reverse()


def f(lines, password, reverse=False):
    password = list(password)
    if reverse:
        lines.reverse()
    for line in lines:
        line = line.split()
        op = ' '.join([line[0], line[1]])

        if op == 'swap position':
            i1, i2 = int(line[2]), int(line[5])
            password[i1], password[i2] = password[i2], password[i1]
        elif op == 'swap letter':
            i1, i2 = password.index(line[2]), password.index(line[5])
            password[i1], password[i2] = password[i2], password[i1]
        elif op == 'rotate right':
            n = int(line[2]) % len(password)
            if reverse:
                n = -n
            rotate(password, n)
        elif op == 'rotate left':
            n = int(line[2]) % len(password)
            if reverse:
                n = -n
            rotate(password, -n)
        elif op == 'rotate based':
            n = password.index(line[6])
            if reverse:
                n = reverse_rotate_indices[n]
            else:
                if n >= 4:
                    n += 1
                n += 1
            rotate(password, n)
        elif op == 'reverse positions':
            i1, i2 = int(line[2]), int(line[4])
            password = password[:i1] + list(reversed(password[i1:i2 + 1])) + password[i2 + 1:]
        elif op == 'move position':
            i1, i2 = int(line[2]), int(line[5])
            if reverse:
                i1, i2 = i2, i1
            c = password[i1]
            password.remove(c)
            password.insert(i2, c)

    return ''.join(password)


# print(f(get_lines_for_day(year2016, 21), 'abcdefgh'))
# part 1
# bacfdgeh is not the right answer


print(f(get_lines_for_day(2016, 21), 'fbgdceah', reverse=True))

# print(f(
#     [
#         'swap position 4 with position 0',
#         'swap letter d with letter b',
#         'reverse positions 0 through 4',
#         'rotate left 1 step',
#         'move position 1 to position 4',
#         'move position 3 to position 0',
#         'rotate based on position of letter b',
#         'rotate based on position of letter d',
#     ],
#     'abcde'))
#
# scrambled = f(['rotate based on position of letter a'], 'abcdefgh')
# print(scrambled, scrambled.index('a'))
# scrambled = f(['rotate based on position of letter b'], 'abcdefgh')
# print(scrambled, scrambled.index('b'))
# scrambled = f(['rotate based on position of letter c'], 'abcdefgh')
# print(scrambled, scrambled.index('c'))
# scrambled = f(['rotate based on position of letter d'], 'abcdefgh')
# print(scrambled, scrambled.index('d'))
# scrambled = f(['rotate based on position of letter e'], 'abcdefgh')
# print(scrambled, scrambled.index('e'))
# scrambled = f(['rotate based on position of letter f'], 'abcdefgh')
# print(scrambled, scrambled.index('f'))
# scrambled = f(['rotate based on position of letter g'], 'abcdefgh')
# print(scrambled, scrambled.index('g'))
# scrambled = f(['rotate based on position of letter h'], 'abcdefgh')
# print(scrambled, scrambled.index('h'))
