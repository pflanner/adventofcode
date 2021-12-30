from util import get_lines_for_day, get_input_for_day, get_groups

match = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

rev = {v: k for k, v in match.items()}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

scores2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def part1(lines):
    total = 0
    for line in lines:
        stack = []
        for c in line:
            if c in rev:
                if match[stack[-1]] == c:
                    stack.pop()
                else:
                    total += scores[c]
                    break
            else:
                stack.append(c)
    return total

def part2(lines):
    total = 0
    all_scores = []
    for line in lines:
        stack = []
        corrupt = False
        for c in line:
            if c in rev:
                if match[stack[-1]] == c:
                    stack.pop()
                else:
                    total += scores[c]
                    corrupt = True
                    break
            else:
                stack.append(c)
        if not corrupt:
            score = 0
            for c in reversed(stack):
                score *= 5
                score += scores2[match[c]]
            all_scores.append(score)
    return sorted(all_scores)[len(all_scores) // 2]


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 10)
    test_lines = get_lines_for_day(2021, '10_test')
    # inp = get_input_for_day(2021, 10)
    groups = get_groups(lines)

    print(part1(lines))
    print(part2(lines))
