def valid_index(list_of_targets: list, index: int):
    if 0 <= index < len(list_of_targets):
        return True
    return False


def valid_radius(list_of_targets: list, index: int, radius: int):
    if not valid_index(list_of_targets, index + radius):
        return False
    if not valid_index(list_of_targets, index - radius):
        return False
    return True


def shot(targets: list, index: int, power: int):
    if not valid_index(targets, index):
        return targets
    targets[index] -= power
    if targets[index] <= 0:
        targets.pop(index)
    return targets


def add(targets: list, index: int, value: int):
    if not valid_index(targets, index):
        print('Invalid placement!')
        return targets
    targets.insert(index, value)
    return targets


def strike(targets: list, index: int, radius: int):
    if not valid_radius(targets, index, radius):
        print('Strike missed!')
        return targets
    area_start = index - radius
    area_end = index + radius
    targets = targets[:area_start] + targets[area_end + 1:]
    return targets


targets = list(map(int, input().split(' ')))
command = input()

while command != 'End':
    command = command.split(' ')
    action = command[0]
    i = int(command[1])
    value = int(command[2])

    if action == 'Shoot':
        targets = shot(targets, i, value)
    elif action == 'Add':
        targets = add(targets, i, value)
    elif action == 'Strike':
        targets = strike(targets, i, value)
    command = input()

targets = '|'.join(list(map(str, targets)))
print(targets)