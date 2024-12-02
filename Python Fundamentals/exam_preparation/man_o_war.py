def valid_index(ship: list, index: int):
    if 0 <= index < len(ship):
        return True
    return False


def fire(warship: list, index: int, damage: int):
    if not valid_index(warship, index):
        return False, warship
    warship[index] -= damage
    if warship[index] <= 0:
        print('You won! The enemy ship has sunken.')
        return True, warship
    return False, warship


def defend(pirate_ship: list, start_index: int, end_index: int, damage: int):
    if not valid_index(pirate_ship, start_index) or not valid_index(pirate_ship, end_index):
        return False, pirate_ship
    damaged_area = range(start_index, end_index + 1)
    for i in damaged_area:
        pirate_ship[i] -= damage
        if pirate_ship[i] <= 0:
            print('You lost! The pirate ship has sunken.')
            return True, pirate_ship
    return False, pirate_ship


def repair(pirate_ship: list, index: int, health: int, max: int):
    if not valid_index(pirate_ship, index):
        return pirate_ship
    pirate_ship[index] += health
    if pirate_ship[index] > max:
        pirate_ship[index] = max
    return pirate_ship


def status(pirate_ship: list, health_section: int):
    need_to_repair_sections = [x for x in pirate_ship if x < 0.2 * health_section]
    print(f'{len(need_to_repair_sections)} sections need repair.')


pirateship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())
command = input()

while command != 'Retire':
    command = command.split()
    action = command[0]
    if action == 'Fire':
        i = int(command[1])
        damage = int(command[2])
        won, warship = fire(warship, i, damage)
        if won:
            exit()
    elif action == 'Defend':
        start_i = int(command[1])
        end_i = int(command[2])
        damage = int(command[3])
        lost, pirateship = defend(pirateship, start_i, end_i, damage)
        if lost:
            exit()
    elif action == 'Repair':
        i = int(command[1])
        health_addition = int(command[2])
        pirateship = repair(pirateship, i, health_addition, max_health)
    elif action == 'Status':
        status(pirateship, max_health)
    command = input()
else:
    print(f'Pirate ship status: {sum(pirateship)}\nWarship status: {sum(warship)}')