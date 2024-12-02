n = int(input())
even = 0
odd = 1
stars = 1
mid_scores = 0
if n % 2 == 0:
    even = 1
    odd = 0
stars += even
half_r = (n - 1) // 2
cicle = 4
if n < 3: cicle = 1

for i in range(cicle):
    if i == 0 or i == cicle - 1: print('-' * half_r + '*' * stars + '-' * half_r)
    else:
        for r in range(1, half_r):
            if i == 1: side_scores = half_r - r
            else: side_scores = r
            mid_scores = n - stars - side_scores * 2 - odd
            print('-' * side_scores, end = '')
            print('*', end = '')
            print('-' * mid_scores, end = '')
            print('*', end='')
            print('-' * side_scores)
    if i == 1: print("*" + '-' * (n - 2) + '*')