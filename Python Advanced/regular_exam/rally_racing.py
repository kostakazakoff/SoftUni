def step_to(d: str):
    global matrix, r, c
    if d == 'up': r -= 1
    elif d == 'down': r += 1
    elif d == 'left': c -= 1
    elif d == 'right': c += 1


def in_tunnel():
    global r, c, matrix, tunnels, km
    pos = [r, c]
    if pos in tunnels:
        matrix[r][c] = '.'
        tunnels = [x for x in tunnels if x != pos]
        r, c = tunnels[0]
        matrix[r][c] = '.'
        km += 30


SIZE = int(input())
racing_number = input()
matrix = []
tunnels = []
r, c = 0, 0
km = 0
disqualified = False

for row in range(SIZE):
    line = input().split()
    if 'T' in line:
        tunnels.append([row, line.index('T')])
    matrix.append(line)

while True:
    direction = input()
    if direction == 'End':
        disqualified = True
        break

    step_to(direction)
    cell = matrix[r][c]

    if cell == 'F':
        km += 10
        break

    if cell == 'T':
        in_tunnel()
        continue

    km += 10

matrix[r][c] = 'C'
if not disqualified: print(f"Racing car {racing_number} finished the stage!")
else: print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {km} km.")
[print(''.join(x)) for x in matrix]