annual_tax = int(input())
shoes_price = annual_tax * 0.6
equip_price = shoes_price * 0.8
ball_price = equip_price * 0.25
accessories_price = ball_price * 0.2
total = annual_tax + shoes_price + equip_price + ball_price + accessories_price
print(f'{total:.2f}')