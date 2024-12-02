price = float(input())
season = input()
car_class = ''
car = ''
if price > 500:
    car_class = 'Luxury class'
    car = 'Jeep'
    price *= 0.9
elif price > 100:
    car_class = 'Compact class'
    if season == 'Summer':
        car = 'Cabrio'
        price *= 0.45
    elif season == 'Winter':
        car = 'Jeep'
        price *= 0.8
else:
    car_class = 'Economy class'
    if season == 'Summer':
        car = 'Cabrio'
        price *= 0.35
    elif season == 'Winter':
        car = 'Jeep'
        price *= 0.65
print(car_class)
print(f'{car} - {price:.2f}')