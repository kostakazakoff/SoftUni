day = input()
work_week = 'Monday, Tuesday, Wednesday, Thursday, Friday'
weekend = 'Saturday, Sunday'
if day in work_week:
    print('Working day')
elif day in weekend:
    print('Weekend')
else:
    print('Error')