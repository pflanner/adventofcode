import browser_cookie3
import pathlib
import requests


def download_input_for_day(year, day):
    year = str(year)
    day = str(day)
    filename = f'input/{day}.txt'
    cookies = browser_cookie3.chrome(domain_name='.adventofcode.com')

    response = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=cookies)

    with open(filename, mode='w') as f:
        f.write(response.text)


def get_input_for_day(year, day):
    year = str(year)
    day = str(day)
    filename = f'input/{day}.txt'

    p = pathlib.Path(filename)
    if not p.exists():
        download_input_for_day(year, day)

    with open(filename) as f:
        return f.read()


def get_lines_for_day(year, day):
    return get_input_for_day(year, day).rstrip().split('\n')


def get_groups(lines):
    groups = []
    group = []

    for line in lines:
        if line:
            group.append(line)
        else:
            groups.append(group)
            group = []

    if group:
        groups.append(group)

    return groups


class ListNode(object):
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        n = self.next if not self.next else self.next.val
        return 'val=%d next=%r' % (self.val, n)
