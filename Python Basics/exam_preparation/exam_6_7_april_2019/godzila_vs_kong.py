budget = float(input())
walk_on_number = int(input())
walk_on_dress_price = float(input())
decor_price = budget * 0.1
if walk_on_number > 150:
    walk_on_dress_price *= 0.9
total_expenses = walk_on_dress_price * walk_on_number + decor_price
diff = abs(total_expenses - budget)
if total_expenses > budget:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')