m = int(input())
counter = 0
password = ''
there_is_a_password = False

for a in range(1, 10):
    for b in range(a+ 1, 10):
        for c in range(1, 10):
            for d in range(1, c):
                if a * b + c * d == m:
                    counter += 1
                    print(f'{a}{b}{c}{d}', end = ' ')
                    if counter == 4:
                        there_is_a_password = True
                        password = 1000 * a + 100 * b + 10 * c + d
if there_is_a_password:
    print()
    print(f'Password: {password}')
else:
    print()
    print('No!')