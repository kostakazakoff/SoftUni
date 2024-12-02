hollydays = int(input())
workdays = 365 - hollydays

hollydays_playtime = hollydays * 127
workdays_playtime = workdays * 63
total_playtime_min = hollydays_playtime + workdays_playtime
difference_min = abs(total_playtime_min - 30000)
h = difference_min // 60
m = abs(difference_min % 60)

if total_playtime_min > 30000:
    print('Tom will run away')
    print(f'{h} hours and {m} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{h} hours and {m} minutes less for play')