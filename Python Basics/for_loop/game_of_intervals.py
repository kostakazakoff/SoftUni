turns = int(input())
points = 0
count_int_1 = 0
count_int_2 = 0
count_int_3 = 0
count_int_4 = 0
count_int_5 = 0
count_int_6 = 0
for i in range(turns):
    number = int(input())
    if 0 <= number < 10:
        points += number * 0.2
        count_int_1 += 1
    elif 10 <= number < 20:
        points += number * 0.3
        count_int_2 += 1
    elif 20 <= number < 30:
        points += number * 0.4
        count_int_3 += 1
    elif 30 <= number < 40:
        points += 50
        count_int_4 += 1
    elif 40 <= number <= 50:
        points += 100
        count_int_5 += 1
    else:
        points /= 2
        count_int_6 += 1
perc_int_1 = count_int_1 * 100 / turns
perc_int_2 = count_int_2 * 100 / turns
perc_int_3 = count_int_3 * 100 / turns
perc_int_4 = count_int_4 * 100 / turns
perc_int_5 = count_int_5 * 100 / turns
perc_int_6 = count_int_6 * 100 / turns
print(f'{points:.2f}')
print(f'From 0 to 9: {perc_int_1:.2f}%')
print(f'From 10 to 19: {perc_int_2:.2f}%')
print(f'From 20 to 29: {perc_int_3:.2f}%')
print(f'From 30 to 39: {perc_int_4:.2f}%')
print(f'From 40 to 50: {perc_int_5:.2f}%')
print(f'Invalid numbers: {perc_int_6:.2f}%')

