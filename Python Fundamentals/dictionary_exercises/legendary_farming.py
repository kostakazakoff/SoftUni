def name(key: str):
    if key == 'shards':
        return 'Shadowmourne'
    elif key == 'fragments':
        return 'Valanyr'
    elif key == 'motes':
        return 'Dragonwrath'


def output(items_dict: dict):
    for item in items_dict:
        print(f'{item}: {str(items_dict[item])}')


useful_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
not_useful = dict()
obtained = False

while not obtained:
    materials = input().split()
    while len(materials) != 0 and not obtained:
        quantity = int(materials.pop(0))
        material = materials.pop(0).lower()
        if material not in useful_materials:
            if material not in not_useful:
                not_useful[material] = 0
            not_useful[material] += quantity
        else:
            useful_materials[material] += quantity
            if useful_materials[material] >= 250:
                obtained = True
                useful_materials[material] -= 250
                legendary_item = name(material)
                print(f'{legendary_item} obtained!')
                output(useful_materials)
                output(not_useful)
