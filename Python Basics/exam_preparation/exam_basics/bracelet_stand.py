saved_per_day = float(input())
profit_per_day = float(input())
total_expenses = float(input())
gift_price = float(input())
total_money = profit_per_day * 5 + saved_per_day * 5
total_profit = total_money - total_expenses
diff = gift_price - total_profit
if total_profit >= gift_price:
    print(f'Profit: {total_profit:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {diff:.2f} BGN.')