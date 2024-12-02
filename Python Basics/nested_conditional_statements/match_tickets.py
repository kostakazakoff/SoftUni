budget = float(input())
category = input()
fans = int(input())
tickets_price = 0
if fans > 50:
    transport_expences = 0.25
elif fans > 24:
    transport_expences = 0.4
elif fans > 9:
    transport_expences = 0.5
elif fans > 4:
    transport_expences = 0.6
else:
    transport_expences = 0.75
transport_expences *= budget

if category == 'VIP':
    tickets_price = fans * 499.99
elif category == 'Normal':
    tickets_price = fans * 249.99

money_left = abs(budget - transport_expences - tickets_price)
if tickets_price <= budget - transport_expences:
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    print(f'Not enough money! You need {money_left:.2f} leva.')
