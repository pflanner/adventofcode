def to_int(password):
    i = 0
    mult = 1

    for c in reversed(password):
        i += (ord(c) - ord('a')) * mult
        mult *= 26

    return i


def to_string(i):
    s = []

    while i > 0:
        s.append(chr(ord('a') + (i % 26)))
        i //= 26

    s += ['a'] * (8 - len(s))

    return ''.join(reversed(s))


def follows_rules(password):
    if 'i' in password or 'o' in password or 'l' in password:
        return False

    straight = False
    pairs = set()

    for i, c in enumerate(password):
        if i < len(password) - 1:
            d = password[i + 1]

            if c == d:
                pairs.add(c)

            if i < len(password) - 2:
                e = password[i + 2]
                if ord(c) + 1 == ord(d) and ord(d) + 1 == ord(e):
                    straight = True

    return len(pairs) >= 2 and straight


def f(password):
    i = to_int(password)
    # count = 0

    while not follows_rules(password):
        # if count % 1000 == 0:
        #     print(count, password)
        # count += 1

        i_index = password.find('i')
        i_index = i_index if i_index != -1 else float('inf')
        o_index = password.find('o')
        o_index = o_index if o_index != -1 else float('inf')
        l_index = password.find('l')
        l_index = l_index if l_index != -1 else float('inf')

        if i_index < o_index and i_index < l_index:
            password = password[:i_index] + 'j' + ''.join(['a'] * (len(password) - i_index - 1))
            i = to_int(password)
            continue

        if o_index < i_index and o_index < l_index:
            password = password[:o_index] + 'p' + ''.join(['a'] * (len(password) - o_index - 1))
            i = to_int(password)
            continue

        if l_index < i_index and l_index < o_index:
            password = password[:l_index] + 'm' + ''.join(['a'] * (len(password) - l_index - 1))
            i = to_int(password)
            continue

        i += 1
        password = to_string(i)

    return password


print(f('hepxxzaa'))
