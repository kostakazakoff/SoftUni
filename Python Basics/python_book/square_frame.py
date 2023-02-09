n = int(input())
print('+', end = ' ')
for c in range(n - 2):
    print('-', end = ' ')
print('+')
for r in range(1, n-1):
    print('|', end = ' ')
    for c in range(n - 2):
        print('-', end = ' ')
    print('|')
print('+', end = ' ')
for c in range(n - 2):
    print('-', end = ' ')
print('+')