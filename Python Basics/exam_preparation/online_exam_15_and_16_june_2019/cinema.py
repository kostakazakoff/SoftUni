capacity = int(input())
profit = 0
discount = 0
command = input()

while command != 'Movie time!':
    discount = 0
    visitors = int(command)
    capacity -= visitors
    if capacity < 0:
        break
    if visitors % 3 == 0 and visitors != 0:
        discount = 5
    profit += visitors * 5 - discount
    command = input()

if command == 'Movie time!':
    print(f'There are {capacity} seats left in the cinema.')
else:
    print('The cinema is full.')
print(f'Cinema income - {profit} lv.')