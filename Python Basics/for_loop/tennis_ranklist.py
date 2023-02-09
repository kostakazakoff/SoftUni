number_of_tournaments = int(input())
points = int(input())
t_points = 0
w_count = 0

for i in range(number_of_tournaments):
    stage_reached = input()
    if stage_reached == 'W':
        t_points += 2000
        w_count += 1
    elif stage_reached == 'F':
        t_points += 1200
    elif stage_reached == 'SF':
        t_points += 720
points += t_points
average_points = t_points // number_of_tournaments
percent_of_wins = w_count * 100 / number_of_tournaments

print(f'Final points: {points}')
print(f'Average points: {average_points}')
print(f'{percent_of_wins:.2f}%')