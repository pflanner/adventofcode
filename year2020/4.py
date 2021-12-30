from util import get_input_for_day
import re


def is_valid(passport):
    required_fields = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': lambda x: x.endswith('cm') and 150 <= int(x[:-2]) <= 193 or x.endswith('in') and 59 <= int(x[:-2]) <= 76,
        'hcl': lambda x: re.match('^#[0-9a-f]{6}$', x),
        'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': lambda x: re.match('^[0-9]{9}$', x),
    }

    for l in passport:
        fields = l.split()
        for field in fields:
            key, value = field.split(':')
            try:
                if not required_fields.get(key, lambda x: True)(value):
                    return False
                else:
                    del required_fields[key]
            except:
                pass

    return len(required_fields) == 0


def part2():
    todays_input = get_input_for_day(4)
    passport = []
    num_valid = 0

    split = todays_input.split('\n')
    for line in split:
        if line:
            passport.append(line)
        else:
            if is_valid(passport):
                num_valid += 1
            passport.clear()

    print(num_valid)


part2()
