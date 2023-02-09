n = int(input())
division_2 = 0
division_3 = 0
division_4 = 0

for i in range(n):
    number = int(input())
    if number % 2 == 0:
        division_2 += 1
    if number % 3 == 0:
        division_3 += 1
    if number % 4 == 0:
        division_4 += 1

percent_2 = division_2 * 100 / n
percent_3 = division_3 * 100 / n
percent_4 = division_4 * 100 / n

print(f'{percent_2:.2f}%')
print(f'{percent_3:.2f}%')
print(f'{percent_4:.2f}%')