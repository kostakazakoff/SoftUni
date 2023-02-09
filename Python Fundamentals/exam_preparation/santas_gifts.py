n = int(input())
list_of_addresses = input()
list_of_addresses = list_of_addresses.split()
position = 0

for i in range(n):
    command = input()
    command = command.split()
    action = command[0]
    if action == 'Forward':
        step = int(command[1])
        if position + step >= len(list_of_addresses):
            continue
        position += step
        list_of_addresses.pop(position)
    elif action == 'Back':
        step = int(command[1])
        if position - step < 0:
            continue
        position -= step
        list_of_addresses.pop(position)
    elif action == 'Gift':
        if int(command[1]) >= len(list_of_addresses):
            continue
        position = int(command[1])
        new_house_number = command[2]
        list_of_addresses.insert(position, new_house_number)
    elif action == 'Swap':
        first_house = command[1]
        second_house = command[2]
        if first_house not in list_of_addresses or second_house not in list_of_addresses:
            continue
        i_1 = list_of_addresses.index(first_house)
        i_2 = list_of_addresses.index(second_house)
        list_of_addresses.pop(i_1)
        list_of_addresses.insert(i_1, second_house)
        list_of_addresses.pop(i_2)
        list_of_addresses.insert(i_2, first_house)

output = ', '.join(list_of_addresses)
print(f'Position: {position}')
print(output)