from util import get_lines_for_day


def f(lines):
    valid_triangles = 0
    t = [[] for _ in range(3)]

    for line in lines:
        a, b, c = map(int, line.split())
        t[0].append(a)
        t[1].append(b)
        t[2].append(c)

        if len(t[0]) == 3:
            for i, triangle in enumerate(t):
                a, b, c = triangle
                if a + b > c and a + c > b and b + c > a:
                    valid_triangles += 1
                t[i].clear()

    return valid_triangles


print(f(get_lines_for_day(2016, 3)))
