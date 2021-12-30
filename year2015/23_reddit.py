"""
https://www.reddit.com/r/adventofcode/comments/kx3xq0/2015_day_23_python_aoc_2019_prepared_me_well_for/
"""
import re
cmd = re.compile(r'^(\w+) (\w)?(?:, )?((?:\+|-)\d+)?$')

with open('input/23.txt') as f:
    # Subtract 1 from jump (offset) to enable ip++ for every instruction
    mem = [(i, r, j if j is None else int(j) - 1) for s in f for i, r, j in [cmd.match(s.strip()).groups()]]


def run(a: int) -> int:
    reg = {'a': a, 'b': 0}
    ip = 0
    while ip >= 0 and ip < len(mem):
        i, r, j = mem[ip]
        if i == 'inc':
            reg[r] += 1
        elif i == 'hlf':
            reg[r] //= 2
        elif i == 'tpl':
            reg[r] *= 3
        elif i == 'jmp' or (i == 'jie' and reg[r] % 2 == 0) or (i == 'jio' and reg[r] == 1):
            ip += j
        ip += 1
    return reg['b']


print(run(0))
