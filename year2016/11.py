from util import get_lines_for_day
from itertools import combinations


class Floor:
    def __init__(self):
        self.microchips = set()
        self.generators = set()

    def items(self):
        items = [m for m in self.microchips]
        items += [g + '-g' for g in self.generators]

        return items

    def floor_id(self):
        return '-'.join(sorted(list(self.items())))

    def copy(self):
        f = Floor()
        f.microchips = self.microchips.copy()
        f.generators = self.generators.copy()

        return f


def is_valid_state(floors):
    for floor in floors:
        if len(floor.generators) == 0:
            continue

        for m in floor.microchips:
            if m not in floor.generators:
                return False

    return True


def f(lines):
    floors = [Floor() for _ in range(4)]
    num_microchips = num_generators = 0

    for i, line in enumerate(lines):
        line = line.replace(',', '')
        line = line.replace('.', '')
        line = line.replace('-compatible', '')
        line = line.replace('a ', '')
        line = line.replace('and ', '')
        line = line.split()

        if line[4] == 'nothing':
            continue

        for j in range(4, len(line), 2):
            if line[j + 1] == 'microchip':
                floors[i].microchips.add(line[j])
                num_microchips += 1
            else:
                floors[i].generators.add(line[j])
                num_generators += 1

    visited = set()
    count = 0

    def dfs(cur_floors, cur_steps, min_steps, i):
        nonlocal count
        count += 1
        print(count)
        if not is_valid_state(cur_floors):
            return min_steps

        if cur_steps >= min_steps:
            return min_steps

        # end state
        if len(cur_floors[3].microchips) == num_microchips and len(cur_floors[3].generators) == num_generators:
            return min(min_steps, cur_steps)

        floors_id = '_'.join(str(n) + floor.floor_id() for n, floor in enumerate(cur_floors))
        if floors_id in visited:
            return min_steps

        visited.add(floors_id)

        floor = floors[i]

        # singles
        for item in floor.items():
            new_floors = [floor.copy() for floor in cur_floors]

            if item.endswith('-g'):
                item = item[:-2]
                new_floors[i].generators.remove(item)
                if i < len(cur_floors) - 1:
                    new_floors[i + 1].generators.add(item)
                    min_steps = dfs(new_floors, cur_steps + 1, min_steps, i + 1)
                if i > 0:
                    new_new_floors = [floor.copy() for floor in new_floors]
                    new_new_floors[i - 1].generators.add(item)
                    min_steps = dfs(new_new_floors, cur_steps + 1, min_steps, i - 1)
                new_floors[i].generators.add(item)
            else:
                new_floors[i].microchips.remove(item)
                if i < len(cur_floors) - 1:
                    new_floors[i + 1].microchips.add(item)
                    min_steps = dfs(new_floors, cur_steps + 1, min_steps, i + 1)
                if i > 0:
                    new_new_floors = [floor.copy() for floor in new_floors]
                    new_new_floors[i - 1].microchips.add(item)
                    min_steps = dfs(new_new_floors, cur_steps + 1, min_steps, i - 1)
                new_floors[i].microchips.add(item)

        # pairs
        for pair in combinations(floor.items(), 2):
            if i < len(cur_floors) - 1:
                new_floors =[floor.copy() for floor in cur_floors]
                for item in pair:
                    if item.endswith('-g'):
                        item = item[:-2]
                        new_floors[i].generators.remove(item)
                        new_floors[i + 1].generators.add(item)
                        min_steps = dfs(new_floors, cur_steps + 1, min_steps, i + 1)
                    else:
                        new_floors[i].microchips.remove(item)
                        new_floors[i + 1].microchips.add(item)
                        min_steps = dfs(new_floors, cur_steps + 1, min_steps, i + 1)
            if i > 0:
                new_floors =[floor.copy() for floor in cur_floors]
                for item in pair:
                    if item.endswith('-g'):
                        item = item[:-2]
                        new_floors[i].generators.remove(item)
                        new_floors[i - 1].generators.add(item)
                        min_steps = dfs(new_floors, cur_steps + 1, min_steps, i - 1)
                    else:
                        new_floors[i].microchips.remove(item)
                        new_floors[i - 1].microchips.add(item)
                        min_steps = dfs(new_floors, cur_steps + 1, min_steps, i - 1)

        return min_steps

    return dfs(floors, 0, float('inf'), 0)


print(f(get_lines_for_day(2016, '11_test')))
