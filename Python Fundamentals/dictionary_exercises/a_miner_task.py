metal = input()
collect = dict()
while metal != 'stop':
    quantity = int(input())
    if metal not in collect:
        collect[metal] = 0
    collect[metal] += quantity
    metal = input()
for metal, quantity in collect.items():
    print(f'{metal} -> {quantity}')