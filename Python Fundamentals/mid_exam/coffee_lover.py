def valid_number_of_coffees(list_of_coffees: list, number_of_coffees: int):
    if number_of_coffees > len(list_of_coffees):
        return False
    return True


def valid_index(list_of_coffees: list, index: int):
    if 0 <= index < len(list_of_coffees):
        return True
    return False


def remove(list_of_coffees: list, position: str, number_of_coffees: int):
    if not valid_number_of_coffees(list_of_coffees, number_of_coffees):
        return list_of_coffees
    if position == 'first':
        list_of_coffees = list_of_coffees[number_of_coffees:]
    elif position == 'last':
        list_of_coffees = list_of_coffees[:-number_of_coffees]
    return list_of_coffees


def prefer(list_of_coffees: list, position_1: int, position_2: int):
    if not valid_index(list_of_coffees, position_1):
        return list_of_coffees
    if not valid_index(list_of_coffees, position_2):
        return list_of_coffees
    list_of_coffees[position_1], list_of_coffees[position_2] = list_of_coffees[position_2], list_of_coffees[position_1]
    return list_of_coffees


coffees = input().split(' ')
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split(' ')
    action = command[0]
    if action == 'Include':
        coffee = command[1]
        coffees.append(coffee)
    elif action == 'Remove':
        pos = command[1]
        num_of_coffees = int(command[2])
        coffees = remove(coffees, pos, num_of_coffees)
    elif action == 'Prefer':
        pos_1 = int(command[1])
        pos_2 = int(command[2])
        coffees = prefer(coffees, pos_1, pos_2)
    elif action == 'Reverse':
        coffees.reverse()

coffees = ' '.join(coffees)
print(f'Coffees:\n{coffees}')