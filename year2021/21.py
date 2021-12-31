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

    def helper(roll, p1, p2, s1, s2, players_turn, num_turns):
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

        key = (roll, p1, p2, s1, s2, players_turn, num_turns)

        if key in mem:
            return mem[key]
        if s1 >= 21:
            return 1, 0
        if s2 >= 21:
            return 0, 1

        wins1 = wins2 = 0
        for r in range(1, 4):
            w1, w2 = helper(r, p1, p2, s1, s2, players_turn, num_turns)
            wins1 += w1
            wins2 += w2

        mem[key] = (wins1, wins2)

        return wins1, wins2

    initial_input = (0, player1, player2, 0, 0, 0, -1)
    w1, w2 = helper(*initial_input)

    return max(w1, w2)



if __name__ == '__main__':
    """
    Player 1 starting position: 6
    Player 2 starting position: 2
    """
    print(part1(6, 2))
    print(part2(6, 2))
