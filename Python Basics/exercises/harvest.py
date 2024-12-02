import math

vineyard = int(input())
grape_per_sqm = float(input())
needed_quantity = int(input())
workers = int(input())
grape_for_liter = 2.5

harvest = vineyard * grape_per_sqm
harvest_for_vine = harvest * 0.4
vine = harvest_for_vine / grape_for_liter
difference = abs(vine - needed_quantity)
vine_for_worker = difference / workers

if vine < needed_quantity:
    print(f'It will be a tough winter! More {math.floor(difference)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(vine)} liters.')
    print(f'{math.ceil(difference)} liters left -> {math.ceil(vine_for_worker)} liters per person.')
