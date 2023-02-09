days = int(input())
room = input()
appraisement = input()
nights = days - 1
price = 0

if room == 'apartment':
    if days < 10:
        price = 0.7 * 25
    elif days <= 15:
        price = 0.65 * 25
    else:
        price = 0.5 * 25
elif room == 'president apartment':
    if days < 10:
        price = 0.9 * 35
    elif days <= 15:
        price = 0.85 * 35
    else:
        price = 0.8 * 35
elif room == 'room for one person':
    price = 18
if appraisement == 'positive':
    price *= 1.25
else:
    price *= 0.9
price *= nights
print(f'{price:.2f}')



