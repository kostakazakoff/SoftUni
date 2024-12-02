def loot(treasure_list: list, items_list: list):
    items_list = [x for x in items_list if x not in treasure_list]
    for item in items_list:
        treasure_list.insert(0, item)
    return treasure_list


def drop(treasure_list: list, index: int):
    if index < 0 or index >= len(treasure_list):
        return treasure_list
    treasure_list.append(treasure_list.pop(index))
    return treasure_list


def steal(treasure_list: list, count: int):
    print(', '.join(treasure_list[-count:]))
    treasure_list = treasure_list[:-count]
    return treasure_list


chest = input().split('|')
command = input()

while command != 'Yohoho!':
    command = command.split()
    action = command[0]
    if action == 'Loot':
        items = command[1:]
        chest = loot(chest, items)
    elif action == 'Drop':
        i = int(command[1])
        chest = drop(chest, i)
    elif action == 'Steal':
        stealed_count = int(command[1])
        chest = steal(chest, stealed_count)
    command = input()

if len(chest) > 0:
    average_treasure_gain = sum([len(x) for x in chest]) / len(chest)
    print(f'Average treasure gain: {average_treasure_gain:.2f} pirate credits.')
else:
    print('Failed treasure hunt.')