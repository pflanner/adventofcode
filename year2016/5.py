from hashlib import md5


def f(door_id):
    password = ['_'] * 8
    i = 0

    while any(map(lambda x: x == '_', password)):
        to_hash = door_id + str(i)
        h = md5(bytes(to_hash, encoding='utf-8')).hexdigest()

        if h.startswith('00000'):
            pos = h[5]
            if '0' <= pos <= '7':
                pos = int(pos)
                if password[pos] == '_':
                    password[pos] = h[6]
            print(''.join(password))

        i += 1

    return ''.join(password)


print(f('cxdnnyjw'))
