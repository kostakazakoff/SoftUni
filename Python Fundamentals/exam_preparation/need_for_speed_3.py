def drive(the_car: str, the_distance: int, the_fuel: int):
    if cars[the_car][FUEL] < the_fuel:
        print('Not enough fuel to make that ride')
        return
    cars[the_car][MILEAGE] += the_distance
    cars[the_car][FUEL] -= the_fuel
    print(f'{the_car} driven for {the_distance} kilometers. {the_fuel} liters of fuel consumed.')
    if cars[the_car][MILEAGE] >= 100000:
        print(f'Time to sell the {the_car}!')
        del cars[the_car]


def refuel(the_car: str, the_fuel: int):
    current_fuel = cars[the_car][FUEL]
    cars[the_car][FUEL] += the_fuel
    if cars[the_car][FUEL] > 75:
        cars[the_car][FUEL] = 75
        the_fuel = 75 - current_fuel
    print(f'{the_car} refueled with {the_fuel} liters')


def revert(the_car: str, the_kilometers: int):
    cars[the_car][MILEAGE] -= the_kilometers
    if cars[the_car][MILEAGE] >= 10000:
        print(f'{the_car} mileage decreased by {the_kilometers} kilometers')
        return
    cars[the_car][MILEAGE] = 10000


cars_count = int(input())
cars = {}
MILEAGE = 'Mileage'
FUEL = 'Fuel'

for _ in range(cars_count):
    car, *car_info = input().split('|')
    car_info = [int(value) for value in car_info]
    cars.update({car: {MILEAGE: car_info[0], FUEL: car_info[1]}})

command = input()

while command != 'Stop':
    action, car, *info = command.split(' : ')
    info = [int(value) for value in info]

    if action == 'Drive':
        distance, fuel = info
        drive(car, distance, fuel)

    elif action == 'Refuel':
        fuel = info[0]
        refuel(car, fuel)

    elif action == 'Revert':
        kilometers = info[0]
        revert(car, kilometers)

    command = input()

[print(f"{car} -> Mileage: {str(value[MILEAGE])} kms, Fuel in the tank: {str(value[FUEL])} lt.") for car, value in cars.items()]
