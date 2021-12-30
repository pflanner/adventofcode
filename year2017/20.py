from util import get_lines_for_day


def get_matching_positions(ps):
    matching = set()
    for i, p1 in enumerate(ps[:-1]):
        for j, p2 in enumerate(ps[i + 1:], i + 1):
            if p1 == p2:
                matching.add(i)
                matching.add(j)
    return matching



def f(lines):
    ps, vs, a_s = [], [], []
    prev_dists = []
    annihilated = set()

    for line in lines:
        line = line.split(', ')
        ps.append(list(map(int, line[0][3:-1].split(','))))
        vs.append(list(map(int, line[1][3:-1].split(','))))
        a_s.append(list(map(int, line[2][3:-1].split(','))))

    for p in ps:
        prev_dists.append(sum(map(abs, p)))

    annihilated.update(get_matching_positions(ps))

    velocity_dirs_match_accel = False

    count = 0
    while not velocity_dirs_match_accel:
        count += 1
        velocity_dirs_match_accel = True

        for i in range(len(ps)):
            if i in annihilated:
                continue

            p = ps[i]
            v = vs[i]
            a = a_s[i]

            for j in range(3):
                v[j] = v[j] + a[j]
                if a[j] != 0 and (v[j] == 0 or v[j] // abs(v[j]) != a[j] // abs(a[j])):
                    velocity_dirs_match_accel = False
                p[j] = p[j] + v[j]

        annihilated.update(get_matching_positions(ps))

    for p in ps:
        prev_dists.append(sum(map(abs, p)))

    all_traveling_away = False

    while not all_traveling_away:
        all_traveling_away = True

        for i in range(len(ps)):
            if i in annihilated:
                continue

            p = ps[i]
            v = vs[i]
            a = a_s[i]

            for j in range(3):
                v[j] = v[j] + a[j]
                p[j] = p[j] + v[j]

            dist = sum(map(abs, p))
            if dist <= prev_dists[i]:
                all_traveling_away = False
            prev_dists[i] = dist

        annihilated.update(get_matching_positions(ps))

    # continue the simulation checking if the closest to the origin is gaining on any other point

    any_closing = True
    mn = min(prev_dists)
    dist_to_min = [d - mn for d in prev_dists]

    while any_closing:
        any_closing = False

        for i in range(len(ps)):
            if i in annihilated:
                continue

            p = ps[i]
            v = vs[i]
            a = a_s[i]

            for j in range(3):
                v[j] = v[j] + a[j]
                p[j] = p[j] + v[j]

            dist = sum(map(abs, p))
            prev_dists[i] = dist

        annihilated.update(get_matching_positions(ps))

        mn = min(prev_dists)
        for i, d in enumerate(prev_dists):
            if d - mn < dist_to_min[i]:
                any_closing = True
            dist_to_min[i] = d - mn

    min_dist_i = 0

    for i, d in enumerate(prev_dists):
        if d < prev_dists[min_dist_i]:
            min_dist_i = i

    return min_dist_i, len(ps) - len(annihilated)


print(f(get_lines_for_day(2017, 20)))
# part 1
# 192 is too high
# part 2
# 2 is not the right answer
