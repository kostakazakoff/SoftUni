fuel = input()
liters = float(input())

if fuel == 'Diesel':
    if liters >= 25:
        print(f'You have enough {fuel.lower()}.')
    else:
        print(f'Fill your tank with {fuel.lower()}!')
elif fuel == 'Gasoline':
    if liters >= 25:
        print(f'You have enough {fuel.lower()}.')
    else:
        print(f'Fill your tank with {fuel.lower()}!')
elif fuel == 'Gas':
    if liters >= 25:
        print(f'You have enough {fuel.lower()}.')
    else:
        print(f'Fill your tank with {fuel.lower()}!')
else:
    print('Invalid fuel!')