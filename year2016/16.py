def reverse_and_bitflip(data):
    data = data[::-1]
    new_data = []

    for bit in data:
        if bit == '1':
            new_data.append('0')
        else:
            new_data.append('1')

    return ''.join(new_data)


def reverse_and_bitflip2(data):
    length = len(data)
    mask = int(''.join(['1'] * length))
    data = int(''.join(data[::-1]))

    data = str(mask ^ data)

    if len(data) < length:
        data = ['0'] * (length - len(data)) + list(data)
        data = ''.join(data)

    return data


def f(data, length):
    while len(data) < length:
        data = data + '0' + reverse_and_bitflip(data)

    data = data[:length]

    checksum = []

    while len(checksum) % 2 == 0:
        checksum = []
        for i in range(0, len(data), 2):
            if data[i] == data[i + 1]:
                checksum.append('1')
            else:
                checksum.append('0')
        data = ''.join(checksum)

    return data


print(f('11101000110010100', 35651584))
