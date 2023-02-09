def valid_coordinates():
    global matrix, matrix_rows, matrix_row_length, row, col
    if row < 0 or row >= matrix_rows:
        return False
    if col < 0 or col >= matrix_row_length:
        return False
    return True


matrix_rows = int(input())
matrix = []

[matrix.append([int(x) for x in input().split()]) for _ in range(matrix_rows)]
matrix_row_length = len(matrix[0])

command = input()
while not command.startswith('END'):
    action = command.split()[0]
    row, col, value = [int(x) for x in command.split()[1::]]

    if not valid_coordinates():
        print("Invalid coordinates")
        command = input()
        continue

    if action == 'Add':
        matrix[row][col] += value

    elif action == 'Subtract':
        matrix[row][col] -= value

    command = input()

[print(*row) for row in matrix]
