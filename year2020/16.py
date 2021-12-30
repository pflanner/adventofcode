from util import get_input_for_day
from collections import defaultdict


def part1(i):
    i = i.strip().split('\n')
    ranges = set()
    error_rate = 0
    valid_tickets = []

    for index1, line in enumerate(i):
        if line == '':
            break

        label, r = line.split(': ')
        r1, r2 = r.split(' or ')
        nums = list(map(int, r1.split('-')))
        ranges.update(set(range(nums[0], nums[1] + 1)))
        nums = list(map(int, r2.split('-')))
        ranges.update(set(range(nums[0], nums[1] + 1)))

    ticket_count = 0
    for index2, line in enumerate(i[index1 + 5:], index1 + 5):
        if line == '':
            break

        ticket_count += 1
        nums = list(map(int, line.split(',')))

        valid = True
        for num in nums:
            if num not in ranges:
                error_rate += num
                valid = False

        if valid:
            valid_tickets.append(nums)

    print(f'tickets={ticket_count}, valid_tickets={len(valid_tickets)}')

    return error_rate, valid_tickets


def part2(i):
    error_rate, valid_tickets = part1(i)
    ranges = {}
    i = i.strip().split('\n')
    my_ticket = list(map(int, i[22].split(',')))
    valid_tickets.append(my_ticket)
    possible_fields = [set() for _ in range(len(my_ticket))]
    impossible_fields = [set() for _ in range(len(my_ticket))]

    for line in i:
        if line == '':
            break

        label, r = line.split(': ')
        r1, r2 = r.split(' or ')
        r_total = set()
        nums = list(map(int, r1.split('-')))
        r_total.update(range(nums[0], nums[1] + 1))
        nums = list(map(int, r2.split('-')))
        r_total.update(range(nums[0], nums[1] + 1))
        ranges[label] = r_total

    for ticket in valid_tickets:
        for i, val in enumerate(ticket):
            for label, r in ranges.items():
                if label not in impossible_fields[i] and val in r:
                    possible_fields[i].add(label)
                else:
                    possible_fields[i].discard(label)
                    impossible_fields[i].add(label)

    count = sum(list(map(len, possible_fields)))
    visited = set()

    while count > len(possible_fields):
        for i, pf in enumerate(possible_fields):
            if i not in visited and len(pf) == 1:
                visited.add(i)
                for j in range(len(possible_fields)):
                    to_discard = next(iter(pf))
                    if j != i and to_discard in possible_fields[j]:
                        possible_fields[j].remove(next(iter(pf)))
                        count -= 1

    result = 1
    for i, pf in enumerate(possible_fields):
        field = next(iter(pf))
        if field.startswith('departure'):
            result *= my_ticket[i]

    return result


print(part2(get_input_for_day(16)))
