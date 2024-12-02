days = int(input())
room = input()
review = input()
nights = days - 1
price = 0

if room == 'room for one person':
    price = 18
elif room == 'apartment':
    price = 25
    if days < 10:
        price *= 0.7
    elif days < 15:
        price *= 0.65
    else:
        price *= 0.50
else:
    price = 35
    if days < 10:
        price *= 0.9
    elif days < 15:
        price *= 0.85
    else:
        price *= 0.80
if review == 'positive':
    price *= 1.25
else:
    price *= 0.9
price *= nights
print(f'{price:.2f}')