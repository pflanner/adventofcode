def get_surrounding_pixels(x, y, image, reverse):
    pixels = []

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            filler = '#' if reverse else '.'
            pixels.append('0' if image.get((x+dx, y+dy), filler) == '.' else '1')

    return pixels


def enhance(algo, image, reverse):
    from functools import reduce
    minx, miny, maxx, maxy = reduce(lambda acc, p: (min(acc[0], p[0]), min(acc[1], p[1]), max(acc[0], p[0]), max(acc[0], p[0])), image)
    buffer = 1

    enhanced_image = {}
    for y in range(miny-buffer, maxy+buffer+1):
        for x in range(minx-buffer, maxx+buffer+1):
            index = int(''.join(get_surrounding_pixels(x, y, image, reverse)), 2)
            enhanced_image[(x, y)] = algo[index]
    return enhanced_image


def enhance_num_steps(algo, image, num_steps):
    for step in range(num_steps):
        reverse = step & 1 == 1
        image = enhance(algo, image, reverse)

    return len([x for x in image.values() if x == '#'])


if __name__ == '__main__':
    with open("input/20.txt") as f:
        lines = f.readlines()
        algo = lines[0].strip()
        image = {}
        for y, line in enumerate(lines[2:]):
            line = line.strip()
            for x, c in enumerate(line):
                image[(x, y)] = c

        print(enhance_num_steps(algo, image, 2))
        print(enhance_num_steps(algo, image, 50))
