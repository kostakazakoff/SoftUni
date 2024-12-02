field = []
bunny_position = []
best_path = []
best_direction = None
max_collected_eggs = 0
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

size = int(input())

for row in range(size):
    line = input().split()

    if 'B' in line:
        bunny_position = [row, line.index('B')]

    field.append(line)

for direction, position in directions.items():
    row, col = [
        bunny_position[0] + position[0],
        bunny_position[1] + position[1]
    ]

    path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:
        if field[row][col] == 'X':
            break

        collected_eggs += int(field[row][col])
        path.append([row, col])

        row += position[0]
        col += position[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_path = path
        best_direction = direction

print(best_direction)
[print(coordinates) for coordinates in best_path]
print(max_collected_eggs)