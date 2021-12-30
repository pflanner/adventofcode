import string


def primes_up_to(n):
    primes = set()
    composites = set()
    i = 2
    while i*i < n:
        if i not in composites:
            primes.add(i)
            j = i
            while i*j <= n:
                composites.add(i*j)
                j += 1
        i += 1

    for j in range(i, n + 1):
        if j not in composites:
            primes.add(j)

    return primes

# count the number of composite numbers between 106500 and 123500 counting by 17
def f():
    h = 0

    primes = primes_up_to(123500)

    for i in range(106500, 123501, 17):
        if i not in primes:
            h += 1

    return h


def g(debug_mode=False):
    registers = {c: 0 for c in string.ascii_lowercase[:8]}

    registers['b'] = 65
    registers['c'] = 65

    if not debug_mode:
        registers['b'] = 106500
        registers['c'] = 123500

    mul_count = 0

    while True:
        registers['f'] = 1
        registers['d'] = 2

        while True:
            registers['e'] = 2

            # optimization
            # registers['d'] = registers['b']
            # registers['e'] = registers['b']
            # registers['g'] = 0

            while True:
                registers['g'] = registers['d']
                registers['g'] *= registers['e']
                mul_count += 1
                registers['g'] -= registers['b']

                # if d * e == b
                if registers['g'] == 0:
                    registers['f'] = 0

                registers['e'] += 1
                registers['g'] = registers['e']
                registers['g'] -= registers['b']

                # if e == b
                if registers['g'] == 0:
                    break

            registers['d'] += 1
            registers['g'] = registers['d']
            registers['g'] -= registers['b']

            # if d == b
            if registers['g'] == 0:
                break

        if registers['f'] == 0:
            registers['h'] += 1

        registers['g'] = registers['b']
        registers['g'] -= registers['c']

        if registers['g'] == 0:
            return mul_count, registers['h']

        registers['b'] += 17


print(f())
