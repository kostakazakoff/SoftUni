capacity = int(input())
they_are_no_places = False
movie_time = False
profit = 0
discount = 0
command = input()

while not movie_time and not they_are_no_places:
    discount = 0
    visitors = int(command)
    capacity -= visitors
    #===========================================
    if capacity <= 0:
        visitors += capacity
        they_are_no_places = True
    #===========================================
    if visitors % 3 == 0 and visitors != 0:
        discount = 5
    profit += visitors * 5 - discount
    if capacity < 0:
        break
    command = input()
    if command == 'Movie time!':
        movie_time = True

if movie_time:
    print(f'There are {capacity} seats left in the cinema.')
else:
    print('The cinema is full.')
print(f'Cinema income - {profit} lv.')