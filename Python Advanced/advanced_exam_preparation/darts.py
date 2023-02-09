def player_wins():
    if type(cell) == int:
        player['points'] -= cell

    else:
        sum_of_numbers = pad[r][0] + pad[r][-1] + pad[0][c] + pad[-1][c]
        if cell == "B": player['points'] = 0
        elif cell == "D": player['points'] -= sum_of_numbers * 2
        elif cell == "T": player['points'] -= sum_of_numbers * 3

    if player['points'] <= 0: return True


names = input().split(', ')
players = [{'name': names[0], 'points': 501, 'throws': 0}, {'name': names[1], 'points': 501, 'throws': 0}]
pad = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(7)]

while True:
    r, c = [int(x) for x in eval(input())]
    player = players[0]
    player['throws'] += 1
    
    if not all((0 <= r < 7, 0 <= c < 7)):
        players[0], players[1] = players[1], players[0]
        continue
    
    cell = pad[r][c]

    if player_wins():
        print(f"{player['name']} won the game with {player['throws']} throws!")
        break

    players[0], players[1] = players[1], players[0]