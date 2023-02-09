number = float(input())

if number == 0:
    print('zero')
elif abs(number) < 1:
    print('small', end = ' ')
elif abs(number) > 1000000:
    print('large', end=' ')

if number > 0:
    print('positive')
elif number < 0:
    print('negative')
