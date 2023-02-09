time = int(input())
number_of_scenes = int(input())
time_for_scene = int(input())

time *= 0.85
time -= number_of_scenes * time_for_scene

if time < 0:
    print(f'Time is up! To complete the movie you need {abs(round(time))} minutes.')
else:
    print(f'You managed to finish the movie on time! You have {round(time)} minutes left!')