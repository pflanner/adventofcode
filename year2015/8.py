from util import get_lines_for_day


def f(lines):
    code = 0
    memory = 0
    recode = 0

    for line in lines:
        code += len(line)

        recode += len(line) + 2
        recode += line.count('"')
        recode += line.count('\\')

        line = line[1:-1]

        i = 0
        while i < len(line):
            memory += 1
            c = line[i]
            if c == '\\':
                if i < len(line) - 1 and line[i + 1] in '\\"':
                    i += 1
                elif i < len(line) - 3 and line[i + 1] == 'x':
                    try:
                        hex_part = line[i + 2:i + 4]
                        int(hex_part, 16)
                        i += 3
                    except (ValueError, TypeError):
                        pass
            i += 1

    return code, memory, code - memory, recode, recode - code
# \x12


print(f(get_lines_for_day(2015, '8')))
