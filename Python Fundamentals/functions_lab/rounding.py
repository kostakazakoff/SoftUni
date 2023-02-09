source_string = input()


def round_numbers(string_of_numbers):
    numbers = list(map(float, string_of_numbers.split()))
    rounded_numbers = list(round(x) for x in numbers)
    return rounded_numbers


print(round_numbers(source_string))
