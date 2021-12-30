def f(input_presents):
    house_number = 2

    while True:
        presents = 0
        i = 1
        while i*i < house_number:
            if house_number % i == 0:
                presents += 10 * house_number // i
                presents += 10 * i
            i += 1

        if i*i == house_number:
            presents += 10 * i

        # print(presents)

        if presents >= input_presents:
            return house_number

        house_number += 1


def g(input_presents):
    house_number = 53

    while True:
        presents = 0
        i = 1
        while i*i < house_number:
            if house_number % i == 0:
                if house_number <= i * 50:
                    presents += 11 * i
                if house_number <= house_number // i * 50:
                    presents += 11 * house_number // i
            i += 1

        if i*i == house_number and house_number <= i * 50:
            presents += 11 * i

        # print(presents)

        if presents >= input_presents:
            return house_number

        house_number += 1


print(g(33100000))
