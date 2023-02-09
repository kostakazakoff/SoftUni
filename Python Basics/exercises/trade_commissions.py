town = input()
sales = float(input())
town_is_in_list = True
they_are_sales = True
commission = 0
if town == 'Sofia':
    if sales > 10000:
        commission = 12
    elif sales > 1000:
        commission = 8
    elif sales > 500:
        commission = 7
    elif sales >= 0:
        commission = 5
    else:
        they_are_sales = False
elif town == 'Varna':
    if sales > 10000:
        commission = 13
    elif sales > 1000:
        commission = 10
    elif sales > 500:
        commission = 7.5
    elif sales >= 0:
        commission = 4.5
    else:
        they_are_sales = False
elif town == 'Plovdiv':
    if sales > 10000:
        commission = 14.5
    elif sales > 1000:
        commission = 12
    elif sales > 500:
        commission = 8
    elif sales >= 0:
        commission = 5.5
    else:
        they_are_sales = False
else:
    town_is_in_list = False
if they_are_sales and town_is_in_list:
    commission *= sales/100
    print(f'{commission:.2f}')
else:
    print('error')