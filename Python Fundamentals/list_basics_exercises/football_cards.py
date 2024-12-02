cards = input().split()
team_a_players = 11
team_b_players = 11
players_off = []
game_is_terminated = False

for red_card in cards:
    players_off.append(red_card)
    if players_off.count(red_card) > 1:
        players_off.pop()
        continue
    if 'A' in red_card:
        team_a_players -= 1
    elif 'B' in red_card:
        team_b_players -= 1
    if team_a_players < 7 or team_b_players < 7:
        game_is_terminated = True
        break

print(f'Team A - {team_a_players}; Team B - {team_b_players}')
if game_is_terminated:
    print('Game was terminated')
