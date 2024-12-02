day = input()

# if day == 'Monday':
#     print('12')
# elif day == 'Tuesday':
#     print('12')
# elif day == 'Wednesday':
#     print('14')
# elif day == 'Thursday':
#     print('14')
# elif day == 'Friday':
#     print('12')
# elif day == 'Saturday':
#     print('16')
# elif day == 'Sunday':
#     print('16')

price_12 = day == 'Monday' or day == 'Tuesday' or day == 'Friday'
price_14 = day == 'Wednesday' or day == 'Thursday'
price_16 = day == 'Saturday' or day == 'Sunday'

if price_16:
    print('16')
elif price_14:
    print('14')
elif price_12:
    print('12')