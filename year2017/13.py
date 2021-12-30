from util import get_lines_for_day


def f(lines):
    caught = True
    delay = 0

    while caught:
        caught = False

        for line in lines:
            layer, depth = map(int, line.split(': '))
            layer += delay

            pathlen = 2*depth-2
            s = layer % pathlen
            t = s % depth
            pos = layer % pathlen if layer % pathlen < depth else depth - 2 - t

            if pos == 0:
                caught = True
                break

        delay += 1

    return delay - 1


print(f(get_lines_for_day(2017, '13')))
# part 1
# 2348 is too high
# 2104 is too high

# part 2
# 3896407 is too high; off by one
