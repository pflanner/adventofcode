from util import get_lines_for_day


def part1(pixels, width, height):
    pixels_per_layer = width * height
    zeros = float('inf')
    fewest_0s = float('inf')
    layer = -1
    fewest_layer = 0

    for i, p in enumerate(pixels):
        if i % pixels_per_layer == 0:
            if zeros < fewest_0s:
                fewest_0s = zeros
                fewest_layer = layer
            zeros = 0
            layer += 1
        if p == 0:
            zeros += 1

    ones = 0
    twos = 0
    start = fewest_layer * pixels_per_layer
    end = start + pixels_per_layer
    for i in range(start, end):
        p = pixels[i]
        if p == 1:
            ones += 1
        if p == 2:
            twos += 1

    return ones * twos


def part2(pixels, width, height):
    pixels_per_layer = width * height
    black, white, transparent = 0, 1, 2
    final_image = []

    for i in range(pixels_per_layer):
        j = i
        while j < len(pixels):
            p = pixels[j]
            if p != transparent:
                final_image.append(p)
                break
            j += pixels_per_layer

    n = 0
    for i in range(height):
        for j in range(width):
            if final_image[n] == black:
                print(' ', end='')
            else:
                print('#', end='')
            n += 1
        print()


if __name__ == '__main__':
    lines = get_lines_for_day(2019, 8)
    pixels = [int(p) for p in lines[0]]

    # print(part1(pixels, 25, 6))
    print(part2(pixels, 25, 6))
