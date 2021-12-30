from util import get_lines_for_day


def f(i):
    wrapping_paper_area = 0
    ribbon_length = 0

    for line in i:
        l, w, h = map(int, line.split('x'))
        areas = [l * w, l * h, w * h]
        perimeters = [2*l + 2*w, 2*l + 2*h, 2*w + 2*h]
        wrapping_paper_area += 2 * sum(areas) + min(areas)
        ribbon_length += min(perimeters) + l * w * h

    return wrapping_paper_area, ribbon_length


print(f(get_lines_for_day(2015, 2)))
