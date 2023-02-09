def move_to(d: str):
    global r, c
    if d == 'up': r -= 1
    elif d == 'down': r += 1
    elif d == 'left': c -= 1
    elif d == 'right': c += 1


def in_burrows():
    global r, c, matrix, burrows
    pos = (r, c)
    if pos in burrows:
        matrix[r][c] = '.'
        burrows = [x for x in burrows if x != pos]
        r, c = burrows[0]
        matrix[r][c] = '.'
        return True
    

SIZE = int(input())
matrix = []
burrows = []
food_eaten = 0
out_of_field = False

for row in range(SIZE):
    line = list(input())
    if 'S' in line:
        r, c = row, line.index('S')
        line[c] = '.'
    if 'B' in line: burrows.append((row, line.index('B')))
    matrix.append(line)

while food_eaten < 10:
    direction = input()
    move_to(direction)
    if not all((0 <= r < SIZE, 0 <= c < SIZE)):
        out_of_field = True
        break
    
    if in_burrows(): continue

    if matrix[r][c] == '*':
        food_eaten += 1
    
    matrix[r][c] = '.'

else:
    print("You won! You fed the snake.")
    matrix[r][c] = 'S'

if out_of_field: print("Game over!")

print(f"Food eaten: {food_eaten}")
[print(''.join(row)) for row in matrix]
