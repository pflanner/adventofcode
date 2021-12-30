from util import get_lines_for_day


def f(lines):
    reindeer = {}
    winner = None

    for line in lines:
        line = line.split()
        name = line[0]
        speed = int(line[3])
        fly = int(line[6])
        rest = int(line[13])

        reindeer[name] = (speed, fly, rest)

    for r, v in reindeer.items():
        speed, fly, rest = v
        flying = True
        count = 0
        distance = 0

        for _ in range(2503):
            if flying:
                if count < fly:
                    count += 1
                    distance += speed
                else:
                    flying = False
                    count = 1
            else:
                if count < rest:
                    count += 1
                else:
                    flying = True
                    distance += speed
                    count = 1

        if winner is None or distance > winner[1]:
            winner = (r, distance)

    return winner


def g(lines):
    reindeer = []
    winner = None

    for line in lines:
        line = line.split()
        name = line[0]
        speed = int(line[3])
        fly = int(line[6])
        rest = int(line[13])

        reindeer.append((name, speed, fly, rest))

    flying = [True] * len(reindeer)
    count = [0] * len(reindeer)
    distance = [0] * len(reindeer)
    points = [0] * len(reindeer)
    for _ in range(2503):
        for i, v in enumerate(reindeer):
            name, speed, fly, rest = v
            if flying[i]:
                if count[i] < fly:
                    count[i] += 1
                    distance[i] += speed
                else:
                    flying[i] = False
                    count[i] = 1
            else:
                if count[i] < rest:
                    count[i] += 1
                else:
                    flying[i] = True
                    distance[i] += speed
                    count[i] = 1

        farthest = max(distance)
        for i, d in enumerate(distance):
            if d == farthest:
                points[i] += 1

    most = max(points)
    for i, p in enumerate(points):
        if p == most:
            print(reindeer[i][0], p)


g(get_lines_for_day(2015, 14))
