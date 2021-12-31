from functools import reduce


def increase(p, magnitude, range):
    return (p - 1 + magnitude) % range + 1

def part1(p1, p2):
    s1 = s2 = 0
    num_rolls = 0
    move = 1

    while True:
            if num_rolls & 1 == 0:
                for _ in range(3):
                    p1 = increase(p1, move, 10)
                    move = increase(move, 1, 100)
                    num_rolls += 1

                s1 += p1
                if s1 >= 1000 or s2 >= 1000:
                    return min(s1, s2) * num_rolls
            else:
                for _ in range(3):
                    p2 = increase(p2, move, 10)
                    move = increase(move, 1, 100)
                    num_rolls += 1

                s2 += p2
                if s1 >= 1000 or s2 >= 1000:
                    return min(s1, s2) * num_rolls


def part2(player1, player2):
    mem = {}

    def helper(roll, p1, p2, s1, s2, rolls, players_turn, num_turns):
        key = (roll, p1, p2, s1, s2, players_turn, num_turns)
        # key = tuple(rolls[:-1])
        # if tuple(rolls) in mem:
        #     return mem[tuple(rolls)]
        if key in mem:
            return mem[key]
        if s1 >= 21:
            # mem[key] = (1, 0)
            return 1, 0
        if s2 >= 21:
            # mem[key] = (0, 1)
            return 0, 1

        if players_turn == 0:
            p1 = increase(p1, roll, 10)
        else:
            p2 = increase(p2, roll, 10)

        if num_turns == 2:
            num_turns = 0
            if players_turn == 0:
                s1 += p1
            else:
                s2 += p2
            players_turn = 0 if players_turn == 1 else 1
        else:
            num_turns += 1

        wins1 = wins2 = 0
        for r in range(1, 4):
            w1, w2 = helper(r, p1, p2, s1, s2, rolls + [r], players_turn, num_turns)
            key2 = (r, p1, p2, s1, s2, players_turn, num_turns)
            # mem[key2] = w1, w2
            # mem[tuple(rolls + [r])] = (w1, w2)
            wins1 += w1
            wins2 += w2

        mem[key] = (wins1, wins2)

        return wins2, wins2

    helper(0, player1, player2, 0, 0, [], 0, -1)
    w1, w2 = mem[(3, 4, 8, 0, 0, 0, 0)]
    # w1, w2 = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), mem.values())

    return max(w1, w2)


def part2_2(player1, player2):
    mem = {}
    score_map = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1,
    }

    def helper(p1, p2, s1, s2, num_dimensions, players_turn):
        key = (p1, p2, s1, s2, players_turn)
        if key in mem:
            return mem[key]
        if s1 >= 21:
            mem[key] = (num_dimensions, 0)
            return mem[key]
        if s2 >= 21:
            mem[key] = (0, num_dimensions)
            return mem[key]

        players_turn = 0 if players_turn == 1 else 1

        wins1 = wins2 = 0
        for s in range(3, 10):
            if players_turn == 0:
                p1 = increase(p1, s, 10)
                s1 += p1
            else:
                p2 = increase(p2, s, 10)
                s2 += p2
            new_dimensions = num_dimensions + 3*score_map[s]
            w1, w2 = helper(p1, p2, s1, s2, new_dimensions, players_turn)
            wins1 += w1
            wins2 += w2

        # mem[tuple(rolls)] = (wins1, wins2)

        return wins2, wins2

    helper(player1, player2, 0, 0, 0, 0)
    w1, w2 = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), mem.values())

    return max(w1, w2)



if __name__ == '__main__':
    """
    Player 1 starting position: 6
    Player 2 starting position: 2
    """
    # print(increase(99, 2, 100))
    print(part1(6, 2))
    print(part2(4, 8))
    # 262812 is not right
    # 213246 is not right
    """
    4567569635410695
    444356092776315
    1025881170542424
    1025881170542424
    """


