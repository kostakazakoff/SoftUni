values = tuple(map(float, input().split()))
output = {}

output = {n: values.count(n) for n in values}

[print(key, f' - {value} times') for key, value in output.items()]
