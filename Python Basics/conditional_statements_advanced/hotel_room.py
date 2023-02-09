month = input() #May, June, July, August, September или October
days = int(input())
price = 0
#Apartment:
if month == 'May' or month == 'October':
    price = 65
elif month == 'June' or month == 'September':
    price = 68.7
else:
    price = 77
if days > 14:
    price *= 0.9 * days
else:
    price *= days
print(f'Apartment: {price:.2f} lv.')

#Studio:
if month == 'May' or month == 'October':
    price = 50
    if days > 14:
        price *= 0.7
    elif days > 7:
        price *= 0.95
elif month == 'June' or month == 'September':
    price = 75.2
    if days > 14:
        price *= 0.8
else:
    price = 76
price *= days
print(f'Studio: {price:.2f} lv.')