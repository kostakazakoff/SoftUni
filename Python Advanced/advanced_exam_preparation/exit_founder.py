SIZE = 6
player = {'name': '', 'turn': True}
players = []
player_names = input().split(', ')
for name in player_names:
    players.append({'name': name, 'turn': True})
maze = [input().split() for _ in range(SIZE)]
win, trap = False, False

while not win and not trap:
    for _ in range(2):
        r, c = [int(n) for n in eval(input())]
        player = players[0]

        if not player['turn']:
            player['turn'] = True
            players[0], players[1] = players[1], players[0]
            continue

        if maze[r][c] == 'E':
            print(f"{player['name']} found the Exit and wins the game!")
            win = True
            break

        elif maze[r][c] == 'T':
            winner = players[1]['name']
            print(f"{player['name']} is out of the game! The winner is {winner}.")
            trap = True
            break

        elif maze[r][c] == 'W':
            print(f'{player["name"]} hits a wall and needs to rest.')
            player['turn'] = False

        players[0], players[1] = players[1], players[0]
