n = int(input())

for first in range(1, 10):
    for second in range(1, 10):
        if n % (first + second) != 0: continue
        for third in range(1, 10):
            for fourth in range(1, 10):
                if n % (third + fourth) != 0 or first + second != third + fourth: continue
                print(f'{first}{second}{third}{fourth}', end = ' ')