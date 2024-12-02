budget = float(input())
season = input()
destination = ''
place = ''
price = 0
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place = 'Camp'
        price = budget * 0.3
    else:
        price = budget * 0.7
        place = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        price = budget * 0.4
    else:
        price = budget * 0.8
        place = 'Hotel'
else:
    destination = 'Europe'
    place = 'Hotel'
    price = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{place} - {price:.2f}')