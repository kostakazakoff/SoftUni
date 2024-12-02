price = float(input())
season = input()
place = ''
location = ''
if price > 3000:
    place = 'Hotel'
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'
    price *= 0.9
elif price > 1000:
    place = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price *= 0.8
    elif season == 'Winter':
        location = 'Morocco'
        price *= 0.6
else:
    place = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price *= 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price *= 0.45

print(f'{location} - {place} - {price:.2f}')