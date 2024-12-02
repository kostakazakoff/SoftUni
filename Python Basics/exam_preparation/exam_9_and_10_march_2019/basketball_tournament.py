command = input()
points_diff = 0
game_count = 0
total_ganes_count = 0
games_win = 0
games_lose = 0
while command != 'End of tournaments':
    number_of_games = int(input())
    tournament_name = command
    game_count = 0
    for game in range(number_of_games):
        desi_points = int(input())
        opposer_points = int(input())
        game_count += 1
        total_ganes_count += 1
        points_diff = desi_points - opposer_points
        if points_diff > 0:
            games_win += 1
            print(f'Game {game_count} of tournament {tournament_name}: win with {points_diff} points.')
        else:
            games_lose += 1
            print(f'Game {game_count} of tournament {tournament_name}: lost with {abs(points_diff)} points.')
    command = input()
percent_of_wins = games_win / total_ganes_count * 100
percent_of_lose = games_lose / total_ganes_count * 100
if command == 'End of tournaments':
    print(f'{percent_of_wins:.2f}% matches win')
    print(f'{percent_of_lose:.2f}% matches lost')