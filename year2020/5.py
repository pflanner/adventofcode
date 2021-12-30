from util import get_input_for_day


def f():
    todays_input = get_input_for_day(5)
    max_id = 0
    seat_ids = set()

    for line in todays_input.split('\n'):
        if not line:
            continue

        row = line[:7]
        row_num = 0
        row_mul = 64

        for c in row:
            if c == 'B':
                row_num += row_mul
            row_mul = row_mul >> 1

        col = line[7:]
        col_num = 0
        col_mul = 4

        for c in col:
            if c == 'R':
                col_num += col_mul
            col_mul = col_mul >>1

        seat_id = row_num * 8 + col_num
        max_id = max(max_id, seat_id)
        seat_ids.add(seat_id)

    # part 1
    print(max_id)

    # part 2
    for i in range(8, 1015):
        if i + 1 in seat_ids and i not in seat_ids and i - 1 in seat_ids:
            print(i)


f()
