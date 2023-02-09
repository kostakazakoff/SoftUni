number_of_lines = int(input())
cars_in_parking = set()

for _ in range(number_of_lines):
    action, plate = input().split(', ')
    if action == 'IN':
        cars_in_parking.add(plate)
    else:
        cars_in_parking.discard(plate)

if cars_in_parking:
    [print(car) for car in cars_in_parking]
else:
    print('Parking Lot is Empty')
