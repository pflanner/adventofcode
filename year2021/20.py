from operator import itemgetter


def get_pixels(x, y, image, reverse):
    pixels = []

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            filler = '#' if reverse else '.'
            pixels.append('0' if image.get((x+dx, y+dy), filler) == '.' else '1')

    return pixels


def print_image(image):
    minx = min(map(itemgetter(0), image))
    miny = min(map(itemgetter(1), image))
    maxx = max(map(itemgetter(0), image))
    maxy = max(map(itemgetter(1), image))

    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            print(image.get((x, y), '.'), end='')
        print()
    print()


def save_image(image):
    minx = min(map(itemgetter(0), image))
    miny = min(map(itemgetter(1), image))
    maxx = max(map(itemgetter(0), image))
    maxy = max(map(itemgetter(1), image))

    image_str = ''

    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            image_str += image.get((x, y), '.')
        image_str += '\n'

    with open('input/20_output2.txt', mode='w') as f:
        f.write(image_str)


def part1(algo, image):
    for step in range(50):
        reverse = step & 1 == 1
        image = enhance(algo, image, reverse)

    return len([x for x in image.values() if x == '#'])


def enhance(algo, image, reverse):
    minx = min(map(itemgetter(0), image))
    miny = min(map(itemgetter(1), image))
    maxx = max(map(itemgetter(0), image))
    maxy = max(map(itemgetter(1), image))

    enhanced_image = {}
    for y in range(miny-4, maxy+5):
        for x in range(minx-4, maxx+5):
            index = int(''.join(get_pixels(x, y, image, reverse)), 2)
            enhanced_image[(x, y)] = algo[index]
    return enhanced_image


if __name__ == '__main__':
    with open("input/20.txt") as f:
        lines = f.readlines()
        algo = lines[0].strip()
        image = {}
        for y, line in enumerate(lines[2:]):
            line = line.strip()
            for x, c in enumerate(line):
                image[(x, y)] = c

        print(part1(algo, image))
        # 6342 is not the right answer

    # with open('input/20_output3.txt') as f:
    #     total = 0
    #     for line in f:
    #         for c in line:
    #             if c == '#':
    #                 total += 1
    #     print(total)

#50 20_output2.txt is the output of the 50th enhancement, 20_output3.txt is that same output stripped
