hour = float(input())
day = input()
workdays = 'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday'
if day in workdays and 10 <= hour <= 18:
    print('open')
else:
    print('closed')