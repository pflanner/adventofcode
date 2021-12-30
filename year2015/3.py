from util import get_lines_for_day


def f(i):
    pos = santa = robo = (0, 0)
    visits = {pos}
    visits2 = {santa}
    is_santa = True

    for line in i:
        for c in line:
            if c == '>':
                pos = (pos[0] + 1, pos[1])
                if is_santa:
                    santa = (santa[0] + 1, santa[1])
                else:
                    robo = (robo[0] + 1, robo[1])
            elif c == '<':
                pos = (pos[0] - 1, pos[1])
                if is_santa:
                    santa = (santa[0] - 1, santa[1])
                else:
                    robo = (robo[0] - 1, robo[1])
            elif c == '^':
                pos = (pos[0], pos[1] + 1)
                if is_santa:
                    santa = (santa[0], santa[1] + 1)
                else:
                    robo = (robo[0], robo[1] + 1)
            elif c == 'v':
                pos = (pos[0], pos[1] - 1)
                if is_santa:
                    santa = (santa[0], santa[1] - 1)
                else:
                    robo = (robo[0], robo[1] - 1)
            is_santa = not is_santa

            visits.add(pos)
            visits2.add(santa)
            visits2.add(robo)

    return len(visits), len(visits2)


print(f(get_lines_for_day(2015, 3)))
