tournaments_number = int(input())
start_points = int(input())
points = 0
final_points = 0
total_points = 0
wins_counter = 0
for i in range(tournaments_number):
    stage = input()
    if stage == 'W':
        points += 2000
        wins_counter += 1
    elif stage == 'F':
        points += 1200
    elif stage == 'SF':
        points += 720
    final_points += points
    total_points = final_points + start_points
    points = 0
average_points = final_points // tournaments_number
percent_of_wins = wins_counter / tournaments_number * 100
print(f'Final points: {total_points}')
print(f'Average points: {average_points}')
print(f'{percent_of_wins:.2f}%')