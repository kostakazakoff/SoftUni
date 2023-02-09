def in_field(y, x):
    if 0 <= y < 5 and 0 <= x < 5:
        return True
    return False


def shoot():
    global directions, targets_hit_positions, targets_hit_count, field
    y, x = my_position
    direction = parameters[0]
    while True:
        y, x = y + directions[direction][0], x + directions[direction][1]
        if not in_field(y, x):
            break
        if field[y][x] == 'x':
            targets_hit_positions.append([y, x])
            targets_hit_count += 1
            field[y][x] = '.'
            break


def move():
    global directions, my_position, field
    direction, distance = parameters[0], int(parameters[1])
    for _ in range(distance):
        target_y = my_position[0] + directions[direction][0]
        target_x = my_position[1] + directions[direction][1]
        if in_field(target_y, target_x) and field[target_y][target_x] == '.':
            my_position = [target_y, target_x]
        else:
            return


field = []
my_position = []
all_targets_count = 0
targets_hit_positions = []
targets_hit_count = 0
directions = {
    'right': (0, 1),
    'left': (0, -1),
    'up': (-1, 0),
    'down': (1, 0)
    }

# Enter matrix and find elements in there:---------
for row in range(5):
    blocks = input().split()
    field.append(blocks)

    if 'A' in blocks:
        my_position = [row, blocks.index('A')]
        field[row][blocks.index('A')] = '.'
    if 'x' in blocks:
        all_targets_count += blocks.count('x')

# -------------------------------------------------

# Act with commands -------------------------------
commands_count = int(input())

for _ in range(commands_count):

    action, *parameters = input().split()

    if action == 'shoot':
        shoot()
    else:
        move()

# -------------------------------------------------

# Print results
if targets_hit_count == all_targets_count:
    print(f"Training completed! All {targets_hit_count} targets hit.")
else:
    print(f"Training not completed! {all_targets_count - targets_hit_count} targets left.")

[print(coordinates) for coordinates in targets_hit_positions]
