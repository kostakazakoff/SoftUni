import math
wall_heigh = int(input())
wall_width = int(input())
percent_of_holes = int(input())
walls_surface_to_paint = wall_width * wall_heigh * 4
walls_surface_to_paint -= math.ceil(walls_surface_to_paint * percent_of_holes / 100)
walls_are_painted = False

command = int(input())
while command != 'Tired!':
    liters_of_paint = int(command)
    walls_surface_to_paint -= liters_of_paint
    if walls_surface_to_paint <= 0:
        walls_are_painted = True
        break
    else:
        command = input()

if command == 'Tired!':
    print(f'{walls_surface_to_paint} quadratic m left.')
elif walls_are_painted and walls_surface_to_paint < 0:
    print(f'All walls are painted and you have {abs(walls_surface_to_paint)} l paint left!')
elif walls_are_painted:
    print('All walls are painted! Great job, Pesho!')
