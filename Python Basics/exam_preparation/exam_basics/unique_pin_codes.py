first = int(input())
second = int(input())
third = int(input())

for f in range(2, first + 1, 2):
    for s in range(1, second + 1):
        for t in range(2, third + 1, 2):
            if s != 2 and s != 3 and s != 5 and s != 7:
                continue
            print(f'{f} {s} {t}')