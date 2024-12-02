def calc_name_value(current_name, current_row):
    value = 0
    for char in current_name:
        value += ord(char)
    value //= current_row
    return value


def odd_even_collect(name_result):
    global odd_values, even_values
    odd_values.add(name_result) if name_result % 2 != 0 else even_values.add(name_result)


n = int(input())
odd_values, even_values = set(), set()

for row in range(1, n + 1):
    name = input()
    name_value = calc_name_value(name, row)
    odd_even_collect(name_value)

odd_sum, even_sum = sum(odd_values), sum(even_values)
if odd_sum == even_sum:
    print(*(odd_values | even_values), sep=', ')
elif odd_sum > even_sum:
    print(*(odd_values - even_values), sep=', ')
else:
    print(*(odd_values ^ even_values), sep=', ')
