from util import get_lines_for_day
from functools import reduce
from operator import xor


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


def create_ring(n):
    root = prev = Node(0)

    for i in range(1, n):
        cur = Node(i)
        prev.next = cur
        cur.prev = prev

    root.prev = cur
    cur.next = root

    return root


def reverse_linked_list(start, n):
    end = start

    for _ in range(n):
        end = end.next

    tmp = start.prev
    start.prev = end.next
    end.next = tmp

    return end


def reverse_array(l, start, n):
    end = (start + n - 1) % len(l) + 1
    if end >= start:
        l = l[:start] + list(reversed(l[start:end])) + l[end:]
    else:
        reversed_part = list(reversed(l[start:] + l[:end]))
        l = reversed_part[-end:] + l[end:start] + reversed_part[:len(l) - start]

    return l


    # this won't work because we need to keep track of the element at the start index
def f(lines):
    lengths = list(map(int, lines[0].split(',')))
    ring = start = create_ring(256)
    skip = 0

    for length in lengths:
        ring = reverse_linked_list(ring, length)
        for _ in range(skip):
            start = ring.next
        skip += 1


def g(lines, ring_size=256):
    lengths = list(map(int, lines[0].split(',')))
    ring = list(range(ring_size))
    i = skip = 0

    for length in lengths:
        ring = reverse_array(ring, i, length)

        i = (i + length + skip) % len(ring)
        skip += 1

    return ring[0] * ring[1]


def h(lines, ring_size=256, rounds=64):
    lengths = list(map(ord, lines[0]))
    lengths += [17, 31, 73, 47, 23]
    ring = list(range(ring_size))
    i = skip = 0

    for _ in range(rounds):
        for length in lengths:
            ring = reverse_array(ring, i, length)

            i = (i + length + skip) % len(ring)
            skip += 1

    dense = []

    for i in range(0, 256, 16):
        chunk = ring[i:i + 16]
        n = reduce(xor, chunk)
        dense.append(n)

    s = []
    for n in dense:
        n = hex(n)[2:]
        if len(n) == 1:
            n = '0' + n
        s.append(n)

    return ''.join(s)


# print(h(get_lines_for_day(2017, '10')))
# print(g(get_lines_for_day(year2017, '10')))
# print('a2582a3a0e66e6e86e3812dcb672a272')
# print(h(['1,2,3']))
# part 1
# 8372 is too high

# part 2
# 1cefc294314d3bc53a63771cb5aade22 is not the right answer
# 353efca7cea58172f6ecec7aa744832 is not the right answer
# 353efca7cea58172f6ecec7aa7440832 is not the right answer

