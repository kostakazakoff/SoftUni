number_of_joinery = int(input())
type_of_joinery = input()
delivery = input()
price = 0

if type_of_joinery == '90X130':
    price = 110
    if number_of_joinery > 60:
        price *= 0.92
    elif number_of_joinery > 30:
        price *= 0.95
elif type_of_joinery == '100X150':
    price = 140
    if number_of_joinery > 80:
        price *= 0.9
    elif number_of_joinery > 40:
        price *= 0.94
elif type_of_joinery == '130X180':
    price = 190
    if number_of_joinery > 50:
        price *= 0.88
    elif number_of_joinery > 20:
        price *= 0.93
elif type_of_joinery == '200X300':
    price = 250
    if number_of_joinery > 50:
        price *= 0.86
    elif number_of_joinery > 25:
        price *= 0.91
price *= number_of_joinery
if delivery == 'With delivery':
    price += 60
if number_of_joinery > 99:
    price *= 0.96

if number_of_joinery < 10:
    print('Invalid order')
else:
    print(f'{price:.2f} BGN')