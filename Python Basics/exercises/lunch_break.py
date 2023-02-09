import math

movie = input()
movie_lenght = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4
time_left = break_time - lunch_time - rest_time
time_left_after_movie = abs(time_left - movie_lenght)
time_left_after_movie = math.ceil(time_left_after_movie)

if time_left >= movie_lenght:
    print(f"You have enough time to watch {movie} and left with {time_left_after_movie} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie}, you need {time_left_after_movie} more minutes.")