from util import get_lines_for_day


def f(lines):
    ingredients = []
    high_score = 0

    for line in lines:
        line = line.split()
        ingredients.append(tuple(map(int, (line[2][:-1], line[4][:-1], line[6][:-1], line[8][:-1], line[10]))))

    for i in range(101):
        for j in range(0, 101 - i):
            for k in range(0, 101 - i - j):
                l = 100 - i - j - k

                capacity = i*ingredients[0][0] + j*ingredients[1][0] + k*ingredients[2][0] + l*ingredients[3][0]
                capacity = 0 if capacity < 0 else capacity
                durability = i*ingredients[0][1] + j*ingredients[1][1] + k*ingredients[2][1] + l*ingredients[3][1]
                durability = 0 if durability < 0 else durability
                flavor = i*ingredients[0][2] + j*ingredients[1][2] + k*ingredients[2][2] + l*ingredients[3][2]
                flavor = 0 if flavor < 0 else flavor
                texture = i*ingredients[0][3] + j*ingredients[1][3] + k*ingredients[2][3] + l*ingredients[3][3]
                texture = 0 if texture < 0 else texture
                calories = i*ingredients[0][4] + j*ingredients[1][4] + k*ingredients[2][4] + l*ingredients[3][4]

                score = capacity * durability * flavor * texture

                if calories == 500 and score > high_score:
                    high_score = score

    return high_score


print(f(get_lines_for_day(2015, 15)))
