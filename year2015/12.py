from util import get_input_for_day
import json


def f(json_string):
    j = json.loads(json_string)
    result = 0

    def compute_sum(obj):
        nonlocal result

        if type(obj) == list:
            for item in obj:
                if type(item) == int:
                    result += int(item)
                else:
                    compute_sum(item)
        elif type(obj) == dict:
            if 'red' in obj.values():
                return

            for k, v in obj.items():
                if type(k) == int:
                    result += int(k)

                if type(v) == int:
                    result += int(v)
                else:
                    compute_sum(v)
        elif type(obj) == int:
            result += int(obj)

    compute_sum(j)

    return result


print(f(get_input_for_day(2015, 12)))
