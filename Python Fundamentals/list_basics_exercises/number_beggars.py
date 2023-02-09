alms = list(map(int, input().split(', ')))
output = []

beggars = int(input())

for sequence in range(beggars):
    current_beggar_profit = 0
    for _ in range(len(alms)):
        if sequence >= len(alms):
            break
        current_beggar_profit += alms[sequence]
        sequence += beggars
    output.append(current_beggar_profit)

print(output)
