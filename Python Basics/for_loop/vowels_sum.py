text = input()
sum = 0
for char in text:
    if char == 'a':
        sum += 1
    elif char == 'e':
        sum += 2
    elif char == 'i':
        sum += 3
    elif char == 'o':
        sum += 4
    elif char == 'u':
        sum += 5
print(sum)