start = int(input())
last = int(input())

for first in range(start, last + 1):
    for second in range(start, last + 1):
        for third in range(start, last + 1):
            if (second + third) % 2 != 0: continue
            for fourth in range(start, last + 1):
                if (first + fourth) % 2 == 0 or first <= fourth: continue
                print(f'{first}{second}{third}{fourth}', end = ' ')