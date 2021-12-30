"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
"""


def get_input_list():
    with open('input/1.txt') as f:
        nums = []
        for line in f:
            nums.append(int(line))

    return nums


def brute_force():
    nums = get_input_list()
    for i in range(len(nums) - 1):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == 2020:
                print(nums[i], nums[j], nums[i] * nums[j])


def sorting_first():
    nums = get_input_list()
    nums.sort()

    i, j = 0, len(nums) - 1

    while i < j:
        m, n = nums[i], nums[j]
        s = m + n

        if s == 2020:
            print(m, n, m * n)
            break
        elif s < 2020:
            i += 1
        else:
            j -= 1


def using_a_set():
    nums = get_input_list()
    s = set()

    for m in nums:
        n = 2020 - m
        if n in s:
            print(m, n, m * n)
        s.add(m)


"""
--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""


def three_sum():
    nums = get_input_list()
    nums.sort()

    for i in range(len(nums) - 2):
        n1 = nums[i]
        target = 2020 - n1

        j, k = i + 1, len(nums) - 1

        while j < k:
            n2, n3 = nums[j], nums[k]
            s = n2 + n3

            if s == target:
                print(n1, n2, n3, n1 * n2 * n3)
                return
            elif s < target:
                j += 1
            else:
                k -= 1


three_sum()
