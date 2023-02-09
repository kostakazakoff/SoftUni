def useful_material(key: str):
    if key == 'shards':
        return True, 'Shadowmourne'
    elif key == 'fragments':
        return True, 'Valanyr'
    elif key == 'motes':
        return True, 'Dragonwrath'
    return False, None


def output(items_dict: dict):
    for item in items_dict:
        print(f'{item}: {str(items_dict[item])}')


items = {'shards': 0, 'fragments': 0, 'motes': 0}
obtained = False

while not obtained:
    materials = input().split()
    while len(materials) != 0 and not obtained:
        quantity = int(materials.pop(0))
        material = materials.pop(0).lower()
        if material not in items:
            items[material] = 0
        items[material] += quantity
        useful, legendary = useful_material(material)
        if not useful:
            continue
        if items[material] >= 250:
            obtained = True
            items[material] -= 250
            print(f'{legendary} obtained!')
            break

output(items)