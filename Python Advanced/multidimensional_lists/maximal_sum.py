def valid_position(r, c):
    if 0 <= r + 3 <= rows and 0 <= c + 3 <= cols:
        return True
    return False


def check_square_sum(r, c):
    global max_sum, square_coordinates
    
    if valid_position(r, c):
        square_sum = 0
        for current_row in range(r, r + 3):
            numbers = matrix[current_row][c:c + 3]
            square_sum += sum(numbers)

        if square_sum > max_sum:
            max_sum = square_sum
            square_coordinates = [r, c]
        

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = float('-inf')
square_coordinates = []

for row in range(rows):
    for col in range(cols):
        check_square_sum(row, col)

print(f'Sum = {max_sum}')
for row in range(square_coordinates[0], square_coordinates[0] + 3):
    print(*matrix[row][square_coordinates[1]: square_coordinates[1] + 3])
