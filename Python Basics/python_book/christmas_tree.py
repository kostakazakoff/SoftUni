n = int(input())
for r in range(n + 1):
    print(' ' * (n - r), end = '')
    print('*' * r, end = ' ')
    print('|', end = ' ')
    print('*' * r)