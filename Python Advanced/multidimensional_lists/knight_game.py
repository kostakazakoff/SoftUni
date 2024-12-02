def knight_moves():
    global knight_attacks, row, col, gamepad_size, gamepad
    for move in valid_moves:
        r = row + move[0]
        c = col + move[1]
        if r < 0 or r >= gamepad_size or c < 0 or c >= gamepad_size:
            continue
        if gamepad[r][c] == 'K':
            knight_attacks += 1


gamepad_size = int(input())
gamepad = []
[gamepad.append(list(input())) for _ in range(gamepad_size)]

valid_moves = (
    (-2, 1),
    (-2, -1),
    (-1, 2),
    (-1, -2),
    (1, 2),
    (1, -2),
    (2, 1),
    (2, -1)
)

removed_knights = 0

while True:
    max_dangerous_knight = []
    max_attacks = 0

    for row in range(gamepad_size):
        for col in range(gamepad_size):
            knight_attacks = 0
            if gamepad[row][col] == 'K':
                knight_moves()
            if not knight_attacks:
                continue
            if knight_attacks > max_attacks:
                max_attacks = knight_attacks
                max_dangerous_knight = [row, col]

    if max_dangerous_knight:
        knight_row = max_dangerous_knight[0]
        knight_col = max_dangerous_knight[1]
        gamepad[knight_row][knight_col] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)