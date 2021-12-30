from util import get_lines_for_day, get_input_for_day, get_groups

def winner(board, called):
    for row in board:
        count = 0
        for col in row:
            if col in called:
                count += 1
        if count == len(row):
            return True

    for i in range(len(board[0])):
        count = 0
        j = 0
        while j < len(board):
            val = board[j][i]
            if val in called:
                count += 1
            j += 1
        if count == j:
            return True

    return False

def calc(board, called):
    result = 0
    for row in board:
        for col in row:
            if col not in called:
                result += col
    return result


def part1(nums, boards):
    called = set()
    for num in nums:
        called.add(num)
        for board in boards:
            if winner(board, called):
                return calc(board, called) * num


def part2(nums, boards):
    called = set()
    winners = set()
    for num in nums:
        called.add(num)
        for i, board in enumerate(boards):
            if winner(board, called):
                winners.add(i)
                if len(winners) == len(boards):
                    return calc(board, called) * num


if __name__ == '__main__':
    lines = get_lines_for_day(2021, 4)
    # inp = get_input_for_day(2021, 4)
    groups = get_groups(lines)

    nums = list(map(int, groups[0][0].split(',')))
    boards = []

    for g in groups[1:]:
        board = []
        for row in g:
            board.append(list(map(int, row.split())))
        boards.append(board)

    print(part1(nums, boards))
    print(part2(nums, boards))
