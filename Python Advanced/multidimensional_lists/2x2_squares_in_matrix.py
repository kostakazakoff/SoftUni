def valid_position(r, c):
    if 0 <= r < rows and 0 <= c < cols:
        return True
    return False


def check_square_equals(r, c):
    global equals_counter, matrix
    current_symbol = matrix[r][c]
    for direction in ((0, 1), (1, 0), (1, 1)):
        y, x = r, c
        y, x = y + direction[0], x + direction[1]
        if not valid_position(y, x) or current_symbol != matrix[y][x]:
            return
    equals_counter += 1


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)] # jagged matrix?
equals_counter = 0

for row in range(rows):
    for col in range(cols):
        check_square_equals(row, col)

print(equals_counter)
