first = list(map(int, input()))
last = list(map(int, input()))
first = list(map(lambda x: x + 1 if x % 2 == 0 else x, first))

for n1 in range(first[0], last[0] + 1, 2):
    for n2 in range(first[1], last[1] + 1, 2):
        for n3 in range(first[2], last[2] + 1, 2):
            for n4 in range(first[3], last[3] + 1, 2):
                print(f'{n1}{n2}{n3}{n4}', end = ' ')

