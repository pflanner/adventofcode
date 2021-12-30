from util import get_input_for_day
from collections import deque
from itertools import islice


def f(i):
    player1, player2 = i.strip().split('\n\n')

    player1 = deque(map(int, player1.split('\n')[1:]))
    player2 = deque(map(int, player2.split('\n')[1:]))

    while player1 and player2:
        c1 = player1.popleft()
        c2 = player2.popleft()

        if c1 > c2:
            player1.append(c1)
            player1.append(c2)
        else:
            player2.append(c2)
            player2.append(c1)

    winner = player1 or player2

    mult = 1
    score = 0
    for c in reversed(winner):
        score += c * mult
        mult += 1

    print(f"Winner's score = {score}")


def g(i):
    def helper(subdeck1, subdeck2):
        cards_this_game = set()

        while subdeck1 and subdeck2:
            if (tuple(subdeck1), tuple(subdeck2)) in cards_this_game:
                return 1

            cards_this_game.add((tuple(subdeck1), tuple(subdeck2)))

            c1 = subdeck1.popleft()
            c2 = subdeck2.popleft()

            if len(subdeck1) >= c1 and len(subdeck2) >= c2:
                winner = helper(deque(islice(subdeck1, c1)), deque(islice(subdeck2, c2)))
                if winner == 1:
                    subdeck1.append(c1)
                    subdeck1.append(c2)
                else:
                    subdeck2.append(c2)
                    subdeck2.append(c1)
                continue
            else:
                if c1 > c2:
                    subdeck1.append(c1)
                    subdeck1.append(c2)
                else:
                    subdeck2.append(c2)
                    subdeck2.append(c1)

        return 1 if not subdeck2 else 2

    player1, player2 = i.strip().split('\n\n')

    player1 = deque(map(int, player1.split('\n')[1:]))
    player2 = deque(map(int, player2.split('\n')[1:]))

    winner = helper(player1, player2)
    winner = player1 if winner == 1 else player2

    mult = 1
    score = 0
    for c in reversed(winner):
        score += c * mult
        mult += 1

    print(f"Winner's score = {score}")



g(get_input_for_day(22))
