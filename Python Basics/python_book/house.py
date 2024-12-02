n = int(input())

for r in range(1, (n + 1) // 2):
    stars = r * 2
    if n % 2 != 0:
        stars -= 1
    score = int((n - stars) / 2)
    print('-' * score, end ='')
    print('*' * stars, end ='')
    print('-' * score)
print('*' * n)
for r in range(n // 2):
    print('|', end = '')
    print('*' * (n - 2), end = '')
    print('|')