from util import get_lines_for_day
from collections import Counter
from operator import itemgetter
import string


def decrypt(full_name, sector_id):
    decrypted_name = []

    for c in full_name:
        if c == '-':
            decrypted_name.append(' ')
        else:
            shift = sector_id % 26
            index = ord(c) - ord('a')
            c = string.ascii_lowercase[(index + shift) % 26]
            decrypted_name.append(c)

    return ''.join(decrypted_name)

def f(lines):
    id_sum = 0

    for line in lines:
        full_name = line[:line.rindex('-')]
        line = line.split('-')
        name = ''.join(line[:-1])
        sector_id, checksum = line[-1].split('[')
        sector_id = int(sector_id)
        checksum = checksum.replace(']', '')

        c = Counter(name)
        cl = [(v, k) for k, v in c.items()]
        cl.sort(key=itemgetter(1))
        cl.sort(key=itemgetter(0), reverse=True)
        gen_checksum = ''.join(map(itemgetter(1), cl[:5]))

        if gen_checksum == checksum:
            id_sum += sector_id
            print(decrypt(full_name, sector_id), sector_id)
        else:
            print('[FAKE] ' + decrypt(full_name, sector_id), sector_id)

    return id_sum


print(f(get_lines_for_day(2016, 4)))
