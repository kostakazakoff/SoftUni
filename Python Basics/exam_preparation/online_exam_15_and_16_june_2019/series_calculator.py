import math

name_of_the_movie = input()
seasons = int(input())
episodes = int(input())
episode_in_min = int(input())

total_time = math.floor(episode_in_min * 1.2 * episodes + 10) * seasons

print(f'Total time needed to watch the {name_of_the_movie} series is {total_time} minutes.')