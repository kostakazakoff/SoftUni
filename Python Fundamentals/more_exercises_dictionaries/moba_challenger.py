def input_type(input_string: str):
    if '->' in input_string:
        return ' -> ', 'Add player'
    elif 'vs' in input_string:
        return ' vs ', 'Duel'


def add_to(players: dict, player: str, position: str, skill: int):
    if player not in players:
        players[player] = {position: skill}
    elif position not in players[player]:
        players[player].update({position: skill})
    if players[player][position] < skill:
        players[player][position] = skill
    return players


def duel(players: dict, players_total_skills: dict, player1: str, player2: str):
    if player1 not in players or player2 not in players:
        return players
    for value in players[player1]:
        if value not in players[player2]:
            continue
        if players_total_skills[player1] < players_total_skills[player2]:
            del players[player1]
            break
        elif players_total_skills[player1] > players_total_skills[player2]:
            del players[player2]
            break
    return players


def total_player_skills(players: dict):
    players_max_skill = {}
    for player, content in players.items():
        players_max_skill[player] = sum(content.values())
    return players_max_skill


def output(players: dict):
    players_max_skill = total_player_skills(players)
    players_max_skill = dict(sorted(players_max_skill.items(), key=lambda x: (-x[1], x[0])))
    for player, content in players_max_skill.items():
        print(f'{player}: {players_max_skill[player]} skill')
        players[player] = dict(sorted(players[player].items(), key=lambda x: (-x[1], x[0])))
        for k, v in players[player].items():
            print(f'- {k} <::> {v}')


moba_players = {}
command = input()
while command != 'Season end':
    separator, action = input_type(command)
    command = command.split(separator)
    moba_player = command[0]
    if action == 'Add player':
        player_position = command[1]
        player_skill = int(command[2])
        moba_players = add_to(moba_players, moba_player, player_position, player_skill)
    elif action == 'Duel':
        moba_player_2 = command[1]
        skills = total_player_skills(moba_players)
        moba_players = duel(moba_players, skills, moba_player, moba_player_2)
    command = input()

output(moba_players)
