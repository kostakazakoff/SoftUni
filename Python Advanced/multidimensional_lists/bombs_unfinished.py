def position_is_valid(r, c):
    global size
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def explosion(*args):
    global bombs_coordinates, matrix
    bomb_r, bomb_c = args
    power = matrix[bomb_r][bomb_c][0]
    matrix[bomb_r][bomb_c][0], matrix[bomb_r][bomb_c][1] = 0, False
    for row in range(bomb_r -1, bomb_r + 2):
        for col in range(bomb_c - 1, bomb_c + 2):
            if position_is_valid(row, col):
                if matrix[row][col][1] == True:
                    matrix[row][col][0] -=  power
                if matrix[row][col][0] <= 0:
                    matrix[row][col][1] = False


size = int(input())
matrix = [[[int(x), True] for x in input().split()] for _ in range(size)]
bombs_coordinates = tuple(tuple(int(c) for c in x.split(',')) for x in input().split())
alive_cells = []

for bomb in bombs_coordinates:
    explosion(*bomb)

for row in matrix:
    [alive_cells.append(x[0]) for x in row if x[1]]

print(f'Alive cells: {len(alive_cells)}')
print(f'Sum: {sum(alive_cells)}')

for row in matrix:
    [print(c[0], end=' ') for c in row]
    print()