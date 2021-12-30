from util import get_lines_for_day
from math import ceil


def f(lines):
    hp = 100
    boss_hp = int(lines[0].split(': ')[1])
    boss_damage = int(lines[1].split(': ')[1])
    boss_armor = int(lines[2].split(': ')[1])
    min_cost = float('inf')
    max_cost = 0

    weapons = [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)]
    armor = [(0, 0), (13, 1), (31, 2), (53, 3), (75, 4), (102, 5)]
    rings = [(0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

    for weapon_cost, weapon_val in weapons:
        for armor_cost, armor_val in armor:
            for ring1 in rings:
                for ring2 in rings:
                    ring_def = ring_damage = ring_cost = 0
                    if ring1 != ring2:
                        ring1_cost, ring1_damage, ring1_armor = ring1
                        ring2_cost, ring2_damage, ring2_armor = ring2
                        ring_cost = ring1_cost + ring2_cost
                        ring_def = ring1_armor + ring2_armor
                        ring_damage = ring1_damage + ring2_damage

                    total_cost = weapon_cost + armor_cost + ring_cost
                    attack = weapon_val + ring_damage - boss_armor
                    attack = attack if attack > 1 else 1

                    defense = armor_val + ring_def

                    rounds_to_kill_boss = ceil(boss_hp / attack)

                    boss_attack = boss_damage - defense
                    boss_attack = boss_attack if boss_attack > 1 else 1

                    rounds_to_kill_me = ceil(hp / boss_attack)

                    if rounds_to_kill_boss <= rounds_to_kill_me:
                        min_cost = min(min_cost, total_cost)

                    if rounds_to_kill_me < rounds_to_kill_boss:
                        max_cost = max(max_cost, total_cost)

    return min_cost, max_cost


print(f(get_lines_for_day(2015, 21)))
