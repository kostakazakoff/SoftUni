expression = input().split('|')
energy = 100
coins = 100
not_enough_money = False

for each in expression:
    event = each.split('-')
    item = event[0]
    value = int(event[1])
    if item == 'rest':
        energy += value
        if energy > 100:
            exceeded_value = energy - 100
            value -= exceeded_value
            energy = 100
        print(f'You gained {value} energy.')
        print(f'Current energy: {energy}.')
    elif item == 'order':
        if energy >= 30:
            energy -= 30
            coins += value
            print(f'You earned {value} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if value <= coins:
            coins -= value
            print(f'You bought {item}.')
        else:
            not_enough_money = True
            break

if not_enough_money:
    print(f'Closed! Cannot afford {item}.')
else:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
