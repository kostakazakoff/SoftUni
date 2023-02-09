string = input()
result = ''

for i in range(1, len(string)):
    if string[i] == string[i - 1]:
        continue
    result += string[i - 1]
result += string[-1]

print(result)
