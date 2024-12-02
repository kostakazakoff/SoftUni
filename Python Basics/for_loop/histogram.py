n = int(input())
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_all = 0
for i in range(n):
    number = int(input())
    if number < 200:
        count_1 += 1
    elif number < 400:
        count_2 += 1
    elif number < 600:
        count_3 += 1
    elif number < 800:
        count_4 += 1
    else:
        count_5 += 1
    count_all += 1
p1 = count_1 * 100 / count_all # count_1 - percent of all numbers
p2 = count_2 * 100 / count_all
p3 = count_3 * 100 / count_all
p4 = count_4 * 100 / count_all
p5 = count_5 * 100 / count_all
print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')