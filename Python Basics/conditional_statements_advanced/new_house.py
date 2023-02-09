flowers_type = input()
quantity = int(input())
budget = int(input())
price = 0
if flowers_type == 'Roses':
    price = 5
    if quantity > 80: price *= 0.9
elif flowers_type == 'Dahlias':
    price = 3.8
    if quantity > 90: price *= 0.85
elif flowers_type == 'Tulips':
    price = 2.80
    if quantity > 80: price *= 0.85
elif flowers_type == 'Narcissus':
    price = 3
    if quantity < 120: price *= 1.15
elif flowers_type == 'Gladiolus':
    price = 2.5
    if quantity < 80: price *= 1.2
price = price * quantity
difference = abs (budget - price)
if budget >= price:
    print(f'Hey, you have a great garden with {quantity} {flowers_type} and {difference:.2f} leva left.')
else:
    print(f'Not enough money, you need {difference:.2f} leva more.')