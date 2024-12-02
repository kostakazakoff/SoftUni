floors = int(input())
units = int(input())

for f in range(floors, 0, -1):
    for u in range(units):
        if f == floors:
            print(f'L{f}{u}', end=' ')
        elif f % 2 == 0:
            print(f'O{f}{u}', end=' ')
        else:
            print(f'A{f}{u}', end=' ')
    print()