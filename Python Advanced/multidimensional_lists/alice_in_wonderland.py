size = int(input())
matrix = []
alice_position = []
tea_bags = 0
rabbit_hole = None
moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
end_conditions = (
    tea_bags == 10,
    rabbit_hole,
)

for row in range(size):
    line = list(input().split())
    matrix.append(line)

    if 'A' in line:
        alice_position = [row, line.index('A')]
        matrix[row][line.index('A')] = '*'

direction = input()
while True:

    alice_position = [
        alice_position[0] + moves[direction][0],
        alice_position[1] + moves[direction][1]
    ]
    y, x = alice_position[0], alice_position[1]

    if y < 0 or y >= size or x < 0 or x >= size:
        break

    if matrix[y][x] == 'R':
        matrix[y][x] = '*'
        break

    if matrix[y][x].isdigit():
        tea_bags += int(matrix[y][x])
        matrix[y][x] = '*'
        if tea_bags >= 10:
            break

    matrix[y][x] = '*'

    direction = input()

if tea_bags >= 10:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]