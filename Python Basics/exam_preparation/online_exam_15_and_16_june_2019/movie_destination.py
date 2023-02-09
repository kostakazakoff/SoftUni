budget = float(input())
destination = input()
season = input()
days = int(input())
price = 0

if destination == 'Dubai':
    if season == 'Winter':
        price = 45000
    elif season == 'Summer':
        price = 40000
    price *= 0.7
elif destination == 'Sofia':
    if season == 'Winter':
        price = 17000
    elif season == 'Summer':
        price = 12500
    price *= 1.25
elif destination == 'London':
    if season == 'Winter':
        price = 24000
    elif season == 'Summer':
        price = 20250
budget -= days * price

if budget < 0:
    print(f'The director needs {abs(budget):.2f} leva more!')
else:
    print(f'The budget for the movie is enough! We have {budget:.2f} leva left!')