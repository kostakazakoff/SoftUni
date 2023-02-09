hour_for_exam = int(input())
min_for_exam = int(input())
hour_for_coming = int(input())
min_for_coming = int(input())

min_for_exam += hour_for_exam * 60
min_for_coming += hour_for_coming * 60
difference = abs(min_for_exam - min_for_coming)
difference_h = difference // 60
difference_m = difference % 60

if min_for_coming < min_for_exam - 30:
    print('Early')
elif min_for_coming <= min_for_exam:
    print('On time')
else:
    print('Late')

if min_for_coming <= min_for_exam - 60:
    print(f'{difference_h}:{difference_m:02d} hours before the start')
elif min_for_coming < min_for_exam:
    print(f'{difference_m} minutes before the start')
elif min_for_coming < min_for_exam + 60:
    print(f'{difference_m} minutes after the start')
else:
    print(f'{difference_h}:{difference_m:02d} hours after the start')