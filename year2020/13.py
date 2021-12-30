from util import get_input_for_day


def part1(i):
    i = i.strip().split('\n')

    departure_time = int(i[0])
    bus_ids = [int(idd) for idd in i[1].split(',') if idd != 'x']
    times = [0] * len(bus_ids)

    while True:
        for ii, bid in enumerate(bus_ids):
            times[ii] += bid
            if times[ii] > departure_time:
                return (times[ii] - departure_time) * bid


def part2_wrong(i):
    i = i.strip().split('\n')

    bus_ids = [int(idd) if idd != 'x' else idd for idd in i[1].split(',')]

    ii = 100000000000000
    step = bus_ids[0]

    # find first case where first two ids meet the criteria 29 start + 19 is when 41 starts
    t1 = ii // 29 * 29 + 29
    t2 = ii // 41 * 41 + 41

    while True:
        diff = t2 - t1
        if diff > 19:
            t1 += 29
        elif diff < 19:
            t2 += 41
        else:
            print(t1)
            break

    lcm = 29 * 41
    t1 *= lcm
    t2 = t1 + 19
    a = t1 % 29
    b = t2 % 41
    print(a, b)

    # while True:
    #     for j, bid in enumerate(bus_ids):
    #         if bid == 'x':
    #             continue
    #
    #         if (ii + j) % bid != 0:
    #             break
    #     else:
    #         return ii
    #     ii += step


def part2_michael_flynn(i):
    i = i.strip().split('\n')

    schedule = [(int(bus_id), i) for i, bus_id in enumerate(i[1].split(',')) if bus_id != 'x']
    start_time = increment = schedule[0][0]

    for bus_id, offset in schedule[1:]:
        while (start_time + offset) % bus_id != 0:
            start_time += increment
        increment *= bus_id

    return start_time


print(part2_michael_flynn(get_input_for_day(13)))

#12:15
