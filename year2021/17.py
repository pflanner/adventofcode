from util import get_lines_for_day


# find a value that works for the x velocity
def find_x_vel(xstart, xend):
    x = 1

    while x < xstart:
        xv = x
        xpos = 0
        while xv > 0:
            xpos += xv
            xv -= 1
            if xstart <= xpos <= xend:
                return x
        x += 1
    return None


def does_hit_target(xstart, xend, ybottom, ytop, xvel, yvel):
    xpos = ypos = 0
    while ypos >= ybottom and xpos <= xend:
        xpos += xvel
        xvel -= 1 if xvel != 0 else 0

        ypos += yvel
        yvel -= 1

        if xstart <= xpos <= xend and ybottom <= ypos <= ytop:
            return True
    return False


# instead of figuring out what the ending condition is here,
# I'm just running an infinite loop and printing out the highest
# y position at each step and will wait until it stabilizes
def highest_y_for_x(xstart, xend, ybottom, ytop, x):
    y = 1
    highesty = float('-inf')

    while True:
        xvel = x
        yvel = y
        xpos = ypos = 0
        highy = 0
        while ypos >= ybottom:
            xpos += xvel
            xvel -= 1 if xvel != 0 else 0

            ypos += yvel
            yvel -= 1
            highy = max(ypos, highy)

            if xstart <= xpos <= xend and ybottom <= ypos <= ytop:
                highesty = max(highy, highesty)

        y += 1
        print(highesty)


def part1(xstart, xend, ybottom, ytop):
    x = find_x_vel(xstart, xend)
    highest_y_for_x(xstart, xend, ybottom, ytop, x)


def part2(xstart, xend, ybottom, ytop):
    x = find_x_vel(xstart, xend)
    y = -200
    count = 0
    found = set()

    while x <= xend:
        while y <= 200:
            if does_hit_target(xstart, xend, ybottom, ytop, x, y):
                count += 1
                found.add((x, y))
            y += 1
        y = -200
        x += 1
    return count


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 17)

    ranges = lines[0].split('target area: ')[1]
    xrange, yrange = ranges.split(', ')
    xstart, xend = map(int, xrange[2:].split('..'))
    ystart, yend = map(int, yrange[2:].split('..'))

    # just let part1 run until it stabilizes and starts printing out the same
    # thing over and over again. Then, once we have the answer for part 1,
    # we can use it to determine the range to use for part 2
    part1(xstart, xend, ystart, yend)
    print(part2(xstart, xend, ystart, yend))