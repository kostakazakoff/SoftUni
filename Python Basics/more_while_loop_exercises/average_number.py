n = int(input())
number = ''
sum = 0
average = 0
for i in range(1, n + 1):
    number = int(input())
    sum += number
average = sum / n
print(f'{average:.2f}')