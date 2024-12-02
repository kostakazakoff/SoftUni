stadium_capacity = int(input())
fans = int(input())
count_a = 0
count_b = 0
count_v = 0
count_g = 0
percent_a = 0
percent_b = 0
percent_v = 0
percent_g = 0
percent_all = 0
for i in range(fans):
    sector = input()
    if sector == 'A':
        count_a += 1
    if sector == 'B':
        count_b += 1
    if sector == 'V':
        count_v += 1
    if sector == 'G':
        count_g += 1
percent_a = count_a * 100 / fans
percent_b = count_b * 100 / fans
percent_v = count_v * 100 / fans
percent_g = count_g * 100 / fans
percent_all = (count_a + count_b + count_v + count_g) * 100 / stadium_capacity
print(f'{percent_a:.2f}%')
print(f'{percent_b:.2f}%')
print(f'{percent_v:.2f}%')
print(f'{percent_g:.2f}%')
print(f'{percent_all:.2f}%')