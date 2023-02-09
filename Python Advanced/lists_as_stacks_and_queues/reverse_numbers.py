numbers = input().split()
reversed = []

while numbers:
    reversed.append(numbers.pop())

print(' '.join(reversed))
