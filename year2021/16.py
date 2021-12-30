from util import get_lines_for_day

class Parser:
    def __init__(self, hex):
        self.total = 0
        self.b = ''.join(self.hex_to_binary(c) for c in hex)
        self.i = 0
        self.type = 0
        self.type_to_op = {
            0: self.sum,
            1: self.product,
            2: self.min,
            3: self.max,
            5: self.gt,
            6: self.lt,
            7: self.eq,
        }

    @staticmethod
    def hex_to_binary(hex):
        b = bin(int(hex, 16))[2:]
        leading_zeros = ''.join(['0']*(4 - len(b)))
        return leading_zeros + b

    def parse_packet(self):
        version = int(self.b[self.i:self.i+3], 2)
        type_code = int(self.b[self.i+3:self.i+6], 2)
        self.total += version
        self.i += 6

        if type_code == 4:
            val = self.parse_literal()
        else:
            val = self.parse_operator(type_code)

        return val

    def parse_literal(self):
        keep_going = self.b[self.i] == '1'
        self.i += 1
        val = []

        while keep_going:
            val.append(self.b[self.i:self.i + 4])
            self.i += 4
            keep_going = self.b[self.i] == '1'
            self.i += 1
        val.append(self.b[self.i:self.i + 4])
        self.i += 4

        return int(''.join(val), 2)

    def parse_operator(self, type_code):
        length_type = self.b[self.i]
        self.i += 1

        if length_type == '0':
            val = self.parse_length(type_code)
        else:
            val = self.parse_sub_packets(type_code)

        return val


    def parse_length(self, type_code):
        length = int(self.b[self.i:self.i+15], 2)
        self.i += 15
        end = self.i + length
        val = None

        while self.i < end:
            val = self.type_to_op[type_code](val, self.parse_packet())

        return val

    def parse_sub_packets(self, type_code):
        num_sub_packets = int(self.b[self.i:self.i+11], 2)
        self.i += 11
        val = None

        for _ in range(num_sub_packets):
            val = self.type_to_op[type_code](val, self.parse_packet())

        return val

    @staticmethod
    def sum(acc, val):
        return acc + val if acc is not None else val

    @staticmethod
    def product(acc, val):
        return acc * val if acc is not None else val

    @staticmethod
    def min(acc, val):
        return min(acc, val) if acc is not None else val

    @staticmethod
    def max(acc, val):
        return max(acc, val) if acc is not None else val

    @staticmethod
    def gt(acc, val):
        if acc is not None:
            return 1 if acc > val else 0
        else:
            return val

    @staticmethod
    def lt(acc, val):
        if acc is not None:
            return 1 if acc < val else 0
        else:
            return val

    @staticmethod
    def eq(acc, val):
        if acc is not None:
            return 1 if acc == val else 0
        else:
            return val

def part1(transmission):
    p = Parser(transmission)

    p.parse_packet()
    return p.total


def part2(transmission):
    p = Parser(transmission)
    return p.parse_packet()


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 16)

    print(part1(lines[0]))
    print(part2(lines[0]))