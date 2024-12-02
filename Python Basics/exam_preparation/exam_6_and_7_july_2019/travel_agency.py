destination = input()
package_type = input()
vip_card = input()
days_of_vacation = int(input())
price = 0
invalid_input = False

if destination == 'Bansko' or destination == 'Borovets':
    if package_type == 'withEquipment':
        price = 100
        if vip_card == 'yes':
            price *= 0.9
    elif package_type == 'noEquipment':
        price = 80
        if vip_card == 'yes':
            price *= 0.95
    else:
        invalid_input = True
elif destination == 'Varna' or destination == 'Burgas':
    if package_type == 'withBreakfast':
        price = 130
        if vip_card == 'yes':
            price *= 0.88
    elif package_type == 'noBreakfast':
        price = 100
        if vip_card == 'yes':
            price *= 0.93
    else:
        invalid_input = True
else:
    invalid_input = True

if days_of_vacation > 7:
    days_of_vacation -= 1
price *= days_of_vacation
if invalid_input:
    print('Invalid input!')
elif days_of_vacation < 1:
    print('Days must be positive number!')
else:
    print(f'The price is {price:.2f}lv! Have a nice time!')



