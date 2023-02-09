drink_type = input()
sugar_choice = input()
number_of_drinks = int(input())
price = 0
if drink_type == 'Espresso':
    if sugar_choice == 'Without':
        price = 0.9 * 0.65
    elif sugar_choice == 'Normal':
        price = 1
    elif sugar_choice == 'Extra':
        price = 1.2
    if number_of_drinks >= 5:
        price *= 0.75
elif drink_type == 'Cappuccino':
    if sugar_choice == 'Without':
        price = 0.65
    elif sugar_choice == 'Normal':
        price = 1.2
    elif sugar_choice == 'Extra':
        price = 1.6
elif drink_type == 'Tea':
    if sugar_choice == 'Without':
        price = 0.5 * 0.65
    elif sugar_choice == 'Normal':
        price = 0.6
    elif sugar_choice == 'Extra':
        price = 0.7
price *= number_of_drinks
if price > 15:
    price *= 0.8
print(f'You bought {number_of_drinks} cups of {drink_type} for {price:.2f} lv.')