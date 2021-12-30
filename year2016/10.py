from util import get_lines_for_day


class Bot:
    def __init__(self, number, high=None, low=None, value=None):
        self.number = number
        self.high = high
        self.low = low
        self.values = set() if value is None else {value}

    def get_low(self):
        if len(self.values) == 2:
            return min(self.values)
        return None

    def get_high(self):
        if len(self.values) == 2:
            return max(self.values)
        return None

def f(lines):
    bots = {}
    output = {}

    for line in lines:
        line = line.split()
        if line[0] == 'value':
            v = int(line[1])
            b = int(line[5])
            if b in bots:
                bots[b].values.add(v)
            else:
                bots[b] = Bot(b, value=v)
        else:
            b = int(line[1])
            l = (line[5], int(line[6]))
            h = (line[10], int(line[11]))

            if b in bots:
                bots[b].high = h
                bots[b].low = l
            else:
                bots[b] = Bot(b, high=h, low=l)

    while True:
        for b, bot in bots.items():
            if len(bot.values) == 2:
                high_val, low_val = max(bot.values), min(bot.values)

                if high_val == 61 and low_val == 17:
                    print(b)

                val = high_val
                bot.values.clear()

                for op, dest in [bot.high, bot.low]:
                    if op == 'output':
                        output[dest] = val
                    elif op == 'bot':
                        bots[dest].values.add(val)
                    val = low_val
            elif len(bot.values) > 2:
                print(f'bot {b} had {bot.values} values')

            if 0 in output and 1 in output and 2 in output:
                return output[0] * output[1] * output[2]


print(f(get_lines_for_day(2016, 10)))
