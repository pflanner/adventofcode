def f(inp):
    mem = {n: i for i, n in enumerate(inp)}
    ans = inp[-1]
    del mem[ans]
    l = inp[:-1]

    for i in range(len(inp) - 1, 30000000):
        tmp = ans
        if ans in mem:
            ans = i - mem[ans]
        else:
            ans = 0
        mem[tmp] = i
        l.append(tmp)

    return tmp


print(f([16,11,15,0,1,7]))
