from collections import deque
from hashlib import md5


def h(data):
    return md5(bytes(data, encoding='utf-8')).hexdigest()[:4]


incs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dirs = ['U', 'D', 'L', 'R']


def f(passcode, width, height):
    destination = (height - 1, width - 1)
    q = deque([(0, 0, '')])

    while q:
        r, c, path = q.pop()
        if (r, c) == destination:
            return path

        doors = [c in 'bcdef' for c in h(passcode + path)]

        for i, door in enumerate(doors):
            if door:
                incr, incc = incs[i]
                dir = dirs[i]
                newr, newc = r + incr, c + incc
                if 0 <= newr < height and 0 <= newc < width:
                    q.appendleft((newr, newc, path + dir))


def g(passcode, width, height):
    destination = (height - 1, width - 1)
    longest_path = ''

    def dfs(r, c, path):
        nonlocal longest_path

        if (r, c) == destination:
            if len(path) > len(longest_path):
                longest_path = path
            return

        doors = [c in 'bcdef' for c in h(passcode + path)]

        for i, door in enumerate(doors):
            if door:
                incr, incc = incs[i]
                dir = dirs[i]
                newr, newc = r + incr, c + incc
                if 0 <= newr < height and 0 <= newc < width:
                    dfs(newr, newc, path + dir)

    dfs(0, 0, '')

    return len(longest_path)


print(g('awrkjxxr', 4, 4))
