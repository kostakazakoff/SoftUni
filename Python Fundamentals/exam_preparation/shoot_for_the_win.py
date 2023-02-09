def valid_index(list_of_targets: list, index: int):
    if 0 <= index < len(list_of_targets):
        return True
    return False


def operate_values(shot_value, value_from_list):
    if value_from_list <= shot_value:
        return value_from_list + shot_value
    return value_from_list - shot_value


targets = list(map(int, input().split(' ')))
shooted = []
command = input()
shoots = 0

while command != 'End':
    index = int(command)
    if not valid_index(targets, index):
        command = input()
        continue
    shooted_value = targets[index]
    if targets[index] != -1:
        targets[index] = -1
        shoots += 1
    for i in range(len(targets)):
        if targets[i] == -1:
            continue
        targets[i] = operate_values(shooted_value, targets[i])
    command = input()

targets = ' '.join(list(map(str, targets)))
print(f'Shot targets: {shoots} -> {targets}')