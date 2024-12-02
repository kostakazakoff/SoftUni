n = int(input())
x = n
for i in range(1, n + 1):
    x -= 1
    print(' ' * (n - i) + ' *' * i, end='')
    print()
