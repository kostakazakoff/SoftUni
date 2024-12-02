name_of_the_team = input()
matches_in_a_season = int(input())
result = ''
points = 0
count_w = 0
count_d = 0
count_l = 0
percent_of_wins = 0

if matches_in_a_season > 0:
    for i in range(1, matches_in_a_season + 1):
        result = input()
        if result == 'W':
            points += 3
            count_w += 1
        elif result == 'D':
            points += 1
            count_d += 1
        elif result == 'L':
            count_l += 1
    percent_of_wins = count_w * 100 / matches_in_a_season

if matches_in_a_season == 0:
    print(f"{name_of_the_team} hasn't played any games during this season.")
else:
    print(f'{name_of_the_team} has won {points} points during this season.')
    print('Total stats:')
    print(f'## W: {count_w}')
    print(f'## D: {count_d}')
    print(f'## L: {count_l}')
    print(f'Win rate: {percent_of_wins:.2f}%')