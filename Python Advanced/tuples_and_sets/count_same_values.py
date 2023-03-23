values = tuple(map(float, input().split()))
output = {}

for n in values:
    if n not in output:
        output[n] = 0
    output[n] += 1

[print(key, f' - {value} times') for key, value in output.items()]
