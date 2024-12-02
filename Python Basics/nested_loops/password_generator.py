n = int(input())
l = int(input())

for i_1 in range(1, n):
    for i_2 in range(1, n):
        i_5_start = 1
        if i_5_start <= i_1: i_5_start = i_1 + 1
        if i_5_start <= i_2: i_5_start = i_2 + 1
        for i_3 in range(97, l + 97):
            for i_4 in range(97, l + 97):
                for i_5 in range(i_5_start, n + 1):
                    print(f'{i_1}{i_2}{chr(i_3)}{chr(i_4)}{i_5}', end = ' ')
