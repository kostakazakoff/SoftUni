n = int(input())
print('*' * n * 2 + ' ' * n + '*' * n * 2)
for r in range(n - 2):
    if r + 1 == (n - 1) // 2:
        print('*' + '/' * (n * 2 - 2) + '*', end='')
        print('|' * n, end = '')
        print('*' + '/' * (n * 2 - 2) + '*')
    else:
        for c in range(2):
            print('*' + '/' * (n * 2 - 2) + '*', end=' ' * n)
        print()
print('*' * n * 2 + ' ' * n + '*' * n * 2)