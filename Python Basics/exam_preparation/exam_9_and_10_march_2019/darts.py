name_of_the_player = input()
points = 301
good_shots_counter = 0
bad_shots_counter = 0
a_bad_shot = False

while points != 0:
    command = input()
    if command == 'Retire':
        break
    area = command
    area_points = int(input())
    if area == 'Single' and points - area_points >= 0:
        points -= area_points
    elif area == 'Double' and points - 2 * area_points >= 0:
        points -= 2 * area_points
    elif area == 'Triple' and points - 3 * area_points >= 0:
        points -= 3 * area_points
    else:
        a_bad_shot = True
        bad_shots_counter += 1
        continue
    good_shots_counter += 1

if command == 'Retire':
    print(f'{name_of_the_player} retired after {bad_shots_counter} unsuccessful shots.')
else:
    print(f'{name_of_the_player} won the leg with {good_shots_counter} shots.')