from util import get_input_for_day


class Operation:
    def __init__(self, lines):
        self.write = lines[0].split()[4][:-1]
        move_text = lines[1].split()[6][:-1]
        self.move = 1 if move_text == 'right' else -1
        self.next = lines[2].split()[4][:-1]

class State:
    def __init__(self, section):
        self.id = section[0].split()[2][:-1]
        self.ops = {}

        for i in range(1, len(section), 4):
            case = section[i].split()[5][:-1]
            op = Operation(section[i + 1:i + 4])
            self.ops[case] = op



def f(inp):
    sections = inp.split('\n\n')

    setup = sections[0].split('\n')
    cur_state = setup[0][:-1].split('Begin in state ')[1]
    steps = int(setup[1].split()[5])
    states = {}
    tape = set()
    pos = 0

    for section in sections[1:]:
        state = State(section.strip().split('\n'))
        states[state.id] = state

    for _ in range(steps):
        s = states[cur_state]
        val = '1' if pos in tape else '0'
        op = s.ops[val]

        if op.write == '0':
            tape.discard(pos)
        else:
            tape.add(pos)

        pos += op.move

        cur_state = op.next

    return len(tape)


print(f(get_input_for_day(2017, 25)))
