product = input()
town = input()
quantity = float(input())
price = 0

if town == 'Sofia':
    if product == 'coffee':
        price = 0.50
    if product == 'water':
        price = 0.80
    if product == 'beer':
        price = 1.20
    if product == 'sweets':
        price = 1.45
    if product == 'peanuts':
        price = 1.60
elif town == 'Plovdiv':
    if product == 'coffee':
        price = 0.40
    if product == 'water':
        price = 0.70
    if product == 'beer':
        price = 1.15
    if product == 'sweets':
        price = 1.30
    if product == 'peanuts':
        price = 1.50
elif town == 'Varna':
    if product == 'coffee':
        price = 0.45
    if product == 'water':
        price = 0.70
    if product == 'beer':
        price = 1.10
    if product == 'sweets':
        price = 1.35
    if product == 'peanuts':
        price = 1.55

price *= quantity
print(price)