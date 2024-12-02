import math

time_first = int(input())
time_second = int(input())
time_third = int(input())

summary_time = time_third + time_second + time_first
minutes = summary_time / 60
seconds = summary_time % 60
minutes = math.floor(minutes)

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")