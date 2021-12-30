def f(sequence):

    for _ in range(50):
        answer = []

        prev = sequence[0]
        repeat = 0

        for c in sequence:
            if c == prev:
                repeat += 1
            else:
                answer.append(str(repeat))
                answer.append(str(prev))
                repeat = 1
            prev = c

        answer.append(str(repeat))
        answer.append(str(prev))

        sequence = ''.join(answer)

    return len(sequence)


print(f('1113222113'))
