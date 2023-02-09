quantity = int(input())
command = input()
not_enough_eggs = False
sold = 0
while command != 'Close':
    action = command
    number_of_eggs = int(input())
    if action == 'Fill':
        quantity += number_of_eggs
    elif action == 'Buy':
        if quantity < number_of_eggs:
            not_enough_eggs = True
            break
        else:
            sold += number_of_eggs
            quantity -= number_of_eggs
    if not_enough_eggs:
        break
    command = input()
if not_enough_eggs:
    print('Not enough eggs in store!')
    print(f'You can buy only {quantity}.')
else:
    print('Store is closed!')
    print(f'{sold} eggs sold.')
