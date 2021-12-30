from util import get_lines_for_day
from collections import defaultdict, deque


class Instruction:
    AND = 'AND'
    OR = 'OR'
    NOT = 'NOT'
    LSHIFT = 'LSHIFT'
    RSHIFT = 'RSHIFT'
    NUMBER = 'NUMBER'
    WIRE = 'WIRE'

    def __init__(self, line):
        self.text = line
        inpt, output = line.split(' -> ')
        if inpt.count(' ') == 1:
            self.op, self.in1 = inpt.split()
        elif inpt.count(' ') == 2:
            self.in1, self.op, self.in2 = inpt.split()
        else:
            try:
                self.in1, self.op = int(inpt), Instruction.NUMBER
            except (ValueError, TypeError):
                self.in1, self.op = inpt, Instruction.WIRE

        try:
            self.in1 = int(self.in1)
        except (ValueError, TypeError):
            pass

        if hasattr(self, 'in2'):
            try:
                self.in2 = int(self.in2)
            except (ValueError, TypeError):
                pass

        self.out = output


def f(i):
    instructions = []
    input_to_instruction = defaultdict(set)
    wire_values = {}
    q = deque()
    visited = set()

    # build our instruction list and starting queue
    for line in i:
        instruction = Instruction(line)
        instructions.append(instruction)
        if type(instruction.in1) == str:
            input_to_instruction[instruction.in1].add(instruction)
        if hasattr(instruction, 'in2') and type(instruction.in2) == str:
            input_to_instruction[instruction.in2].add(instruction)
        if instruction.op == Instruction.NUMBER:
            q.appendleft(instruction)
            visited.add(instruction)
            wire_values[instruction.out] = instruction.in1

    # breadth first traversal of instructions
    while q:
        cur = q.pop()
        
        for neighbor in input_to_instruction.get(cur.out, []):
            if neighbor in visited:
                continue
                
            output = None
            in1 = neighbor.in1 if type(neighbor.in1) == int else wire_values.get(neighbor.in1)
            in2 = None
            if hasattr(neighbor, 'in2'):
                in2 = neighbor.in2 if type(neighbor.in2) == int else wire_values.get(neighbor.in2)

            if neighbor.op == Instruction.WIRE:
                output = wire_values.get(neighbor.in1)
            elif neighbor.op == Instruction.AND:
                if in1 is not None and in2 is not None:
                    output = in1 & in2
            elif neighbor.op == Instruction.OR:
                if in1 is not None and in2 is not None:
                    output = in1 | in2
            elif neighbor.op == Instruction.NOT:
                if in1 is not None:
                    output = ~in1
            elif neighbor.op == Instruction.LSHIFT:
                if in1 is not None:
                    output = in1 << in2
            elif neighbor.op == Instruction.RSHIFT:
                if in1 is not None:
                    output = in1 >> in2
            
            if output is not None:
                visited.add(neighbor)
                q.appendleft(neighbor)
                wire_values[neighbor.out] = output

    for wire in wire_values:
        for ins in input_to_instruction[wire]:
            if ins.out not in wire_values:
                if type(ins.in1) == int or ins.in1 in wire_values:
                    if hasattr(ins, 'in2') and (type(ins.in2) == int or ins.in2 in wire_values):
                        print(ins.text)

    return wire_values['a']


print(f(get_lines_for_day(2015, '7_part2')))
