number_of_bakers = int(input())
max_points = 0
best_baker = ''

for baker in range(number_of_bakers):
    name_of_baker = input()
    command = input()
    the_best = False
    baker_points_counter = 0

    while command != 'Stop':
        points = int(command)
        baker_points_counter += points
        command = input()

    if baker_points_counter > max_points:
        max_points = baker_points_counter
        best_baker = name_of_baker
        the_best = True

    print(f'{name_of_baker} has {baker_points_counter} points.')
    if the_best:
        print(f'{best_baker} is the new number 1!')
print(f'{best_baker} won competition with {max_points} points!')