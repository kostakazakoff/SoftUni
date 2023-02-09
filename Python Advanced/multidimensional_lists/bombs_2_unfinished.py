size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]
BOMB_COORDINATES = tuple(tuple(int(c) for c in x.split(',')) for x in input().split())
alive_cells = []

for (r, c) in BOMB_COORDINATES:
    power = matrix[r][c]
    matrix[r][c] = 0
    for direction in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
        row, col = r + direction[0], c + direction[1]
        if 0 <= row < size and 0 <= col < size and matrix[row][col] > 0:
            matrix[row][col] -= power

[[alive_cells.append(n) for n in row if n > 0] for row in matrix]

print(f'Alive cells: {len(alive_cells)}')
print(f'Sum: {sum(alive_cells)}')
[print(*row) for row in matrix]
