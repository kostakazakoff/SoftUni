def average_value(array: list):
    return sum(array) / len(array)


def top_five(array: list):
    average = average_value(array)
    sorted_array = sorted(array, reverse=True)
    first_5 = sorted_array[:5]
    result = [n for n in first_5 if n > average]
    return result


numbers = list(map(int, input().split(' ')))
top_5 = top_five(numbers)
output = ' '.join([str(n) for n in top_5]) if len(top_5) > 0 else 'No'

print(output)