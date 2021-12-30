low = 168630
high = 718098


def meets_criteria(i):
    two_in_a_row = False
    for prev, cur in zip(i, i[1:]):
        if int(prev) > int(cur):
            return False
        if prev == cur:
            two_in_a_row = True

    return two_in_a_row


def meets_criteria_part2(i):
    two_in_a_row = False
    same_count = 1
    prev = -1
    for j in range(len(i)):
        cur = int(i[j])
        if prev > cur:
            return False
        if prev == cur:
            same_count += 1
        else:
            if same_count == 2:
                two_in_a_row = True
            same_count = 1
        prev = cur

    return two_in_a_row or same_count == 2


def part1():
    count = 0
    for i in range(low, high + 1):
        if meets_criteria(str(i)):
            count += 1
    return count


def part2():
    count = 0
    for i in range(low, high + 1):
        if meets_criteria_part2(str(i)):
            count += 1
    return count


if  __name__ == '__main__':
    # print(part1())
    print(part2())
    # 987 is too low
