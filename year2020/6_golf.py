from util import get_input_for_day as gi


def day_6_golf():
    print(sum(len(set.union(*group)) for group in ((set(a) for a in g.split('\n')) for g in gi(6).strip().split('\n\n'))))
    print(sum(len(set.intersection(*group)) for group in ((set(a) for a in g.split('\n')) for g in gi(6).strip().split('\n\n'))))


day_6_golf()
