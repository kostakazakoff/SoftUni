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
if n < 3: half_r = 0

print('-' * half_r + '*' * stars + '-' * half_r)
if n > 2:
    for r in range(1, half_r):
        side_scores = half_r - r
        mid_scores = n - stars - side_scores * 2 - odd
        print('-' * side_scores, end = '')
        print('*', end = '')
        print('-' * mid_scores, end = '')
        print('*', end='')
        print('-' * side_scores)
    print("*" + '-' * (n - 2) + '*')
    for r in range(1, half_r):
        side_scores = r
        mid_scores = n - stars - side_scores * 2 - odd
        print('-' * side_scores, end='')
        print('*', end='')
        print('-' * mid_scores, end='')
        print('*', end='')
        print('-' * side_scores)
    print('-' * half_r + '*' * stars + '-' * half_r)