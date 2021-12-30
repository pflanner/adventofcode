from util import get_lines_for_day


def f(lines):
    card_pk, door_pk = map(int, lines)
    subject_number = 7
    mod_number = 20201227

    loop_size = val = 1
    card_ls = door_ls = None

    while True:
        val *= subject_number
        val %= mod_number

        if val == card_pk:
            card_ls = loop_size
            break
        if val == door_pk:
            door_ls = loop_size
            break
        loop_size += 1

    pk_to_transform = card_pk if door_ls else door_pk
    val = 1

    for _ in range(loop_size):
        val *= pk_to_transform
        val %= mod_number

    print(val)


def g(lines):
    card_pk, door_pk = map(int, lines)
    subject_number = 7
    mod_number = 20201227
    card_ls = door_ls = None

    def calc_pk(ls):
        card_ls = door_ls = None
        val = 1
        for _ in range(loop_size):
            val *= subject_number
            val %= mod_number

        if val == card_pk:
            card_ls = ls
        if val == door_pk:
            door_ls = ls

        return card_ls, door_ls

    loop_size = 1
    while True:
        if loop_size & 1023 == 0:
            print(loop_size)
        card_ls, door_ls = calc_pk(loop_size)
        if card_ls or door_ls:
            break
        loop_size += 1

    print(card_ls, door_ls)


f(get_lines_for_day(25))
