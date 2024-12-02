import math

hour = int(input())
minutes = int(input())
hour_is_real = False
minute_is_real = False

if 0 <= hour <= 23:
    hour_is_real = True
if 0 <= minutes <= 59:
    minute_is_real = True
if hour_is_real and minute_is_real:
    hour_in_future = math.floor(hour + (minutes/60) + 0.25)
    minutes_in_future = (hour * 60 + minutes + 15) % 60
    if hour_in_future > 23:
        hour_in_future = 0
    if minutes_in_future > 59:
        minutes_in_future = 0
    if minutes_in_future <10:
        print(f"{hour_in_future}:0{minutes_in_future}")
    else:
        print(f"{hour_in_future}:{minutes_in_future}")