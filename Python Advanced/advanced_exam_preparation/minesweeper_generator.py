def bombs_arownd(r, c):
    global gamepad
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1))
    bombs_count = 0
    for d in directions:
        target_r, target_c = r + d[0], c + d[1]
        if not all((0 <= target_r < SIZE, 0 <= target_c < SIZE)):
            continue
        if gamepad[target_r][target_c] == '*':
            bombs_count += 1
    return bombs_count


SIZE = int(input())
NUMBER_OF_BOMBS = int(input())
gamepad, bombs_coordinates = [], []
gamepad = [SIZE * [0] for x in range(SIZE)]

for _ in range(NUMBER_OF_BOMBS):
    bombs_coordinates.append([int(x) for x in eval(input())])

for coordinates in bombs_coordinates:
    gamepad[coordinates[0]][coordinates[1]] = '*'

for row in range(SIZE):
    for col in range(SIZE):
        if gamepad[row][col] == '*':
            continue
        gamepad[row][col] = bombs_arownd(row, col)

[print(*x) for x in gamepad]