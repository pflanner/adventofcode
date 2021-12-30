from util import get_lines_for_day


def has_bad_letters(line):
    bad = {'ab', 'cd', 'pq', 'xy'}
    for b in bad:
        if b in line:
            return True

    return False


def f(i):
    num_nice_words = 0

    for line in i:
        vowels = twice = num_pairs = split = 0
        pairs = {}

        # if has_bad_letters(line):
        #     continue

        for index in range(len(line)):
            c = line[index]
            if c in 'aeiou':
                vowels += 1
            if index > 0:
                d = line[index - 1]
                if c == d:
                    twice += 1
                if pairs.get(d + c, index) <= index - 2:
                    num_pairs += 1
                if d + c not in pairs:
                    pairs[d + c] = index
            if index > 1:
                e = line[index - 2]
                if c == e:
                    split += 1

        if num_pairs >= 1 and split >= 1:
            num_nice_words += 1

    return num_nice_words


print(f(get_lines_for_day(2015, 5)))
# part 2
# 67 is not the right answer
