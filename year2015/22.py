from util import get_lines_for_day
from collections import Counter
from operator import attrgetter


class Spell:
    def __init__(self, name='No spell', cost=0, damage_effect=0, immediate_damage=0, heal=0, armor=0, recharge=0, effect=0):
        self.name = name
        self.cost = cost
        self.damage_effect = damage_effect
        self.immediate_damage = immediate_damage
        self.heal = heal
        self.armor = armor
        self.recharge = recharge
        self.effect = effect

    def copy(self):
        return Spell(self.name, self.cost, self.damage_effect, self.immediate_damage, self.heal, self.armor, self.recharge, self.effect)

    def print_effects(self):
        print(f'{self.name}', end='')

        if self.armor:
            print(f'\'s ', end='')
        elif self.damage_effect:
            print(f' deals {self.damage_effect} damage; its ', end='')
        elif self.recharge:
            print(f' provides {self.recharge} mana; its ', end='')

        print(f'timer is now {self.effect}')


def f(lines, hp=50, mana=500, logging=False, hard_mode=False):
    boss_hp = int(lines[0].split(': ')[1])
    boss_damage = int(lines[1].split(': ')[1])
    min_cost = float('inf')

    no_spell = Spell()
    magic_missle = Spell(name='Magic Missile', cost=53, immediate_damage=4)
    drain = Spell(name='Drain', cost=73, immediate_damage=2, heal=2)
    shield = Spell(name='Shield', cost=113, armor=7, effect=6)
    poison = Spell(name='Poison', cost=173, damage_effect=3, effect=6)
    recharge = Spell(name='Recharge', cost=229, recharge=101, effect=5)
    spells = [magic_missle, drain, shield, poison, recharge]

    def dfs(spell, spells_in_effect, mana_used, mana_remaining, hp_remaining, boss_hp_remaining):
        nonlocal min_cost

        if hard_mode:
            hp_remaining -= 1
            if hp_remaining <= 0:
                if logging:
                    print('Player died')
                return

        # Player's turn --------------------------
        if logging:
            armor = sum(map(attrgetter('armor'), spells_in_effect))
            print('-- Player turn --')
            print(f'- Player has {hp_remaining} hit points, {armor} armor, {mana_remaining} mana')
            print(f'- Boss has {boss_hp_remaining} hit points')

        new_spells_in_effect = []

        # player casts a new spell (the one passed in)
        if logging:
            print(f'Player casts {spell.name}')
            print()
        mana_used += spell.cost
        mana_remaining -= spell.cost
        if spell.effect == 0:
            boss_hp_remaining -= spell.immediate_damage
            hp_remaining += spell.heal
        else:
            new_spells_in_effect.append(spell)

        # check if boss is dead
        if boss_hp_remaining <= 0:
            if logging:
                print('This kills the boss, and the player wins.')
            min_cost = min(min_cost, mana_used)
            return

        # things that are in effect happen
        for s in spells_in_effect:
            boss_hp_remaining -= s.damage_effect
            # hp_remaining += s.heal
            mana_remaining += s.recharge
            s.effect -= 1

            if logging:
                s.print_effects()

            if s.effect >= 1:
                new_spells_in_effect.append(s)

        # check if boss is dead
        if boss_hp_remaining <= 0:
            if logging:
                print('This kills the boss, and the player wins.')
            min_cost = min(min_cost, mana_used)
            return

        # Boss's turn -------------------------------------
        armor = sum(map(attrgetter('armor'), new_spells_in_effect))
        if logging:
            print('-- Boss turn --')
            print(f'- Player has {hp_remaining} hit points, {armor} armor, {mana_remaining} mana')
            print(f'- Boss has {boss_hp_remaining} hit points')

        # things that are in effect happen
        newer_spells_in_effect = []
        for s in new_spells_in_effect:
            boss_hp_remaining -= s.damage_effect
            # hp_remaining += s.heal
            mana_remaining += s.recharge
            s.effect -= 1

            if logging:
                s.print_effects()

            if s.effect >= 1:
                newer_spells_in_effect.append(s)

        # check if boss is dead
        if boss_hp_remaining <= 0:
            if logging:
                print('This kills the boss, and the player wins.')
            min_cost = min(min_cost, mana_used)
            return

        # boss attacks
        boss_attack = boss_damage - armor
        boss_attack = boss_attack if boss_attack > 1 else 1

        hp_remaining -= boss_attack
        if logging:
            print(f'Boss attacks for {boss_attack} damage!')
            print()

        # check if player is dead
        if hp_remaining <= 0:
            if logging:
                print('Player died')
            return

        # effects can be started on the same round they end, so if any effect has 1 tick left now, that spell can be cast
        effect_times_left = {s.name: s.effect for s in newer_spells_in_effect}

        for s in spells:
            if mana_remaining >= s.cost and effect_times_left.get(s.name, 0) < 2 and mana_used < min_cost:
                dfs(s.copy(), [ns.copy() for ns in newer_spells_in_effect], mana_used, mana_remaining, hp_remaining, boss_hp_remaining)

    for s in spells:
        dfs(s.copy(), [], 0, mana, hp, boss_hp)

    return min_cost


print(f(get_lines_for_day(2015, '22'), hard_mode=True))
# part 1
# 212 is too low
#
# part 2
# 1242 is too high
# 1169 is too low
