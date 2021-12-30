class ListNode(object):
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        n = self.next if not self.next else self.next.val
        return 'val=%d next=%r' % (self.val, n)


def f(skip):
    buffer = ListNode(0)
    buffer.prev = buffer
    buffer.next = buffer
    cur = buffer
    count = 0

    for i in range(1, 2018):
        if count % 100000 == 0:
            print(count, buffer.next.val)
        count += 1
        for _ in range(skip):
            cur = cur.next

        n = ListNode(i)
        n.prev = cur
        n.next = cur.next
        cur.next.prev = n
        cur.next = n
        cur = cur.next

    return cur.next.val


def g(skip):
    n = 0
    result = 0

    for i in range(1, 50000001):
        n = (n + skip) % i + 1
        if n == 1:
            result = i

    return result


print(g(356))
# part 2
# 133859 is not the right answer
# 810485 is too low
# other values: 5383224, 8153400, 8479960, 14049895
