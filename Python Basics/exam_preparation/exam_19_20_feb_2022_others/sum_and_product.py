n = int(input())
solution = False
for a in range(1, 10):
    for b in range(9, a, -1):
        for c in range(10):
            for d in range(9, c, -1):
                if a + b + c + d == a * b * c * d and n % 5 == 0:
                    print(f'{a}{b}{c}{d}')
                    exit()
                elif a * b * c * d // (a + b + c + d) == 3 and n % 3 == 0:
                    print(f'Var 2: {d}{c}{b}{a}')
                    exit()
print('Nothing found')