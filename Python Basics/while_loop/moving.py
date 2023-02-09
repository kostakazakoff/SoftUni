width = int(input())
lenght = int(input())
heigh = int(input())
command = input()
volume_of_the_room = width * lenght * heigh
no_more_place = False
while command != 'Done':
    number_of_boxes = int(command)
    volume_of_the_room -= number_of_boxes
    if volume_of_the_room <= 0:
        no_more_place = True
        break
    command = input()
if no_more_place:
    print(f'No more free space! You need {abs(volume_of_the_room)} Cubic meters more.')
if command == 'Done' and volume_of_the_room > 0:
    print(f'{volume_of_the_room} Cubic meters left.')