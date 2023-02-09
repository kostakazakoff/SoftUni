fuel = input()
liters = float(input())
card = input()
price = 0

if card == 'Yes':
    if fuel == 'Gas':
        price = 0.85
    elif fuel == 'Diesel':
        price = 2.21
    elif fuel == 'Gasoline':
        price = 2.04
if card == 'No':
    if fuel == 'Gas':
        price = 0.93
    elif fuel == 'Diesel':
        price = 2.33
    elif fuel == 'Gasoline':
        price = 2.22
if liters > 25:
    price -= price * 0.1
elif liters > 20:
    price -= price * 0.08
payment = liters * price
print(f'{payment:.2f} lv.')