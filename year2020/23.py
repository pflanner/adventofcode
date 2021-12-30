from collections import deque
from heapq import heapify, heappop, heappush


class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        n = self.next if not self.next else self.next.val
        p = self.prev if not self.prev else self.prev.val
        return 'val=%d next=%r, prev=%r' % (self.val, n, p)


def f(label, times):
    cups = list(map(int, label))
    cur_index = 0
    cur_cup = cups[cur_index]

    for _ in range(times):
        indices_to_pick_up = range(cur_index + 1, cur_index + 4)
        picked_up = []
        for i in indices_to_pick_up:
            picked_up.append(cups[i % len(cups)])

        for c in picked_up:
            cups.remove(c)

        destination_cup = cur_cup - 1
        while destination_cup not in cups:
            if destination_cup < min(cups):
                destination_cup = max(cups)
            else:
                destination_cup -= 1

        destination_cup_index = cups.index(destination_cup)
        cups = cups[:destination_cup_index + 1] + picked_up + cups[destination_cup_index + 1:]

        cur_index = cups.index(cur_cup)
        cur_index = (cur_index + 1) % len(cups)
        cur_cup = cups[cur_index]

    print(''.join(map(str, cups)))
    answer = ''
    starti = cups.index(1)
    for i in range(starti + 1, starti + 9):
        i %= 9
        answer += str(cups[i])
    print(answer)


class CupCircle:
    def __init__(self, label):
        self.cur_cup = ListNode(int(label[0]))
        self.val_to_node = {self.cur_cup.val: self.cur_cup}
        self.taken_cups = set()
        self.taken_start = self.taken_end = None
        cur = self.cur_cup
        max_cup = self.cur_cup.val

        for cup_num in map(int, label[1:]):
            cur.next = ListNode(cup_num, prev=cur)
            cur = cur.next
            self.val_to_node[cur.val] = cur
            max_cup = max(max_cup, cur.val)

        for i in range(max_cup + 1, 1000001):
            cur.next = ListNode(i, prev=cur)
            cur = cur.next
            self.val_to_node[cur.val] = cur

        self.cur_cup.prev = cur
        cur.next = self.cur_cup

    def take_cups(self):
        start = end = self.cur_cup.next
        self.taken_cups.add(start.val)

        for _ in range(2):
            end = end.next
            self.taken_cups.add(end.val)

        start.prev.next = end.next
        end.next.prev = start.prev
        start.prev = None
        end.next = None

        self.taken_start, self.taken_end = start, end

    def insert_taken_cups(self):
        destination = self.cur_cup.val - 1

        while destination in self.taken_cups:
            destination = (destination - 1) % 1000000

        if destination == 0:
            destination = 1000000

        destination = self.val_to_node[destination]

        self.taken_start.prev = destination
        self.taken_end.next = destination.next
        destination.next.prev = self.taken_end
        destination.next = self.taken_start

        self.taken_cups.clear()

        self.cur_cup = self.cur_cup.next


def g(label, times):
    cups = CupCircle(label)

    for time in range(times):
        if time & 1023 == 0:
            print(time)

        cups.take_cups()
        cups.insert_taken_cups()

    cup_one = cups.val_to_node[1]
    answer = cup_one.next.val * cup_one.next.next.val

    print(answer)


g('925176834', 10000000)
# f('389125467', 10)
