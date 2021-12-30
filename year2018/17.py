from util import get_lines_for_day
from time import sleep


def get_input_from_data(data):
    minx = maxx = 500
    miny = maxy = 0
    real_miny = float('inf')

    clay = set()
    touched = set()
    water = set()

    for line in data:
        line = line.split(', ')
        left_label, left_val = line[0].split('=')
        left_val = int(left_val)
        right_val = line[1].split('=')[1]
        start, end = map(int, right_val.split('..'))

        for i in range(start, end + 1):
            if left_label == 'x':
                real_miny = min(real_miny, i)
                clay.add((left_val, i))
                minx = min(minx, left_val)
                miny = min(miny, i)
                maxx = max(maxx, left_val)
                maxy = max(maxy, i)
            else:
                real_miny = min(real_miny, left_val)
                clay.add((i, left_val))
                minx = min(minx, i)
                miny = min(miny, left_val)
                maxx = max(maxx, i)
                maxy = max(maxy, left_val)

    return clay, water, touched, (500, 0), minx, miny, maxx, maxy, real_miny


def get_input_from_picture(filename):
    minx = miny = maxx = maxy = 0
    real_miny = float('inf')

    clay = set()
    touched = set()
    water = set()

    spring_location = None

    with open(filename) as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line):
                maxx = max(maxx, x)
                maxy = max(maxy, y)

                if c == '+':
                    spring_location = (x, y)
                elif c == '#':
                    real_miny = min(real_miny, y)
                    clay.add((x, y))

    return clay, water, touched, spring_location, minx, miny, maxx, maxy, real_miny


def print_ground_scan(clay, water, touched, minx, miny, maxx, maxy, print_delay, spring_location=(500, 0)):
    print('\033c')
    for y in range(miny, maxy + 1):
        for x in range(minx - 1, maxx + 2):
            if (x, y) == spring_location:
                print('+', end='')
                continue

            if (x, y) in clay:
                print('#', end='')
            elif (x, y) in water:
                print('~', end='')
            elif (x, y) in touched:
                print('|', end='')
            else:
                print('.', end='')

        print()

    if print_delay > 0:
        sleep(print_delay)


def crop(clay, water, touched, minx, miny, maxx, maxy):
    new_clay = set()
    new_water = set()
    new_touched = set()

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            pos = (x, y)

            if pos in clay:
                new_clay.add(pos)

            if pos in water:
                new_water.add(pos)

            if pos in touched:
                new_touched.add(pos)

    return new_clay, new_water, new_touched


def get_retained_water(clay, water, touched, minx, miny, maxx, maxy):
    # add all touched to water
    water.update(touched)

    # traverse the grid row by row looking for water. when water is found, check if it is bound left and right by clay
    # only water bound left and right by clay will be retained
    x, y = minx - 1, miny
    while y <= maxy:
        while x <= maxx + 1:
            if (x, y) in water:
                lx = x - 1
                while (lx, y) in water:
                    lx -= 1

                rx = x + 1
                while (rx, y) in water:
                    rx += 1

                if (lx, y) not in clay or (rx, y) not in clay:
                    for xx in range(lx + 1, rx):
                        water.remove((xx, y))

                x = rx
            x += 1
        y += 1
        x = minx - 1

    return water


def f(clay, water, touched, spring_location, minx, miny, maxx, maxy, real_miny, should_print=False, print_delay=0.1, should_crop=False):
    if should_crop:
        minx, miny, maxx, maxy = 475, 0, 525, 50
        clay, water, touched = crop(clay, water, touched, 475, 0, 525, 50)
    # print_ground_scan(clay, water, touched, 475, 0, 525, 50, print_delay)
    # print_ground_scan(clay, water, touched, minx, miny, maxx, maxy, print_delay)
    # return
    # print(f'minx={minx}, miny={miny}, maxx={maxx}, maxy={maxy}, pixels={(maxx-minx)*(maxy-miny)}')

    def is_empty(pos):
        return pos not in clay and pos not in water and pos not in touched

    def dfs(x, y):
        while y <= maxy and ((x, y) not in water or (x-1, y-1) in clay or (x+1, y-1) in clay):
            down = (x, y)
            if is_empty(down):
                touched.add(down)
                y += 1
            else:
                y -= 1
                if (x, y) not in clay:
                    touched.add((x, y))
                # go left
                left = (x - 1, y)
                down = (x - 1, y + 1)
                while (is_empty(left) or left in touched) and not is_empty(down):
                    if left not in touched:
                        water.add(left)
                    if down in touched:
                        touched.remove(down)
                        water.add(down)
                    left = (left[0] - 1, y)
                    down = (left[0], y + 1)

                    if should_print:
                        print_ground_scan(clay, water, touched, minx, miny, maxx, maxy, print_delay)

                if is_empty(down) and (down[0] + 1, down[1]) in clay:
                    dfs(down[0], down[1] - 1)

                # go right
                right = (x + 1, y)
                down = (x + 1, y + 1)
                while (is_empty(right) or right in touched) and not is_empty(down):
                    if right not in touched:
                        water.add(right)
                    right = (right[0] + 1, y)
                    down = (right[0], y + 1)

                    if should_print:
                        print_ground_scan(clay, water, touched, minx, miny, maxx, maxy, print_delay)

                if is_empty(down):
                    dfs(down[0], down[1] - 1)

                if not is_empty(left) and left not in touched and not is_empty(right) and right not in touched:
                    dfs(x, y)

                break

            if should_print:
                print_ground_scan(clay, water, touched, minx, miny, maxx, maxy, print_delay)

    dfs(spring_location[0], spring_location[1] + 1)

    # print(f'minx={minx}, miny={miny}, maxx={maxx}, maxy={maxy}')
    retained_water = get_retained_water(clay, water, touched, minx, miny, maxx, maxy)
    print_ground_scan(clay, retained_water, set(), minx, miny, maxx, maxy, print_delay)
    non_empty = set()
    for s in [touched, water]:
        for t in s:
            x, y = t
            if minx - 1 <= x <= maxx + 1 and real_miny <= y <= maxy:
                non_empty.add(t)

    return len(non_empty), len(water.union(touched)), len(retained_water), len(retained_water.intersection(clay))


def g(clay, water, touched, spring_location, minx, miny, maxx, maxy, real_miny, should_print=False, print_delay=0.1, should_crop=False):
    if should_crop:
        minx, miny, maxx, maxy = 475, 0, 525, 50
        clay, water, touched = crop(clay, water, touched, 475, 0, 525, 50)
    # print_ground_scan(clay, water, touched, 475, 0, 525, 50, print_delay)
    # print_ground_scan(clay, water, touched, minx, miny, maxx, maxy, print_delay)
    # return
    # print(f'minx={minx}, miny={miny}, maxx={maxx}, maxy={maxy}, pixels={(maxx-minx)*(maxy-miny)}')

    def is_empty(pos):
        return pos not in clay and pos not in water and pos not in touched

    def dfs(x, y):
        while y <= maxy and ((x, y) not in water or (x-1, y-1) in clay or (x+1, y-1) in clay):
            down = (x, y)
            if down in touched:
                touched.remove(down)
                water.add(down)

            if is_empty(down):
                touched.add(down)
                y += 1
            else:
                y -= 1
                if (x, y) not in clay:
                    touched.add((x, y))
                # go left
                left = (x - 1, y)
                down = (x - 1, y + 1)
                while (is_empty(left) or left in touched) and not is_empty(down):
                    touched.add(left)
                    # if left not in touched:
                    #     water.add(left)
                    # else:
                    #     touched.remove(left)
                    #     water.add(left)
                    if down in touched:
                        touched.remove(down)
                        water.add(down)

                    left = (left[0] - 1, y)
                    down = (left[0], y + 1)

                    if should_print:
                        print_ground_scan(clay, water, touched, minx, miny, maxx, maxy, print_delay)

                if is_empty(down) and (down[0] + 1, down[1]) in clay:
                    dfs(down[0], down[1] - 1)

                # go right
                right = (x + 1, y)
                down = (x + 1, y + 1)
                while (is_empty(right) or right in touched) and not is_empty(down):
                    touched.add(right)
                    # if right not in touched:
                    #     water.add(right)
                    # else:
                    #     touched.remove(right)
                    #     water.add(right)
                    if down in touched:
                        touched.remove(down)
                        water.add(down)

                    right = (right[0] + 1, y)
                    down = (right[0], y + 1)

                    if should_print:
                        print_ground_scan(clay, water, touched, minx, miny, maxx, maxy, print_delay)

                if is_empty(down):
                    dfs(down[0], down[1] - 1)

                if not is_empty(left) and left not in touched and not is_empty(right) and right not in touched:
                    dfs(x, y)

                break

            if should_print:
                print_ground_scan(clay, water, touched, minx, miny, maxx, maxy, print_delay)

    dfs(spring_location[0], spring_location[1] + 1)

    # print(f'minx={minx}, miny={miny}, maxx={maxx}, maxy={maxy}')
    print_ground_scan(clay, water, touched, minx, miny, maxx, maxy, print_delay)
    non_empty = set()
    for s in [touched, water]:
        for t in s:
            x, y = t
            if minx - 1 <= x <= maxx + 1 and real_miny <= y <= maxy:
                non_empty.add(t)

    return len(non_empty), len(water.union(touched))


def h(clay, water, touched, spring_location, minx, miny, maxx, maxy, real_miny, should_print=False, print_delay=0.1, should_crop=False):
    if should_crop:
        minx, miny, maxx, maxy = 475, 0, 525, 50
        clay, water, _ = crop(clay, water, set(), 475, 0, 525, 50)
    # print_ground_scan(clay, water, touched, 475, 0, 525, 50, print_delay)
    # print_ground_scan(clay, water, touched, minx, miny, maxx, maxy, print_delay)
    # return
    # print(f'minx={minx}, miny={miny}, maxx={maxx}, maxy={maxy}, pixels={(maxx-minx)*(maxy-miny)}')

    def is_empty(pos):
        return pos not in clay and pos not in water

    def dfs(x, y):
        if y > maxy:
            return False

        if (x, y) in clay:
            return True

        water.add((x, y))
        if should_print:
            print_ground_scan(clay, water, set(), minx, miny, maxx, maxy, print_delay, spring_location)

        # filling
        if dfs(x, y + 1):
            left = (x - 1, y)
            down = (x - 1, y + 1)

            while left not in clay and not is_empty(down):
                water.add(left)
                if should_print:
                    print_ground_scan(clay, water, set(), minx, miny, maxx, maxy, print_delay, spring_location)
                left = (left[0] - 1, left[1])
                down = (left[0], down[1])

            if is_empty(down) and is_empty(left):
                dfs(*left)

            right = (x + 1, y)
            down = (x + 1, y + 1)

            while right not in clay and not is_empty(down):
                water.add(right)
                if should_print:
                    print_ground_scan(clay, water, set(), minx, miny, maxx, maxy, print_delay, spring_location)
                right = (right[0] + 1, right[1])
                down = (right[0], down[1])

            if is_empty(down) and is_empty(right):
                dfs(*right)

            if left in clay and right in clay:
                return True

        return False

    dfs(spring_location[0], spring_location[1] + 1)

    # print(f'minx={minx}, miny={miny}, maxx={maxx}, maxy={maxy}')
    print_ground_scan(clay, water, set(), minx, miny, maxx, maxy, print_delay, spring_location)
    non_empty = set()
    for t in water:
        x, y = t
        if minx - 1 <= x <= maxx + 1 and real_miny <= y <= maxy:
            non_empty.add(t)

    return len(non_empty), len(water)


data = get_lines_for_day(2018, '17')
picture_filename = 'input/17_input_picture3.txt'

# print(f(*get_input_from_picture(picture_filename), should_print=False, print_delay=0.2, should_crop=False))
print(f(*get_input_from_data(data), should_print=False, print_delay=0.05, should_crop=False))

# with open('input/17_big_picture.txt') as f:
#     count = 0
#     for line in f:
#         for c in line:
#             if c == '|' or c == '~':
#                 count += 1
#     print(f'count={count}')
# part 1
# 6632387 is more than the total number of pixels (340670)
# 38043 is too high
#
# part 2
# 30866 is too high