from collections import deque
from hashlib import md5


def generate_hash(h):
    for _ in range(2017):
        h = md5(bytes(h, encoding='utf8')).hexdigest()

    return h


def f(salt):
    i = 0
    cur = generate_hash(salt + str(i))
    next_1000 = deque([generate_hash(salt + str(n)) for n in range(1, 1001)])
    keys = []

    while len(keys) < 64:
        for j, c in enumerate(cur[:-2]):
            if c == cur[j + 1] == cur[j + 2]:
                for n in next_1000:
                    if c + c + c + c + c in n:
                        keys.append(cur)
                        break
                break

        cur = next_1000.popleft()
        i += 1
        next_1000.append(generate_hash(salt + str(i)))

    return i - 1


# print(f('cuanljph'))
print(f('abc'))
# print(generate_hash('abc5'))
# part 1
# 626065 is too high
# 20188 is too low

# part 2
# 21606 is too high
