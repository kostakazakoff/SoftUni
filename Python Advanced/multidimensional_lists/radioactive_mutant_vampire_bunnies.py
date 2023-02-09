def in_field(r, c):
    global rows, cols
    if 0 <= r < rows and 0 <= c < cols:
        return True
    return False


def locate_positions():
    global field, player_pos, bunny_positions
    for r in range(rows):
        for c in range(cols):
            if field[r][c] == 'P':
                player_pos = [r, c]
                field[r][c] = '.'
            if field[r][c] == 'B':
                bunny_positions.append([r, c])


def bunny_spreads():
    global bunny_positions, new_bunny_positions, field
    for pos in bunny_positions:
        for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            target_r, target_c = pos[0] + direction[0], pos[1] + direction[1]
            if in_field(target_r, target_c):
                field[target_r][target_c] = 'B'
                new_bunny_positions.append([target_r, target_c])


def step_to(to: str):
    global rows, cols, player_escape, player_pos
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    target_r, target_c = player_pos[0] + directions[to][0], player_pos[1] + directions[to][1]
    if not in_field(target_r, target_c):
        player_escape = True
        return
    player_pos = [target_r, target_c]


rows, cols = tuple(map(int, input().split()))
field = [list(input()) for _ in range(rows)]
commands = list(input())
bunny_positions = []
new_bunny_positions = []
player_pos = []
player_escape = False


for direction in commands:
    locate_positions()
    bunny_spreads()
    step_to(direction)
    if player_escape:
        break
    elif field[player_pos[0]][player_pos[1]] == 'B':
        break

[print(''.join(r)) for r in field]

if player_escape:
    print(f"won: {player_pos[0]} {player_pos[1]}")
else:
    print(f"dead: {player_pos[0]} {player_pos[1]}")
