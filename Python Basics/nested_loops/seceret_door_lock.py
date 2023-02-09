max_000 = int(input())
max_00 = int(input())
max_0 = int(input())

for i_000 in range(2, max_000 + 1, 2):
    for i_00 in range(1, max_00 + 1):
        for i_0 in range(2, max_0 + 1, 2):
            if i_00  == 2 or i_00 == 3 or i_00 == 5 or i_00 == 7:
                print(f'{i_000} {i_00} {i_0}')