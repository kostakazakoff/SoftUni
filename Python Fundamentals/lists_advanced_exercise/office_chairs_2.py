number_of_rooms = int(input())
chairs = []

# creating a list of the rooms with chairs:
for room in range(number_of_rooms):
    chairs.append(list(input().split()))

# creating lists of available and needed chairs in rooms:
available = [len(chairs[x][0]) for x in range(len(chairs))]
needed = [int(chairs[x][1]) for x in range(len(chairs))]

# creating a list of chair differences (positive - chairs left, negative - chairs not enough):
difference = list(map(lambda x, y: x - y, available, needed))

# check if they are the not_enough chairs in any of the rooms (negative values):
not_enough = len(list(filter(lambda x: x < 0, difference))) > 0

# printing the result (if there are missing chairs in the rooms):
if not_enough:
    for i in range(len(difference)):
        if difference[i] < 0: print(f'{abs(difference[i])} more chairs needed in room {i + 1}')

# printing the result if the chairs are enough:
else:
    print(f'Game On, {sum(difference)} free chairs left')
