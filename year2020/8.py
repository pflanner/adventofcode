from util import get_input_for_day

def f():
    todays_input = get_input_for_day(8)
    todays_input = todays_input.strip()
    base_lines = todays_input.split('\n')

    for i in range(len(base_lines)):
        lines = base_lines[:]
        acc = 0
        visited = set()
        cur = 0

        if 'nop' in lines[i]:
            lines[i] = lines[i].replace('nop', 'jmp')
        elif 'jmp' in lines[i]:
            lines[i] = lines[i].replace('jmp', 'nop')

        while cur not in visited:
            if cur == len(lines):
                print(acc)
            line = lines[cur]
            visited.add(cur)
            line = line.split()
            op = line[0]
            sign = line[1][:1]
            val = int(line[1][1:])
            if sign == '-':
                val *= -1

            if op == 'acc':
                acc += val
                cur += 1
            elif op == 'jmp':
                cur += val
            else:
                cur += 1


f()