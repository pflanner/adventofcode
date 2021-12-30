from util import get_lines_for_day
from math import sqrt
from PIL import Image


def make_image(pattern):
    side = round(sqrt(len(pattern) - 2))
    image = Image.new(mode='1', size=(side, side))
    x = y = 0

    for c in pattern:
        if c == '/':
            x = 0
            y += 1
        else:
            val = 1 if c == '#' else 0
            image.putpixel((x, y), val)
            x += 1

    return image


def make_pattern(image):
    pattern = []

    for y in range(image.height):
        for x in range(image.width):
            val = image.getpixel((x, y))
            pattern.append('#' if val == 1 else '.')
        pattern.append('/')

    return ''.join(pattern[:-1])


def get_new_image(section, rules):
    # try all 8 rotation/flip combinations and see which one fits a rule

    for angle in range(0, 360, 90):
        pattern = make_pattern(section.rotate(angle, expand=True))

        if pattern in rules:
            return make_image(rules[pattern])

        flipped_section = section.transpose(method=Image.FLIP_LEFT_RIGHT)
        pattern = make_pattern(flipped_section.rotate(angle, expand=True))

        if pattern in rules:
            return make_image(rules[pattern])


def get_new_images(image, section_size, rules):
    new_images = []

    for starty in range(0, image.height, section_size):
        new_images.append([])

        for startx in range(0, image.width, section_size):
            section = Image.new(mode='1', size=(section_size, section_size))

            for y in range(section_size):
                for x in range(section_size):
                    section.putpixel((x, y), image.getpixel((startx + x, starty + y)))

            new_images[-1].append(get_new_image(section, rules))

    return new_images


def stitch_images(images):
    side = images[0][0].width
    big_side = len(images) * side
    big_image = Image.new(mode='1', size=(big_side, big_side))

    for i, row in enumerate(images):
        for j, image in enumerate(row):
            bigx = j * side
            bigy = i * side
            for y in range(image.height):
                for x in range(image.width):
                    val = image.getpixel((x, y))
                    big_image.putpixel((bigx, bigy), val)
                    bigx += 1
                bigy += 1
                bigx = j * side

    return big_image


def print_image(image):
    for y in range(image.height):
        for x in range(image.width):
            val = image.getpixel((x, y))
            print('#' if val == 1 else '.', end='')
        print()


def f(lines, iterations=5):
    pattern = '.#./..#/###'
    image = make_image(pattern)
    rules = {}

    for line in lines:
        line = line.split(' => ')
        rules[line[0]] = line[1]

    for i in range(iterations):
        if image.width % 2 == 0:
            new_images = get_new_images(image, 2, rules)
        elif image.width % 3 == 0:
            new_images = get_new_images(image, 3, rules)

        image = stitch_images(new_images)

        # print_image(image)
        # print()
        print('iteration {}'.format(i + 1))

    count = 0
    for y in range(image.height):
        for x in range(image.width):
            if image.getpixel((x, y)) == 1:
                count += 1

    return count


print(f(get_lines_for_day(2017, 21), 18))
# print(f(get_lines_for_day(2017, '21_test'), 2))
# part 1
# 180 is too high
