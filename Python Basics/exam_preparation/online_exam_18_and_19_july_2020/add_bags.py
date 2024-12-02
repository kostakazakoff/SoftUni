price = float(input())
weight = float(input())
days_to_trip = int(input())
bags = int(input())
if weight < 10:
    price = price * 0.2
elif weight <= 20:
    price = price * 0.5
if days_to_trip > 30:
    price *= 1.1
elif days_to_trip >= 7:
    price *= 1.15
else:
    price *= 1.4
price = bags * price
print(f'The total price of bags is: {price:.2f} lv.')