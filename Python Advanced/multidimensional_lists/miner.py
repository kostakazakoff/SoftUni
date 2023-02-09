def step_to(to: str):
    global miner_r, miner_c, size
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    if 0 <= miner_r + directions[to][0] < size and 0 <= miner_c + directions[to][1] < size:
        miner_r, miner_c = miner_r + directions[to][0], miner_c + directions[to][1]


size = int(input())
commands = input().split()
field = []
coal = 0

for row in range(size):
    line = input().split()
    if 's' in line: miner_r, miner_c = row, line.index('s')
    if 'c' in line: coal += line.count('c')
    field.append(line)

for direction in commands:
    step_to(direction)

    if field[miner_r][miner_c] == 'e':
        print(f"Game over! ({miner_r}, {miner_c})")
        break

    elif field[miner_r][miner_c] == 'c':
        coal -= 1

        if not coal:
            print(f"You collected all coal! ({miner_r}, {miner_c})")
            break

    field[miner_r][miner_c] = '*'

else:
    print(f"{coal} pieces of coal left. ({miner_r}, {miner_c})")
