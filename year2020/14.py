from util import get_input_for_day


def f(i):
    i = i.strip().split('\n')
    mem = {}

    for op in i:
        if op.startswith('mask'):
            zero_mask = int(''.join([c if c == '0' else '1' for c in op.split(' = ')[1]]), 2)
            one_mask = int(''.join([c if c == '1' else '0' for c in op.split(' = ')[1]]), 2)
        else:
            loc = op.split(' = ')[0].split(']')[0][4:]
            val = int(op.split(' = ')[1])

            val &= zero_mask
            val |= one_mask
            mem[loc] = val

    return sum(mem.values())


def g(i):
    i = i.strip().split('\n')
    mem = {}

    for op in i:
        if op.startswith('mask'):
            mask_str = op.split(' = ')[1]
        else:
            loc = int(op.split(' = ')[0].split(']')[0][4:])
            val = int(op.split(' = ')[1])

            new_loc = []
            while loc > 0:
                new_loc.append(str(loc % 2))
                loc //= 2

            new_loc.extend(['0'] * (36 - len(new_loc)))
            new_loc.reverse()

            for i, mask_bit in enumerate(mask_str):
                if mask_bit != '0':
                    new_loc[i] = mask_bit

            def dfs(prefix=''):
                if len(prefix) == 36:
                    mem[prefix] = val
                    return

                if new_loc[len(prefix)] == 'X':
                    dfs(prefix + '0')
                    dfs(prefix + '1')
                else:
                    dfs(prefix + new_loc[len(prefix)])

            dfs()

    return sum(mem.values())



print(g(get_input_for_day(14)))
