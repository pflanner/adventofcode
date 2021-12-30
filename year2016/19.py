class Node:
    def __init__(self, index, val):
        self.index = index
        self.val = val
        self.prev = None
        self.next = None


def f(num_elves):
    root = n = Node(1, 1)
    for i in range(2, num_elves + 1):
        n.next = Node(i, 1)
        n.next.prev = n
        n = n.next
    n.next = root
    root.prev = n

    n = root
    while True:
        if n.val == num_elves:
            return n.index

        if n.val == 0:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            n.val += n.next.val
            n.next.val = 0

        n = n.next


def g(num_elves):
    half = num_elves // 2 + 1
    root = n = across = Node(1, 1)
    for i in range(2, num_elves + 1):
        n.next = Node(i, 1)
        n.next.prev = n
        n = n.next
        if i == half:
            across = n
    n.next = root
    root.prev = n

    n = root
    remaining = num_elves
    while True:
        if n.val == num_elves:
            return n.index

        n.val += across.val
        across.prev.next = across.next
        across.next.prev = across.prev
        if remaining % 2 == 1:
            across = across.next
        remaining -= 1

        n = n.next
        across = across.next


print(g(3001330))
# print(g(5))
