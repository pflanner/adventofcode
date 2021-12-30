from util import get_lines_for_day
from collections import Counter
from operator import itemgetter


def f(lines):
    all_allergens = set()
    all_ingredients = Counter()
    allergen_ingredients = {}

    for line in lines:
        ingredients, allergens = line.split(' (')
        ingredients = ingredients.split()
        allergens = allergens[9:].split(', ')
        allergens[-1] = allergens[-1][:-1]

        for allergen in allergens:
            if allergen not in allergen_ingredients:
                allergen_ingredients[allergen] = set(ingredients)
            else:
                allergen_ingredients[allergen].intersection_update(set(ingredients))
        all_allergens.update(allergens)
        all_ingredients.update(ingredients)

    keep_going = True
    visited = set()

    while keep_going:
        for a, i in allergen_ingredients.items():
            if len(i) == 1 and a not in visited:
                visited.add(a)
                the_ingredient = next(iter(i))
                for aa, ii in allergen_ingredients.items():
                    if aa != a:
                        ii.discard(the_ingredient)
                break
        else:
            keep_going = False

    print(all_allergens)
    print(all_ingredients)
    print(allergen_ingredients)

    for s in allergen_ingredients.values():
        ingredient = next(iter(s))
        del all_ingredients[ingredient]

    print(sum(all_ingredients.values()))

    dangerous = [(k, next(iter(v))) for k, v in allergen_ingredients.items()]
    dangerous.sort()
    print(','.join(map(itemgetter(1), dangerous)))


f(get_lines_for_day(21))
