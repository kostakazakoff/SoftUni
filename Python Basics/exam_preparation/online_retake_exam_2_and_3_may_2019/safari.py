budget = float(input())
fuel_l = float(input())
day = input()
fuel_price = fuel_l * 2.1
total = fuel_price + 100
if day == 'Saturday':
    total *= 0.9
else:
    total *= 0.8
diff = abs(budget - total)
if total <= budget:
    print(f'Safari time! Money left: {diff:.2f} lv. ')
else:
    print(f'Not enough money! Money needed: {diff:.2f} lv.')