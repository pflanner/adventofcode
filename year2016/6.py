from util import get_lines_for_day
from collections import Counter


def f(lines):
    frequencies_by_position = map(Counter, zip(*lines))
    word = []

    for i, frequencies in enumerate(frequencies_by_position):
        count = len(lines)
        for c, f in frequencies.items():
            if f < count:
                if len(word) > i:
                    word[i] = c
                else:
                    word.append(c)
                count = f

    return ''.join(word)


print(f(get_lines_for_day(2016, 6)))
