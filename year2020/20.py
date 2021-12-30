# NOTE: xy coordinate system and row/column are opposite
# PIL uses xy, and I am using row/column here, so instead of switching all of my row/column usage to xy
# after I started using PIL, I cheated a bit by multiplying my rotation angle by -1 and flipping left to right when
# I really want top to bottom and vice versa

from util import get_input_for_day
from collections import defaultdict, deque
from functools import reduce
from operator import attrgetter, mul
from PIL import Image


class Tile:
    def __init__(self, lines, id_num):
        self.dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        self.image = Image.new(mode='1', size=(8, 8))
        for r in range(1, 9):
            for c in range(1, 9):
                pixel = 1 if lines[r][c] == '#' else 0
                self.image.putpixel((r - 1, c - 1), pixel)

        top = lines[0]
        bottom = lines[-1]
        left = ''.join(list(zip(*lines))[0])
        right = ''.join(list(zip(*lines))[-1])
        self.edges = [top, left, bottom, right]

        self.id_num = id_num
        self.inversion_lr = 1
        self.inversion_ud = 1
        self.location = None

    def add_edges_to(self, edges_map, r, c):
        for index in range(len(self.edges)):
            edge = self.edges[index]
            i, j = self.dirs[index]

            loc = (r + i, c + j)
            edges_map[edge] = (loc, index,)

    def flip(self, edge_index):
        # flip edge and its parallel edge
        self.edges[edge_index] = self.edges[edge_index][::-1]
        self.edges[(edge_index + 2) % 4] = self.edges[(edge_index + 2) % 4][::-1]

        # swap adjacent edge and its parallel
        j, k = (edge_index + 1) % 4, (edge_index + 3) % 4
        self.edges[j], self.edges[k] = self.edges[k], self.edges[j]

        # flip the image
        transpose_method = Image.FLIP_TOP_BOTTOM if edge_index in [0, 2] else Image.FLIP_LEFT_RIGHT
        self.image = self.image.transpose(method=transpose_method)

    def rotate_counterclockwise_90(self, number_of_times):
        for _ in range(number_of_times):
            tmp = self.edges[0]
            tmp, self.edges[1] = self.edges[1], tmp[::-1]
            tmp, self.edges[2] = self.edges[2], tmp
            tmp, self.edges[3] = self.edges[3], tmp[::-1]
            tmp, self.edges[0] = self.edges[0], tmp

        # rotate the image
        self.image = self.image.rotate(angle=90*number_of_times*-1, expand=True)


def get_tile_grid_bounds(tile_grid):
    minr = minc = maxr = maxc = 0
    for r, c in tile_grid:
        minr = min(minr, r)
        minc = min(minc, c)
        maxr = max(maxr, r)
        maxc = max(maxc, c)

    return minr, minc, maxr, maxc


def print_tile_grid_counts(tile_grid):
    minr, minc, maxr, maxc = get_tile_grid_bounds(tile_grid)

    for i in range(minr, maxr + 1):
        for j in range(minc, maxc + 1):
            if (i, j) in tile_grid:
                print(len(tile_grid[(i, j)]), end='')
            else:
                print('.', end='')
        print()
    print()


def print_tile_grid(tile_grid):
    minr, minc, maxr, maxc = get_tile_grid_bounds(tile_grid)
    str_grid = [[' '] * (10 * (maxc - minc + 1)) for _ in range(10 * (maxr - minr + 1))]

    for i in range(minr, maxr + 1):
        for j in range(minc, maxc + 1):
            if (i, j) in tile_grid:
                tile = tile_grid[(i, j)][0]

                # top edge
                r = 10 * (i - minr)
                c = (10 * (j - minc))
                for k, pixel in enumerate(tile.edges[0]):
                    str_grid[r][c + k] = pixel

                # middle
                for k in range(1, 9):
                    r += 1
                    str_grid[r][c] = tile.edges[1][k]
                    str_grid[r][c + 9] = tile.edges[3][k]

                # bottom
                for k, pixel in enumerate(tile.edges[2]):
                    str_grid[r + 1][c + k] = pixel

    for row in str_grid:
        for col in row:
            print(col, end='')
        print()
    print('--------------------------------------')


def print_image(image):
    for r in range(image.size[0]):
        for c in range(image.size[1]):
            symbol = '#' if image.getpixel((r, c)) == 1 else '.'
            print(symbol, end='')
        print()
    print()


def load_seamonster():
    seamonster = set()
    with open('input/20_seamonster.txt') as f:
        for i, line in enumerate(f):
            for j, c in enumerate(line):
                if c == '#':
                    seamonster.add((i, j))

    return seamonster


def f(i):
    i = i.strip().split('\n\n')
    tiles = deque()
    # map of position of tile in grid tuple to tile e.g. {(0, 0): Tile}
    tile_grid = defaultdict(list)
    # map of edge to position matching tile must take and the index of the edge e.g. {'#..##.#...': ((-1, 0), 3)}
    edges = {}

    for index, tile in enumerate(i):
        tile = tile.split('\n')
        id_num = int(tile[0][5:9])
        tiles.append(Tile(tile[1:], id_num))

    tile = tiles.pop()
    tile_grid[(0, 0)].append(tile)
    for index in range(len(tile.edges)):
        edge = tile.edges[index]
        edges[edge] = (tile.dirs[index], index)

    while tiles:
        tile = tiles.pop()

        for index in range(len(tile.edges)):
            edge = tile.edges[index]

            if edge in edges or edge[::-1] in edges:
                # we need to match right with left, etc. or else we have to rotate this tile so that it doesn't overlap
                opposite_index = (edges.get(edge, edges.get(edge[::-1]))[1] + 2) % 4
                if index != opposite_index:
                    tile.rotate_counterclockwise_90((opposite_index - index) % 4)

                edge = tile.edges[opposite_index]
                if edge not in edges:
                    tile.flip(opposite_index)
                    edge = tile.edges[opposite_index]

                loc = edges[edge][0]
                if loc in tile_grid:
                    print(f"{loc} was already in tile_grid")
                tile_grid[loc].append(tile)
                tile.add_edges_to(edges, *loc)
                break
        else:
            tiles.appendleft(tile)

    print_tile_grid_counts(tile_grid)

    minr, minc, maxr, maxc = get_tile_grid_bounds(tile_grid)

    answer = [
        tile_grid[(minr, minc)][0],
        tile_grid[(minr, maxc)][0],
        tile_grid[(maxr, minc)][0],
        tile_grid[(maxr, maxc)][0],
    ]

    pixel_count = 0
    tile = next(iter(tile_grid.values()))[0]
    tw, th = tile.image.size
    gw, gh = maxc - minc + 1, maxr - minr + 1
    big_image = Image.new(mode='1', size=(tw*gw, th*gh))
    for r in range(minr, maxr + 1):
        for c in range(minc, maxc + 1):
            image = tile_grid[(r, c)][0].image
            for rr in range(th):
                for cc in range(tw):
                    pixel = image.getpixel((rr, cc))
                    big_image.putpixel(((r - minr) * th + rr, (c - minc) * tw + cc), pixel)
                    if pixel == 1:
                        pixel_count += 1

    seamonster = load_seamonster()
    seamonster_width = 20
    seamonster_height = 3

    def count_seamonsters():
        seamonster_count = 0

        for r in range(th*gh - seamonster_height):
            for c in range(tw*gw - seamonster_width):
                for rr, cc in seamonster:
                    loc = (r + rr, c + cc)
                    if big_image.getpixel(loc) != 1:
                        break
                else:
                    seamonster_count += 1

        return seamonster_count

    sc = 0

    for degrees in range(0, 360, 90):
        big_image = big_image.rotate(angle=degrees, expand=True)
        sc = count_seamonsters()
        if sc:
            break
    else:
        big_image = big_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        for degrees in range(0, 360, 90):
            big_image = big_image.rotate(angle=degrees, expand=True)
            sc = count_seamonsters()
            if sc:
                break

    print_image(big_image)
    # big_image.show()

    return reduce(mul, map(attrgetter('id_num'), answer)), pixel_count - (sc * len(seamonster))

# part 2
# 2654 is not the right answer


print(f(get_input_for_day(20)))


def test():
    i = get_input_for_day(22)

    i = i.strip().split('\n')
    id_num = int(i[0][5:9])
    tile = Tile(i[1:], id_num)

    print_image(tile.image)
    tile.flip(3)
    print_image(tile.image)


# test()
