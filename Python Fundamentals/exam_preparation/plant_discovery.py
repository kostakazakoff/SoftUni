def in_dict(plant_to_check: str):
    if plant_to_check not in plants:
        print('error')
        return
    return True


def rate(plant_to_rate: str, plant_rating: float):
    if in_dict(plant_to_rate):
        plants[plant_to_rate]['Rating'].append(plant_rating)


def update(plant_to_update: str, new_rarity: str):
    if in_dict(plant_to_update):
        plants[plant_to_update]['Rarity'] = new_rarity


def reset_ratings(plant_to_reset: str):
    if in_dict(plant_to_reset):
        plants[plant_to_reset]['Rating'] = []


def average(list_of_values: list):
    if len(list_of_values) == 0:
        return 0
    return sum(list_of_values) / len(list_of_values)


def output():
    print('Plants for the exhibition:')
    for item, values in plants.items():
        r = values['Rarity']
        ar = average(values['Rating'])
        print(f'- {item}; Rarity: {r}; Rating: {ar:.2f}')


number_of_lines = int(input())
plants = {}

for _ in range(number_of_lines):
    plant, rarity = input().split('<->')
    plants.update({plant: {'Rarity': rarity, 'Rating': []}})


command = input()
while command != 'Exhibition':
    action, details = command.split(': ')
    details = details.split(' - ')
    if action == 'Rate':
        plant, rating = [float(x) if x.isdigit() else x for x in details]
        rate(plant, rating)
    elif action == 'Update':
        plant, new_plant_rarity = details
        update(plant, new_plant_rarity)
    else:
        plant = details[0]
        reset_ratings(plant)
    command = input()

output()
