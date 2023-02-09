def valid(price: float):
    if price < 0:
        print('Invalid price!')
        return False
    elif price == 0:
        print('Invalid order!')
        return False
    return True


price_without_taxes = 0

command = input()
while command != 'special' and command != 'regular':
    part_price = float(command)
    if not valid(part_price):
        command = input()
        continue
    price_without_taxes += part_price
    command = input()

if not valid(price_without_taxes):
    exit()

price_with_taxes = price_without_taxes * 1.2
taxes = price_without_taxes * 0.2

if command == 'special':
    price_with_taxes = price_with_taxes * 0.9

print("Congratulations you've just bought a new computer!")
print(f'Price without taxes: {price_without_taxes:.2f}$')
print(f'Taxes: {taxes:.2f}$')
print('-----------')
print(f'Total price: {price_with_taxes:.2f}$')
