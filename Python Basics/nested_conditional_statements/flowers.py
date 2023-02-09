hrizantemi = int(input())
rozi = int(input())
laleta = int(input())
season = input()
hollyday = input()
discount = 0

all_flowers = hrizantemi + rozi + laleta
price_hrizantemi = 2
price_rozi = 4.1
price_laleta = 2.5
if season == 'Autumn' or season == 'Winter':
    price_hrizantemi = 3.75
    price_rozi = 4.50
    price_laleta = 4.15
price = price_rozi * rozi + price_laleta * laleta + price_hrizantemi * hrizantemi

if hollyday == 'Y':
    price += price * 0.15
if laleta > 7 and season == 'Spring':
    price -= price * 0.05
if rozi >= 10 and season == 'Winter':
    price -= price * 0.1
if all_flowers > 20:
    price -= price * 0.2
price += 2

print(f'{price:.2f}')
