values = tuple(map(float, input().split()))
output = {}
unique = []

for number in values:
    if number not in unique:
        unique.append(number)

for number in unique:
    output[number] = str(f'- {values.count(number)} times')

[print(key, value) for key, value in output.items()]
