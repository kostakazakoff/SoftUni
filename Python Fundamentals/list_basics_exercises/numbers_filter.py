def filter_numbers(numbers, definition):
    output = []
    for number in numbers:
        definitions = (
            (definition == 'even' and number % 2 == 0),
            (definition == 'odd' and number % 2 != 0),
            (definition == 'negative' and number < 0),
            (definition == 'positive' and number >= 0)
        )
        if any(definitions):
            output.append(number)
    return output


lines = int(input())
integers = []

for i in range(lines):
    n = int(input())
    integers.append(n)
num_type = input()

print(filter_numbers(integers, num_type))
