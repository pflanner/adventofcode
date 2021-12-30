from util import get_lines_for_day
from collections import defaultdict
from itertools import product


class Rule:
    def __init__(self, rule_text):
        self.subrules = []
        self.superrules = []
        self.letter = None
        self.number, rule_text = rule_text.split(': ')

        if rule_text.startswith('"'):
            self.letter = rule_text[1]
        else:
            for subrule in rule_text.split(' | '):
                self.subrules.append(subrule.split(' '))


def generate_all_possibilities(rules, max_len):
    possibilities = defaultdict(set)

    # TODO for part 2 – this has been left in a broken state
    def dfs(rule_number='0'):
        if rule_number in possibilities:
            return

        rule = rules[rule_number]

        if rule.letter:
            possibilities[rule_number].add(rule.letter)
        elif rule.subrules:
            stop = False
            for subrule in rule.subrules:
                for part in subrule:
                    if stop and part == rule_number:
                        break
                    dfs(part)

                if not stop:
                    new = list(map(''.join, product(*[possibilities[r] for r in subrule])))
                    if max(map(len, new)) >= max_len:
                        stop = True
                    possibilities[rule_number].update(new)

    dfs()

    return possibilities['0']


def bottom_up(rules, max_length, all_message_prefixes):
    possibilities = defaultdict(set)

    for rule in rules.values():
        if rule.letter:
            possibilities[rule.number].add(rule.letter)
    # possibilities.update({'54': {'a'}, '117': {'b'}})
    old_len = 0

    # generate all possibilities except for rule 8, 11 and 0
    while len(possibilities) > old_len:
        old_len = len(possibilities)
        for rule_number, rule in rules.items():
            if rule_number in possibilities:
                continue

            # does this rule have any parts that we haven't already calculated?
            if any([part not in possibilities for subrule in rule.subrules for part in subrule]):
                continue

            for subrule in rule.subrules:
                possibilities[rule_number].update(map(''.join, product(*[possibilities[part] for part in subrule])))

    return possibilities


def f(i):
    first_part = True
    rules = {}
    messages = []
    count = 0

    for line in i:
        if line == '':
            first_part = False
            continue

        if first_part:
            rule = Rule(line)
            rules[rule.number] = rule
            continue

        if not line.startswith('#'):
            messages.append(line)

    all_message_prefixes = set()
    for message in messages:
        for i in range(1, len(message)):
            all_message_prefixes.add(message[i:])
    all_possibilities = bottom_up(rules, max(map(len, messages)), all_message_prefixes)

    test_message_list = ([next(iter(all_possibilities['42']))] * 6) + ([next(iter(all_possibilities['31']))] * 5)
    test_message = ''.join(test_message_list)
    test_messages = {
        'bbabbbbaabaabba',
        'babbbbaabbbbbabbbbbbaabaaabaaa',
        'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
        'bbbbbbbaaaabbbbaaabbabaaa',
        'bbbababbbbaaaaaaaabbababaaababaabab',
        'ababaaaaaabaaab',
        'ababaaaaabbbaba',
        'baabbaaaabbaaaababbaababb',
        'abbbbabbbbaaaababbbbbbaaaababb',
        'aaaaabbaabaaaaababaa',
        'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
        'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba',
    }

    inc = len(next(iter(all_possibilities['42'])))
    for message in messages:
        if len(message) % inc != 0:
            continue

        for i in range(inc, len(message) + 1, inc):
            if message[i - inc:i] not in all_possibilities['42']:
                break
        else:
            continue

        if i - inc <= len(message) // 2:
            continue

        for i in range(i, len(message) + 1, inc):
            if message[i - inc:i] not in all_possibilities['31']:
                break
        else:
            count += 1

    return count


print(f(get_lines_for_day(19)))
# part 2
# 212 is not the right answer
# 14 is not the right answer
# 267 is not the right answer
